#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Product & Workspace Reviewer (v4.5) - review gate auditor (review_gate_audit.py)

What it checks (and what it does not):
  * Ledger documents: present, substantive, and free of [[FILL: ...]] markers. The check is
    structural, so documents may be written in any language.
  * TRACE.md: every row has a status; DONE needs evidence; a High-weight row may be DEFERRED
    only with `agreed: "<user's words>"`; Gate 6 allows no OPEN rows.
  * Gate 3: a critique score >= 85 is recorded. The script records the number the critique
    produced; it cannot judge whether the critique was honest.
  * Gates 5-6: proven slices (ledger mode), a stub scan of the built product, and the required
    number of passed change scenarios.
  * LEAN mode: when no ledger folder exists but `_apex/TRACE.md` does, the TRACE, stub-scan and
    change-scenario checks still run.
"""

import argparse
import json
import os
import re
import sys

TOOL = "APEX v4.5 REVIEW GATE AUDITOR"
LEDGER_SUBDIR = "apex-review"
STATE_FILE = "REVIEW-STATE.json"
SCAFFOLD_HINT = "Run xray_scanner.py to scaffold docs/apex-review/, or xray_scanner.py --lean for _apex/TRACE.md only."
SCAN_FLAG = "--scan-target"
SCORE_DOC = "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md"
SCORE_LABEL = "TOTAL UPGRADED SCORE"
SCORE_STATE_KEY = "upgraded_health_score"
SCORE_LINE = re.compile(r"TOTAL UPGRADED SCORE:\W*(\d{1,3})\s*/\s*100", re.IGNORECASE)

# (gate, filename, weight, label)
DOCS = [
    (1, "00-PRESERVATION-CONSTITUTION.md", 15, "Gate 1: sacred items and protection contract"),
    (2, "01-FORENSIC-XRAY-AND-LEAKS.md", 15, "Gate 2: root vision, gap matrix, leaks"),
    (2, "02-KANO-UPGRADE-SPEC.md", 20, "Gate 2: upgrade spec and parity contract"),
    (3, "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md", 15, "Gate 3: before/after scorecard and rollback"),
    (4, "03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md", 20, "Gate 4: upgrade architecture and routine"),
    (4, "04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md", 15, "Gate 4: slices and 12-month roadmap"),
]

PASS_SCORE = 85
MIN_DOC_CHARS = 200  # a ledger document with less real text than this is treated as empty
CODE_EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".html", ".css", ".ps1", ".sh", ".gs"}
IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".agents", ".claude", "skills"}
SELF_NAMES = {"fitness_audit.py", "review_gate_audit.py"}

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
FILL_MARKER = re.compile(r"\[\[FILL:[^\]]*\]\]")
TABLE_SEPARATOR = re.compile(r"^\|\s*:?-{2,}")
UNESCAPED_PIPE = re.compile(r"(?<!\\)\|")
# Status and weight codes stay in English even when the rest of the table is translated.
TRACE_STATUSES = {"OPEN", "DONE", "DEFERRED", "DROPPED", "N/A"}


def force_utf8_output() -> None:
    """Windows consoles default to cp1252 and crash on paths such as 'Từ idea'."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def load_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except FileNotFoundError:
        return None, None
    except Exception as e:  # invalid JSON, permissions
        return None, f"{os.path.basename(path)} could not be read: {e}"


def legacy_version(state):
    """Return the schema version of a ledger written by APEX before v4, else None.

    Older scaffolds shipped pre-written content and pre-filled scores, so such a ledger proves nothing.
    """
    version = str((state or {}).get("schema_version", "") or "unknown")
    try:
        return None if int(version.split(".")[0]) >= 4 else version
    except ValueError:
        return version


# ----------------------------------------------------------------------------- TRACE.md


def trace_rows(path: str):
    """Yield (line_number, cells) for every data row of every Markdown table in the file.

    A header is the row directly above a separator row, whatever language it is written in.
    Escaped pipes (\\|) inside a cell are kept as part of the cell.
    """
    with open(path, "r", encoding="utf-8") as f:
        table = [(n, line.strip()) for n, line in enumerate(f, start=1) if line.strip().startswith("|")]
    for i, (n, s) in enumerate(table):
        if TABLE_SEPARATOR.match(s):
            continue
        nxt = table[i + 1] if i + 1 < len(table) else None
        if nxt and nxt[0] == n + 1 and TABLE_SEPARATOR.match(nxt[1]):
            continue  # header row
        inner = s[1:-1] if s.endswith("|") and not s.endswith("\\|") else s[1:]
        yield n, [c.strip().replace("\\|", "|") for c in UNESCAPED_PIPE.split(inner)]


