#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APEX Idea-to-Product — Project Blueprint Scaffolder (init_project.py)
Scaffolds the persistent 6-document Project Memory Ledger + STATE.json
to prevent AI context drift and enforce the 12-Month Evergreen Guarantee.
"""

import argparse
import datetime
import json
import os
import sys

DOMAIN_MAP = {
    "DOM-01": "Software, SaaS & AI Agents",
    "DOM-02": "Construction, Architecture & Real Estate",
    "DOM-03": "Content, SEO, AIO (GEO) & Digital Media",
    "DOM-04": "E-Commerce, Retail, D2C & Billing/Supply Chain",
    "DOM-05": "B2B Services, Agency, Consulting & Internal Operations OS",
    "DOM-06": "Regulated & High-Trust Domains (FinTech, EdTech, Legal, Healthcare)",
    "DOM-07": "Hardware, IoT & Physical-Digital Hybrid Systems",
}


def build_state_json(project_name: str, domain_key: str, today: str) -> dict:
    return {
        "schema_version": "4.4.0-apex",
        "project_name": project_name,
        "domain_primary": domain_key,
        "domain_label": DOMAIN_MAP.get(domain_key, domain_key),
        "created_at": today,
        "last_updated": today,
        "current_phase": "Phase 1: Discovery & Elicitation",
        "c_suite_audit_score": 0,
        "evergreen_horizon_months": 12,
        "locked_decisions": [],
        "active_slice": "Slice 1",
        "slices": [
            {
                "id": "slice-1",
                "name": "Heaviest flow, working end to end",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-2",
                "name": "Remaining must-haves",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-3",
                "name": "Beyond-expectation additions",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-4",
                "name": "Hardening, backup and handover",
                "status": "pending",
                "verification_proof": None,
            },
        ],
        "volatile_configs_isolated": [],
        "known_risks_mitigated": [],
        # 12-month change scenarios (see references/08): {"id", "event", "expected", "status": "pass"|"fail", "proof"}
        "change_scenarios": [],
        # Lower only for one-off or low-stakes work, with a reason (references/08 §4).
        "change_scenarios_required": 3,
        "change_scenarios_waiver": "",
        # Context profile (references/07 Step 0): rules not activated here are N/A with a reason.
        "context_profile": {"a_money_with_parties": None, "b_personal_data": None, "c_regulated": None,
                            "d_others_operate": None, "e_controls_for_others": None, "f_replaces_existing": None,
                            "g_long_lived": None, "h_established_trade": None, "i_stakes": None},
    }


def get_templates(project_name: str, domain_key: str, today: str) -> dict:
    domain_label = DOMAIN_MAP.get(domain_key, domain_key)
    note = "> Every `[[FILL: ...]]` marker is a decision drawn from the user's answers or from evidence. The gate script vetoes a gate while any marker remains.\n> Add or remove rows and items to fit. If an item does not apply, replace its marker with `N/A` and a short reason, or delete the row. Never invent content to fill a row.\n> You may rewrite headings and text in the user's language."
    return {
        "TRACE.md": f"""# TRACE — {project_name}
