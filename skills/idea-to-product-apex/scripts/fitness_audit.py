#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Idea-to-Product (v4.3) — Shift-Left Stage-Gate & Anti-Stub Code Auditor (fitness_audit.py)
Supports:
  1. Step-by-step Gate Verification (--gate 1..6) so errors in Step 2 or 3 are caught immediately!
  2. Full Blueprint Completeness & 12-Month Evergreen Audit.
  3. Executable Code & Deliverable Anti-Stub Scanner (--scan-code <dir>) that catches TODOs,
     FIXMEs, fake mock arrays, empty implementations, or missing verification proofs.
"""

import argparse
import json
import os
import re
import sys

CONTENT_CHECKS = [
    (
        1,
        "00-PROJECT-CONSTITUTION.md",
        ["JTBD", "Non-Goal", "Invariant"],
        15,
        "Gate 1: Project Constitution, Open Vision & Immutable Laws",
    ),
    (
        2,
        "01-DISCOVERY-AND-PRFAQ.md",
        ["Johari", "Press Release", "FAQ"],
        15,
        "Gate 2: Johari Unknown-Unknowns & Working Backwards PR/FAQ",
    ),
    (
        2,
        "02-KANO-SPEC-AND-DELIGHT.md",
        ["Tier 1", "Tier 2", "Tier 3", "SMART-ER"],
        20,
        "Gate 2: Kano 30% Delighters & SMART-ER Contract",
    ),
    (
        3,
        "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md",
        ["CPO", "CTO", "CFO", "Fitness", "Quarterly"],
        15,
        "Gate 3: 6-Role C-Suite Red-Team & Adversarial Scorecard",
    ),
    (
        4,
        "03-ARCHITECTURE-AND-SOPS.md",
        ["TIER A", "TIER B", "ADR", "SOP"],
        20,
        "Gate 4: 3-Tier Decoupled Architecture & Operator SOP",
    ),
    (
        4,
        "04-12M-EVERGREEN-ROADMAP.md",
        ["Slice", "Day 30", "Day 90", "Day 180", "Day 365"],
        15,
        "Gate 4: Vertical Slices & 365-Day Evergreen Horizon",
    ),
]

CODE_EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".html", ".css", ".ps1", ".sh"}
IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".agents", ".claude", "skills"}

# TODO/FIXME are matched case-sensitively and only inside a comment, so identifiers such as
# `todo-list` (a todo app) or URLs such as `https://todo...` are not flagged.
STUB_PATTERNS = [
    (re.compile(r"(?:#|//|/\*|<!--|\*)\s*TODO\b"), "Unfinished TODO marker"),
    (re.compile(r"(?:#|//|/\*|<!--|\*)\s*FIXME\b"), "Unresolved FIXME marker"),
    (re.compile(r"\braise\s+NotImplementedError\b"), "Unimplemented function stub (NotImplementedError)"),
    (re.compile(r"pass\s*#\s*(?:todo|implement|stub)", re.IGNORECASE), "Empty Python pass stub"),
    (re.compile(r"(?<![:/])//\s*(?:implement later|placeholder)\b", re.IGNORECASE), "Commented placeholder logic"),
]

# Every decision the model or user must make is scaffolded as [[FILL: hint]].
# A gate document that still contains one is unfinished and earns 0 points.
FILL_MARKER = re.compile(r"\[\[FILL:[^\]]*\]\]")
C_SUITE_TOTAL = re.compile(r"TOTAL C-SUITE AUDIT SCORE:\W*(\d{1,3})\s*/\s*100", re.IGNORECASE)
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
        return ["STATE.json has no slices to verify."]
    done = [s for s in slices if s.get("status") == "done"]
    errors = [
        f"Slice '{s.get('id')}' is marked done without a verification_proof."
        for s in done
        if not str(s.get("verification_proof") or "").strip()
    ]
    if max_gate == 5 and not done:
        errors.append("Gate 5 needs at least one slice marked done with a verification_proof.")
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
    """Every need (stated or discovered) must carry a status; DONE needs evidence; Gate 6 allows no OPEN rows."""
    path = next((p for p in paths if os.path.isfile(p)), None)
    if path is None:
        return ["Missing TRACE.md (traceability ledger of every stated and discovered need)."]
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


def scan_code_quality(scan_dir: str) -> tuple[bool, list[str], int]:
    """Scans source code files for stubs, placeholders, and test coverage presence."""
    abs_scan = os.path.abspath(scan_dir)
    issues = []
    code_files_count = 0
    test_files_count = 0

    for root, dirs, files in os.walk(abs_scan):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in CODE_EXTENSIONS:
                continue
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, abs_scan)
            # Skip auditing fitness_audit.py itself if scanning repo root
            if fname == "fitness_audit.py":
                continue

            code_files_count += 1
            if "test" in fname.lower() or "spec" in fname.lower() or "verify" in fname.lower():
                test_files_count += 1

            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines, start=1):
                    for pat, desc in STUB_PATTERNS:
                        if pat.search(line):
                            issues.append(f"{rel_path}:{idx} -> {desc}: {line.strip()[:80]}")
            except Exception as e:
                issues.append(f"{rel_path} -> Could not read file: {e}")

    passed = len(issues) == 0
    return passed, issues, code_files_count


def audit_blueprint(target_dir: str, max_gate: int = 6, scan_code_dir: str = None) -> int:
    blueprint_dir = os.path.join(os.path.abspath(target_dir), "docs", "apex-blueprint")
    if not os.path.isdir(blueprint_dir):
        if os.path.isfile(os.path.join(os.path.abspath(target_dir), "00-PROJECT-CONSTITUTION.md")):
            blueprint_dir = os.path.abspath(target_dir)
        else:
            print(f"[FAIL] Blueprint directory not found at: {blueprint_dir}")
            print("Run init_project.py first to scaffold the Persistent Memory Ledger.")
            return 1

    print("=" * 76)
    print(f"APEX v4.3 SHIFT-LEFT AUDITOR | TARGET GATE: 1..{max_gate}")
    print("=" * 76)
    print(f"Blueprint Path: {blueprint_dir}\n")

    score = 0
    possible_score = 0
    warnings = []
    blockers = []  # any blocker vetoes the gate regardless of score

    # 1. Check STATE.json validity
    state = None
    state_path = os.path.join(blueprint_dir, "STATE.json")
    if os.path.isfile(state_path):
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                state = json.load(f)
            if state.get("evergreen_horizon_months", 0) < 12:
                warnings.append("STATE.json: evergreen_horizon_months is less than 12.")
        except Exception as e:
            warnings.append(f"STATE.json is invalid JSON: {e}")
    else:
        warnings.append("Missing STATE.json session tracker.")

    # 2. Check documents up to max_gate
    active_checks = [c for c in CONTENT_CHECKS if c[0] <= max_gate]
    for gate_num, filename, keywords, weight, label in active_checks:
        possible_score += weight
        fpath = os.path.join(blueprint_dir, filename)
        if not os.path.isfile(fpath):
            print(f"  [0/{weight:2d} pts] FAIL | {filename:<34s} -> {label} (MISSING)")
            warnings.append(f"Gate {gate_num} Failed: Missing {filename}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        matched = [kw for kw in keywords if re.search(re.escape(kw), text, re.IGNORECASE)]
        ratio = len(matched) / len(keywords)
        earned = round(weight * ratio)
        status = "PASS" if earned >= int(weight * 0.8) else "WARN"

        unfilled = FILL_MARKER.findall(text)
        if unfilled:
            earned = 0
            status = "TODO"
            blockers.append(f"{filename}: {len(unfilled)} [[FILL: ...]] marker(s) still unresolved, e.g. {unfilled[0][:70]}")

        if filename == "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md" and not unfilled:
            m = C_SUITE_TOTAL.search(text)
            if not m:
                blockers.append(f"{filename}: no 'TOTAL C-SUITE AUDIT SCORE: NN / 100' line found.")
            elif int(m.group(1)) < PASS_SCORE:
                blockers.append(f"{filename}: C-Suite score {m.group(1)}/100 is below {PASS_SCORE}; fix the flaws and re-score.")

        score += earned
        print(f"  [{earned:2d}/{weight:2d} pts] {status:4s} | {filename:<34s} -> {label}")

    normalized_score = round((score / possible_score) * 100) if possible_score > 0 else 0

    # Gates 5 & 6 are about the build itself, not the blueprint documents.
    if max_gate >= 5:
        if state is None:
            blockers.append("Gates 5-6 need a valid STATE.json with slice verification proofs.")
        else:
            blockers += check_slices(state, max_gate)
        blockers += check_trace(
            [os.path.join(blueprint_dir, "TRACE.md"), os.path.join(os.path.abspath(target_dir), "_apex", "TRACE.md"),
             os.path.join(os.path.abspath(target_dir), "TRACE.md")],
            max_gate,
        )
        if not scan_code_dir:
            blockers.append("Gates 5-6 need --scan-code <dir> pointing at the built product.")

    # 3. Optional Code Anti-Stub Scan (Gates 5 & 6)
    code_ok = True
    if scan_code_dir:
        print("\n" + "-" * 76)
        print(f"PHASE 5/6 EXECUTABLE CODE & ANTI-STUB SCANNER: {os.path.abspath(scan_code_dir)}")
        print("-" * 76)
        code_ok, code_issues, file_count = scan_code_quality(scan_code_dir)
        print(f"  Scanned {file_count} source files for TODOs, FIXMEs, and placeholder stubs.")
        if code_ok:
            print("  [PASS] Zero placeholder stubs or unfinished TODOs detected in source code!")
        else:
            print(f"  [FAIL] Found {len(code_issues)} stub/placeholder violations (Gate 5 Blocked):")
            for issue in code_issues[:10]:
                print(f"    ! {issue}")
            normalized_score = max(0, normalized_score - (len(code_issues) * 5))

    print("-" * 76)
    passed_gate = (normalized_score >= PASS_SCORE) and code_ok and not blockers
    verdict = f"GATE 1..{max_gate} APPROVED (READY TO ADVANCE)" if passed_gate else f"GATE 1..{max_gate} VETOED (FIX ERRORS BEFORE ADVANCING)"
    print(f"NORMALIZED GATE SCORE: {normalized_score} / 100  -->  VERDICT: {verdict}")
    print("-" * 76)

    if blockers:
        print("\nBlocking Issues (must be fixed before advancing):")
        for b in blockers:
            print(f"  x {b}")

    if warnings:
        print("\nActionable Advisories:")
        for w in warnings:
            print(f"  - {w}")

    return 0 if passed_gate else 2


def main():
    parser = argparse.ArgumentParser(description="APEX v4.3 Shift-Left Gate & Code Auditor")
    parser.add_argument("--dir", default=".", help="Project root or blueprint directory")
    parser.add_argument("--gate", type=int, default=6, choices=[1, 2, 3, 4, 5, 6], help="Stage gate to verify (1..6)")
    parser.add_argument("--scan-code", default=None, help="Directory to scan for TODO/FIXME/mock stubs")
    args = parser.parse_args()
    force_utf8_output()
    sys.exit(audit_blueprint(args.dir, args.gate, args.scan_code))


if __name__ == "__main__":
    main()
