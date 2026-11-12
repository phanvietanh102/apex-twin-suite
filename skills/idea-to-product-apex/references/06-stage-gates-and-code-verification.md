# 06. Step-by-Step Stage Gates, Code Verification & Anti-Bloat Protocol

## 1. Solving the "Context Bloat vs. Output Quality" Paradox

**The Engineering Reality:**
When an AI agent loads a massive workflow prompt into its context window while simultaneously trying to write code, design UI, or draft deep content, **Transformer Attention Dilution** occurs. The model spends 40% of its token and reasoning capacity on "meta-bureaucracy" (writing long process reports) and rushes the actual product output!

### The APEX v3.5 Solution: 3 Laws of Zero-Bloat Execution

1. **Law of Phase-Isolated Context (Load Only Active Phase Reference):**
   * Never read all reference files at once.
   * Read **only** the reference file for the current active phase:
     * Phase 1–2 $\rightarrow$ Read only `01` & `02`.
     * Phase 3 $\rightarrow$ Read only `03`.
     * Phase 4 $\rightarrow$ Read only `04` & `05`.
     * Phase 5 (Building/Coding) $\rightarrow$ **Drop all philosophical prose!** Read only the locked `02-KANO-SPEC-AND-DELIGHT.md` acceptance table and dedicate **95% of output tokens to writing complete, production-grade code/assets**.
2. **Law of Adaptive Rigor Tiers (3 Modes Matched to Project Scale):**
   Classify the project size in Phase 1 so bureaucracy never exceeds product value:
   * **Mode 1 — `LEAN` (Micro-products / Fast tools / Single-session execution):**
     Compress Phases 1–4 into a single compact `docs/apex-blueprint/APEX-COMPACT-SPEC.md` ($\le 150$ lines) and spend **85% of time building and testing the actual product**.
   * **Mode 2 — `STANDARD` (Standard products / Websites / Operational workflows):**
     Standard 6-phase flow with concise blueprint files and per-slice automated testing.
   * **Mode 3 — `DEEP-ENTERPRISE` (Large systems / Multi-domain architectures / Long-term investments):**
     Full 6-document ledger + isolated Subagent C-Suite Red-Team + full stress-test suite.
3. **Law of Code/Output Supremacy:**
   A blueprint is only a contract, never the final product. In Phase 5, every turn must produce **100% complete, working, non-truncated implementation files** with zero placeholders.

---

## 2. Shift-Left Stage-Gate Verification (Gates 1 $\rightarrow$ 6)

**Why End-of-Pipeline Scoring Fails:**
If Step 1 (JTBD/Vision) or Step 2 (Scope/Delight) or Step 3 (Architecture) has a flaw, discovering it at Step 6 means throwing away 80% of the work.

Every phase has its own **Hard Stage-Gate Breaker** enforced before moving to the next phase:

| Gate | Trigger Point | Mandatory Verification Check | Fail/Block Condition (Stop & Fix Immediately) |
| :--- | :--- | :--- | :--- |
| **Gate 1** | End of Phase 1 (Discovery) | `fitness_audit.py --gate 1` + User confirmation | Fails if user's open-ended unique vision wasn't probed, or if JTBD + Hard Constraints (Budget, Bus Factor) are still ambiguous. |
| **Gate 2** | End of Phase 2 (Blind-Spots & Kano) | `fitness_audit.py --gate 2` | Fails if $<4$ Quadrant-4 domain blind spots are identified, or if 30% Kano Delighters introduce fragile maintenance burdens. |
| **Gate 3** | End of Phase 3 (C-Suite Red-Team) | `fitness_audit.py --gate 3` (Adversarial Deduction Score $\ge 85/100$) | Fails if any C-Suite persona gave generic praise without mathematical/architectural proof, or if $<3$ concrete flaws were caught and fixed. |
| **Gate 4** | End of Phase 4 (12M Architecture) | `fitness_audit.py --gate 4` | Fails if Tier-A (Core) and Tier-B (Volatile Config/Prices) are mixed, or if historical snapshot isolation is missing. |
| **Gate 5** | During Phase 5 (After **EVERY** Vertical Slice) | `fitness_audit.py --gate 5 --scan-code <dir>` + **Actual Test Execution** | Fails if **ANY** test fails, if `TODO`/`FIXME`/`mock`/placeholder stubs exist in code, or if volatile values are hardcoded. |
| **Gate 6** | End of Phase 6 (365-Day Handover) | `fitness_audit.py --gate 6 --scan-code <dir>` | Fails if 1-Click Backup/Export, 5-Min Manual Fallback SOP, or Quarterly Audit Prompt is missing/untested. |

---

## 3. Phase 5 Executable Code & Deliverable Verification Protocol

When building software, scripts, calculators, spreadsheets, or automated workflows in Phase 5, **self-reported "I finished coding" is strictly forbidden.**

For **every vertical slice** (`Slice 1`, `Slice 2`, `Slice 3`, `Slice 4`), execute this 4-step verification loop before marking the slice `done` in `STATE.json`:

### Step 1: Automated Anti-Stub & Anti-Hardcode Scan
Run `python "<skill_dir>/scripts/fitness_audit.py" --dir "<project_dir>" --scan-code "<project_dir>"` to verify:
* **Zero Stubs/Mocks:** No `TODO`, `FIXME`, `pass # implement`, `mockData`, or fake UI buttons without real handlers.
* **Zero Hardcoded Secrets/Volatility:** No hardcoded API keys or magic business numbers inside Tier-A core logic files.

### Step 2: Deterministic Unit & Edge-Case Tests (TDD Enforcement)
Write and execute an automated test script (`tests/test_slice_<N>.py` or `npm test`) covering:
1. **Happy Path:** Standard valid inputs produce exact expected output.
2. **Boundary / Zero / Negative Values:** `0`, negative numbers, empty strings, huge numbers ($10^9$), non-ASCII Unicode characters.
3. **Config Mutation Isolation Test:** Change a price/rule in Tier-B `config` $\rightarrow$ verify that a new calculation uses the new price **AND** previously saved historical snapshots remain 100% unchanged!

### Step 3: Live Runtime / UI Smoke Verification
* If CLI / Backend / Script: Execute the actual command via `run_command` and inspect stdout/stderr and generated output files.
* If Web / UI App: Start the local server and verify the rendered DOM/console (zero runtime JS errors, mobile viewport layout intact).
* If Document / Spreadsheet / Content System: Verify formula integrity, formatting, and schema compliance.

### Step 4: Mid-Flight Scope Change Guard
If the user requests a new feature or change during Phase 5:
1. **Pause 10 seconds** and classify the change:
   * *Type 1 (Config/Parameter tweak):* Update Tier-B config only.
   * *Type 2 (New Modular Capability):* Add as a decoupled Tier-C plugin/adapter or schedule as `Slice N+1`.
   * *Type 3 (Core Invariant Conflict):* Warn the user if the change violates `00-PROJECT-CONSTITUTION.md` (e.g., breaks historical immutability or explodes recurring costs) and propose a safe alternative.
