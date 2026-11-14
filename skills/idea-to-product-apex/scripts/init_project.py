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
        "schema_version": "2.0.0-apex",
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
                "name": "Tier-A Immutable Core & Tier-B Externalized Config",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-2",
                "name": "Primary End-to-End Workflow (Must-Be MVP)",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-3",
                "name": "30% Kano Asymmetric Delighters & Automation",
                "status": "pending",
                "verification_proof": None,
            },
            {
                "id": "slice-4",
                "name": "12-Month Fitness Functions, Backup & Bus-Factor-1 Runbook",
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
    return {
        "TRACE.md": f"""# TRACE — {project_name}
> Every need the user stated, every need discovered (completeness lenses, domain brief), and every question whose answer creates work gets a row. Rows never disappear; update them.
> Status: OPEN while working; final = DONE (evidence) / DEFERRED (reason + when) / DROPPED (user agreed — quote) / N/A (why). Order rows by weight. A High row (law, safety, money at risk, irreversible data, root vision, #1 pain) may be DEFERRED only with evidence `agreed: "<user's words>"`. See references/08.

| ID | Need | Source | Weight | Status | Evidence / Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | [[FILL: the heaviest flow the user needs (most volume/money/risk)]] | user | High | OPEN | |
""",
        "00-PROJECT-CONSTITUTION.md": f"""# 00. Project Constitution — {project_name}
> **Generated:** {today} | **Domain Archetype:** `{domain_key}` ({domain_label})
> **Longevity Contract:** 12-Month Evergreen / Zero-Rewrite Guarantee

> Every `[[FILL: ...]]` marker is a decision taken from the user's own answers. `fitness_audit.py` vetoes a gate while any marker remains.

## 1. Core Identity & North Star JTBD (Job-to-be-Done)
- **Target Persona / Operator:** [[FILL: primary user & operator, in the user's words]]
- **Core JTBD Statement:** [[FILL: "When <situation>, the user wants to <progress>, so they can <outcome> without <current pain>."]]
- **User's Own Unique Vision (Section 1 answers):** [[FILL: the personal/contrarian ideas the user gave that no option A/B/C contained]]

## 2. Hard Constraints & Operational Reality
- **Budget & Cost Ceiling:** [[FILL: e.g. < $10/month recurring; zero uncapped variable API bills]]
- **Operational Bus Factor:** [[FILL: e.g. solo operator, max 15 minutes/day routine maintenance]]
- **Tech / Tooling Stack:** [[FILL: chosen stack + one-line reason]]

## 3. Explicit Non-Goals (Scope Guardrails)
1. **Non-Goal 1:** [[FILL: one concrete feature deliberately NOT built in v1, and why]]
2. **Non-Goal 2:** Do NOT hardcode volatile prices, rates, API keys, or seasonal rules inside core logic.
3. **Non-Goal 3:** Do NOT rely on single-point-of-failure external services without an offline/manual fallback.

## 4. Immutable Architectural Invariants (12-Month Laws)
- **Invariant 1 (3-Tier Separation):** Core logic (Tier A) is strictly separated from editable config/prices/prompts (Tier B) and UI/export adapters (Tier C).
- **Invariant 2 (Snapshot Immutability):** Historical transactions/outputs are saved as immutable snapshots; future config edits never corrupt past records.
- **Invariant 3 (Verification First):** Every slice requires objective verification proof before completion.
""",
        "01-DISCOVERY-AND-PRFAQ.md": f"""# 01. Discovery, Blind-Spot Radar & Working Backwards PR/FAQ — {project_name}

## 1. Socratic Elicitation Decisions
- **Q1 (Target Workflow & Scope):** [[FILL: locked option + the user's reason]]
- **Q2 (Operation & Automation Level):** [[FILL: locked option + the user's reason]]
- **Q3 (Monetization / Value Metric):** [[FILL: locked option + the user's reason]]

## 2. Johari Quadrant 4 — Domain Blind-Spot Radar (Unknown-Unknowns)
> Each trap must be specific to `{domain_key}` and to this project — something the user did not mention. Generic rows such as "prices change" do not count.

| # | Hidden Industry Trap (`{domain_key}`) | Impact If Ignored | Built-in Countermeasure in {project_name} |
| :--- | :--- | :--- | :--- |
| 1 | [[FILL: domain-specific trap]] | [[FILL: concrete impact]] | [[FILL: countermeasure]] |
| 2 | [[FILL: domain-specific trap]] | [[FILL: concrete impact]] | [[FILL: countermeasure]] |
| 3 | [[FILL: domain-specific trap]] | [[FILL: concrete impact]] | [[FILL: countermeasure]] |
| 4 | [[FILL: domain-specific trap]] | [[FILL: concrete impact]] | [[FILL: countermeasure]] |

## 3. Working Backwards — Future Press Release (PR)
- **Headline:** [[FILL: "{project_name} lets <audience> achieve <outcome> in <measurable time>"]]
- **Problem:** [[FILL: the two pains the user actually described]]
- **Solution & Asymmetric Edge:** [[FILL: core + the top Kano delighters chosen in 02]]

## 4. Hardest FAQs (Customer & Operational)
- **Customer FAQ 1:** [[FILL: hardest question a real customer would ask, and the honest answer]]
- **Operational FAQ 2:** [[FILL: what happens when the riskiest dependency fails]]
""",
        "02-KANO-SPEC-AND-DELIGHT.md": f"""# 02. Kano Feature Specification & SMART-ER Criteria — {project_name}

## 1. Tier 1 — Must-Be Baseline (Core MVP — 50% Effort)
- [ ] **MB-01:** [[FILL: must-have capability tied to the JTBD]]
- [ ] **MB-02:** [[FILL: must-have capability]]
- [ ] **MB-03:** [[FILL: must-have capability]]

## 2. Tier 2 — Performance Multipliers (10x Efficiency — 20% Effort)
- [ ] **PM-01:** [[FILL: multiplier that removes a repeated manual step]]
- [ ] **PM-02:** [[FILL: multiplier]]

## 3. Tier 3 — Asymmetric Delighters (30% Beyond-Expectation Features)
> A delighter is something the user did not ask for and would not have known to ask for, cheap to build and to maintain. State why it surprises *this* user.

- [ ] **DL-01:** [[FILL: delighter + why it is beyond this user's expectation]]
- [ ] **DL-02:** [[FILL: delighter + why it is beyond this user's expectation]]
- [ ] **DL-03:** [[FILL: delighter + why it is beyond this user's expectation]]

## 4. SMART-ER Acceptance Criteria Contract
| ID | Requirement | Specific & Measurable (S/M) | 12-Month Resilience (R) | Verification Proof (E) |
| :--- | :--- | :--- | :--- | :--- |
| `MB-01` | [[FILL: requirement]] | [[FILL: measurable target]] | [[FILL: how it survives 12 months]] | [[FILL: test or check that proves it]] |
| `MB-02` | [[FILL: requirement]] | [[FILL: measurable target]] | [[FILL: how it survives 12 months]] | [[FILL: test or check that proves it]] |
| `DL-01` | [[FILL: requirement]] | [[FILL: measurable target]] | [[FILL: how it survives 12 months]] | [[FILL: test or check that proves it]] |
""",
        "03-ARCHITECTURE-AND-SOPS.md": f"""# 03. Evolutionary Architecture & Standard Operating Procedures — {project_name}

## 1. Three-Tier Decoupled Architecture
```
+-------------------------------------------------------------------+
| TIER C: Presentation & Adapters (UI, Export PDF/XLSX, AI Wrapper) |
+-------------------------------------------------------------------+
                                 |
                                 v
+-------------------------------------------------------------------+
| TIER A: Immutable Core Engine (Pure Logic, Validation, Snapshots) |
+-------------------------------------------------------------------+
                                 ^
                                 |
+-------------------------------------------------------------------+
| TIER B: Externalized Config & Rules (config.json / Editable Sheet)|
+-------------------------------------------------------------------+
```

- **Tier A for this project:** [[FILL: the actual modules/files that form the core]]
- **Tier B for this project:** [[FILL: the actual volatile values extracted to config, and where they live]]

## 2. Architecture Decision Records (ADRs for 12-Month Longevity)
- **ADR-01 (Stack):** [[FILL: chosen stack, the rejected alternative, and why]]
- **ADR-02 (Externalized Volatility):** All unit prices, rates, templates, and provider settings are isolated in Tier B.
- **ADR-03 (Immutable History):** Every committed record stores its own snapshot of parameters active at creation time.
- **ADR-04 (Upgrade Trigger):** [[FILL: the volume/scale ceiling up to which no architectural upgrade is needed]]

## 3. Daily / Weekly Operator SOP (< 15 Minutes)
1. **Routine Use:** [[FILL: the real daily steps for this product, with times]]
2. **Updating Rates/Rules:** [[FILL: which file/sheet to edit and how to verify]]
3. **Backup Routine:** [[FILL: exact backup command or action and where it goes]]
""",
        "04-12M-EVERGREEN-ROADMAP.md": f"""# 04. Vertical-Slice Execution Plan & 365-Day Evergreen Roadmap — {project_name}

## 1. Vertical-Slice Build Sequence
- **Slice 1 (Foundation & Config Isolation):** [[FILL: concrete scope + how it will be verified]]
- **Slice 2 (End-to-End Core Workflow):** [[FILL: concrete scope + how it will be verified]]
- **Slice 3 (30% Kano Delighters):** [[FILL: which DL-xx items + how they will be verified]]
- **Slice 4 (Hardening & Verification):** [[FILL: tests, backup and runbook deliverables]]

## 2. The 365-Day Zero-Rewrite Horizon Playbook
| Milestone | Expected Real-World State | Built-In System Capability Used | Operator Action (Time) |
| :--- | :--- | :--- | :--- |
| **Day 1–7** | [[FILL: expected state]] | [[FILL: capability used]] | [[FILL: action + time]] |
| **Day 30** | [[FILL: expected state]] | [[FILL: capability used]] | [[FILL: action + time]] |
| **Day 90** | [[FILL: expected state]] | [[FILL: capability used]] | [[FILL: action + time]] |
| **Day 180** | [[FILL: expected state]] | [[FILL: capability used]] | [[FILL: action + time]] |
| **Day 365** | [[FILL: expected state]] | [[FILL: capability used]] | [[FILL: action + time]] |
""",
        "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md": f"""# 05. C-Suite Red-Team Log, Fitness Functions & Emergency Runbook — {project_name}

## 1. C-Suite Executive Council Red-Team Critique
> Fill this from a real critique pass (ideally an isolated subagent). Each row names a flaw found in *this* plan, not a generic risk. Status is FIXED or OPEN, never assumed.

| Executive Role | Initial Vulnerability Identified | Engineered Countermeasure Applied | Status |
| :--- | :--- | :--- | :--- |
| **CPO (Product)** | [[FILL: flaw found]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |
| **CTO (Systems)** | [[FILL: flaw found]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |
| **VP Domain (`{domain_key}`)** | [[FILL: flaw found]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |
| **CFO (FinOps)** | [[FILL: flaw found + unit-economics math]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |
| **CRO/COO (Risk/Ops)** | [[FILL: flaw found + pre-mortem]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |
| **Devil's Advocate User** | [[FILL: flaw found]] | [[FILL: fix applied]] | [[FILL: FIXED/OPEN]] |

## 2. Executive Council Scorecard
- **JTBD Clarity & Immediate Value:** [[FILL: score]] / 20
- **Kano Delight & Differentiation:** [[FILL: score]] / 15
- **Multi-Domain Fit & Authenticity:** [[FILL: score]] / 15
- **12-Month Architectural Evergreenness:** [[FILL: score]] / 20
- **Unit Economics & Resource Viability:** [[FILL: score]] / 15
- **Resilience, Verification & Rollback:** [[FILL: score]] / 15
- **TOTAL C-SUITE AUDIT SCORE:** [[FILL: sum]] / 100 (Gate 3 requires >= 85)

## 3. Automated Fitness Functions (Health Guardrails)
1. **FF-01 (Config Schema Guard):** [[FILL: what is checked and the command that runs it]]
2. **FF-02 (Deterministic Accuracy Check):** [[FILL: gold-standard case and the command that runs it]]
3. **FF-03 (Cost & Margin Breaker):** [[FILL: threshold and what happens when it is breached]]

## 4. Quarterly 15-Minute Self-Audit Prompt (Paste into Claude / Antigravity every 90 days)
```text
/apex-audit Read docs/apex-blueprint/ and STATE.json for {project_name}.
Audit the past 90 days of operation against 00-PROJECT-CONSTITUTION.md and propose Tier-B configuration calibrations without altering Tier-A core architecture.
```
""",
    }


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
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # cp1252 consoles crash on paths like 'Từ idea'
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    target_root = os.path.abspath(args.dir)
    blueprint_dir = os.path.join(target_root, "docs", "apex-blueprint")
    os.makedirs(blueprint_dir, exist_ok=True)

    today = datetime.date.today().isoformat()
    state_path = os.path.join(blueprint_dir, "STATE.json")

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
