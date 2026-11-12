# 05. Canonical Forensic Audit & Evolution Templates — The Persistent Review Ledger (`docs/apex-review/`)

To maintain **100% architectural symmetry** with `idea-to-product-apex` (`docs/apex-blueprint/`), every existing product, app, or workspace reviewed by `product-workspace-reviewer-apex` maintains a 6-document ledger in `docs/apex-review/` plus a machine-readable `REVIEW-STATE.json` (scaffolded automatically by `scripts/xray_scanner.py`).

---

## 1. `REVIEW-STATE.json` (Forensic Audit & Migration Tracker)
```json
{
  "schema_version": "3.5.0-apex-review",
  "target_name": "Existing Product or Workspace Name",
  "domain_primary": "DOM-01",
  "created_at": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "current_phase": "Phase 1: Forensic X-Ray & Pain Excavation",
  "baseline_health_score": 0,
  "upgraded_health_score": 0,
  "entropy_files_detected": 0,
  "sacred_habits_locked": [],
  "blast_radius_zones": {
    "green_safe": [],
    "yellow_tested": [],
    "red_immutable": []
  },
  "slices": [
    {
      "id": "slice-1",
      "name": "Pre-Flight Snapshot Backup & Red-Zone Quarantine",
      "status": "pending",
      "verification_proof": null
    },
    {
      "id": "slice-2",
      "name": "Tier-B Volatility Extraction & Structural Cleanup",
      "status": "pending",
      "verification_proof": null
    },
    {
      "id": "slice-3",
      "name": "30% Kano Modernization Delighters & Automation",
      "status": "pending",
      "verification_proof": null
    },
    {
      "id": "slice-4",
      "name": "Behavioral Parity Regression Tests & 365-Day Immunity Runbook",
      "status": "pending",
      "verification_proof": null
    }
  ]
}
```

---

## 2. `00-PRESERVATION-CONSTITUTION.md` (Heritage Preservation & Non-Breaking Constitution)
* **1. Target System Identity & Domain (`DOM-01`..`07`):** Current state overview.
* **2. Sacred Workflows & Muscle-Memory Habits (Must Not Break):** Explicit list of user habits, URLs, formulas, or layouts that must remain familiar.
* **3. Blast-Radius Zoning Contract (Green / Yellow / Red Zones):**
  * 🟢 **Green Zone:** Safe to modernize immediately.
  * 🟡 **Yellow Zone:** Refactor with behavioral parity tests.
  * 🔴 **Red Zone:** Historical records, invoices, customer data — 100% read-only / snapshot-protected.
* **4. Explicit Non-Breaking Invariants:** Zero data loss, zero broken internal links, 1-click rollback guarantee.

---

## 3. `01-FORENSIC-XRAY-AND-LEAKS.md` (Forensic X-Ray & 4 Silent Leaks Report)
* **1. Automated X-Ray Inventory Summary:** File counts, directory depth, duplicate/versioned files (`v1`, `v2`, `copy`), hardcoded constants.
* **2. Dual-Mode Operator Elicitation Summary:** User's custom frustrations, secret upgrade ideas, and selected modernization path (A/B/C/D).
* **3. The 4 Silent Leaks Discovered (Johari Quadrant-4 Equivalent):**
  * Leak 1: Cognitive & Time Bleed (Hours wasted/month)
  * Leak 2: Revenue & Unit Economics Bleed
  * Leak 3: Hardcoded Volatility Rot
  * Leak 4: Catastrophic Single-Point Fragility

---

## 4. `02-KANO-UPGRADE-SPEC.md` (3-Tier Kano Modernization Spec & SMART-ER Contract)
* **1. Tier 1 — Critical Debt & Leak Fixes (50% Effort):** Immediate pain removal and structural cleanup.
* **2. Tier 2 — 10x Workflow & Hygiene Multipliers (20% Effort):** Unified templates, naming standards, 1-click batch operations.
* **3. Tier 3 — Asymmetric Modernization Delighters (30% Beyond-Expectation Features):** Smart validation, margin/anomaly alerts, instant dual PDF/Excel/Schema outputs.
* **4. SMART-ER Upgrade & Parity Contract Table:**
  * Columns: `Upgrade ID | Target Component | Before Metric | After Target (S/M) | 12M Immunity (R) | Parity Proof (E)`

---

## 5. `03-STRANGLER-ARCHITECTURE-AND-HYGIENE.md` (Strangler-Fig Architecture & Workspace Hygiene)
* **1. 3-Tier Volatility Extraction Plan:** Moving hardcoded prices/rules/prompts from legacy files into a clean Tier-B Config.
* **2. Workspace / Codebase Reorganization Map:** Before $\rightarrow$ After directory tree and path-update mapping.
* **3. Architecture Decision Records (ADRs):** Why each refactor pattern was chosen to ensure 12 months of zero maintenance.
* **4. Upgraded Daily Operator SOP ($<10$ Minutes/Day):** Before vs. After step count.

---

## 6. `04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md` (Zero-Downtime Migration & 365-Day Immunity Roadmap)
* **1. Surgical 4-Slice Execution Plan:**
  * Slice 1: Snapshot Backup & Red-Zone Quarantine
  * Slice 2: Tier-B Config Extraction & Hygiene Cleanup
  * Slice 3: 30% Kano Modernization Features
  * Slice 4: Behavioral Parity Regression & Handover
* **2. The 365-Day Post-Upgrade Immunity Playbook:**
  * Day 1, Day 30, Day 90, Day 180, and Day 365 maintenance-free checkpoints.

---

## 7. `05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md` (Before/After Scorecard, Regression Suite & Rollback Runbook)
* **1. 6-Role C-Suite Before vs. After Scorecard:**
  * Shows exact score jump (e.g., Baseline `48/100` $\rightarrow$ Upgraded `94/100`).
* **2. Automated Regression & Hygiene Fitness Functions:** Commands to verify zero broken links, zero stubs, and 100% calculation parity.
* **3. 1-Click Rollback & 5-Minute Manual Fallback Runbook:** Exact steps to restore pre-upgrade snapshot if ever needed, plus the **Quarterly 15-Minute Drift Audit Prompt**.
