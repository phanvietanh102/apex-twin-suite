#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Product, App & Workspace Reviewer (v4.4) — Automated Forensic X-Ray & Ledger Scaffolder (xray_scanner.py)
Performs a non-destructive forensic scan of an existing workspace, app, or project folder:
  1. Inventories file topology, extensions, and directory depth.
  2. Detects Workspace Entropy (duplicate/versioned files like v1, v2, final, copy, (1)).
  3. Maps files into Green (Safe), Yellow (Test-Protected), and Red (Immutable Data/Billing) Zones.
  4. Scaffolds docs/apex-review/ (6 Forensic Ledger files + REVIEW-STATE.json) populated with real scan data.
"""

import argparse
import collections
import datetime
import json
import os
import re
import sys

DOMAIN_MAP = {
    "DOM-01": "Software, SaaS & AI Applications",
    "DOM-02": "Construction, Architecture & Real Estate Workspaces/Portals",
    "DOM-03": "Content, SEO, AIO (GEO) & Digital Media Systems",
    "DOM-04": "E-Commerce, Retail & Invoice/Billing Workspaces",
    "DOM-05": "B2B Services, Agency, Consulting & Internal Operations OS",
    "DOM-06": "Regulated & High-Trust Systems (FinTech, EdTech, Legal, Healthcare)",
    "DOM-07": "Hardware, IoT & Physical-Digital Hybrid Systems",
}

IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".agents", ".claude", "apex-review", "apex-blueprint", "_apex"}
# Version/duplicate markers must stand as their own token: `report_v2.xlsx`, `x - Copy.docx`,
# `Copy of x`, `hoadon (1).xlsx` match; `copywriting.md` or `dev2.py` do not.
ENTROPY_REGEX = re.compile(
    r"(?:[-_\s]v\d+(?=[-_\s.(]|$)"
    r"|[-_\s]final(?=[-_\s.(]|$)"
    r"|(?:^|[-_\s(])(?:copy|sao\s*ch[eé]p)(?=[-_\s.\d)]|$)"
    r"|\(\d+\)|\.bak$|\.old$|~$)",
    re.IGNORECASE,
)

RED_EXTS = {".db", ".sqlite", ".sqlite3", ".sql", ".xlsx", ".xls", ".csv", ".pdf", ".env", ".pem", ".key"}
YELLOW_EXTS = {".py", ".js", ".ts", ".tsx", ".jsx", ".ps1", ".sh", ".json", ".yaml", ".yml", ".html", ".php"}
RECORD_WORDS = ("hoa_don", "hoadon", "invoice", "baogia", "bao_gia", "contract", "hop_dong")
GREEN_EXTS = {".md", ".txt", ".css", ".scss", ".svg", ".png", ".jpg", ".jpeg", ".webp"}


def scan_workspace(target_root: str) -> dict:
    ext_counts = collections.Counter()
    entropy_files = []
    green_zone = []
    yellow_zone = []
    red_zone = []
    total_files = 0
    total_bytes = 0
    max_depth = 0

    for root, dirs, files in os.walk(target_root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel_dir = os.path.relpath(root, target_root)
        depth = 0 if rel_dir == "." else len(rel_dir.split(os.sep))
        max_depth = max(max_depth, depth)

        for fname in files:
            total_files += 1
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, target_root)
            try:
                total_bytes += os.path.getsize(fpath)
            except OSError:
                pass

            lower = fname.lower()
            # ".env" has no extension for splitext; treat the whole dotfile name as its type.
            ext = os.path.splitext(fname)[1].lower() or (lower if lower.startswith(".") else "(no-ext)")
            ext_counts[ext] += 1

            if ENTROPY_REGEX.search(fname):
                entropy_files.append(rel_path)

            # A filename scan is only a first guess; the model corrects it by reading the files.
            is_secret = lower.startswith(".env") or ext in {".pem", ".key"} or "secret" in lower or "credential" in lower
            is_record = ext in RED_EXTS or any(k in lower for k in RECORD_WORDS)
            if is_secret:
                red_zone.append(rel_path)
            elif ext in YELLOW_EXTS:
                yellow_zone.append(rel_path)  # code is "change with tests", whatever its name says
            elif is_record:
                red_zone.append(rel_path)
            else:
                green_zone.append(rel_path)

    return {
        "total_files": total_files,
        "total_kb": round(total_bytes / 1024, 1),
        "max_depth": max_depth,
        "top_extensions": dict(ext_counts.most_common(8)),
        "entropy_files": entropy_files[:20],
        "entropy_count": len(entropy_files),
        "zones": {
            "green_safe": green_zone[:15],
            "yellow_tested": yellow_zone[:15],
            "red_immutable": red_zone[:15],
            "counts": {
                "green": len(green_zone),
                "yellow": len(yellow_zone),
                "red": len(red_zone),
            },
        },
    }


def build_review_state(project_name: str, domain_key: str, today: str, xray: dict) -> dict:
    return {
        "schema_version": "4.4.0-apex-review",
        "target_name": project_name,
        "domain_primary": domain_key,
        "domain_label": DOMAIN_MAP.get(domain_key, domain_key),
        # 12-month change scenarios (see references/08): {"id", "event", "expected", "status": "pass"|"fail", "proof"}
        "change_scenarios": [],
        # Lower only for one-off or low-stakes work, with a reason (references/08 §4).
        "change_scenarios_required": 3,
        "change_scenarios_waiver": "",
        # Context profile (references/07 Step 0): rules not activated here are N/A with a reason.
        "context_profile": {"a_money_with_parties": None, "b_personal_data": None, "c_regulated": None,
                            "d_others_operate": None, "e_controls_for_others": None, "f_replaces_existing": None,
                            "g_long_lived": None, "h_established_trade": None, "i_stakes": None},
        "created_at": today,
        "last_updated": today,
        "current_phase": "Phase 1: Forensic X-Ray & Pain Excavation",
        # Both scores are set only by a real critique, never by the scaffolder.
        "baseline_health_score": None,
        "upgraded_health_score": None,
        "evergreen_horizon_months": 12,
        "xray_summary": {
            "total_files": xray["total_files"],
            "total_kb": xray["total_kb"],
            "entropy_count": xray["entropy_count"],
            "zone_counts": xray["zones"]["counts"],
        },
        "sacred_habits_locked": [],
        "slices": [
            {
                "id": "slice-1",
                "name": "Verified backup and history locked in place",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-2",
                "name": "The owner's biggest pain or heaviest flow",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-3",
                "name": "Remaining gaps and beyond-expectation additions",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-4",
                "name": "Parity checks and handover",
                "status": "pending",
                "verification_proof": None,
            },
        ],
    }


def build_review_templates(project_name: str, domain_key: str, today: str, xray: dict) -> dict:
    domain_label = DOMAIN_MAP.get(domain_key, domain_key)
    zc = xray["zones"]["counts"]
    ext_str = ", ".join(f"`{k}` ({v})" for k, v in xray["top_extensions"].items()) or "None"
    entropy_list = "\n".join(f"  - `{p}`" for p in xray["entropy_files"][:8]) or "  - None found"
    note = "> Every `[[FILL: ...]]` marker is a decision drawn from the owner's answers or from evidence. The gate script vetoes a gate while any marker remains.\n> Add or remove rows and items to fit. If an item does not apply, replace its marker with `N/A` and a short reason, or delete the row. Never invent content to fill a row.\n> You may rewrite headings and text in the owner's language."

    return {
        "TRACE.md": f"""# TRACE — {project_name}