def check_trace(paths, max_gate: int):
    """Every need (stated or discovered) must carry a status; DONE needs evidence; Gate 6 allows no OPEN rows."""
    path = next((p for p in paths if os.path.isfile(p)), None)
    if path is None:
        return ["Missing TRACE.md (traceability ledger of every stated and discovered need)."]
    errors, rows = [], 0
    for lineno, cells in trace_rows(path):
        rows += 1
        where = f"TRACE.md:{lineno}"
        if FILL_MARKER.search(" ".join(cells)):
            errors.append(f"{where}: unresolved [[FILL]] marker.")
            continue
        if len(cells) < 6:
            errors.append(f"{where}: expected 6 columns (ID | Need | Source | Weight | Status | Evidence / Reason).")
            continue
        row_id, weight, evidence = cells[0], cells[3].strip("*` ").lower(), cells[5]
        status = cells[4].strip("*` ").upper()
        if status not in TRACE_STATUSES:
            errors.append(f"{where}: status '{cells[4]}' is not one of {sorted(TRACE_STATUSES)} (keep status codes in English).")
        elif status != "OPEN" and not evidence:
            errors.append(f"{where}: {status} row '{row_id}' needs evidence or a reason.")
        elif status == "DEFERRED" and weight.startswith("high") and not evidence.lower().startswith("agreed:"):
            errors.append(
                f"{where}: High-weight row '{row_id}' is DEFERRED without the user's agreement "
                f"(write evidence as agreed: \"<user's words>\", or deliver a minimal DONE version)."
            )
        elif status == "OPEN" and max_gate >= 6:
            errors.append(f"{where}: row '{row_id}' is still OPEN at Gate 6.")
    if rows == 0:
        errors.append("TRACE.md has no rows.")
    return errors


# ----------------------------------------------------------------------------- STATE checks


def check_slices(state: dict, max_gate: int):
    """Gate 5 needs at least one verified slice; Gate 6 needs every slice verified."""
    slices = state.get("slices") or []
    if not slices:
        return [f"{STATE_FILE} has no slices to verify."]
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
    return errors


def check_change_scenarios(state: dict):
    """Gate 6: the number of passed 12-month change scenarios the context profile requires."""
    passed = [
        c for c in (state.get("change_scenarios") or [])
        if str(c.get("status", "")).lower() == "pass" and str(c.get("proof") or "").strip()
    ]
    try:
        required = int(state.get("change_scenarios_required", 3))
    except (TypeError, ValueError):
        required = 3
    errors = []
    # The context profile may lower the count (one-off or low-stakes work), but only with a stated reason.
    if required < 3 and not str(state.get("change_scenarios_waiver") or "").strip():
        errors.append(f"change_scenarios_required={required} (< 3) needs a one-line change_scenarios_waiver reason.")
    if len(passed) < required:
        errors.append(f"Gate 6 needs >= {required} change_scenarios with status 'pass' and a proof; found {len(passed)}.")
    return errors


def check_score(doc_text, state):
    """Gate 3: read the critique score from the scorecard line or, in any language, from STATE."""
    value = None
    m = SCORE_LINE.search(doc_text or "")
    if m:
        value = int(m.group(1))
    elif isinstance((state or {}).get(SCORE_STATE_KEY), (int, float)) and state[SCORE_STATE_KEY] > 0:
        value = int(state[SCORE_STATE_KEY])
    if value is None:
        return [
            f"No critique score found: keep a '{SCORE_LABEL}: NN / 100' line in {SCORE_DOC}, "
            f"or set \"{SCORE_STATE_KEY}\" in {STATE_FILE}."
        ]
    if value < PASS_SCORE:
        return [f"Critique score {value}/100 is below {PASS_SCORE}; fix the flaws and re-score."]
    return []


# ----------------------------------------------------------------------------- stub scan


