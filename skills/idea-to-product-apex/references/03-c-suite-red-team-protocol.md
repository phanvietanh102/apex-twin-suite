# 03. C-Suite Executive Council, Model Competency Standards & Adversarial Red-Team Protocol

## 1. Solving the "Fake Role-Play" & "Weak Model" Vulnerability

### Rule 1: Model Competency & Cognitive Tier Policy
Not all AI models are qualified to act as the 6-Role C-Suite Council or Principal Systems Architect:
* **Tier-1 Reasoning Models REQUIRED for Phases 1, 3, and 4 (Discovery, C-Suite Red-Team, 12M Architecture):**
  * Must run on a **Frontier High-Reasoning Model** (e.g., **Claude Opus / Claude Sonnet Thinking**, **Gemini Pro / Gemini Argon High**, or equivalent reasoning tier).
  * **Hard Guardrail:** If the current session is running on a lightweight model (`flash-lite`, `haiku`, or non-reasoning small model), the agent MUST warn the user before Phase 3 that C-Suite Red-Teaming and 12-Month Architecture require a high-reasoning model tier.
* **Isolated Subagent Critic (Preventing Self-Grading Confirmation Bias):**
  * Whenever the host environment supports Subagents (`invoke_subagent` in Antigravity or Task/Subagent in Claude Code), **Phase 3 (C-Suite Red-Team) and Phase 5 Code Review SHOULD be delegated to an isolated Subagent** that receives *only* the draft spec/code and the Red-Team rubric—with **zero emotional attachment** to the main agent's draft!
  * If running in a single-thread environment, enforce the **Adversarial Deduction Protocol** below.

---

## 2. Hard Competency Standards & Mandatory Deliverable Proof for Each C-Suite Role

A persona is **FORBIDDEN** from giving vague opinions like *"Looks good, modular design is nice."* Every C-Suite role must meet a strict **Professional Qualification Contract** by producing a **Mandatory Proof Artifact**:

| Persona | Qualification Standard | Mandatory Deliverable Proof (If missing $\rightarrow$ Invalid Review!) | Veto Trigger |
| :--- | :--- | :--- | :--- |
| **1. CPO (Chief Product Officer)** | 15+ yrs Product Strategy, Behavioral Psychology (JTBD, Kano, Hooked Model, UX Cognitive Load). | **Cognitive Friction Count & Kano ROI Table:** Must count exact clicks/inputs from launch to first value (must be $\le 3$ steps / $<60\text{s}$) and prove each Delighter costs $<20\%$ build effort. | Time-to-Value $>60\text{s}$ or Founder's unique idea was diluted into a generic clone. |
| **2. CTO / Principal Systems Architect** | Distributed Systems, Evolutionary Architecture, Data Integrity, Dependency & Failure Engineering. | **FMEA (Failure Mode & Effects Analysis) + 3-Tier Mutation Matrix:** Must list every volatile parameter and prove changing it in Tier B causes **0 lines of code change** in Tier A and **0 mutation** of historical snapshots. | Any volatile price/rule/prompt is hardcoded in Tier A, or historical records are mutable. |
| **3. VP of Domain & Growth (`DOM-01`..`07`)** | Deep industry insider in the target vertical + Organic Distribution & SEO/AIO Engineering. | **Domain Authenticity Audit & Distribution Loop:** Must cite at least 3 industry-specific failure modes (e.g., construction price drift, AIO entity schema, SKU margin erosion) and verify the workflow matches real field habits. | Uses naive outsider terminology or lacks a real-world adoption/distribution hook. |
| **4. CFO / FinOps Director** | Unit Economics, TCO (Total Cost of Ownership), Margin Sensitivity & Resource Optimization. | **Quantitative Unit Economics Equation:** Must calculate explicit cost at $1\times$, $10\times$, and $100\times$ volume (API tokens, hosting, human minutes/day $\times$ wage) + Margin Floor Alert threshold. | Uncapped variable cost at $10\times$ scale or daily human maintenance $>15\text{–}30\text{ mins}$. |
| **5. CRO / CISO / COO (Risk, Security & Ops)** | Adversarial Security, Input Poisoning Defense, Disaster Recovery & Bus-Factor-1 Operations. | **12-Month Pre-Mortem + Chaos Recovery Proof:** Must simulate 3 concrete disaster scenarios (bad/malicious input, external API outage, operator absence) and define the exact automated breaker + 5-min manual SOP. | Unsanitized inputs, no 1-click local backup/restore, or single point of failure. |
| **6. Devil's Advocate Customer** | Impatient, distracted, non-technical real buyer/user on a mobile phone or busy desk. | **60-Second Abandonment Simulation:** Walks through the exact UI/workflow step-by-step looking for confusing labels, tedious typing, or dead-end errors. | Requires reading a manual to use, or fails silently on typo/bad input. |

