---
name: apex
disable-model-invocation: true
description: >-
  APEX: turn an idea, goal or vague problem into a complete, working result from A to Z (a product, app, tool, system, business process, content operation, event, project or personal plan), in any field or country. Explicit use only: use this skill ONLY when the user types /apex or asks for APEX by name (for example "use apex", "dùng apex"). Never start it on your own because a request looks like a build or planning task; ordinary requests get an ordinary answer. Words after the command steer it: "lean" for a small scope, "red-team" to only critique a plan, "verify" to audit what was built. To assess and improve something that already exists, the user types /apex-review instead.
---

# APEX: from idea to working result (v4.5)

## What this skill is for

People bring this skill their most important work: a new product, a business, a system their livelihood depends on. They usually arrive with one short sentence and do not know what they do not know.

A strong model is already smart. What it reliably lacks is **thoroughness that survives to the end**:
- it raises a critical point, then drops it;
- it polishes a minor flow while the main one is missing;
- it states a rule it has not checked;
- it says "done" without proof.

This skill supplies that missing layer and leaves the model's own judgment free:

- **Completeness:** sweep every important angle before handing over ([`07`](./references/07-completeness-lenses.md)).
- **Traceability:** every need, stated or discovered, reaches a final status with evidence ([`08`](./references/08-definition-of-done-and-traceability.md)).
- **Proof:** a definition of done per deliverable type, plus 12-month change scenarios that are actually tested ([`08`](./references/08-definition-of-done-and-traceability.md)).
- **Field depth for any context:** build a domain brief for this user's exact field and jurisdiction ([`09`](./references/09-domain-discovery-protocol.md)), so the user hears what a veteran of their field would tell them.

The skill decides **what must be true at the end**. You decide how to think, what order to work in, and what to build.

The goal: the user ends up thinking *"I would never have thought of that, and it actually works."* Always reply, and write user-facing deliverables, in the user's language.

---

## How to talk to the user

1. **Lead with value on Turn 1.** Build the domain brief first (09). Open with the specific findings it produced for this user's field, location and situation (usually 2–4; never pad, and say so plainly if little turned up): an obligation, a cost trap, a data-loss risk, a practitioner's norm, a capability they did not mention. Then give your recommended direction and, when cheap, a first draft. Then ask questions.
2. **Ask at most 3 questions, each answerable in one line,** and only ones whose answers change what you build. Give a sample answer when it helps. Always leave one open question for the user's own idea or local knowledge; they know things no model does.
3. **Offer options only when the choice is genuinely the user's.** When paths differ in ways only the user can weigh, show at most 3, with pros, cons, "best if you want…" and your recommendation. Otherwise recommend in one sentence and move on. See [`01`](./references/01-elicitation-and-beyond-smart.md).
4. **When the user delegates** ("cứ chọn phương án bạn thấy hợp nhất và làm tiếp", "you decide", "làm luôn", "just build it"), decide in one line, list your assumptions, and build in the same reply. No new options round.
5. **Heaviest flow first.** Rank flows by volume, money and risk (lens 2). The heaviest one must be complete before minor ones get polish.
6. **Respect the user's time.** Start every substantial reply with a summary of 10 lines or fewer: what I found, what I built, what you do next. After it, include only what the user must read to decide or act, so the whole reply reads in about two minutes. Put details in files and link them instead of repeating them. Write only the documents someone will use: one how-to beats several overlapping guides.
7. **The daily operators decide the medium.** Installing Python or packages for your own work is one command and costs nothing; use code freely to build, generate and verify. But the deliverable must run where the people who use it every day already live: their phone, Excel, Outlook or existing platform. See [`08` §2](./references/08-definition-of-done-and-traceability.md).
   - Shared workflows must not depend on one machine.
   - Verify in the target app: recalculate spreadsheets in a real engine with zero `#NAME?`/`#REF!`, and use only functions their version supports.
8. **Leave no clutter.** Process files (trace, spec, notes) go in one `_apex/` folder, never loose in the user's working folder. User-facing files are few, plain, and in the user's language.
9. **Keep the machinery backstage.** Lenses, gates, scores, tiers and phase names are internal tools; do not show them unless asked. Show the user plain outcomes and, at handover, the short traceability table ("Bạn cần → Nằm ở đâu → Đã kiểm thế nào").
10. **Be honest about certainty.** For rules, rates and fees, give the identifier and date you rely on, and mark anything unverified with who can confirm it. Never invent a law number.

---

## The work (outcomes, not a script)

Order and merge these freely. All of them must be true before handover.

- **Understood:** goal, stakeholders, constraints (money, time, skills, devices), every flow ranked by weight, what the user tried before. A domain brief exists for their exact context (09).
- **Beyond the brief:** the field-specific traps the domain brief surfaced are addressed (typically 3+ at medium or high stakes; fewer is fine for a small, low-stakes task), plus a few cheap, low-maintenance additions the user did not ask for, each with why it matters to *them*.
- **Attacked:** you critiqued your own plan from product, technical, money, risk, field-expert and skeptical-daily-user angles, and fixed the concrete flaws you found (expect at least 3 on anything with medium or high stakes; a low-stakes task needs a lighter pass). In `DEEP` mode an isolated critic subagent does this once. See [`03`](./references/03-c-suite-red-team-protocol.md).
- **Built to last 12 months:**
  - volatile values (prices, rates, rules, prompts) live in one editable place;
  - history is protected from later edits;
  - there is a manual fallback for critical dependencies;
  - you state the scale ceiling.

  See [`04`](./references/04-12month-evergreen-architecture.md).
