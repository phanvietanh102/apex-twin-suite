---
name: apex-review
disable-model-invocation: true
description: >-
  APEX Review: a whole-system audit of something the user ALREADY uses (a product, app, business workflow, spreadsheet or invoice system, content operation, project workspace), followed by concrete optimisation proposals and, when they agree, the upgrade itself, in any field or country. Explicit use only: use this skill ONLY when the user types /apex-review or asks for an APEX review by name (for example "use apex-review", "dùng apex review"). Never start it on your own because a request says "review", "audit" or "improve": an ordinary review request, a code review, a pull request or diff, a single file, or a small task gets an ordinary review without this skill. Words after the command steer it: "improve" for continuous improvement of a system that already works, "lean" for a compact report. To build something new from an idea, the user types /apex instead.
---

# APEX Review: audit and optimise what already exists (v4.5)

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
2. **Lead with what you found (usually 3–6 items), ranked by money, data and safety risk, each with evidence.** Never pad; if the workspace is healthy, say so and name what could still be better: file and line, the number you computed, the record affected, and what it costs the owner. Proposing *what* to fix is fine. Do not edit, move or create files in the workspace yet: you do not know what the owner considers sacred.
3. **Ask at most 3 questions, each answerable in one line,** set apart from the findings:
   - *Original vision:* "What did you originally want this to do, start to finish?"
   - *Pain and gaps:* "Where does it waste your time, and what did you want that it never did?"
   - *Sacred:* "Which files, data or habits must stay exactly as they are?"

   Merge or drop any the workspace already answers. Stop and wait.

   **Exception:** if the owner's first message already says what must stay untouched *and* tells you to decide and proceed, do not wait. Take the verified backup, then continue with the outcomes below in the same reply.

**If the workspace was built or reviewed with APEX before** (the inventory lists "Earlier APEX files"):
- **`docs/apex-blueprint/` or `docs/apex-review/` from an older version:** read it, but with care. Older templates were pre-filled, so much of it may be boilerplate that nobody decided. Trust only the parts that are clearly specific to this project (names, numbers, features the owner would recognise). Offer those back to the owner in one line to confirm, and ask about the rest. Ignore its scores, "PASS" and "approved" lines. A promise in the old ledger that the app does not keep is a finding only if the owner confirms they wanted it. Leave the old ledger in place, unedited.
- **`_apex/` from a current version:** continue it. Keep the existing rows and update their statuses; do not start a new trace.
- New process files go in `_apex/` (`LEAN`). For `STANDARD` work where an older `docs/apex-review/` exists, stay in `_apex/` or ask the owner before moving the old folder aside.

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
- **Safe first:** slice 1 is a verified backup of the current state plus locked history. Put the backup beside the workspace (for example `<workspace>_backup_<date>/` or a zip) or where the owner says, on a different drive or cloud location when one is available, and tell the owner where it is. Finished records (issued invoices, signed contracts, closed periods) are protected in place: a hash, read-only where that does not disturb the system, never moved or edited. Live data the system still writes to (a running database, the current sheet) is backed up but **not** set read-only; change it only with a tested rollback.
- **Heaviest flow next:** then the owner's biggest pain or volume, then the rest of *never built*, then the delighters.
- **Proven:**
  - every slice has real tests or a real run;
  - parity holds: existing valid inputs give the same results unless intentionally corrected, and you state it when they do;
  - the number of change scenarios the context profile requires pass (08 §4; usually 3).
- **Tailored, then swept:** answer the context profile (07 Step 0), then sweep with the rules it activates (07); the others are `N/A` with a reason. All `TRACE.md` rows are final.
- **Measured:** a baseline and a before/after on the few metrics the owner cares about. When the system will keep running (profile g) and already works, run the continuous-improvement loop (10) and leave `IMPROVEMENT-LOG.md` plus a re-review prompt; for a one-off review, a before/after is enough.
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

The failure to avoid: an accountant who only uses Excel receives a Python engine, and its summary sheet shows `#NAME?` when opened in real Excel. Code that *builds and verifies* a native workbook gives both: the operators keep their tool and the owner gets reproducibility.
- Shared workflows must not depend on one machine.
- Verify in the target app: recalculate spreadsheets in a real engine with zero error values, and use only functions their version supports. If you could not, say so and give a 1-minute check.

## Beyond the obvious fixes

These are easy to miss. They are generic but **not universal**: apply the ones the context profile activates (07 Step 0), mark the rest `N/A` with a one-line reason, and scale depth to the stakes:
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
- **Keep replies short.** After the summary, include only what the owner must read to decide or act: the findings, what changed, what they do next. Aim for a reply the owner can read in about two minutes. Do not repeat in chat what a file already says; link the file.
- **Write only the documents someone will use.** One how-to for the operators beats several overlapping guides. Do not produce documents that restate the chat or exist to show effort.
- **Leave no clutter:** process files (trace, ledger, notes) go in one `_apex/` folder (or `docs/apex-review/` in STANDARD/DEEP mode), never loose in the owner's working folder. User-facing files are few, plain, and in the owner's language.
- Lenses, gates, zone colours, scores and phase names are internal; do not show them unless asked.
- For rules, rates and fees, give the identifier and date, and mark unverified items with who can confirm them.

