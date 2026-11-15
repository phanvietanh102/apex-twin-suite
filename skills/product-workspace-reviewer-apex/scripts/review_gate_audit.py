#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Product, App & Workspace Reviewer (v4.3) — Shift-Left Stage-Gate & Parity Auditor (review_gate_audit.py)
Audits docs/apex-review/ across Gates 1..6 and optionally scans the target workspace/codebase
for unfinished TODO/FIXME stubs, unquarantined entropy files, and C-Suite Delta Score >= 85/100.
"""

import argparse
import json
import os
import re
import sys

REVIEW_CHECKS = [
    (
        1,
        "00-PRESERVATION-CONSTITUTION.md",
        ["Sacred", "Green Zone", "Yellow Zone", "Red Zone", "Invariant"],
        15,
        "Gate 1: Sacred Habits & Green/Yellow/Red Blast-Radius Contract",
    ),
    (
        2,
        "01-FORENSIC-XRAY-AND-LEAKS.md",
        ["X-Ray", "Root Vision", "MISSING A-TO-Z BUILD", "Silent Leak", "Volatility"],
        15,
        "Gate 2: Root-Vision vs. X-Ray Gap Matrix & 4 Silent Leaks",
    ),
    (
        2,
        "02-KANO-UPGRADE-SPEC.md",
        ["Tier 1", "Tier 2", "Tier 3", "SMART-ER", "Parity"],
        20,
        "Gate 2: Kano 30% Modernization Spec & Parity Contract",
    ),
    (
        3,
        "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md",
        ["CPO", "CTO", "CFO", "Before", "After", "Rollback"],
        15,
        "Gate 3: 6-Role C-Suite Before/After Delta Scorecard & Rollback",
    ),
    (
        4,
        "03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md",
        ["TIER A", "TIER B", "ADR", "SOP"],
        20,
        "Gate 4: Strangler-Fig 3-Tier Extraction & Workspace Hygiene",
    ),
    (
        4,
        "04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md",
        ["Slice", "Day 30", "Day 90", "Day 180", "Day 365"],
        15,
        "Gate 4: Surgical 4-Slice Plan & 365-Day Immunity Roadmap",
    ),
]

CODE_EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".html", ".css", ".ps1", ".sh"}
IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".agents", ".claude", "skills"}
# TODO/FIXME are matched case-sensitively and only inside a comment, so identifiers such as
# `todo-list` or URLs such as `https://todo...` are not flagged.
STUB_PATTERNS = [
    (re.compile(r"(?:#|//|/\*|<!--|\*)\s*TODO\b"), "Unfinished TODO marker"),
    (re.compile(r"(?:#|//|/\*|<!--|\*)\s*FIXME\b"), "Unresolved FIXME marker"),
    (re.compile(r"\braise\s+NotImplementedError\b"), "Unimplemented function stub"),
    (re.compile(r"pass\s*#\s*(?:todo|implement|stub)", re.IGNORECASE), "Empty Python pass stub"),
]

# Every decision taken from the user's answers is scaffolded as [[FILL: hint]].
# A gate document that still contains one is unfinished and earns 0 points.
FILL_MARKER = re.compile(r"\[\[FILL:[^\]]*\]\]")
UPGRADED_TOTAL = re.compile(r"TOTAL UPGRADED SCORE:\W*(\d{1,3})\s*/\s*100", re.IGNORECASE)
PASS_SCORE = 85


def force_utf8_output() -> None:
    """Windows consoles default to cp1252 and crash on paths such as 'Từ idea'."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def check_slices(state: dict, max_gate: int) -> list[str]:
    """Gate 5 needs at least one verified slice; Gate 6 needs every slice verified."""
    slices = state.get("slices") or []
    if not slices:
        return ["REVIEW-STATE.json has no slices to verify."]
    done = [s for s in slices if s.get("status") == "done"]
    errors = [
        f"Slice '{s.get('id')}' is marked done without a verification_proof."
        for s in done
        if not str(s.get("verification_proof") or "").strip()
    ]
    if max_gate == 5 and not done:
        errors.append("Gate 5 needs at least one slice marked done with a verification_proof (slice-1 = pre-flight backup).")
    if max_gate >= 6:
        errors += [
            f"Gate 6 needs every slice done; '{s.get('id')}' is '{s.get('status')}'."
            for s in slices
            if s.get("status") != "done"
        ]
        passed = [
            c for c in (state.get("change_scenarios") or [])
            if str(c.get("status", "")).lower() == "pass" and str(c.get("proof") or "").strip()
        ]
        # The context profile may lower the count (one-off or low-stakes work), but only with a stated reason.
        try:
            required = int(state.get("change_scenarios_required", 3))
        except (TypeError, ValueError):
            required = 3
        if required < 3 and not str(state.get("change_scenarios_waiver") or "").strip():
            errors.append(f"change_scenarios_required={required} (< 3) needs a one-line change_scenarios_waiver reason.")
        if len(passed) < required:
            errors.append(f"Gate 6 needs >= {required} change_scenarios with status 'pass' and a proof; found {len(passed)}.")
    return errors