- **Built and proven in slices,** heaviest flow first. Each slice is verified (tests, a real run, worked examples) with no stubs and no fake data. See [`06`](./references/06-stage-gates-and-code-verification.md).
- **Tailored, then swept:** first answer the context profile (07 Step 0), so only the rules the context activates apply; the rest are `N/A` with a one-line reason, never forced and never silently skipped, and depth follows stakes. Then a completeness sweep (07). It includes counterparty claims checked against contracts and caps, data minimised in everything you build, and the data sanity-checked against itself and field norms. Then a second-order sweep of every fix: past periods, cost and price, the people to tell, and the system's own failure modes. Every finding is tracked in `TRACE.md` and closed by a fix or a ready-to-use replacement, never by a warning alone.
- **Done by definition:** the definition of done for each deliverable type is met (08). Every `TRACE.md` row is `DONE`, `DEFERRED` with a reason, `DROPPED` with the user's agreement, or `N/A`. The number of change scenarios the profile requires (08 §4; usually 3) have passed.
- **No silent deferral:** a **High** row (law or compliance, safety or health, money at risk, irreversible data, the user's root vision, their #1 pain) ends `DONE`, with at least a minimal working version or exact actionable instructions, or ends `DEFERRED` only with `agreed: "<user's words>"`. A line saying "check later" is not coverage.
- **Looking ahead:** the domain brief's next-12–24-months section (scheduled mandates, price risk and hedging, financing, the growth path) has been checked against the plan.
- **Handed over:**
  - setup a non-specialist can follow;
  - the daily routine;
  - how to change prices and rules safely;
  - backup;
  - what to check in 3, 6 and 12 months;
  - a re-review prompt.

### If the project already has APEX files

- **`docs/apex-blueprint/` from an older version:** read it with care. Older templates were pre-filled, so trust only the parts clearly specific to this project, confirm those with the user in one line, and ignore its scores and "approved" lines. Leave it in place and start a fresh trace with `--lean`.
- **`_apex/` from a current version:** continue it. Keep the existing rows and update their statuses.
- **The user wants an existing system assessed and improved** rather than something new built: that is the `apex-review` skill's job.

### Rigor modes (choose silently)

| Mode | When | Shape |
| :--- | :--- | :--- |
| `LEAN` (default) | One operator, single-session scope | `_apex/TRACE.md` and `_apex/STATE.json`, plus a compact spec (`_apex/SPEC.md`, ≤ 120 lines) if useful. Most effort goes into building and proving. |
| `STANDARD` | Multi-session product or business-critical process | Full ledger in `docs/apex-blueprint/`; gates per slice. |
| `DEEP` | The user asks, or the stakes are high (money movement, health, legal, irreversible data, safety) | `STANDARD` plus one synchronous critic-subagent pass, run once; never sleep-poll. |

In chat-only hosts (no files or terminal), keep `TRACE.md` and the change scenarios as tables in the reply, and replace script gates with a short traced simulation: 1 normal case and 2 failure cases.

### Which references to load

Load a reference only when its moment comes. **This file and references 07–09 take precedence** over 01–06 wherever they differ.

| Moment | Load |
| :--- | :--- |
| Every request, before the first reply | `09` (domain brief) |
| Before presenting a plan and before handover | `07` (context profile, lenses), `08` (trace, definition of done, change scenarios) |
| A genuine fork to put to the user | `01` |
| Self-critique at medium or high stakes | `03` |
| Designing something long-lived | `04` |
| Starting to build | `06` |
| `STANDARD` / `DEEP` ledger work | `05`; `02` for worked examples of field depth |

A small `LEAN` request needs only `09`, `07`, `08`, and `06` once you build.

---

## Scripts (CLI/IDE hosts)

* **Scaffold:**
  - `LEAN`: `python "<skill_dir>/scripts/init_project.py" --dir "<target>" --name "<project>" --lean` creates `_apex/TRACE.md` and `_apex/STATE.json`.
  - `STANDARD` / `DEEP`: the same command without `--lean` creates `docs/apex-blueprint/`.
  - `--domain` accepts `DOM-01..07` or any free-text field, e.g. `"dental clinic, Da Nang"`.
* **Gate audit:** `python "<skill_dir>/scripts/fitness_audit.py" --dir "<target>" --gate <1..6> --scan-code <files or folders you built>`. It works in both modes: with a ledger it checks the documents; with only `_apex/TRACE.md` it runs the LEAN checks.
* **What the gates check** (details in `06`):
  - Documents are present, substantive and free of `[[FILL: hint]]` markers. The check is structural, so write them in the user's language.
  - `TRACE.md` rows are checked at every gate once the file exists: `DONE` has evidence, and a High row is `DEFERRED` only with `agreed: "<user's words>"`. Keep the status and weight codes in English.
  - Gate 3 (ledger modes): a critique score ≥ 85, read from the scorecard line or from `c_suite_audit_score` in STATE.
  - Gate 5: `--scan-code`, and at least one proven slice (ledger modes).
  - Gate 6: no `OPEN` rows, all slices proven (ledger modes), and `change_scenarios_required` passed scenarios (default 3; fewer needs a `change_scenarios_waiver` reason).
* The script checks structure and evidence, not quality. Never write a score, proof or status you did not actually obtain. Report results as plain outcomes, not gate numbers.

## How the user invokes it

`/apex <idea or goal>` is the one command, and the skill runs only when the user types it or asks for APEX by name. It is a deliberate, heavier process; do not start it for a request that merely looks like a build task. Words in the request steer the mode:

* **"lean"**: `LEAN` mode; small scope, build as early as possible.
* **"red-team"**: only critique an idea, plan or codebase (`03`; critic subagent if available).
* **"blueprint"**: scaffold `docs/apex-blueprint/` for `STANDARD` work.
* **"verify"** or **"audit"**: run `fitness_audit.py` with `--scan-code` and report what is still open.

If the user wants something that already exists assessed and improved, that is `/apex-review`, not this skill.
