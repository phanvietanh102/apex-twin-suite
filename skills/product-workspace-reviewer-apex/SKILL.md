---
name: product-workspace-reviewer-apex
description: >-
  Use this skill when someone wants something they ALREADY use assessed as a whole and made better: a product, app, business workflow, spreadsheet or invoice system, content operation, service process, project workspace or personal system, in ANY field, industry, country or context. Includes short requests such as "review giùm tôi workspace này" pointing at a folder, "audit / clean up / modernize what I've been using", or "it works, but how can it be better?". Triggers on "/review-product", "/apex-review", "/audit-workspace", "/apex-improve". Not for reviewing a single pull request or diff, a line-by-line code review of a change, or fixing one specific bug.
---

# APEX Product & Workspace Reviewer (v4.0)

## What this skill is for

The owner brings something they rely on, often their livelihood. It is usually an incomplete or drifted attempt at what they originally wanted. Often they believe it is already as good as it gets, while it quietly loses time, money or safety every day. A strong model can review files competently. What it reliably lacks is **thoroughness that survives to the end**: it notices an issue and never fixes it, fixes the visible thing while the costly one stays hidden, or calls the job done without proof.

This skill adds the missing layer and leaves the model's judgment free:

- **Completeness:** sweep every important angle ([`07`](./references/07-completeness-lenses.md)).
- **Traceability:** every issue and wish reaches a final status with evidence ([`08`](./references/08-definition-of-done-and-traceability.md)).
- **Proof:** parity with what already works, protected history, and tested change scenarios ([`08`](./references/08-definition-of-done-and-traceability.md)).
- **Field depth for any context:** a domain brief for the owner's exact field and jurisdiction ([`09`](./references/09-domain-discovery-protocol.md)).
- **Continuous improvement:** a measured baseline and a habit of getting better ([`10`](./references/10-continuous-improvement.md)).

The goal: the owner ends up thinking *"I didn't know it could be this much better, and nothing I relied on broke."* Always reply, and write user-facing deliverables, in the owner's language.

---

## Turn 1: findings first, then the root-vision questions; no file changes

1. **Read the workspace for real.** The quick inventory is `python "<skill_dir>/scripts/xray_scanner.py" --dir "<target>" --name "<name>" --scan-only`; it writes nothing. Then open the actual files, run what is safe to run, recompute the numbers, and read the records. Build the domain brief (09) for this field and place.
2. **Lead with 3–6 findings, ranked by money, data and safety risk, each with evidence:** file and line, the number you computed, the record affected, and what it costs the owner. Proposing *what* to fix is fine. Do not edit, move or create files in the workspace yet: you do not know what the owner considers sacred.
3. **Ask at most 3 questions, each answerable in one line,** set apart from the findings:
   - *Original vision:* "What did you originally want this to do, start to finish?"
   - *Pain and gaps:* "Where does it waste your time, and what did you want that it never did?"
   - *Sacred:* "Which files, data or habits must stay exactly as they are?"

   Merge or drop any the workspace already answers. Stop and wait.

**Why this order:** findings prove the review is worth the owner's time. The vision questions stop you from polishing the wrong thing. A read-only Turn 1 protects data the owner has not yet called sacred.

---

## Turn 2 onward: outcomes, not a script

All of these must be true before handover.

- **Gap matrix shown, short and plain:**
  - *keep*: what already serves the vision;
  - *built wrong*: what drifted;
  - *never built*: vision items with no implementation;
  - *beyond expectation*: cheap, high-value additions and silent-leak fixes.

  See [`01`](./references/01-forensic-discovery-and-dual-elicitation.md) and [`02`](./references/02-multi-domain-audit-matrix.md); the archetypes there are examples, not a boundary. Every item becomes a `TRACE.md` row.
- **Path chosen:**
  - If the owner delegates ("cứ chọn phương án bạn thấy hợp nhất và làm tiếp", "you decide", "làm luôn"), decide in one line and build in the same reply.
  - Otherwise, show at most 3 options with pros, cons, best-fit and your recommendation, only where the choice is genuinely theirs.
- **Safe first:** slice 1 is a verified backup of the current state plus locked history. Historical invoices, customer records and live data stay read-only, with a hash, and are never moved or edited.
- **Heaviest flow next:** then the owner's biggest pain or volume, then the rest of *never built*, then the delighters.
- **Proven:**
  - every slice has real tests or a real run;
  - parity holds: existing valid inputs give the same results unless intentionally corrected, and you state it when they do;
  - the number of change scenarios the context profile requires pass (08 §4; usually 3).
- **Tailored, then swept:** answer the context profile (07 Step 0), then sweep with the rules it activates (07); the others are `N/A` with a reason. All `TRACE.md` rows are final.
- **Measured:** a baseline and a before/after on 2–4 metrics the owner cares about. When the system already works, run the continuous-improvement loop (10) and leave `IMPROVEMENT-LOG.md` plus a re-review prompt.
- **Handed over:**
  - what changed, before and after;
  - the daily use;
  - how to change prices or rules safely;
  - backup and rollback;
  - the short traceability table ("Bạn cần → Nằm ở đâu → Đã kiểm thế nào").