> Every Turn-1 finding, every gap-matrix item, every wish the owner stated and every need discovered (completeness lenses, domain brief) gets a row. Rows never disappear; update them.
> Status: OPEN while working; final = DONE (evidence) / DEFERRED (reason + when) / DROPPED (owner agreed — quote) / N/A (why). Order rows by weight. A High row (law, safety, money at risk, irreversible data, root vision, #1 pain) may be DEFERRED only with evidence `agreed: "<owner's words>"`. Keep the Status and Weight codes in English (OPEN/DONE/DEFERRED/DROPPED/N/A, High/Medium/Low) even if the rest is in the owner's language. See references/08.

| ID | Need / Finding | Source | Weight | Status | Evidence / Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Verified backup of the current state; finished records protected in place | discovered (safety) | High | OPEN | |
| R-02 | [[FILL: the owner's biggest pain or heaviest flow]] | owner | High | OPEN | |
""",
        "00-PRESERVATION-CONSTITUTION.md": f"""# 00. What must not break — {project_name}
> Reviewed {today} | Field: {domain_label}

{note}

## 1. What the owner said must stay as it is
- [[FILL: habit, file or data the owner named]]
- [[FILL: another, or N/A]]

## 2. Zones
> Counts come from a filename scan, which is only a first guess. Correct it by reading the files.

- **Safe to change ({zc['green']} files):** documents, static assets.
- **Change only with tests ({zc['yellow']} files):** scripts, logic, templates in use.
- **Protect ({zc['red']} files):** finished records such as issued invoices and contracts, customer data, credentials.
- **Corrections to the scan:** [[FILL: files the scan put in the wrong zone, or "none"]]

## 3. Rules for this upgrade
1. A verified backup exists before any file outside the safe zone is changed.
2. Finished historical records are not edited, moved or renamed. Live data the system still writes to is backed up, never set read-only, and migrated only with a tested rollback.
3. Existing valid inputs give the same results after a change, unless a correction is intended and stated.
""",
        "01-FORENSIC-XRAY-AND-LEAKS.md": f"""# 01. Inventory, root vision and gaps — {project_name}

{note}

## 1. Measured inventory
- **Files scanned:** `{xray['total_files']}` (`{xray['total_kb']} KB`), max folder depth `{xray['max_depth']}`
- **File types:** {ext_str}
- **Duplicate or version-named files (`{xray['entropy_count']}`):**
{entropy_list}

## 2. The owner's vision, in their words
- **What they originally wanted:** [[FILL: the owner's answer]]
- **Wanted but never built:** [[FILL: the owner's answer]]
- **Must stay as it is:** [[FILL: the owner's answer]]
- **Chosen path:** [[FILL: the path the owner chose, or the one you chose when they delegated, with the reason]]

## 3. Gap matrix
> Leave a bucket empty (N/A) when nothing belongs in it.

| Bucket | What belongs here, with file evidence | Action |
| :--- | :--- | :--- |
| **Keep** | [[FILL: parts that already serve the vision]] | Protect |
| **Built wrong** | [[FILL: parts that drifted or were built poorly]] | Quick fix or careful refactor |
| **Never built** | [[FILL: vision items with no implementation]] | Build |
| **Beyond expectation** | [[FILL: additions the owner did not ask for, and why they matter]] | Add the few that are cheap and matter |

## 4. Silent leaks
> Evidence must point at real files or behaviour. Delete a row that has no evidence; add rows for other leaks.

| Leak | Evidence | Cost if left | Remedy |
| :--- | :--- | :--- | :--- |
| Time lost to manual work | [[FILL: evidence]] | [[FILL: cost]] | [[FILL: remedy]] |
| Money leaking | [[FILL: evidence]] | [[FILL: cost]] | [[FILL: remedy]] |
| Changing values hard-coded in files | [[FILL: evidence]] | [[FILL: cost]] | [[FILL: remedy]] |
| One failure can lose data | [[FILL: evidence]] | [[FILL: cost]] | [[FILL: remedy]] |
""",
        "02-KANO-UPGRADE-SPEC.md": f"""# 02. Upgrade spec and acceptance — {project_name}

{note}

## 1. Fixes (what was built wrong)
- [ ] **FIX-01:** [[FILL: fix, naming the files]]

## 2. Builds (what was never built)
- [ ] **BUILD-01:** [[FILL: build item]]

## 3. Beyond-expectation additions
- [ ] **ADD-01:** [[FILL: addition + why it matters to this owner]]

## 4. Acceptance and parity
| ID | Component | Measurable target | How it stays healthy for 12 months | Proof (parity test or check) |
| :--- | :--- | :--- | :--- | :--- |
| `FIX-01` | [[FILL: component]] | [[FILL: target]] | [[FILL: durability]] | [[FILL: proof]] |
| `BUILD-01` | [[FILL: component]] | [[FILL: target]] | [[FILL: durability]] | [[FILL: proof]] |
""",
        "03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md": f"""# 03. Upgrade architecture and routine — {project_name}

{note}

## 1. Where things live after the upgrade
- **Values that change (prices, rates, rules):** [[FILL: the one editable place, and who edits it]]
- **Core logic:** [[FILL: the modules, sheets or steps that form the core]]
- **Outputs:** [[FILL: what people see or receive]]
- **History:** [[FILL: where finished records are and how they are protected in place]]

## 2. Decisions and their reasons
- **Upgrade approach:** improve around what works; nothing historical is deleted or moved without the owner's agreement.
- **Medium:** [[FILL: the tool the daily operators use, what was chosen, and why]]
- **Folder organisation:** [[FILL: leave as is, or the reorganisation the owner agreed to]]

## 3. Routine after the upgrade
1. **Normal use:** [[FILL: the real steps, with rough times]]
2. **Changing a price or rule:** [[FILL: where to edit and how to check it]]
3. **Regular check:** [[FILL: the exact check and what "healthy" means here]]
""",
        "04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md": f"""# 04. Upgrade slices and 12-month roadmap — {project_name}

{note}

## 1. Slices
> Rename, add or remove slices to fit; keep `REVIEW-STATE.json` slices in step.

- **Slice 1 (Verified backup, finished records protected in place):** [[FILL: where the backup is, how it was verified, which records are protected]]
- **Slice 2 (The owner's biggest pain or heaviest flow):** [[FILL: scope + verification]]
- **Slice 3 (Remaining gaps and beyond-expectation additions):** [[FILL: which items + verification]]
- **Slice 4 (Parity checks and handover):** [[FILL: parity cases + rollback test]]

## 2. 12-month roadmap
> Drop horizons this system will not reach.

| When | What to expect | What protects the owner | What the owner does |
| :--- | :--- | :--- | :--- |
| **Day 1** | [[FILL: state]] | [[FILL: protection]] | [[FILL: action]] |
| **Month 1** | [[FILL: state]] | [[FILL: protection]] | [[FILL: action]] |
| **Month 3** | [[FILL: state]] | [[FILL: protection]] | [[FILL: action]] |
| **Month 6** | [[FILL: state]] | [[FILL: protection]] | [[FILL: action]] |
| **Month 12** | [[FILL: state]] | [[FILL: protection]] | [[FILL: action]] |
""",
        "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md": f"""# 05. Critique scorecard, health checks and rollback — {project_name}

{note}

## 1. Before/after scorecard
> From a real critique pass (an isolated subagent in DEEP mode). Internal summary; do not inflate it. "After" is the plan once the flaws found are fixed. See references/03.

| Angle | Before | Flaw found (evidence) | After | Fix |
| :--- | :---: | :--- | :---: | :--- |
| **Product / UX (20)** | [[FILL: /20]] | [[FILL: flaw]] | [[FILL: /20]] | [[FILL: fix]] |
| **Systems / architecture (20)** | [[FILL: /20]] | [[FILL: flaw]] | [[FILL: /20]] | [[FILL: fix]] |
| **Field expert (15)** | [[FILL: /15]] | [[FILL: flaw]] | [[FILL: /15]] | [[FILL: fix]] |
| **Money / time (15)** | [[FILL: /15]] | [[FILL: flaw]] | [[FILL: /15]] | [[FILL: fix]] |
| **Risk / operations (15)** | [[FILL: /15]] | [[FILL: flaw]] | [[FILL: /15]] | [[FILL: fix]] |
| **Daily operator (15)** | [[FILL: /15]] | [[FILL: flaw]] | [[FILL: /15]] | [[FILL: fix]] |

- **TOTAL BASELINE SCORE:** [[FILL: sum]] / 100
- **TOTAL UPGRADED SCORE:** [[FILL: sum]] / 100

## 2. Checks that keep it healthy
1. **Parity check:** [[FILL: the past cases re-run on the upgraded version, and the command or steps to repeat it]]
2. [[FILL: another check, or N/A]]

## 3. Rollback and re-review
- **Rollback:** [[FILL: where the backup is and the exact steps to restore it]]
- **Re-review prompt (paste every 1–3 months):**
```text
/apex-improve Read IMPROVEMENT-LOG.md and the last months of use for {project_name}. Compare with the baseline and propose the next improvements with the best return on effort.
```
""",
    }


def legacy_ledger_version(state_path: str):
    """Schema version of an existing ledger written by APEX before v4, else None."""
    if not os.path.isfile(state_path):
        return None
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            version = str(json.load(f).get("schema_version", "") or "unknown")
        return None if int(version.split(".")[0]) >= 4 else version
    except Exception:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Run Forensic X-Ray Scan & Scaffold APEX Review Ledger")
    parser.add_argument("--dir", default=".", help="Target product or workspace directory to scan")
    parser.add_argument("--name", required=True, help="Target product/workspace name")
    parser.add_argument(
        "--domain",
        default="DOM-01",
        help="Archetype ID (DOM-01..DOM-07) or any free-text field/context, e.g. 'family dental clinic, Da Nang'",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing review ledger files")
    parser.add_argument(
        "--lean",
        action="store_true",
        help="LEAN mode: create only _apex/TRACE.md and _apex/STATE.json (no ledger documents)",
    )
    parser.add_argument(
        "--scan-only",
        action="store_true",
        help="Turn 1: print the X-Ray inventory and write nothing into the user's workspace",
    )
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # cp1252 consoles crash on paths like 'Từ idea'
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    target_root = os.path.abspath(args.dir)
    if not os.path.isdir(target_root):
        print(f"[ERROR] Target directory does not exist: {target_root}")
        sys.exit(1)

    print("=" * 76)
    print(f"APEX v4.4 FORENSIC X-RAY SCANNER | TARGET: {target_root}")
    print("=" * 76)
    xray = scan_workspace(target_root)
    print(f"  - Total Files Scanned : {xray['total_files']} ({xray['total_kb']} KB, max depth {xray['max_depth']})")
    print(f"  - Entropy/Dup Signals : {xray['entropy_count']} files matching v1/v2/copy/final patterns")
    print(
        f"  - Blast-Radius Zones  : Green={xray['zones']['counts']['green']} | "
        f"Yellow={xray['zones']['counts']['yellow']} | Red={xray['zones']['counts']['red']}"
    )
    print()
    for label, key in (("Red-Zone files", "red_immutable"), ("Yellow-Zone files", "yellow_tested")):
        if xray["zones"][key]:
            print(f"  {label}: " + ", ".join(xray["zones"][key]))
    if xray["entropy_files"]:
        print("  Duplicate/version files: " + ", ".join(xray["entropy_files"]))

    for sub_dir, state_name in (("apex-blueprint", "STATE.json"), ("apex-review", "REVIEW-STATE.json")):
        found = os.path.join(target_root, "docs", sub_dir)
        if os.path.isdir(found):
            old = legacy_ledger_version(os.path.join(found, state_name))
            note = f"older APEX version (schema {old}): read for context, do not trust its scores" if old else "current APEX ledger"
            print(f"  Earlier APEX files: docs/{sub_dir}/ -> {note}")
    if os.path.isdir(os.path.join(target_root, "_apex")):
        print("  Earlier APEX files: _apex/ -> an existing trace; continue it instead of starting over")

    if args.scan_only:
        print("\n[SCAN-ONLY] Nothing was written. Read the files themselves for findings; scaffold the ledger after the owner replies.")
        return

    today = datetime.date.today().isoformat()

    if args.lean:
        lean_dir = os.path.join(target_root, "_apex")
        os.makedirs(lean_dir, exist_ok=True)
        full = build_review_state(args.name, args.domain, today, xray)
        keep = ("schema_version", "target_name", "domain_primary", "domain_label", "created_at", "last_updated",
                "xray_summary", "context_profile", "change_scenarios", "change_scenarios_required",
                "change_scenarios_waiver")
        lean_state = {"mode": "LEAN", **{k: full[k] for k in keep if k in full}}
        files = {
            "STATE.json": json.dumps(lean_state, ensure_ascii=False, indent=2),
            "TRACE.md": build_review_templates(args.name, args.domain, today, xray)["TRACE.md"],
        }
        for filename, content in files.items():
            filepath = os.path.join(lean_dir, filename)
            if not os.path.exists(filepath) or args.force:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[CREATED] {filepath}")
            else:
                print(f"[SKIPPED] {filepath} (already exists)")
        print(f"\n[SUCCESS] LEAN trace initialized at: {lean_dir}")
        return

    review_dir = os.path.join(target_root, "docs", "apex-review")
    old = legacy_ledger_version(os.path.join(review_dir, "REVIEW-STATE.json"))
    if old and not args.force:
        print(f"\n[LEGACY] {review_dir} was written by an older APEX version (schema {old}).")
        print("  Its templates were pre-filled, so the gates cannot use it. Nothing was changed.")
        print("  Recommended: re-run with --lean to start a fresh trace in _apex/ and keep the old ledger as context.")
        print("  To replace it, move it aside first (for example to docs/apex-review-legacy/), or pass --force.")
        sys.exit(1)
    os.makedirs(review_dir, exist_ok=True)

    state_path = os.path.join(review_dir, "REVIEW-STATE.json")
    if not os.path.exists(state_path) or args.force:
        state_data = build_review_state(args.name, args.domain, today, xray)
        with open(state_path, "w", encoding="utf-8") as f:
            json.dump(state_data, f, ensure_ascii=False, indent=2)
        print(f"[CREATED] {state_path}")
    else:
        print(f"[SKIPPED] {state_path} (already exists, use --force to overwrite)")

    templates = build_review_templates(args.name, args.domain, today, xray)
    for filename, content in templates.items():
        filepath = os.path.join(review_dir, filename)
        if not os.path.exists(filepath) or args.force:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[CREATED] {filepath}")
        else:
            print(f"[SKIPPED] {filepath} (already exists)")

    print(f"\n[SUCCESS] Forensic Review Ledger initialized at: {review_dir}")
    print("=" * 76)
    print("[LEDGER SCAFFOLDED] Fill every [[FILL: ...]] marker from the owner's answers and file evidence.")
    print("  Use --scan-only on Turn 1; scaffold only after the owner has shared their root vision.")
    print("=" * 76)


if __name__ == "__main__":
    main()