TRACE_STATUSES = {"OPEN", "DONE", "DEFERRED", "DROPPED", "N/A"}


def check_trace(paths: list[str], max_gate: int) -> list[str]:
    """Every finding and wish must carry a status; DONE needs evidence; Gate 6 allows no OPEN rows."""
    path = next((p for p in paths if os.path.isfile(p)), None)
    if path is None:
        return ["Missing TRACE.md (traceability ledger of every finding and wish)."]
    errors, rows = [], 0
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            s = line.strip()
            if not s.startswith("|") or re.match(r"^\|\s*:?-{3,}", s):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cells and cells[0].upper() == "ID":
                continue
            rows += 1
            where = f"TRACE.md:{lineno}"
            if FILL_MARKER.search(s):
                errors.append(f"{where}: unresolved [[FILL]] marker.")
                continue
            if len(cells) < 6:
                errors.append(f"{where}: expected 6 columns (ID | Need | Source | Weight | Status | Evidence / Reason).")
                continue
            status, evidence = cells[4].upper(), cells[5]
            if status not in TRACE_STATUSES:
                errors.append(f"{where}: status '{cells[4]}' is not one of {sorted(TRACE_STATUSES)}.")
            elif status != "OPEN" and not evidence:
                errors.append(f"{where}: {status} row '{cells[0]}' needs evidence or a reason.")
            elif status == "DEFERRED" and cells[3].lower().startswith("high") and not evidence.lower().startswith("agreed:"):
                errors.append(f"{where}: High-weight row '{cells[0]}' is DEFERRED without the user's agreement "
                              f"(write evidence as agreed: \"<user's words>\", or deliver a minimal DONE version).")
            elif status == "OPEN" and max_gate >= 6:
                errors.append(f"{where}: row '{cells[0]}' is still OPEN at Gate 6.")
    if rows == 0:
        errors.append("TRACE.md has no rows.")
    return errors


def scan_target_quality(scan_dir: str) -> tuple[bool, list[str], int]:
    abs_scan = os.path.abspath(scan_dir)
    issues = []
    code_files_count = 0

    for root, dirs, files in os.walk(abs_scan):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname in ("review_gate_audit.py", "fitness_audit.py"):
                continue
            ext = os.path.splitext(fname)[1].lower()
            if ext not in CODE_EXTENSIONS:
                continue
            code_files_count += 1
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, abs_scan)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    for idx, line in enumerate(f, start=1):
                        for pat, desc in STUB_PATTERNS:
                            if pat.search(line):
                                issues.append(f"{rel_path}:{idx} -> {desc}: {line.strip()[:80]}")
            except Exception as e:
                issues.append(f"{rel_path} -> Read error: {e}")

    return len(issues) == 0, issues, code_files_count


