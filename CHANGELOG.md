# Changelog — APEX Twin Engine Suite

All notable changes to the **APEX Twin Suite** (`idea-to-product-apex` & `product-workspace-reviewer-apex`) are documented in this file.

## [4.3.0] — 2026-11-15
### Release housekeeping
- **README rewritten for v4.3:** what the skills do, how they work, honest eval evidence and caveats, install, and usage. The unverified competitor comparison and the v3.7 mechanics that v4 replaced are removed.
- All manifests (`.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `.antigravity-plugin`, `plugin.json`), installers, script banners and SKILL.md headers are synced to **4.3.0**.
- `dist/` archives are rebuilt from the current skills. The bundle is renamed `apex-twin-suite-bundle.zip`.

### Changed (v4.3: context applicability, so rules are tailored rather than forced)
- **07 Step 0, context profile:** 9 quick questions (money with other parties, personal data, regulated, others operate it, controls on behalf of others, replaces something existing, long-lived, established trade, stakes). Applicability is decided by **context features, not the industry label**.
- **Activation table:** every lens and v4.2 rule has an activation condition. Rules that do not apply are `N/A` with a one-line reason, never forced and never silently skipped. Depth follows stakes.
- **Change scenarios scale with the profile:** ≥3 when long-lived and medium/high stakes; 1–2 when LEAN or low stakes; 0 for one-offs. Below 3 needs `change_scenarios_waiver`, which Gate 6 enforces. STATE now carries `context_profile`, `change_scenarios_required` and `change_scenarios_waiver`.
- The fixed "at least 3 traps / 3 flaws" minimums now scale with stakes. The reviewer's "apply all of them" became "apply what the profile activates".

### Changed (v4.2: reverse-analysis of where the plain model beat the skill; not yet re-evaluated)
See `evals/GAP-ANALYSIS.md`. All changes are generic, not tied to any eval scenario.
- **Lens 3, audit counterparties:** check penalties, fees and deductions against the contract and legal caps; check the user's own protection (terms, liability caps, insurance).
- **Lens 5, minimise data:** artifacts you build carry only the personal data they need; ID, bank and health data stay masked or restricted, with retention and deletion rules. Preserving history is not a reason to spread it.
- **Lens 6, plausibility:** sanity-check data against itself and field norms (impossible dates, contradictory statuses, beyond-norm volumes, impossible stock).
- **Lens 7, governance:** conflicts of interest of whoever controls money or data.
- **Second-order sweep:** for every fix, consider past periods (retroactive remedy), cost and price (reprice), people (tell them first, with ready messages), and the system's own failure (owner account, silent-stop alarm, permissions, parallel run or drill).
- **Closing rule:** a finding is closed by a fix or a ready-to-use replacement, not by a warning.
- **Domain brief:** use the field's standard instruments first, before inventing custom ones.
- **Definition of done:** new "replacing a live process" type (switchover plan, role ownership, silent-stop alarm).
- **Delivery rule reframed for AI-literate users:** installs for the agent's own work are not a cost. The *daily operators'* environment decides the deliverable's medium. Code that builds and verifies a native artifact is encouraged.

### Fixed (v4.1, driven by eval run 3)
- **No silent deferral:** High-weight `TRACE.md` rows (law, safety, money at risk, irreversible data, root vision, #1 pain) must be `DONE` in a minimal form, or `DEFERRED` with `agreed: "<user's words>"`. Gate 5 enforces this.
- **Native-first delivery ladder** (`08` §2): configure what the user has → native artifacts in their tool → light automation in that tool → code only if they already run it. Shared workflows must not depend on one machine. Spreadsheets must recalculate in the target app with zero error values, using only functions the user's version supports.
- **No clutter:** all process files go in `_apex/`, and the gates look there.
- **Domain brief adds a "next 12–24 months" section:** scheduled mandates, price risk and hedging, financing, growth path.
- **Eval run 4** (pre-registered; 3 fresh random scenarios including 2 greenfield): v4.1 scored **147 vs. 130** against no skill, with recall **91.75% vs. 81.75%**. All 6 pre-registered criteria passed (P1 by a hair). Cost is 1.9× tokens.

### Added (v4.0: completeness layer for any field)
- **`07-completeness-lenses.md`:** 12 field-agnostic lenses, used as a DO-CONFIRM sweep after drafting and before handover. Every finding must become a tracked row.
- **`08-definition-of-done-and-traceability.md`:**
  - `TRACE.md` ledger: every stated or discovered need reaches `DONE`+evidence, `DEFERRED`+reason, `DROPPED`+user agreement, or `N/A`;
  - definition of done per deliverable type: software, spreadsheet, plan, content, physical project/event, personal goal, review;
  - 12-month **change scenarios** recorded in STATE as tested proof.
- **`09-domain-discovery-protocol.md`:** build a domain brief for any field, jurisdiction or context (rules with identifier, date and certainty; a practitioner's checklist; failure modes; tools already in use). The 7 `DOM-*` archetypes are now worked examples, not a boundary.
- **`10-continuous-improvement.md`** (reviewer) and `/apex-improve`: baseline metrics, ROI-ranked improvements, self-measuring workflows, `IMPROVEMENT-LOG.md` and a re-review prompt.
- **Scripts:**
  - `init_project.py` and `xray_scanner.py` scaffold `TRACE.md` and add `change_scenarios` to STATE, and `--domain` accepts free text;
  - Gate 5 validates `TRACE.md`; Gate 6 also requires no `OPEN` rows and at least 3 passed change scenarios.
- **Both SKILL.md files (v4.0)** reframed around the missing layer (completeness, traceability, proof, field depth) while keeping the model's reasoning free. The skills also gained a ≤10-line summary rule and "deliver on what the user already has". Descriptions now cover any field, country or personal context.

### Changed (v3.8 prompt rewrite, driven by `evals/`)
- **Both SKILL.md files rewritten.** The "Iron Laws" in capitals are replaced by explained rules:
  - wow-first Turn 1 (concrete domain findings before questions);
  - at most 3 questions;
  - options only when there is a genuine fork;
  - **decide and build when the user delegates**;
  - biggest flow first;
  - gates, scores and tiers kept backstage;
  - honest certainty on legal and tax claims;
  - `LEAN` is the default mode; the critic subagent runs only in `DEEP`, once, with no sleep-polling.
- **Reviewer Turn 1** now gives read-only, evidence-backed findings first, then at most 3 root-vision questions. The description no longer triggers on PR/diff reviews or single-bug fixes.
- `xray_scanner.py --scan-only` prints the inventory without writing into the user's workspace.
- `references/01-*` in both skills: the 2-section format applies only to genuine forks, and is skipped when the user delegates.
- **Eval result:** with-skill score went from 120 to 148, winning 3/3 cases against the unchanged without-skill outputs, at 31% fewer tokens than run 1. See `evals/EVAL-RESULTS.md`.

### Added
- `evals/`: a 3-case with/without-skill eval pack (`EVAL-PROMPTS.md`), a messy construction-quote fixture, and results.

### Fixed
- **Gates no longer pass on an empty scaffold.** Previously `init_project.py` → `fitness_audit.py --gate 6` (and `xray_scanner.py` → `review_gate_audit.py --gate 6`) scored 100/100 APPROVED with zero work done, because templates already contained every keyword the gates looked for. Templates now carry `[[FILL: hint]]` markers for every decision; a document with an unresolved marker scores 0 and vetoes the gate.
- **No more self-certified scores.** Removed the pre-filled `93/100 APPROVED`, all-`PASS` C-Suite rows, `upgraded_health_score: 94`, and the pre-selected `Option B` that the reviewer scaffold wrote on Turn 1 before the user was interviewed. Gate 3 now parses the real total and requires ≥ 85.
- **Gates 5–6 now check the build.** They require `--scan-code`/`--scan-target` and slices marked `done` with a `verification_proof` (Gate 5: at least one; Gate 6: all).
- **Crash on non-ASCII paths on Windows** (`UnicodeEncodeError` on e.g. `Từ idea to products`): all 4 scripts now write UTF-8 output.
- **Anti-stub false positives:** `TODO`/`FIXME` are matched only in comments and case-sensitively, so `todo-list` or `https://todo...` no longer block Gate 5; only `raise NotImplementedError` counts as a stub.
- **Entropy false positives:** `copy` must be its own token, so `copywriting-notes.md` is no longer flagged as a duplicate.

## [3.7.0] — 2026-11-13 (Behavioral Decision Matrix & Direct GitHub Auto-Sync Edition)
### Added & Upgraded
- **2-Section Personal-First & Pros/Cons/Best-Fit Decision Matrix:** Eliminates Choice Paralysis and Anchoring Bias by strictly separating **Section 1 (Dedicated Personal Open Excavation)** from **Section 2 (3-Option Decision Matrix with explicit `✅ Pros`, `⚠️ Cons`, and `🎯 Best Fit If You Want...` + `Option D Hybrid`)** across both Twin Engines.
- **Direct GitHub Link Auto-Sync Manifests:** Added `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `.antigravity-plugin/plugin.json`, `.codex-plugin/plugin.json`, and `.cursor-plugin/plugin.json` for 10-second installation and automatic updates directly via GitHub URL.
- **Psychological Conversion Documentation Overhaul:** Re-architected `README.md`, `EXECUTIVE-PITCH-DECK.md`, and `DEEPSEARCH-ARCHITECTURE-WHITEPAPER.md` around Prospect Theory (Loss Aversion), Cognitive Contrast, Show-Don't-Tell Previews, and BJ Fogg Frictionless Activation.

## [3.6.0] — 2026-11-12 (Root-Vision Re-Anchored Reviewer & Superset Edition)
### Added & Fixed
- **Turn-1 Anti-Premature-Fix Gate (`product-workspace-reviewer-apex`):** Enforces a strict Turn-1 protocol where the engine records the objective X-Ray inventory (`Step 1A`) and immediately interviews the user from the root of their **Original Idea & Ultimate Product Vision** (`Step 1B`) before proposing any repair or architecture changes.
- **4-Column Vision-vs-Reality Gap Matrix (Phase 2):** Cross-examines the user's Root Vision against the current workspace across 4 explicit buckets: `1. Met & Healthy (KEEP)`, `2. Built Wrong / Drifted (REALIGN & REFACTOR)`, `3. Unbuilt Core Vision (MISSING A-TO-Z BUILD)`, and `4. 30% Beyond-Expectation (KANO DELIGHTERS + 4 SILENT LEAKS)`—followed by full A-to-Z `idea-to-product` execution.
- **Epistemic Honesty Tags, Non-Code Chaos Simulation (`1 Normal + 2 Sabotage`), & Quantitative Upgrade Triggers:** Synchronized across both Twin Engines.

## [3.5.0] — 2026-11-12 (Twin-Synchronized Edition)
### Added
- **Symmetric Twin Engine Architecture (100/100 Parity):**
  - `idea-to-product-apex` (Greenfield 0 -> 1 -> 12M Evergreen development).
  - `product-workspace-reviewer-apex` (Brownfield Existing Product, App & Workspace Forensic Audit, Strangler-Fig Refactoring & 12M Immunity).
- **Automated Forensic X-Ray Scanner (`xray_scanner.py`):** Non-destructive workspace inventory, duplicate/version entropy detection (`v1/v2/final/copy`), and automatic **Green / Yellow / Red Blast-Radius Zoning**.
- **Brownfield Shift-Left Gate Auditor (`review_gate_audit.py`):** Per-stage gate verification (`--gate 1..6`), Before vs. After C-Suite Delta Scorecard, and surgical code/workspace stub scanning (`--scan-target`).
- **Cross-Pollinated 5-Zone Workspace Taxonomy:** Synchronized `00-CONFIG`, `01-ACTIVE`, `02-CORE`, `03-IMMUTABLE-ARCHIVE`, and `04-EXPORTS` across both Greenfield and Brownfield engines.

## [3.0.0] — 2026-11-12 (Zero-Bloat & Shift-Left Verification Edition)
### Added
- **Dual-Mode Hybrid Elicitation:** Combines Open Contrarian Excavation + Brutal Socratic Grilling (`/grill-me` style) + AI Benchmark Options (A/B/C + Option D Wildcard) to eliminate Anchoring Bias.
- **Model Competency Policy & Isolated Subagent Critic:** Enforces Frontier High-Reasoning models for Phases 1, 3, 4 and delegates Red-Team/Code Audits to isolated subagents with Adversarial Deduction Scoring (starts at 100, mandatory $\ge 3$ flaws found in Pass 1).
- **Shift-Left Stage Gates (`--gate 1..6`) & Anti-Stub Scanner (`--scan-code`):** Blocks advancement immediately if an early step has errors or if source code contains `TODO`, `FIXME`, `NotImplementedError`, or fake mock stubs.
- **Phase-Isolated Context Loading & 3 Rigor Modes (`LEAN` / `STANDARD` / `DEEP`):** Prevents process instructions from diluting output token quality during Phase 5 build.

## [2.0.0] — 2026-11-12 (Multi-Domain & 12-Month Evergreen Edition)
### Added
- **7-Domain Universal Adapter Matrix (`DOM-01`..`DOM-07`):** Software/AI, Construction/Real Estate, Content/SEO/AIO, E-Commerce/Retail, B2B Services/SOP, Regulated FinTech/EdTech/Health, and IoT/Hardware.
- **6-Role C-Suite Executive Council:** CPO, CTO, VP Domain, CFO, CRO/COO, and Devil's Advocate Customer.
- **3-Tier Decoupled Evergreen Architecture:** Tier A (Immutable Core), Tier B (2-Minute Editable Config), Tier C (Adapters/Output) + Historical Snapshot Isolation.
