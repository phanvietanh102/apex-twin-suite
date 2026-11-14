#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Product, App & Workspace Reviewer (v3.5) — Automated Forensic X-Ray & Ledger Scaffolder (xray_scanner.py)
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

IGNORE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".agents", ".claude", "apex-review", "apex-blueprint"}
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

            ext = os.path.splitext(fname)[1].lower() or "(no-ext)"
            ext_counts[ext] += 1

            if ENTROPY_REGEX.search(fname):
                entropy_files.append(rel_path)

            if ext in RED_EXTS or any(k in fname.lower() for k in ("hoa_don", "hoadon", "invoice", "baogia", "contract", "secret")):
                red_zone.append(rel_path)
            elif ext in YELLOW_EXTS:
                yellow_zone.append(rel_path)
            else:
                green_zone.append(rel_path)

    baseline_score = max(35, min(72, 75 - len(entropy_files) * 3 - (5 if max_depth > 5 else 0)))
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
        "estimated_baseline_score": baseline_score,
    }


def build_review_state(project_name: str, domain_key: str, today: str, xray: dict) -> dict:
    return {
        "schema_version": "3.5.0-apex-review",
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
        # Heuristic from file entropy only — confirm in Phase 3. The upgraded score is set
        # by the Phase 3 critique, never by the scaffolder.
        "baseline_health_score": xray["estimated_baseline_score"],
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
                "name": "Pre-Flight Snapshot Backup & Red-Zone Quarantine",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-2",
                "name": "Tier-B Volatility Extraction & Workspace/Code Hygiene",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-3",
                "name": "30% Kano Modernization Delighters & Automation",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-4",
                "name": "Behavioral Parity Regression Tests & 365-Day Immunity Runbook",
                "status": "pending",
                "verification_proof": None,
            },
        ],
    }


