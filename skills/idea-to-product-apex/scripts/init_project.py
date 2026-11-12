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
        "domain_label": DOMAIN_MAP.get(domain_key, DOMAIN_MAP["DOM-01"]),
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
    }


def get_templates(project_name: str, domain_key: str, today: str) -> dict:
    domain_label = DOMAIN_MAP.get(domain_key, DOMAIN_MAP["DOM-01"])
    return {
        "00-PROJECT-CONSTITUTION.md": f"""# 00. Project Constitution — {project_name}
> **Generated:** {today} | **Domain Archetype:** `{domain_key}` ({domain_label})
> **Longevity Contract:** 12-Month Evergreen / Zero-Rewrite Guarantee

## 1. Core Identity & North Star JTBD (Job-to-be-Done)
- **Target Persona / Operator:** [Specify primary user & operator]
- **Core JTBD Statement:** *"When [situation/trigger], the user wants to [core progress/action], so they can [desired outcome/value] without [current friction/pain]."*

## 2. Hard Constraints & Operational Reality
- **Budget & Cost Ceiling:** [e.g., < $10/month recurring; zero uncapped variable API bills]
- **Operational Bus Factor:** [e.g., Solo operator, max 15 minutes/day routine maintenance]
- **Tech / Tooling Stack:** [Choose battle-tested, low-maintenance stack]

## 3. Explicit Non-Goals (Scope Guardrails)
1. **Non-Goal 1:** Do NOT build [feature X] in v1 if it adds maintenance burden without moving core JTBD.
2. **Non-Goal 2:** Do NOT hardcode volatile prices, rates, API keys, or seasonal rules inside core logic.
3. **Non-Goal 3:** Do NOT rely on single-point-of-failure external services without an offline/manual fallback.

## 4. Immutable Architectural Invariants (12-Month Laws)
- **Invariant 1 (3-Tier Separation):** Core logic (Tier A) is strictly separated from editable config/prices/prompts (Tier B) and UI/export adapters (Tier C).
- **Invariant 2 (Snapshot Immutability):** Historical transactions/outputs are saved as immutable snapshots; future config edits never corrupt past records.
- **Invariant 3 (Verification First):** Every slice requires objective verification proof before completion.
""",
        "01-DISCOVERY-AND-PRFAQ.md": f"""# 01. Discovery, Blind-Spot Radar & Working Backwards PR/FAQ — {project_name}

## 1. Socratic Elicitation Decisions
- **Q1 (Target Workflow & Scope):** [Locked Option]
- **Q2 (Operation & Automation Level):** [Locked Option]
- **Q3 (Monetization / Value Metric):** [Locked Option]

## 2. Johari Quadrant 4 — Domain Blind-Spot Radar (Unknown-Unknowns)
| # | Hidden Industry Trap (Điểm mù ngành `{domain_key}`) | Impact If Ignored | Built-in Countermeasure in {project_name} |
| :--- | :--- | :--- | :--- |
| 1 | Volatility of prices / rules / algorithms | System becomes obsolete in 60 days | Externalized into editable Config Table |
| 2 | User friction / drop-off in first 60 seconds | Low adoption / abandonment | Instant presets + guided 1-click flow |
| 3 | Silent data loss or historical overwrite | Financial / operational audit failure | Immutable snapshots + 1-click JSON/Excel export |
| 4 | Edge-case unit economics / cost spike | Negative ROI at scale | Hard cost/margin guardrails & deterministic core |

## 3. Working Backwards — Future Press Release (PR)
- **Headline:** {project_name} transforms how [Target Audience] achieves [Core Outcome] in under [X minutes].
- **Problem:** Previously, teams/users struggled with [Pain Point 1] and [Pain Point 2].
- **Solution & Asymmetric Edge:** {project_name} combines a rock-solid deterministic core with [Top Kano Delighters].

## 4. Hardest FAQs (Customer & Operational)
- **Customer FAQ 1:** *What if my requirements/prices change next month?* -> Update the config table in 2 minutes; zero code changes needed.
- **Operational FAQ 2:** *What if an external API or internet connection drops?* -> System degrades gracefully to deterministic/local fallback mode.
""",
        "02-KANO-SPEC-AND-DELIGHT.md": f"""# 02. Kano Feature Specification & SMART-ER Criteria — {project_name}

## 1. Tier 1 — Must-Be Baseline (Core MVP — 50% Effort)
- [ ] **MB-01:** Core input capture with strict validation and clear error messages.
- [ ] **MB-02:** Deterministic calculation / processing engine with 100% accuracy.
- [ ] **MB-03:** Clean, exportable output (Web / PDF / Excel / JSON) and local data persistence.

## 2. Tier 2 — Performance Multipliers (10x Efficiency — 20% Effort)
- [ ] **PM-01:** Pre-configured templates / presets for 1-click execution.
- [ ] **PM-02:** Instant search, filter, and historical snapshot comparison.

## 3. Tier 3 — Asymmetric Delighters (30% Beyond-Expectation Features)
- [ ] **DL-01 (Proactive Intelligence):** Automatically flags anomalies, margin risks, or optimization opportunities.
- [ ] **DL-02 (Instant Shareable Artifact):** Generates a client-ready or executive-ready summary in 1 click.
- [ ] **DL-03 (Zero-Code Live Configurator):** Allows non-technical operators to adjust rates/rules/prompts live.

## 4. SMART-ER Acceptance Criteria Contract
| ID | Requirement | Specific & Measurable (S/M) | 12-Month Resilience (R) | Verification Proof (E) |
| :--- | :--- | :--- | :--- | :--- |
| `MB-01` | Input & Validation | Rejects invalid types in <50ms with human-readable hint | Schema-driven rules | Automated validation test |
| `MB-02` | Core Processing | 100% deterministic math/rule accuracy | Pure functions, zero external drift | Unit test suite pass |
| `DL-01` | Delighter Engine | Surfaces actionable insight on every run | Rule thresholds stored in config | End-to-end smoke test |
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

## 2. Architecture Decision Records (ADRs for 12-Month Longevity)
- **ADR-01 (Boring, Self-Contained Stack):** Chosen to eliminate dependency rot over 365 days.
- **ADR-02 (Externalized Volatility):** All unit prices, rates, templates, and provider settings are isolated in Tier B.
- **ADR-03 (Immutable History):** Every committed record stores its own snapshot of parameters active at creation time.

## 3. Daily / Weekly Operator SOP (< 15 Minutes)
1. **Routine Use (2–5 mins):** Select preset -> Enter/Import data -> Review proactive delight alerts -> Export/Commit.
2. **Updating Rates/Rules (2 mins/month):** Open Tier-B Config -> Update values -> Run verification check.
3. **Backup Routine (1 min/week):** Trigger 1-Click Export/Backup to local/cloud archive.
""",
        "04-12M-EVERGREEN-ROADMAP.md": f"""# 04. Vertical-Slice Execution Plan & 365-Day Evergreen Roadmap — {project_name}

## 1. Vertical-Slice Build Sequence
- **Slice 1 (Foundation & Config Isolation):** Set up Tier-B config schema, Tier-A core logic, and validation guards.
- **Slice 2 (End-to-End Core Workflow):** Connect UI/CLI intake to core engine and output generator.
- **Slice 3 (30% Kano Delighters):** Implement proactive insights, presets, and 1-click export formats.
- **Slice 4 (Hardening & Verification):** Add automated smoke tests, backup utility, and operator runbook.

## 2. The 365-Day Zero-Rewrite Horizon Playbook
| Milestone | Expected Real-World State | Built-In System Capability Used | Operator Action (Time) |
| :--- | :--- | :--- | :--- |
| **Day 1–7** | Launch & initial real-world runs | Presets + guided validation | Run first 5 real cases (15m) |
| **Day 30** | Market prices / operational tweaks needed | Tier-B Externalized Config | Edit config file/table (5m) |
| **Day 90** | Q1 data accumulation ($5\\times$ volume) | Built-in filter, search & archive export | Export Q1 backup archive (5m) |
| **Day 180** | Mid-year competitive or workflow expansion | Toggleable Phase-2 modules & adapter hooks | Run Quarterly AI Audit prompt (15m) |
| **Day 365** | Full-year review & Year-2 rollover | Immutable historical ledger + annual summary | Export annual report; continue seamlessly |
""",
        "05-FITNESS-FUNCTIONS-AND-RUNBOOK.md": f"""# 05. C-Suite Red-Team Log, Fitness Functions & Emergency Runbook — {project_name}

## 1. C-Suite Executive Council Red-Team Critique
| Executive Role | Initial Vulnerability Identified | Engineered Countermeasure Applied | Status |
| :--- | :--- | :--- | :--- |
| **CPO (Product)** | Risk of generic output / user friction | Added 30% Kano Delighters + 1-click presets | PASS |
| **CTO (Systems)** | Hardcoded parameters rotting in Month 2 | Strict Tier-A / Tier-B config decoupling | PASS |
| **VP Domain (`{domain_key}`)** | Missing domain-specific edge cases | Domain Blind-Spot Radar rules embedded | PASS |
| **CFO (FinOps)** | Hidden recurring costs / margin erosion | Zero-cost local core + margin guardrail alerts | PASS |
| **CRO/COO (Risk/Ops)** | Data loss or external dependency outage | Immutable snapshots + 5-min manual fallback | PASS |
| **Devil's Advocate User** | Confusing inputs or silent errors | Instant inline validation + sensible defaults | PASS |

## 2. Executive Council Scorecard
- **JTBD Clarity & Immediate Value:** 18 / 20
- **Kano Delight & Differentiation:** 14 / 15
- **Multi-Domain Fit & Authenticity:** 14 / 15
- **12-Month Architectural Evergreenness:** 19 / 20
- **Unit Economics & Resource Viability:** 14 / 15
- **Resilience, Verification & Rollback:** 14 / 15
- **TOTAL C-SUITE AUDIT SCORE:** **93 / 100** (APPROVED FOR EXECUTION)

## 3. Automated Fitness Functions (Health Guardrails)
1. **FF-01 (Config Schema Guard):** Fails fast with clear message if any config parameter is missing or out of bounds.
2. **FF-02 (Deterministic Accuracy Check):** Automated smoke test verifies core calculation/workflow output matches gold standard.
3. **FF-03 (Cost & Margin Breaker):** Warns operator immediately if unit economics or resource thresholds are breached.

## 4. Quarterly 15-Minute Self-Audit Prompt (Paste into Claude / Antigravity every 90 days)
```text
/apex-audit Hãy đọc thư mục docs/apex-blueprint/ và STATE.json của dự án {project_name}.
Kiểm tra dữ liệu vận hành 90 ngày qua, đối chiếu với 00-PROJECT-CONSTITUTION.md và đề xuất tinh chỉnh tầng cấu hình (Tier B) mà KHÔNG phá vỡ kiến trúc lõi (Tier A).
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
        choices=list(DOMAIN_MAP.keys()),
        help="Primary domain archetype ID (DOM-01 to DOM-07)",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing blueprint files")
    args = parser.parse_args()

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