> Every need the user stated, every need discovered (completeness lenses, domain brief), and every question whose answer creates work gets a row. Rows never disappear; update them.
> Status: OPEN while working; final = DONE (evidence) / DEFERRED (reason + when) / DROPPED (user agreed — quote) / N/A (why). Order rows by weight. A High row (law, safety, money at risk, irreversible data, root vision, #1 pain) may be DEFERRED only with evidence `agreed: "<user's words>"`. Keep the Status and Weight codes in English (OPEN/DONE/DEFERRED/DROPPED/N/A, High/Medium/Low) even if the rest is in the user's language. See references/08.

| ID | Need | Source | Weight | Status | Evidence / Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | [[FILL: the heaviest flow the user needs (most volume/money/risk)]] | user | High | OPEN | |
""",
        "00-PROJECT-CONSTITUTION.md": f"""# 00. Goal, constraints and rules — {project_name}
> Created {today} | Field: {domain_label}

{note}

## 1. Who it is for and what it must do
- **User and daily operator:** [[FILL: who uses it and who operates it, in the user's words]]
- **Job to be done:** [[FILL: "When <situation>, they want to <progress>, so they can <outcome> without <current pain>."]]
- **The user's own ideas:** [[FILL: ideas the user brought that you did not suggest]]

## 2. Constraints
- **Budget:** [[FILL: one-off and recurring limits]]
- **Time and people:** [[FILL: who maintains it and how much time they have]]
- **Tools and devices:** [[FILL: what the daily operators already use; the chosen medium and why]]

## 3. Out of scope for now
- [[FILL: one thing deliberately not built in this version, and why]]

## 4. Design rules that must hold
- Values that change over time (prices, rates, rules, prompts) live in one editable place, not inside core logic.
- Records already issued or saved are not altered by later changes to those values.
- A slice counts as done only with proof that it works.
- [[FILL: any rule specific to this project, or N/A]]
""",
        "01-DISCOVERY-AND-PRFAQ.md": f"""# 01. Decisions, field traps and the finished picture — {project_name}

{note}

## 1. Decisions taken in discovery
- [[FILL: decision + the user's reason]]
- [[FILL: decision + the user's reason]]

## 2. Field-specific traps
> From the domain brief for this field and place. Each must be something this user did not mention. Generic rows such as "prices change" do not count.

| Trap | What it costs if ignored | How this project handles it |
| :--- | :--- | :--- |
| [[FILL: trap]] | [[FILL: cost]] | [[FILL: countermeasure]] |
| [[FILL: trap]] | [[FILL: cost]] | [[FILL: countermeasure]] |

## 3. The finished result, as a short announcement
- **Headline:** [[FILL: "{project_name} lets <audience> achieve <outcome>"]]
- **Problem it removes:** [[FILL: the pains the user actually described]]
- **What makes it more than expected:** [[FILL: the additions chosen in 02]]

## 4. Hardest questions, answered honestly
- **From a customer or user:** [[FILL: question and honest answer]]
- **From operations:** [[FILL: what happens when the riskiest dependency fails]]
""",
        "02-KANO-SPEC-AND-DELIGHT.md": f"""# 02. Feature spec and acceptance — {project_name}

{note}

## 1. Must-haves
- [ ] **MB-01:** [[FILL: must-have tied to the job to be done]]
- [ ] **MB-02:** [[FILL: must-have]]

## 2. Multipliers (remove repeated manual work)
- [ ] **PM-01:** [[FILL: multiplier]]

## 3. Beyond-expectation additions
> Something the user did not ask for and would not have known to ask for, cheap to build and to maintain. Say why it matters to this user.

- [ ] **DL-01:** [[FILL: addition + why it matters to this user]]

## 4. Acceptance criteria
| ID | Requirement | Measurable target | How it holds up for 12 months | Proof (test, check or walk-through) |
| :--- | :--- | :--- | :--- | :--- |
| `MB-01` | [[FILL: requirement]] | [[FILL: target]] | [[FILL: durability]] | [[FILL: proof]] |
| `DL-01` | [[FILL: requirement]] | [[FILL: target]] | [[FILL: durability]] | [[FILL: proof]] |
""",
        "03-ARCHITECTURE-AND-SOPS.md": f"""# 03. Architecture and operator routine — {project_name}

{note}

## 1. Where things live
- **Values that change (prices, rates, rules, prompts):** [[FILL: the one editable place, and who edits it]]
- **Core logic:** [[FILL: the modules, sheets or steps that form the core]]
- **Outputs and interfaces:** [[FILL: what people see or receive]]
- **History:** [[FILL: how saved or issued records are protected from later edits]]

## 2. Decisions and their reasons
- **Medium and stack:** [[FILL: what was chosen, the alternative rejected, and why]]
- **Fallback:** [[FILL: what the operators do if the riskiest dependency fails]]
- **Scale ceiling:** [[FILL: the volume up to which this design needs no rework]]

## 3. Operator routine
1. **Normal use:** [[FILL: the real steps, with rough times]]
2. **Changing a price or rule:** [[FILL: where to edit and how to check it]]
3. **Backup:** [[FILL: the exact action and where the backup goes]]
""",
        "04-12M-EVERGREEN-ROADMAP.md": f"""# 04. Build slices and 12-month roadmap — {project_name}

{note}

## 1. Build slices
> Rename, add or remove slices to fit; keep `STATE.json` slices in step. The heaviest flow comes first.

- **Slice 1 (Heaviest flow, end to end):** [[FILL: scope + how it will be verified]]
- **Slice 2 (Remaining must-haves):** [[FILL: scope + how it will be verified]]
- **Slice 3 (Beyond-expectation additions):** [[FILL: which items + how they will be verified]]
- **Slice 4 (Hardening, backup and handover):** [[FILL: tests, backup and handover deliverables]]

## 2. 12-month roadmap
> Drop horizons this project will not reach.

| When | What to expect | What the design already provides | What the operator does |
| :--- | :--- | :--- | :--- |
| **Week 1** | [[FILL: state]] | [[FILL: capability]] | [[FILL: action]] |
| **Month 1** | [[FILL: state]] | [[FILL: capability]] | [[FILL: action]] |
| **Month 3** | [[FILL: state]] | [[FILL: capability]] | [[FILL: action]] |
| **Month 6** | [[FILL: state]] | [[FILL: capability]] | [[FILL: action]] |
| **Month 12** | [[FILL: state]] | [[FILL: capability]] | [[FILL: action]] |
""",
        "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md": f"""# 05. Critique log, health checks and re-review — {project_name}

{note}

## 1. Critique log
> From a real critique pass (an isolated subagent in DEEP mode). Each row names a flaw found in this plan, not a generic risk. Delete an angle that does not apply.

| Angle | Flaw found | Fix applied | Status |
| :--- | :--- | :--- | :--- |
| **Product** | [[FILL: flaw]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |
| **Systems** | [[FILL: flaw]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |
| **Field expert** | [[FILL: flaw]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |
| **Money** | [[FILL: flaw, with the numbers]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |
| **Risk and operations** | [[FILL: flaw]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |
| **Skeptical daily user** | [[FILL: flaw]] | [[FILL: fix]] | [[FILL: FIXED/OPEN]] |

## 2. Score
> Internal summary of the critique; do not inflate it. See references/03.

- **TOTAL C-SUITE AUDIT SCORE:** [[FILL: sum]] / 100

## 3. Checks that keep it healthy
1. [[FILL: what is checked, and the command or steps that run it]]
2. [[FILL: another check, or N/A]]

## 4. Re-review prompt (paste every 1–3 months)
```text
/apex-audit Read the project ledger and STATE.json for {project_name}. Compare the last months of use with 00 and 02, and propose the changes with the best return on effort.
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
    parser = argparse.ArgumentParser(description="Scaffold APEX Idea-to-Product Blueprint")
    parser.add_argument("--dir", default=".", help="Target project directory")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument(
        "--domain",
        default="DOM-01",
        help="Archetype ID (DOM-01..DOM-07) or any free-text field/context, e.g. 'dental clinic, Da Nang'",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing blueprint files")
    parser.add_argument(
        "--lean",
        action="store_true",
        help="LEAN mode: create only _apex/TRACE.md and _apex/STATE.json (no blueprint documents)",
    )
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # cp1252 consoles crash on paths like 'Từ idea'
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    target_root = os.path.abspath(args.dir)
    today = datetime.date.today().isoformat()

    if args.lean:
        lean_dir = os.path.join(target_root, "_apex")
        os.makedirs(lean_dir, exist_ok=True)
        full = build_state_json(args.name, args.domain, today)
        keep = ("schema_version", "project_name", "domain_primary", "domain_label", "created_at", "last_updated",
                "context_profile", "change_scenarios", "change_scenarios_required", "change_scenarios_waiver")
        lean_state = {"mode": "LEAN", **{k: full[k] for k in keep}}
        files = {
            "STATE.json": json.dumps(lean_state, ensure_ascii=False, indent=2),
            "TRACE.md": get_templates(args.name, args.domain, today)["TRACE.md"],
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

    blueprint_dir = os.path.join(target_root, "docs", "apex-blueprint")
    state_path = os.path.join(blueprint_dir, "STATE.json")
    old = legacy_ledger_version(state_path)
    if old and not args.force:
        print(f"[LEGACY] {blueprint_dir} was written by an older APEX version (schema {old}).")
        print("  Its templates were pre-filled, so the gates cannot use it. Nothing was changed.")
        print("  Recommended: re-run with --lean to start a fresh trace in _apex/ and keep the old ledger as context.")
        print("  To replace it, move it aside first (for example to docs/apex-blueprint-legacy/), or pass --force.")
        sys.exit(1)
    os.makedirs(blueprint_dir, exist_ok=True)


    if not os.path.exists(state_path) or args.force:
        state_data = build_state_json(args.name, args.domain, today)
        with open(state_path, "w", encoding="utf-8") as f:
            json.dump(state_data, f, ensure_ascii=False, indent=2)
        print(f"[CREATED] {state_path}")
    else:
        print(f"[SKIPPED] {state_path} (already exists, use --force to overwrite)")

    templates = get_templates(args.name, args.domain, today)
    for filename, content in templates.items():
        filepath = os.path.join(blueprint_dir, filename)
        if not os.path.exists(filepath) or args.force:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[CREATED] {filepath}")
        else:
            print(f"[SKIPPED] {filepath} (already exists)")

    print(f"\n[SUCCESS] APEX Blueprint Ledger initialized at: {blueprint_dir}")


if __name__ == "__main__":
    main()