def iter_code_files(path: str):
    """Yield (file_path, display_path) for one file, or for every code file under a folder."""
    abs_path = os.path.abspath(path)
    if os.path.isfile(abs_path):
        yield abs_path, os.path.basename(abs_path)
        return
    for root, dirs, files in os.walk(abs_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for fname in files:
            if fname in SELF_NAMES or os.path.splitext(fname)[1].lower() not in CODE_EXTENSIONS:
                continue
            fpath = os.path.join(root, fname)
            yield fpath, os.path.relpath(fpath, abs_path)


def scan_for_stubs(scan_paths):
    """Scan the given files and folders for unfinished stubs. Returns (issues, files_scanned)."""
    issues, count = [], 0
    for path in scan_paths:
        for fpath, shown in iter_code_files(path):
            count += 1
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    for idx, line in enumerate(f, start=1):
                        for pat, desc in STUB_PATTERNS:
                            if pat.search(line):
                                issues.append(f"{shown}:{idx} -> {desc}: {line.strip()[:80]}")
            except Exception as e:
                issues.append(f"{shown} -> Could not read file: {e}")
    return issues, count


def run_stub_scan(scan_dir, blockers):
    print("\n" + "-" * 78)
    print("STUB SCAN: " + ", ".join(os.path.abspath(p) for p in scan_dir))
    print("-" * 78)
    issues, count = scan_for_stubs(scan_dir)
    print(f"  Scanned {count} source files for TODO/FIXME comments and unimplemented stubs.")
    if not issues:
        print("  [PASS] No unfinished stubs found.")
        return
    print(f"  [FAIL] Found {len(issues)} stub violations:")
    for issue in issues[:10]:
        print(f"    ! {issue}")
    blockers.append(
        f"{len(issues)} unfinished stub(s) in the scanned files (see the list above). "
        f"If they are in code you did not write or change, scan only your own files and report these as findings."
    )


# ----------------------------------------------------------------------------- audits


def finish(max_gate, score_line, blockers, warnings) -> int:
    print("-" * 78)
    passed = not blockers
    verdict = "APPROVED (READY TO ADVANCE)" if passed else "VETOED (FIX BEFORE ADVANCING)"
    print(f"{score_line}  -->  VERDICT: GATE 1..{max_gate} {verdict}")
    print("-" * 78)
    if blockers:
        print("\nBlocking Issues (must be fixed before advancing):")
        for b in blockers:
            print(f"  x {b}")
    if warnings:
        print("\nAdvisories:")
        for w in warnings:
            print(f"  - {w}")
    return 0 if passed else 2


def audit_lean(root: str, trace_path: str, max_gate: int, scan_dir) -> int:
    """LEAN mode: no ledger documents, only `_apex/TRACE.md` (+ optional `_apex/STATE.json`)."""
    print("=" * 78)
    print(f"{TOOL} | LEAN MODE | TARGET GATE: 1..{max_gate}")
    print("=" * 78)
    print(f"Trace: {trace_path}")
    print("  Document gates (1-4) do not apply in LEAN mode; TRACE.md is checked at every gate.\n")
    blockers, warnings = [], []
    blockers += check_trace([trace_path], max_gate)
    state, err = load_json(os.path.join(root, "_apex", "STATE.json"))
    if err:
        warnings.append(err)
    if max_gate >= 5 and not scan_dir:
        blockers.append(f"Gates 5-6 need {SCAN_FLAG} <dir> pointing at the built product.")
    if max_gate >= 6:
        if state is None:
            blockers.append(
                "Gate 6 needs _apex/STATE.json with change_scenarios "
                "(or change_scenarios_required: 0 plus a change_scenarios_waiver reason for one-off work)."
            )
        else:
            blockers += check_change_scenarios(state)
    if scan_dir:
        run_stub_scan(scan_dir, blockers)
    return finish(max_gate, "LEAN CHECKS: " + ("all passed" if not blockers else f"{len(blockers)} blocking"), blockers, warnings)


def audit(target_dir: str, max_gate: int = 6, scan_dir=None) -> int:
    root = os.path.abspath(target_dir)
    ledger = os.path.join(root, "docs", LEDGER_SUBDIR)
    if not os.path.isdir(ledger):
        if os.path.isfile(os.path.join(root, DOCS[0][1])):
            ledger = root
        else:
            lean_trace = next(
                (p for p in (os.path.join(root, "_apex", "TRACE.md"), os.path.join(root, "TRACE.md")) if os.path.isfile(p)),
                None,
            )
            if lean_trace:
                return audit_lean(root, lean_trace, max_gate, scan_dir)
            print(f"[FAIL] Nothing to audit: no ledger at {ledger} and no _apex/TRACE.md.")
            print(SCAFFOLD_HINT)
            return 1

    state, err = load_json(os.path.join(ledger, STATE_FILE))
    if err:
        print(f"[FAIL] {err}")
        print(f"  Fix the JSON in {os.path.join(ledger, STATE_FILE)} and run again.")
        return 1
    old = legacy_version(state)
    if old:
        lean_trace = os.path.join(root, "_apex", "TRACE.md")
        print(f"[LEGACY] {ledger} was written by an older APEX version (schema {old}).")
        print("  Its templates were pre-filled, so it cannot be audited. Read it for context only.")
        if os.path.isfile(lean_trace):
            print("  Auditing _apex/TRACE.md instead.\n")
            return audit_lean(root, lean_trace, max_gate, scan_dir)
        print("  Start a fresh trace with the scaffolder's --lean flag (recommended), then run this audit again.")
        print("  To replace the old ledger, move it aside first (for example to docs/%s-legacy/)." % LEDGER_SUBDIR)
        return 1

    print("=" * 78)
    print(f"{TOOL} | TARGET GATE: 1..{max_gate}")
    print("=" * 78)
    print(f"Ledger: {ledger}\n")

    blockers, warnings = [], []

    earned_total = possible_total = 0
    score_doc_text = None
    for gate_num, filename, weight, label in [d for d in DOCS if d[0] <= max_gate]:
        possible_total += weight
        fpath = os.path.join(ledger, filename)
        earned, status = weight, "PASS"
        if not os.path.isfile(fpath):
            earned, status = 0, "MISS"
            blockers.append(f"Gate {gate_num}: missing {filename}.")
        else:
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            if filename == SCORE_DOC:
                score_doc_text = text
            unfilled = FILL_MARKER.findall(text)
            if unfilled:
                earned, status = 0, "TODO"
                blockers.append(f"{filename}: {len(unfilled)} [[FILL: ...]] marker(s) still unresolved, e.g. {unfilled[0][:70]}")
            elif len(re.sub(r"\s+", "", text)) < MIN_DOC_CHARS:
                earned, status = 0, "THIN"
                blockers.append(f"{filename}: almost empty; it must hold the real decisions for this gate.")
        earned_total += earned
        print(f"  [{earned:2d}/{weight:2d} pts] {status:4s} | {filename:<42s} -> {label}")

    if max_gate >= 3 and score_doc_text is not None and not FILL_MARKER.search(score_doc_text):
        blockers += check_score(score_doc_text, state)

    # TRACE.md is checked at every gate once it exists; from Gate 5 on it is required.
    trace_paths = [os.path.join(ledger, "TRACE.md"), os.path.join(root, "_apex", "TRACE.md"), os.path.join(root, "TRACE.md")]
    if max_gate >= 5 or any(os.path.isfile(p) for p in trace_paths):
        blockers += check_trace(trace_paths, max_gate)

    # Gates 5 & 6 are about the work itself, not the ledger documents.
    if max_gate >= 5:
        if state is None:
            blockers.append(f"Gates 5-6 need a valid {STATE_FILE} with slice verification proofs.")
        else:
            blockers += check_slices(state, max_gate)
            if max_gate >= 6:
                blockers += check_change_scenarios(state)
        if not scan_dir:
            blockers.append(f"Gates 5-6 need {SCAN_FLAG} <dir> pointing at the built product.")

    if scan_dir:
        run_stub_scan(scan_dir, blockers)

    pct = round(earned_total / possible_total * 100) if possible_total else 0
    return finish(max_gate, f"LEDGER COMPLETENESS: {pct} / 100", blockers, warnings)


def main():
    parser = argparse.ArgumentParser(description=TOOL)
    parser.add_argument("--dir", default=".", help="Project root (holds docs/%s/ or _apex/TRACE.md)" % LEDGER_SUBDIR)
    parser.add_argument("--gate", type=int, default=6, choices=[1, 2, 3, 4, 5, 6], help="Stage gate to verify (1..6)")
    parser.add_argument(
        SCAN_FLAG, dest="scan_dir", nargs="+", default=None,
        help="Files or folders you built or changed, to scan for stubs (pre-existing code you did not touch is not your gate)",
    )
    args = parser.parse_args()
    force_utf8_output()
    sys.exit(audit(args.dir, args.gate, args.scan_dir))


if __name__ == "__main__":
    main()