def audit_review_ledger(target_dir: str, max_gate: int = 6, scan_target_dir: str = None) -> int:
    review_dir = os.path.join(os.path.abspath(target_dir), "docs", "apex-review")
    if not os.path.isdir(review_dir):
        if os.path.isfile(os.path.join(os.path.abspath(target_dir), "00-PRESERVATION-CONSTITUTION.md")):
            review_dir = os.path.abspath(target_dir)
        else:
            print(f"[FAIL] Review ledger not found at: {review_dir}")
            print("Run xray_scanner.py first to perform the X-Ray scan and initialize docs/apex-review/.")
            return 1

    print("=" * 78)
    print(f"APEX v4.3 BROWNFIELD REVIEW GATE AUDITOR | TARGET GATE: 1..{max_gate}")
    print("=" * 78)
    print(f"Review Ledger Path: {review_dir}\n")

    score = 0
    possible_score = 0
    warnings = []
    blockers = []  # any blocker vetoes the gate regardless of score

    state = None
    state_path = os.path.join(review_dir, "REVIEW-STATE.json")
    if os.path.isfile(state_path):
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                state = json.load(f)
            b_score = state.get("baseline_health_score")
            u_score = state.get("upgraded_health_score")
            if isinstance(b_score, (int, float)) and isinstance(u_score, (int, float)):
                print(f"  [TELEMETRY] Baseline Score: {b_score}/100  -->  Target Upgraded Score: {u_score}/100 (Delta: {u_score - b_score:+})\n")
            else:
                print(f"  [TELEMETRY] Baseline Score: {b_score}/100 (heuristic)  -->  Upgraded Score: not scored yet (set after Phase 3)\n")
        except Exception as e:
            warnings.append(f"REVIEW-STATE.json parse error: {e}")
    else:
        warnings.append("Missing REVIEW-STATE.json tracker.")

    active_checks = [c for c in REVIEW_CHECKS if c[0] <= max_gate]
    for gate_num, filename, keywords, weight, label in active_checks:
        possible_score += weight
        fpath = os.path.join(review_dir, filename)
        if not os.path.isfile(fpath):
            print(f"  [0/{weight:2d} pts] FAIL | {filename:<42s} -> {label} (MISSING)")
            warnings.append(f"Gate {gate_num} Failed: Missing {filename}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        matched = [kw for kw in keywords if re.search(re.escape(kw), text, re.IGNORECASE)]
        earned = round(weight * (len(matched) / len(keywords)))
        status = "PASS" if earned >= int(weight * 0.8) else "WARN"

        unfilled = FILL_MARKER.findall(text)
        if unfilled:
            earned = 0
            status = "TODO"
            blockers.append(f"{filename}: {len(unfilled)} [[FILL: ...]] marker(s) still unresolved, e.g. {unfilled[0][:70]}")

        if filename == "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md" and not unfilled:
            m = UPGRADED_TOTAL.search(text)
            if not m:
                blockers.append(f"{filename}: no 'TOTAL UPGRADED SCORE: NN / 100' line found.")
            elif int(m.group(1)) < PASS_SCORE:
                blockers.append(f"{filename}: upgraded score {m.group(1)}/100 is below {PASS_SCORE}; strengthen the plan and re-score.")

        score += earned
        print(f"  [{earned:2d}/{weight:2d} pts] {status:4s} | {filename:<42s} -> {label}")

    normalized_score = round((score / possible_score) * 100) if possible_score > 0 else 0

    # Gates 5 & 6 are about the executed upgrade, not the ledger documents.
    if max_gate >= 5:
        if state is None:
            blockers.append("Gates 5-6 need a valid REVIEW-STATE.json with slice verification proofs.")
        else:
            blockers += check_slices(state, max_gate)
        blockers += check_trace(
            [os.path.join(review_dir, "TRACE.md"), os.path.join(os.path.abspath(target_dir), "_apex", "TRACE.md"),
             os.path.join(os.path.abspath(target_dir), "TRACE.md")],
            max_gate,
        )
        if not scan_target_dir:
            blockers.append("Gates 5-6 need --scan-target <dir> pointing at the upgraded workspace.")

    code_ok = True
    if scan_target_dir:
        print("\n" + "-" * 78)
        print(f"PHASE 5/6 SURGICAL REFACTOR & ANTI-STUB SCANNER: {os.path.abspath(scan_target_dir)}")
        print("-" * 78)
        code_ok, issues, fcount = scan_target_quality(scan_target_dir)
        print(f"  Scanned {fcount} code/script files for unfinished TODOs, FIXMEs, and stubs.")
        if code_ok:
            print("  [PASS] Zero unfinished stubs detected in refactored target!")
        else:
            print(f"  [FAIL] Found {len(issues)} stub violations:")
            for issue in issues[:10]:
                print(f"    ! {issue}")
            normalized_score = max(0, normalized_score - len(issues) * 5)

    print("-" * 78)
    passed = (normalized_score >= PASS_SCORE) and code_ok and not blockers
    verdict = f"REVIEW GATE 1..{max_gate} APPROVED (READY TO ADVANCE)" if passed else f"REVIEW GATE 1..{max_gate} VETOED (FIX BEFORE ADVANCING)"
    print(f"NORMALIZED REVIEW GATE SCORE: {normalized_score} / 100  -->  VERDICT: {verdict}")
    print("-" * 78)

    if blockers:
        print("\nBlocking Issues (must be fixed before advancing):")
        for b in blockers:
            print(f"  x {b}")

    if warnings:
        print("\nActionable Advisories:")
        for w in warnings:
            print(f"  - {w}")

    return 0 if passed else 2


def main():
    parser = argparse.ArgumentParser(description="APEX v4.3 Brownfield Review Gate Auditor")
    parser.add_argument("--dir", default=".", help="Project root or docs/apex-review directory")
    parser.add_argument("--gate", type=int, default=6, choices=[1, 2, 3, 4, 5, 6], help="Stage gate to verify (1..6)")
    parser.add_argument("--scan-target", default=None, help="Directory to scan for code stubs during Phase 5/6")
    args = parser.parse_args()
    force_utf8_output()
    sys.exit(audit_review_ledger(args.dir, args.gate, args.scan_target))


if __name__ == "__main__":
    main()