def build_review_templates(project_name: str, domain_key: str, today: str, xray: dict) -> dict:
    domain_label = DOMAIN_MAP.get(domain_key, domain_key)
    zc = xray["zones"]["counts"]
    ext_str = ", ".join(f"`{k}` ({v})" for k, v in xray["top_extensions"].items()) or "None"
    entropy_list = "\n".join(f"  - `{p}`" for p in xray["entropy_files"][:8]) or "  - None detected in top-level scan"

    return {
        "TRACE.md": f"""# TRACE — {project_name}
> Every Turn-1 finding, every gap-matrix item, every wish the owner stated and every need discovered (completeness lenses, domain brief) gets a row. Rows never disappear; update them.
> Status: OPEN while working; final = DONE (evidence) / DEFERRED (reason + when) / DROPPED (owner agreed — quote) / N/A (why). Order rows by weight. A High row (law, safety, money at risk, irreversible data, root vision, #1 pain) may be DEFERRED only with evidence `agreed: "<user's words>"`. See references/08.

| ID | Need / Finding | Source | Weight | Status | Evidence / Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Verified backup of current state + history locked read-only | discovered (safety) | High | OPEN | |
| R-02 | [[FILL: the owner's biggest pain or heaviest flow]] | owner | High | OPEN | |
""",
        "00-PRESERVATION-CONSTITUTION.md": f"""# 00. Preservation Constitution & Blast-Radius Contract — {project_name}
> **Audited On:** {today} | **Domain Archetype:** `{domain_key}` ({domain_label})
> **Immunity Contract:** 12-Month Evergreen Evolution (Zero Data Loss / Zero Habit Breakage)

> Every `[[FILL: ...]]` marker is filled from the user's Step 1B answers. `review_gate_audit.py` vetoes a gate while any marker remains.

## 1. Sacred Workflows & Muscle-Memory Habits (Must Not Break)
- **Sacred Habit 1:** [[FILL: habit/asset the user named in Step 1B Q4]]
- **Sacred Habit 2:** [[FILL: habit/asset the user named in Step 1B Q4]]
- **Always Sacred:** Never alter historical customer records, issued invoices, or completed project files.

## 2. Blast-Radius Zoning Map (Green / Yellow / Red Zones)
- **Green Zone ({zc['green']} files — Safe to Modernize):** Docs, UI polish, new export templates, static assets.
- **Yellow Zone ({zc['yellow']} files — Test-Protected Refactor):** Scripts, business logic, active templates.
- **Red Zone ({zc['red']} files — 100% Immutable / Snapshot Quarantine):** Historical invoices/records, databases, credentials.

## 3. Non-Breaking Invariants
1. **Invariant 1 (Pre-Flight Backup):** Every Yellow/Red Zone modification is preceded by a verified backup snapshot.
2. **Invariant 2 (3-Tier Volatility Extraction):** Hardcoded prices/rules/prompts are extracted into Tier-B Config without changing historical outputs.
3. **Invariant 3 (Behavioral Parity):** Existing valid inputs must produce 100% matching deterministic calculations before and after refactoring.
""",
        "01-FORENSIC-XRAY-AND-LEAKS.md": f"""# 01. Automated Forensic X-Ray & Silent Leak Report — {project_name}

## 1. Automated X-Ray Telemetry Summary
- **Total Files Scanned:** `{xray['total_files']}` files (`{xray['total_kb']} KB`) | **Max Directory Depth:** `{xray['max_depth']}`
- **File Extension Distribution:** {ext_str}
- **Manual Version / Entropy Files Detected (`{xray['entropy_count']}` files):**
{entropy_list}

## 2. Root-Vision Elicitation & 4-Column Vision-vs-Reality Gap Matrix
- **Original Root Vision (From Scratch Interview):** [[FILL: the user's Step 1B answer, in their words]]
- **Unbuilt Ideas & Wild Ambitions:** [[FILL: Step 1B Q2 answer]]
- **Sacred Elements to Keep:** [[FILL: Step 1B Q4 answer]]
- **Selected A-to-Z Evolution Path:** [[FILL: option A/B/C/D the USER chose after seeing Pros/Cons/Best-Fit]]

| Gap Bucket | Root Vision vs. Current Workspace Reality | Action in A-to-Z Pipeline |
| :--- | :--- | :--- |
| **1. Met & Healthy (`KEEP & PROTECT`)** | [[FILL: specific files/modules that already serve the vision]] | Preserve 100% & wrap cleanly |
| **2. Built Wrong / Drifted (`REALIGN & REFACTOR`)** | [[FILL: specific parts built wrong, with file evidence]] | 15-Min Quick-Win Patch + Surgical 3-Tier Refactor |
| **3. Unbuilt Core Vision (`MISSING A-TO-Z BUILD`)** | [[FILL: specific vision items with no implementation]] | Full Greenfield A-to-Z Engineering |
| **4. 30% Beyond-Expectation (`KANO DELIGHTERS`)** | [[FILL: delighters the user did not ask for, and why they will surprise]] | Inject high-ROI delight features |

## 3. Johari Silent Leak Radar (4 Hidden System Leaks)
> Evidence must point at real files or behaviour found in the X-Ray. Leave a leak out rather than invent evidence.

| # | Silent Leak Category | Forensic Evidence in {project_name} | 12-Month Impact If Unfixed | Engineered Remedy |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Cognitive & Time Bleed** | [[FILL: file/behaviour evidence]] | [[FILL: impact]] | [[FILL: remedy]] |
| 2 | **Unit Economics / Revenue Leak** | [[FILL: file/behaviour evidence]] | [[FILL: impact]] | [[FILL: remedy]] |
| 3 | **Hardcoded Volatility Rot** | [[FILL: file/behaviour evidence]] | [[FILL: impact]] | [[FILL: remedy]] |
| 4 | **Catastrophic Fragility** | [[FILL: file/behaviour evidence]] | [[FILL: impact]] | [[FILL: remedy]] |
""",
        "02-KANO-UPGRADE-SPEC.md": f"""# 02. Three-Tier Kano Modernization Specification & SMART-ER Contract — {project_name}

## 1. Tier 1 — Critical Debt & Leak Remediation (50% Effort)
- [ ] **FIX-01:** [[FILL: fix for a Bucket-2 gap, naming the files]]
- [ ] **FIX-02:** [[FILL: fix for a Bucket-2 gap, naming the files]]
- [ ] **FIX-03:** [[FILL: fix for a Bucket-2 gap, naming the files]]

## 2. Tier 2 — 10x Workflow & Hygiene Multipliers (20% Effort)
- [ ] **MUL-01:** [[FILL: multiplier or Bucket-3 build item]]
- [ ] **MUL-02:** [[FILL: multiplier or Bucket-3 build item]]

## 3. Tier 3 — Asymmetric Modernization Delighters (30% Beyond-Expectation Features)
- [ ] **DEL-01:** [[FILL: Bucket-4 delighter + why it is beyond this user's expectation]]
- [ ] **DEL-02:** [[FILL: Bucket-4 delighter + why it is beyond this user's expectation]]
- [ ] **DEL-03:** [[FILL: Bucket-4 delighter + why it is beyond this user's expectation]]

## 4. SMART-ER Upgrade & Behavioral Parity Contract
| ID | Target Component | Specific & Measurable Target (S/M) | 12-Month Immunity (R) | Behavioral Parity Proof (E) |
| :--- | :--- | :--- | :--- | :--- |
| `FIX-01` | [[FILL: component]] | [[FILL: measurable target]] | [[FILL: how it stays healthy]] | [[FILL: parity test/check]] |
| `FIX-02` | [[FILL: component]] | [[FILL: measurable target]] | [[FILL: how it stays healthy]] | [[FILL: parity test/check]] |
| `DEL-01` | [[FILL: component]] | [[FILL: measurable target]] | [[FILL: how it stays healthy]] | [[FILL: parity test/check]] |
""",
        "03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md": f"""# 03. Strangler-Fig Evolution Architecture & Workspace Hygiene — {project_name}

## 1. Three-Tier Decoupled Extraction Architecture
```
+-----------------------------------------------------------------------+
| TIER C: Upgraded Adapters & Delight Outputs (PDF/XLSX/UI/AIO Schema)  |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
| TIER A: Cleaned Core Engine (Deterministic Logic + Parity Protection) |
+-----------------------------------------------------------------------+
                  ^                                  |
                  | (Reads Live Rates)               v (Writes Immutable Copy)
+----------------------------------+   +--------------------------------+
| TIER B: 2-Min Editable Config    |   | RED ZONE: Immutable Archive    |
+----------------------------------+   +--------------------------------+
```

## 2. Architecture Decision Records (ADRs for Brownfield Evolution)
- **ADR-01 (Strangler-Fig Non-Destructive Wrapping):** Wrap and upgrade workflows without deleting historical assets.
- **ADR-02 (Single Source of Truth Config):** Consolidate scattered parameters into Tier B (`00-CONFIG-AND-TEMPLATES`).
- **ADR-03 (5-Zone Workspace Taxonomy):** Separate Config (`00`), Active (`01`), Tools (`02`), Archive (`03`), and Exports (`04`).

## 3. Upgraded Daily Operator SOP (< 10 Minutes/Day)
1. **Daily Execution:** [[FILL: the real daily steps after the upgrade, with times]]
2. **Price/Rule Change:** [[FILL: which Tier-B file/sheet to edit and how to verify]]
3. **Weekly Hygiene:** [[FILL: the exact check/command and what "clean" means here]]
""",
        "04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md": f"""# 04. Surgical 4-Slice Migration Plan & 365-Day Immunity Roadmap — {project_name}

## 1. Surgical Non-Destructive Execution Slices
- **Slice 1 (Pre-Flight Backup & Red-Zone Quarantine):** [[FILL: exact backup target + which Red-Zone files are locked]]
- **Slice 2 (Tier-B Config Extraction & Taxonomy Cleanup):** [[FILL: concrete scope + verification]]
- **Slice 3 (30% Kano Modernization Delighters):** [[FILL: which DEL-xx items + verification]]
- **Slice 4 (Behavioral Parity Verification & Handover):** [[FILL: parity cases + rollback test]]

## 2. The 365-Day Post-Upgrade Immunity Horizon
| Milestone | System State | Built-In Immunity Mechanism | Operator Effort |
| :--- | :--- | :--- | :--- |
| **Day 1** | Surgical upgrade live; zero downtime | Pre-flight backup + parity tests passed | Immediate daily use |
| **Day 30** | First monthly rate/rule adjustment | Edit Tier-B Config without duplicating files | 2 mins config edit |
| **Day 90** | Q1 completed operations accumulated | Move Q1 snapshots to `03-IMMUTABLE-ARCHIVE` | 5 mins Q1 archive |
| **Day 180** | Mid-year market or platform shift | Decoupled adapter layer + `schema_version` | 15 mins Mid-Year AI Audit |
| **Day 365** | 12 months of zero-rewrite operation | 1-Click Annual Summary & Archive | Seamless Year-2 transition |
""",
        "05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md": f"""# 05. C-Suite Before/After Scorecard, Regression Suite & Rollback Runbook — {project_name}

## 1. 6-Role C-Suite Comparative Delta Scorecard (Before vs. After)
> Fill from a real critique pass (ideally an isolated subagent). The X-Ray heuristic baseline below is `[Assumption to Confirm]`; it only counts file entropy.

| C-Suite Auditor Role | Baseline Score (Before) | Forensic Flaw Found | Upgraded Score (After) | Engineered Fix |
| :--- | :---: | :--- | :---: | :--- |
| **CPO (UX & Friction)** | [[FILL: /20]] | [[FILL: flaw with evidence]] | [[FILL: /20]] | [[FILL: fix]] |
| **CTO (Debt & Coupling)** | [[FILL: /20]] | [[FILL: flaw with evidence]] | [[FILL: /20]] | [[FILL: fix]] |
| **VP Domain (`{domain_key}`)** | [[FILL: /15]] | [[FILL: flaw with evidence]] | [[FILL: /15]] | [[FILL: fix]] |
| **CFO (Time & Unit Econ)** | [[FILL: /15]] | [[FILL: flaw with evidence]] | [[FILL: /15]] | [[FILL: fix]] |
| **CRO/COO (Risk & Entropy)** | [[FILL: /15]] | [[FILL: flaw; X-Ray found {xray['entropy_count']} entropy files]] | [[FILL: /15]] | [[FILL: fix]] |
| **Daily Operator User** | [[FILL: /15]] | [[FILL: flaw with evidence]] | [[FILL: /15]] | [[FILL: fix]] |

- **X-Ray Heuristic Baseline:** {xray['estimated_baseline_score']}/100 `[Assumption to Confirm]`
- **TOTAL BASELINE SCORE:** [[FILL: sum]] / 100
- **TOTAL UPGRADED SCORE:** [[FILL: sum]] / 100 (Gate 3 requires >= 85)

## 2. Automated Fitness & Behavioral Parity Checks
1. **FF-01 (Parity Regression Check):** Historical inputs produce 100% accurate outputs on upgraded engine.
2. **FF-02 (Anti-Entropy Guard):** Zero unorganized `v1/v2/copy` clutter in active core directories.
3. **FF-03 (Config Integrity Guard):** Validates Tier-B config bounds before execution.

## 3. 1-Click Rollback & Quarterly Drift Audit Prompt
- **Emergency Rollback (< 60 seconds):** Restore pre-upgrade snapshot manifest from backup archive.
- **Quarterly 15-Minute Drift Audit Prompt:**
```text
/apex-review Read docs/apex-review/ and REVIEW-STATE.json for {project_name}.
Audit workspace hygiene after 90 days of operation against 00-PRESERVATION-CONSTITUTION.md and propose Tier-B configuration optimizations without disrupting Sacred Habits.
```
""",
    }


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
    print(f"APEX v3.5 FORENSIC X-RAY SCANNER | TARGET: {target_root}")
    print("=" * 76)
    xray = scan_workspace(target_root)
    print(f"  - Total Files Scanned : {xray['total_files']} ({xray['total_kb']} KB, max depth {xray['max_depth']})")
    print(f"  - Entropy/Dup Signals : {xray['entropy_count']} files matching v1/v2/copy/final patterns")
    print(
        f"  - Blast-Radius Zones  : Green={xray['zones']['counts']['green']} | "
        f"Yellow={xray['zones']['counts']['yellow']} | Red={xray['zones']['counts']['red']}"
    )
    print(f"  - Est. Baseline Score : {xray['estimated_baseline_score']} / 100 (heuristic, entropy only)\n")
    for label, key in (("Red-Zone files", "red_immutable"), ("Yellow-Zone files", "yellow_tested")):
        if xray["zones"][key]:
            print(f"  {label}: " + ", ".join(xray["zones"][key]))
    if xray["entropy_files"]:
        print("  Duplicate/version files: " + ", ".join(xray["entropy_files"]))

    if args.scan_only:
        print("\n[SCAN-ONLY] Nothing was written. Read the files themselves for findings; scaffold the ledger after the owner replies.")
        return

    review_dir = os.path.join(target_root, "docs", "apex-review")
    os.makedirs(review_dir, exist_ok=True)
    today = datetime.date.today().isoformat()

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
