# 03. Red-Team: Attack Your Own Plan from Six Angles

Load this for the self-critique step. In `LEAN` mode or at low stakes, a light pass is enough. In `DEEP` mode, hand the critique to one isolated subagent (whatever subagent tool the host offers), run once, giving it only the draft and this rubric so it has no attachment to the plan. SKILL.md and references 07–09 take precedence over anything here.

## 1. Why a separate critique

A model tends to approve its own draft. The cure is to look for concrete flaws on purpose, with evidence, before building. On anything with medium or high stakes, expect to find at least three real flaws; if you find none, look harder at the heaviest flow and at money and data. On a small, low-stakes task, a shorter pass is fine. Never invent flaws to reach a count.

## 2. Six angles, each backed by evidence

A remark such as "looks good, nicely modular" is not a critique. Each angle should produce something checkable. Skip an angle the context profile (07 Step 0) does not activate.

| Angle | Looks for | Evidence to produce |
| :--- | :--- | :--- |
| **Product** | Time and effort to first value; whether the user's own idea survived | The steps from start to first useful result; which of the user's own ideas are in the plan |
| **Systems** | Volatile values in core logic; history that later edits can change; dependency failure | Every volatile value and where it lives; what happens to old records when a value changes |
| **Field expert** | Mismatch with how the field really works | Field-specific failure modes from the domain brief (09); the field's standard instruments |
| **Money** | Cost at larger volume; daily human effort; margins | Cost and effort at today's volume and at 10×, with the inputs shown |
| **Risk and operations** | Bad or malicious input, outages, the key person absent, no backup | For each scenario: how it is detected, contained and recovered |
| **Skeptical daily user** | Confusing labels, tedious input, silent failures, phone use | A step-by-step walk-through as a busy, non-technical user |

## 3. Scoring

The score is your own summary of the critique and stays internal unless the user asks. Start from 100 and deduct for every flaw that is still open after your fixes. Typical serious deductions:
- volatile data hard-coded in core logic;
- history that later edits can alter;
- missing input validation or edge-case handling;
- the user's own idea ignored;
- no test or verification for the heaviest flow.

Proceed when the score is 85 or above with no serious flaw open. If the plan cannot get there, tell the user what is blocking instead of raising the number.

Record the total as `TOTAL C-SUITE AUDIT SCORE: NN / 100` in `05-FITNESS-FUNCTIONS-AND-RUNBOOK.md` (STANDARD/DEEP), or as `c_suite_audit_score` in `STATE.json` when the document is in another language. The gate script only reads this number; it cannot verify that the critique was honest, so an inflated score defeats its purpose.

## 4. Risks this step guards against

| Risk | How it goes wrong | Defence |
| :--- | :--- | :--- |
| Self-approval | The author praises a flawed design | Deliberate flaw hunt; isolated critic in `DEEP` |
| Late discovery | Quality is checked only at the end | Verify each slice as it is built |
| Placeholder code | Stubs or fake data presented as done | Stub scan plus real tests or runs |
| Process overload | Process text crowds out the product | `LEAN` by default; load references only when needed |
| Scope creep mid-build | A new idea is hacked into the core | Config change, separate module, or a later slice |
| Data migration trap | A later format change breaks saved data | A version field in saved data and a backward-compatible default |
| Input and locale bugs | Non-ASCII text, spreadsheet formulas or empty values crash it | Sanitise at the boundary; test zero, negative, empty and Unicode input |
