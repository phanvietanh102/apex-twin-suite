# 05. Canonical Artifact Templates — The Persistent Project Memory Ledger

To prevent AI context drift across sessions and ensure the project remains 100% understandable and maintainable for 12+ months, every project initialized by **APEX Idea-to-Product** maintains a structured `docs/apex-blueprint/` directory plus a machine-readable `STATE.json`.

Below are the canonical structures for each file (automatically scaffolded by `scripts/init_project.py`).

---

## 1. `STATE.json` (Machine & AI Session Memory Tracker)
```json
{
  "project_name": "Project Name",
  "domain_primary": "DOM-01",
  "domain_secondary": null,
  "created_at": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "current_phase": "Phase 1: Discovery",
  "c_suite_audit_score": 0,
  "evergreen_horizon_months": 12,
  "locked_decisions": [],
  "active_slice": "Slice 1",
  "slices": [
    {
      "id": "slice-1",
      "name": "Core Backbone & Must-Have MVP",
      "status": "pending",
      "verification_proof": null
    }
  ],
  "volatile_configs_isolated": [],
  "known_risks_mitigated": []
}
```

---

## 2. `00-PROJECT-CONSTITUTION.md` (12-Month Immutable Project Constitution)
Contains the non-negotiable laws of the project that no future AI session or quick-fix is allowed to violate:
* **1. Core Identity & Domain Archetype:** Primary & secondary domain classification.
* **2. The North Star Job-to-be-Done (JTBD):** *"When [situation], the user wants to [progress], so they can [outcome] without [pain]."*
* **3. Hard Constraints (Budget, Timeline, Bus Factor, Tech Stack):** Explicit ceilings.
* **4. Explicit Non-Goals (Scope Guardrails):** At least 3 anti-goals.
* **5. Architectural Invariants (1-Year Durability Laws):**
  * All volatile parameters isolated in `[path/to/config]`.
  * Historical records are immutable snapshots.
  * Zero unverified changes.

---

## 3. `01-DISCOVERY-AND-PRFAQ.md` (Discovery Ledger & Working Backwards PR/FAQ)
* **1. Dual-Mode Elicitation Summary:** Decisions locked from user interview.
* **2. Johari Window — Industry Blind-Spot Radar (Quadrant 4 Unknown-Unknowns):**
  * Top 4–5 domain traps discovered and how this project neutralizes them.
* **3. Working Backwards — Future Press Release (PR):**
  * Headline, Summary, Problem, Solution, Customer Quote.
* **4. Hardest FAQs (Customer FAQ + Internal/Operational FAQ):**
  * Addressing skepticism, edge cases, unit economics, and failure recovery upfront.

---

## 4. `02-KANO-SPEC-AND-DELIGHT.md` (Kano Feature Specification & SMART-ER Contract)
* **1. Tier 1 — Must-Be Baseline (Core MVP):** Essential workflows required on Day 1.
* **2. Tier 2 — Performance Multipliers:** Speed, automation, and ergonomics upgrades.
* **3. Tier 3 — Asymmetric Delighters (30% Beyond-Expectation Features):**
  * Specific high-value, low-complexity innovations added by the AI Council.
* **4. SMART-ER Acceptance Criteria Table:**
  * Columns: `Feature ID | Requirement | Metric (M) | Resilience 12M (R) | Verification Proof (E)`

---

## 5. `03-ARCHITECTURE-AND-SOPS.md` (Evolutionary Architecture & Standard Operating Procedures)
* **1. 3-Tier System Decomposition:**
  * Tier A (Immutable Core), Tier B (Externalized Config/Prices/Prompts), Tier C (Adapters/UI/Output).
* **2. Data Model & Snapshot Isolation:** How active config vs. historical records are stored and backed up.
* **3. Architecture Decision Records (ADR):** Why this stack/workflow was chosen for 12-month zero-rewrite longevity.
* **4. Human-in-the-Loop SOP (< 15 Minutes/Day Operation):** Step-by-step operational flow.

---

## 6. `04-12M-EVERGREEN-ROADMAP.md` (Vertical-Slice Execution Plan & 365-Day Roadmap)
* **1. Vertical Slice Implementation Plan:**
  * Slice 1: Core Engine & Config Isolation
  * Slice 2: Primary End-to-End Workflow & Export
  * Slice 3: 30% Kano Delighters & UX Polish
  * Slice 4: Automated Verification, Backup & Runbook
* **2. The 365-Day Evergreen Horizon Playbook (Zero Core Rewrites):**
  * **Day 1–7:** Launch & Initial Verification.
  * **Day 30:** Config Calibration (adjusting numbers/templates without touching core).
  * **Day 90:** Q1 Volume & Archive Routine.
  * **Day 180:** Mid-Year Pre-Planned Module Activation.
  * **Day 365:** Annual Roll-over & Audit.

---

## 7. `05-FITNESS-FUNCTIONS-AND-RUNBOOK.md` (C-Suite Red-Team Log, Fitness Functions & Emergency Runbook)
* **1. C-Suite Red-Team Critique & Resolution Log:**
  * Findings from CPO, CTO, VP Domain, CFO, CRO/COO, and Devil's Advocate Customer.
  * Executive Council Scorecard ($\ge 85/100$).
* **2. Automated Fitness Functions & Circuit Breakers:**
  * Exact validation commands, cost/margin guardrails, and health checks.
* **3. Bus-Factor-1 Emergency Runbook:**
  * How to update prices/rules in 2 minutes.
  * How to backup/restore data in 1 click.
  * 5-Minute Manual Fallback SOP if any external service is temporarily unavailable.
  * Quarterly 15-Minute AI Self-Audit Prompt.