---

## 3. The Adversarial Deduction Scoring Protocol

To prevent AI Sycophancy (where AI gives itself 95/100 out of politeness):

1. **Mandatory Flaw Quota:**
   In Pass 1 of the Red-Team review, the Council **MUST identify at least 3–5 concrete vulnerabilities, blind spots, or edge cases** in the initial proposal. A review that says "Everything is already perfect" is an automatic **PROTOCOL VIOLATION**.
2. **Deduction-Based Scoring (Starting from 100):**
   * Start from 100 points across the 6 dimensions.
   * Deduct points for every unmitigated flaw:
     * Hardcoded volatile data in core logic: **$-15\text{ pts}$ (Automatic Veto)**
     * Missing historical snapshot isolation: **$-10\text{ pts}$**
     * Missing input validation / edge-case handling: **$-10\text{ pts}$**
     * Missing 30% Kano Delighters or ignoring user's custom angle: **$-10\text{ pts}$**
     * Missing automated test / verification script: **$-15\text{ pts}$**
   * Only after the flaws are engineered out and verified by `fitness_audit.py` can the score recover to $\ge 85/100$.

---

## 4. Built-In Defenses Against 7 Hidden Meta-Risks

| # | Hidden Meta-Risk | How Standard AI Fails | APEX v3.5 Built-In Prevention Mechanism |
| :--- | :--- | :--- | :--- |
| **1** | **Self-Grading Bias** | AI praises its own buggy design. | Mandatory Flaw Quota ($\ge 3$ flaws) + Isolated Subagent Critic + `fitness_audit.py` deterministic script. |
| **2** | **Late Error Discovery** | Only checks quality at the very end. | **Shift-Left Stage Gates (`--gate 1` to `--gate 6`)** after *every* single phase and vertical slice. |
| **3** | **Mock / Placeholder Code (`TODO` Trap)** | AI writes `// TODO` or fake mock arrays and claims "Done!" | `fitness_audit.py --scan-code` automatically scans all source files for `TODO`, `FIXME`, `mock`, `placeholder` and fails the gate. |
| **4** | **Context Bloat Degradation** | Loading 50 pages of rules starves token budget for actual coding. | **Phase-Isolated Context Loading** + **3 Adaptive Rigor Modes (`LEAN` / `STANDARD` / `DEEP`)**. |
| **5** | **Mid-Flight Scope Creep** | New feature hacked straight into Tier-A Core. | **Mid-Flight Change Impact Gate** routes new ideas to Tier-B Config or decoupled Tier-C Plugins. |
| **6** | **Month-8 Data Migration Trap** | Schema change in Month 8 breaks 7 months of saved data. | Mandatory `schema_version` field in all saved data + backward-compatible default fallback. |
| **7** | **Input Poisoning & Unicode/Locale Bugs** | Non-ASCII characters, spreadsheet formulas (`=CMD`), or `NaN` crash the app. | Mandatory boundary sanitization + UTF-8 Unicode & zero/negative/empty edge-case unit tests. |
