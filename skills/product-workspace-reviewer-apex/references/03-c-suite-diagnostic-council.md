# 03. C-Suite Forensic Diagnostic Council, Competency Standards & Deduction Scoring

## 1. Twin-Parity Model Competency & Subagent Critic Policy

To maintain **100% parity** with `idea-to-product-apex`:
1. **Frontier High-Reasoning Model Required (Phases 1, 3, 4):**
   * Forensic architecture auditing and root-cause analysis require a **High-Reasoning Model** (`Claude Opus / Sonnet Thinking`, `Gemini Pro / Argon High`). Warn the user if running on a lightweight model.
2. **Isolated Subagent Forensic Critic:**
   * When subagents are supported (`invoke_subagent` / Task tool), spawn an **isolated Forensic Auditor Subagent** to inspect the target product/workspace with fresh, ruthless eyes.

---

## 2. Hard Competency Standards & Mandatory Forensic Proof per Executive Role

Every member of the 6-Role Diagnostic Council must produce a **Mandatory Quantitative Forensic Proof** (generic advice is strictly rejected):

| Persona | Diagnostic Role | Mandatory Forensic Deliverable Proof | Veto / Block Condition |
| :--- | :--- | :--- | :--- |
| **1. CPO (Product & UX Auditor)** | Cognitive Walkthrough & Conversion Leak Hunter | **Step-by-Step Friction & Drop-Off Map:** Counts exact steps, clicks, and manual copy-pastes required to complete the core workflow Today vs. After Upgrade, plus **30% Kano Modernization Table**. | Upgrade fails to cut manual friction by $\ge 40\%$ or breaks a Sacred User Habit. |
| **2. CTO / Principal Legacy Architect** | Technical Debt, Blast-Radius & Coupling Forensics | **Green/Yellow/Red Zone Map + Hardcoded Volatility Inventory:** Lists exact file paths and line numbers where volatile data (prices, rules, URLs, prompts) is hardcoded or where files are duplicated. | Refactor touches a Red Zone without a verified snapshot backup or leaves hardcoded volatility in Tier A. |
| **3. VP of Domain & Benchmark Strategy (`DOM-01`..`07`)** | Industry Gap & Competitive Moat Auditor | **Domain Benchmark Gap Table:** Compares current product/workspace against Top 1% industry standards (SEO/AIO schema, construction BOQ standards, invoice accuracy, etc.). | Leaves major industry blind spots unaddressed. |
| **4. CFO / FinOps & Time-Bleed Director** | Unit Economics & Operational Waste Auditor | **Annualized Time & Money Leak Calculation:** Quantifies exact hours/year wasted on manual repetition + API/infra/margin leaks ($\text{Hours Saved/Yr} \times \text{Value}$). | Upgrade adds recurring cost or increases daily maintenance time. |
| **5. CRO / CISO / COO (Risk & Operations)** | Entropy, Data Loss & Disaster Recovery Auditor | **Single-Point-of-Failure & Entropy Audit:** Quantifies workspace clutter index (duplicate `v1/v2` files, missing backups, unvalidated inputs) and verifies the **1-Click Rollback & 5-Min Manual SOP**. | No rollback mechanism exists before modifying existing files, or historical records risk overwrite. |
| **6. Frustrated Daily Operator / End-User** | Real-World Muscle-Memory & Edge-Case Tester | **Pain-Point Walkthrough Log:** Simulates daily high-stress usage (rushed edits, typos, mobile viewing, messy real-world data). | New upgrade feels more complicated or slower to use than the old system. |

---

## 3. Dual-Scorecard Protocol: "Before (Baseline)" vs. "After (Upgraded)"

Unlike a Greenfield project (which only scores the proposed blueprint), a Brownfield Review MUST produce a **Comparative Delta Scorecard** across all 6 dimensions (100 points total):

```markdown
| C-Suite Audit Dimension (100 Pts) | Baseline Score (Before) | Forensic Flaw Detected (Evidence) | Upgraded Score (After) | Engineered Countermeasure |
| :--- | :---: | :--- | :---: | :--- |
| **1. Workflow & UX Efficiency (20)** | [X]/20 | [Manual steps / bottlenecks] | [Y]/20 | [Streamlined flow + 1-Click Presets] |
| **2. Kano 30% Delight Value (15)** | [X]/15 | [Missing proactive intelligence] | [Y]/15 | [3 Automated Kano Delighters] |
| **3. Domain Benchmark Fit (15)** | [X]/15 | [Missing DOM-0X standards] | [Y]/15 | [Top-1% Industry Standards Embedded] |
| **4. 3-Tier & Config Decoupling (20)**| [X]/20 | [Hardcoded prices/rules in file X] | [Y]/20 | [Extracted Tier-B 2-Min Config] |
| **5. Cost & Time Optimization (15)** | [X]/15 | [X hrs/week leaked on manual tasks] | [Y]/15 | [80% Time Saved + Margin Guards] |
| **6. Data Safety, Hygiene & Backup (15)**| [X]/15 | [Duplicate v1/v2 files, no backup] | [Y]/15 | [Immutable Archive + 1-Click Rollback] |
| **TOTAL SYSTEM HEALTH SCORE** | **[Before]/100** | **Net Gain: +[Delta] pts** | **[After >= 85]/100** | **12-MONTH IMMUNITY VERIFIED** |
```

---

## 4. Built-In Defenses Against 7 Brownfield Review Meta-Risks

| # | Brownfield Meta-Risk | Naive AI Failure | APEX v3.5 Built-In Defense |
| :--- | :--- | :--- | :--- |
| **1** | **Destructive Refactoring** | Deletes or overwrites working files/data. | **Mandatory Pre-Flight Snapshot Backup** + Red-Zone Quarantine before any edit. |
| **2** | **Breaking Muscle Memory** | Changes familiar shortcuts/layouts unnecessarily. | **Sacred Habit Lock** in `00-PRESERVATION-CONSTITUTION.md`. |
| **3** | **Broken Internal Links / Imports** | Moving messy files breaks scripts, formulas, or HTML links. | Automated path-reference scan & update verification in Gate 5. |
| **4** | **Silent Calculation Regression** | New code produces slightly different numbers on old invoices/data. | **Behavioral Parity Test:** Run old inputs through new engine and assert 100% match. |
| **5** | **Superficial "Consultancy Talk"** | Writes a long critique report but doesn't actually fix the workspace/code. | Phases 5–6 execute the actual surgical upgrades and verify with `review_gate_audit.py`. |
| **6** | **Context Bloat on Large Workspaces** | Tries to read 500 files into context at once and crashes/hallucinates. | Uses `xray_scanner.py` to map metadata first; reads only targeted files per slice. |
| **7** | **Relapse into Chaos After 60 Days** | Cleaned workspace gets messy again next month. | Leaves behind an automated **Hygiene/Validation Script** & 2-Minute SOP. |
