# 03. Critique Council: Six Angles, Before/After Scorecard

Load this for the critique step. In `LEAN` mode or at low stakes, a light pass through the six angles is enough. In `DEEP` mode, hand the critique to one isolated subagent (whatever subagent tool the host offers), run once. SKILL.md and references 07–09 take precedence over anything here.

## 1. Six angles, each backed by evidence

Generic advice does not count. Each angle should produce evidence from the owner's actual files and behaviour. Scale the effort to the stakes; skip an angle the context profile (07 Step 0) does not activate.

| Angle | Looks for | Evidence to produce |
| :--- | :--- | :--- |
| **Product / UX** | Friction in the core workflow | The steps, clicks and copy-pastes needed today vs. after the upgrade |
| **Systems / architecture** | Coupling, duplication, hard-coded volatile values | File paths and lines where prices, rules, URLs or prompts are hard-coded or duplicated |
| **Field expert** | Gaps against how good practitioners in this field work | A short gap list drawn from the domain brief (09), including the field's standard instruments |
| **Money / time** | Waste and leakage | A calculation: hours per month lost, money at risk, with the inputs shown |
| **Risk / operations** | Data loss, single points of failure, missing backups, unvalidated input | What would be lost in each failure, and whether a rollback exists |
| **Daily operator** | Real-world use under pressure | A walk-through with rushed edits, typos, phone use and messy data |

An upgrade should not add recurring cost, daily maintenance or complexity for the operators without a clear gain the owner accepts.

## 2. Before/after scorecard

The scorecard is your own summary of the critique. It stays internal unless the owner asks. Score honestly: the gate script only reads the number, so an inflated score defeats its purpose. If the plan cannot reach 85 after fixes, say what is blocking instead of raising the score.

Record it in `05-DIAGNOSTIC-SCORECARD-AND-ROLLBACK.md` (STANDARD/DEEP), which the scaffolder creates with one row per angle above. Keep the two total lines exactly, because the gate reads them. "After" is the plan once the flaws found are fixed, not a prediction of the finished build. If the document is written in another language, also set `upgraded_health_score` in `REVIEW-STATE.json`.

```markdown
| Angle | Before | Flaw found (evidence) | After | Fix |
| :--- | :---: | :--- | :---: | :--- |
| Product / UX (20) | x/20 | ... | y/20 | ... |
| Systems / architecture (20) | x/20 | ... | y/20 | ... |
| Field expert (15) | x/15 | ... | y/15 | ... |
| Money / time (15) | x/15 | ... | y/15 | ... |
| Risk / operations (15) | x/15 | ... | y/15 | ... |
| Daily operator (15) | x/15 | ... | y/15 | ... |

- **TOTAL BASELINE SCORE:** NN / 100
- **TOTAL UPGRADED SCORE:** NN / 100
```

## 3. Risks specific to upgrading a live system

| Risk | How it goes wrong | Defence |
| :--- | :--- | :--- |
| Destructive refactoring | Working files or data deleted or overwritten | Verified backup first; history protected in place |
| Broken habits | Familiar entry points or layouts changed for no gain | The owner's sacred items, captured on Turn 1 |
| Broken links | Moved files break scripts, formulas or links | Reference scan after any move (06 §3) |
| Silent calculation change | New logic gives slightly different numbers on old cases | Parity check on real past cases |
| Report without results | A long critique and nothing fixed | Slices built and proven, tracked in `TRACE.md` |
| Context overload | Hundreds of files read at once | `--scan-only` map first, then targeted reading |
| Relapse | The workspace is messy again in two months | A simple routine and, where cheap, a self-check (10) |
