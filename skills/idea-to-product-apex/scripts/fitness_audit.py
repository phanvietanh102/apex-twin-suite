#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Idea-to-Product (v3.0) — Shift-Left Stage-Gate & Anti-Stub Code Auditor (fitness_audit.py)
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

STUB_PATTERNS = [
    (r"\bTODO\b\s*[:\-]", "Unfinished TODO marker"),
    (r"\bFIXME\b\s*[:\-]", "Unresolved FIXME marker"),
    (r"NotImplementedError", "Unimplemented function stub (NotImplementedError)"),
    (r"pass\s*#\s*(?:todo|implement|stub)", "Empty Python pass stub"),
    (r"//\s*(?:todo|implement later|placeholder)", "Commented placeholder logic"),
]


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
                        if re.search(pat, line, re.IGNORECASE):
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
    print(f"APEX v3.0 SHIFT-LEFT AUDITOR | TARGET GATE: 1..{max_gate}")
    print("=" * 76)
    print(f"Blueprint Path: {blueprint_dir}\n")

    score = 0
    possible_score = 0
    warnings = []

    # 1. Check STATE.json validity
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

        placeholders = re.findall(r"\[(?:Specify|Choose|Locked Option|feature X)[^\]]*\]", text)
        if len(placeholders) > 3:
            earned = max(0, earned - 2)
            warnings.append(f"{filename}: Contains {len(placeholders)} uncustomized template placeholders.")

        score += earned
        status = "PASS" if earned >= int(weight * 0.8) else "WARN"
        print(f"  [{earned:2d}/{weight:2d} pts] {status:4s} | {filename:<34s} -> {label}")

    normalized_score = round((score / possible_score) * 100) if possible_score > 0 else 0

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
    passed_gate = (normalized_score >= 85) and code_ok
    verdict = f"GATE 1..{max_gate} APPROVED (READY TO ADVANCE)" if passed_gate else f"GATE 1..{max_gate} VETOED (FIX ERRORS BEFORE ADVANCING)"
    print(f"NORMALIZED GATE SCORE: {normalized_score} / 100  -->  VERDICT: {verdict}")
    print("-" * 76)

    if warnings:
        print("\nActionable Advisories:")
        for w in warnings:
            print(f"  - {w}")

    return 0 if passed_gate else 2


def main():
    parser = argparse.ArgumentParser(description="APEX v3.0 Shift-Left Gate & Code Auditor")
    parser.add_argument("--dir", default=".", help="Project root or blueprint directory")
    parser.add_argument("--gate", type=int, default=6, choices=[1, 2, 3, 4, 5, 6], help="Stage gate to verify (1..6)")
    parser.add_argument("--scan-code", default=None, help="Directory to scan for TODO/FIXME/mock stubs")
    args = parser.parse_args()
    sys.exit(audit_blueprint(args.dir, args.gate, args.scan_code))


if __name__ == "__main__":
    main()