- **No silent deferral:** a **High** row (law or compliance, safety or health, money at risk, irreversible or historical data, the owner's root vision, their #1 pain) ends `DONE`, with at least a minimal working version or exact actionable instructions, or ends `DEFERRED` only with `agreed: "<owner's words>"`. A line saying "check later" is not coverage.
- **Looking ahead:** the domain brief's next-12–24-months section (scheduled mandates, price risk and hedging, financing, the growth path toward the owner's long-term goal) has been checked against the plan.

## The daily operators decide the medium

Installing Python or packages for your own analysis, generation and testing is one command and costs nothing; use code freely. But what the owner's people operate every day must run where they already live: their phone, Excel, Outlook, Zalo or existing platform. See [`08` §2](./references/08-definition-of-done-and-traceability.md).

Eval run 3 showed why this matters: an Excel-only accountant received a Python engine whose summary sheet showed `#NAME?` in real Excel. Code that *builds and verifies* a native workbook gives both: the operators keep their tool and the owner gets reproducibility.
- Shared workflows must not depend on one machine.
- Verify in the target app: recalculate spreadsheets in a real engine with zero error values, and use only functions their version supports. If you could not, say so and give a 1-minute check.

## Beyond the obvious fixes

Eval runs 3–4 found that the plain model sometimes beat the skill on these. They are generic but **not universal**: apply the ones the context profile activates (07 Step 0), mark the rest `N/A` with a one-line reason, and scale depth to the stakes:
- **Audit the counterparties, not only the owner:** check penalties, fees and deductions claimed against the contract and legal caps, and send a ready dispute message.
- **Minimise data:** no ID, bank or health data copied into shared files; set retention and deletion.
- **Sanity-check the data:** against itself and field norms (impossible dates, yields above the norm, stock contradictions, claims the owner's own data disproves).
- **Standard instruments of the field first** (09).
- **Second-order effects of every fix:**
  - remedy past periods;
  - reprice when compliance raises cost;
  - tell affected people first, with ready messages;
  - plan for the system's own failure (owner account, silent-stop alarm, permissions, a parallel run or drill before cut-over).
- **Close findings with a fix or a ready replacement,** not a warning.

## Respect the owner's time

- Start every substantial reply with a summary of 10 lines or fewer. Put details in files written in the owner's language.
- **Leave no clutter:** process files (trace, ledger, notes) go in one `_apex/` folder (or `docs/apex-review/` in STANDARD/DEEP mode), never loose in the owner's working folder. User-facing files are few, plain, and in the owner's language.
- Lenses, gates, zone colours, scores and phase names are internal; do not show them unless asked.
- For rules, rates and fees, give the identifier and date, and mark unverified items with who can confirm them.

## Rigor modes (choose silently)

| Mode | When | Shape |
| :--- | :--- | :--- |
| `LEAN` (default) | Small workspace, one to a few operators | `_apex/TRACE.md` + one compact review (`_apex/REVIEW.md`, ≤ 120 lines) or none. |
| `STANDARD` | Multi-module app or business-critical workflow | Ledger in `docs/apex-review/`; gates per slice. |
| `DEEP` | The owner asks, or the stakes are high (money movement, health, legal, irreversible data, safety) | One synchronous critic-subagent pass, run once; never sleep-poll. See [`03`](./references/03-c-suite-diagnostic-council.md). |

In chat-only hosts, keep `TRACE.md` and the change scenarios as tables in the reply, and replace script gates with a traced simulation: 1 normal case and 2 failure cases.

## Scripts (CLI/IDE hosts)

* **Turn-1 inventory (read-only):** `python "<skill_dir>/scripts/xray_scanner.py" --dir "<target>" --name "<name>" --scan-only`
* **Scaffold (Turn 2+):** the same command with `--domain "<DOM-01..07 or any free-text field>"` and without `--scan-only`. It writes `docs/apex-review/` and `TRACE.md`. In `LEAN` mode skip the scaffold and create only `_apex/TRACE.md` yourself.
* **Gate audit:** `python "<skill_dir>/scripts/review_gate_audit.py" --dir "<target>" --gate <1..6> --scan-target "<target>"`
* **How the gates judge:**
  - Documents contain `[[FILL: hint]]` markers; a gate is vetoed while any remain.
  - Gate 3 needs `TOTAL UPGRADED SCORE` ≥ 85.
  - Gate 5 needs `--scan-target`, a proven slice in `REVIEW-STATE.json` (slice-1 = backup), and a valid `TRACE.md`.
  - Gate 6 needs all slices proven, no `OPEN` rows, and `change_scenarios_required` passed scenarios (default 3; fewer needs a `change_scenarios_waiver` reason).
  - Never pre-select an option or write a score, proof or status you did not obtain.
* When building, load only [`06`](./references/06-stage-gates-rollback-and-regression.md), `TRACE.md` and the locked plan.

## Shortcuts the user may type

* `/review-product [path or description]` or `/apex-review`: Turn-1 findings and questions, then the upgrade.
* `/audit-workspace`: findings on organisation and risk, then a cleaner structure with protected history.
* `/apex-improve`: continuous-improvement loop on a system that already works (10).
* `/apex-review-lean`: `LEAN` mode; findings plus an upgrade in one compact report.
* `/apex-delta`: before/after comparison with `review_gate_audit.py`.
