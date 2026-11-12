#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Product, App & Workspace Reviewer (v3.5) — Shift-Left Stage-Gate & Parity Auditor (review_gate_audit.py)
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
        ["X-Ray", "Silent Leak", "Cognitive", "Volatility"],
        15,
        "Gate 2: Automated X-Ray Telemetry & 4 Silent Leaks",
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
STUB_PATTERNS = [
    (r"\bTODO\b\s*[:\-]", "Unfinished TODO marker"),
    (r"\bFIXME\b\s*[:\-]", "Unresolved FIXME marker"),
    (r"NotImplementedError", "Unimplemented function stub"),
    (r"pass\s*#\s*(?:todo|implement|stub)", "Empty Python pass stub"),
]


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
                            if re.search(pat, line, re.IGNORECASE):
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
    print(f"APEX v3.5 BROWNFIELD REVIEW GATE AUDITOR | TARGET GATE: 1..{max_gate}")
    print("=" * 78)
    print(f"Review Ledger Path: {review_dir}\n")

    score = 0
    possible_score = 0
    warnings = []

    state_path = os.path.join(review_dir, "REVIEW-STATE.json")
    if os.path.isfile(state_path):
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                state = json.load(f)
            b_score = state.get("baseline_health_score", 0)
            u_score = state.get("upgraded_health_score", 0)
            print(f"  [TELEMETRY] Baseline Score: {b_score}/100  -->  Target Upgraded Score: {u_score}/100 (Delta: +{u_score - b_score})\n")
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
        score += earned
        status = "PASS" if earned >= int(weight * 0.8) else "WARN"
        print(f"  [{earned:2d}/{weight:2d} pts] {status:4s} | {filename:<42s} -> {label}")

    normalized_score = round((score / possible_score) * 100) if possible_score > 0 else 0

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
    passed = (normalized_score >= 85) and code_ok
    verdict = f"REVIEW GATE 1..{max_gate} APPROVED (READY TO ADVANCE)" if passed else f"REVIEW GATE 1..{max_gate} VETOED (FIX BEFORE ADVANCING)"
    print(f"NORMALIZED REVIEW GATE SCORE: {normalized_score} / 100  -->  VERDICT: {verdict}")
    print("-" * 78)

    if warnings:
        print("\nActionable Advisories:")
        for w in warnings:
            print(f"  - {w}")

    return 0 if passed else 2


def main():
    parser = argparse.ArgumentParser(description="APEX v3.5 Brownfield Review Gate Auditor")
    parser.add_argument("--dir", default=".", help="Project root or docs/apex-review directory")
    parser.add_argument("--gate", type=int, default=6, choices=[1, 2, 3, 4, 5, 6], help="Stage gate to verify (1..6)")
    parser.add_argument("--scan-target", default=None, help="Directory to scan for code stubs during Phase 5/6")
    args = parser.parse_args()
    sys.exit(audit_review_ledger(args.dir, args.gate, args.scan_target))


if __name__ == "__main__":
    main()