## Rigor modes (choose silently)

| Mode | When | Shape |
| :--- | :--- | :--- |
| `LEAN` (default) | Small workspace, one to a few operators | `_apex/TRACE.md` and `_apex/STATE.json`, plus one compact review (`_apex/REVIEW.md`, ≤ 120 lines) if useful. |
| `STANDARD` | Multi-module app or business-critical workflow | Ledger in `docs/apex-review/`; gates per slice. |
| `DEEP` | The owner asks, or the stakes are high (money movement, health, legal, irreversible data, safety) | `STANDARD` plus one synchronous critic-subagent pass, run once; never sleep-poll. |

In chat-only hosts, keep `TRACE.md` and the change scenarios as tables in the reply, and replace script gates with a traced simulation: 1 normal case and 2 failure cases.

## Which references to load

Load a reference only when its moment comes. **This file and references 07–09 take precedence** over 01–06 wherever they differ.

| Moment | Load |
| :--- | :--- |
| Turn 1, before the first reply | `09` (domain brief) |
| Building the gap matrix; a genuine fork to put to the owner | `01` |
| Before presenting the plan and before handover | `07` (context profile, lenses), `08` (trace, definition of done, change scenarios) |
| Critique at medium or high stakes | `03` |
| Planning the upgrade architecture | `04` |
| Starting to change files | `06` |
| The system already works and the owner wants it better | `10` |
| `STANDARD` / `DEEP` ledger work | `05`; `02` for worked examples of field depth |

A small `LEAN` review needs only `09`, `07`, `08`, and `06` once you change files.

## Scripts (CLI/IDE hosts)

* **Turn-1 inventory (read-only):** `python "<skill_dir>/scripts/xray_scanner.py" --dir "<target>" --name "<name>" --scan-only`
* **Scaffold (Turn 2+):**
  - `LEAN`: the same command with `--lean` instead of `--scan-only` creates `_apex/TRACE.md` and `_apex/STATE.json`.
  - `STANDARD` / `DEEP`: without either flag it creates `docs/apex-review/`.
  - `--domain` accepts `DOM-01..07` or any free-text field.
* **Gate audit:** `python "<skill_dir>/scripts/review_gate_audit.py" --dir "<target>" --gate <1..6> --scan-target <files or folders you built or changed>`. Point the stub scan at your own work, not the whole app: a `TODO` already in the owner's code is a finding to report, not a reason to edit code nobody asked you to touch. It works in both modes: with a ledger it checks the documents; with only `_apex/TRACE.md` it runs the LEAN checks.
* **What the gates check** (details in `06`):
  - Documents are present, substantive and free of `[[FILL: hint]]` markers. The check is structural, so write them in the owner's language.
  - `TRACE.md` rows are checked at every gate once the file exists: `DONE` has evidence, and a High row is `DEFERRED` only with `agreed: "<owner's words>"`. Keep the status and weight codes in English.
  - Gate 3 (ledger modes): a critique score ≥ 85 for the plan once the flaws the critique found are fixed, read from the `TOTAL UPGRADED SCORE` line or from `upgraded_health_score` in STATE.
  - Gate 5: `--scan-target`, and at least one proven slice (ledger modes; slice 1 is the backup).
  - Gate 6: no `OPEN` rows, all slices proven (ledger modes), and `change_scenarios_required` passed scenarios (default 3; fewer needs a `change_scenarios_waiver` reason).
* The script checks structure and evidence, not quality. Never pre-select an option or write a score, proof or status you did not obtain. Report results as plain outcomes, not gate numbers.

## How the user invokes it

`/apex-review <path or description>` is the one command, and the skill runs only when the user types it or asks for an APEX review by name. It is a deliberate, heavier process; a request that merely says "review" or "audit" gets an ordinary review. Words in the request steer the mode:

* **"improve"**: the system already works; run the continuous-improvement loop (`10`).
* **"lean"**: `LEAN` mode; findings plus an upgrade in one compact report.
* **"organise"** or **"clean up"**: findings on organisation and risk, then a cleaner structure with protected history (`04` §2).
* **"delta"**: a before/after comparison on the baseline metrics (`10`), plus `review_gate_audit.py` to list what is still open.

This is a deeper job than an ordinary review. If the user only wants a code review, a pull request or a single file looked at, say that `/apex-review` is the whole-system audit and do the plain review they asked for instead. If they want something new built from an idea, that is `/apex`.
