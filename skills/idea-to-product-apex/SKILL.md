---
name: idea-to-product-apex
description: >-
  Use this skill when someone wants to turn an idea, goal or vague problem that matters to them into a complete, working result: a product, app, tool, system, business process, content operation, event, project or personal plan, in ANY field, industry, country or context (business, public sector, education, health, creative, personal). Includes short requests such as "build me an app that does a, b, c", "help me plan X" or "I want to start Y". Triggers on "/idea-to-product", "/apex", "/apex-lean", or when the user asks to brainstorm, elicit requirements, red-team a plan, or design something meant to run for 12+ months. Not for small edits, single bug fixes, or quick factual questions.
---

# APEX Idea-to-Product (v4.0)

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

1. **Lead with value on Turn 1.** Build the domain brief first (09). Open with 2–4 specific findings from it for this user's field, location and situation: an obligation, a cost trap, a data-loss risk, a practitioner's norm, a capability they did not mention. Then give your recommended direction and, when cheap, a first draft. Then ask questions.
2. **Ask at most 3 questions, each answerable in one line,** and only ones whose answers change what you build. Give a sample answer when it helps. Always leave one open question for the user's own idea or local knowledge; they know things no model does.
3. **Offer options only when the choice is genuinely the user's.** When paths differ in ways only the user can weigh, show at most 3, with pros, cons, "best if you want…" and your recommendation. Otherwise recommend in one sentence and move on. See [`01`](./references/01-elicitation-and-beyond-smart.md).
4. **When the user delegates** ("cứ chọn phương án bạn thấy hợp nhất và làm tiếp", "you decide", "làm luôn", "just build it"), decide in one line, list your assumptions, and build in the same reply. No new options round.
5. **Heaviest flow first.** Rank flows by volume, money and risk (lens 2). The heaviest one must be complete before minor ones get polish.
6. **Respect the user's time.** Start every substantial reply with a summary of 10 lines or fewer: what I found, what I built, what you do next. Put details in files.
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
- **Beyond the brief:** at least 3 field-specific traps addressed, plus a few cheap, low-maintenance additions the user did not ask for, each with why it matters to *them*.
- **Attacked:** you critiqued your own plan from product, technical, money, risk, field-expert and skeptical-daily-user angles, and fixed at least 3 concrete flaws. In `DEEP` mode an isolated critic subagent does this once. See [`03`](./references/03-c-suite-red-team-protocol.md).
- **Built to last 12 months:**
  - volatile values (prices, rates, rules, prompts) live in one editable place;
  - history is protected from later edits;
  - there is a manual fallback for critical dependencies;
  - you state the scale ceiling.

  See [`04`](./references/04-12month-evergreen-architecture.md).
- **Built and proven in slices,** heaviest flow first. Each slice is verified (tests, a real run, worked examples) with no stubs and no fake data. See [`06`](./references/06-stage-gates-and-code-verification.md).
- **Swept:** a full completeness sweep (07). It includes counterparty claims checked against contracts and caps, data minimised in everything you build, and the data sanity-checked against itself and field norms. Then a second-order sweep of every fix: past periods, cost and price, the people to tell, and the system's own failure modes. Every finding is tracked in `TRACE.md` and closed by a fix or a ready-to-use replacement, never by a warning alone.
- **Done by definition:** the definition of done for each deliverable type is met (08). Every `TRACE.md` row is `DONE`, `DEFERRED` with a reason, `DROPPED` with the user's agreement, or `N/A`. At least 3 change scenarios have passed.
- **No silent deferral:** a **High** row (law or compliance, safety or health, money at risk, irreversible data, the user's root vision, their #1 pain) ends `DONE`, with at least a minimal working version or exact actionable instructions, or ends `DEFERRED` only with `agreed: "<user's words>"`. A line saying "check later" is not coverage.
- **Looking ahead:** the domain brief's next-12–24-months section (scheduled mandates, price risk and hedging, financing, the growth path) has been checked against the plan.
- **Handed over:**
  - setup a non-specialist can follow;
  - the daily routine;
  - how to change prices and rules safely;
  - backup;
  - what to check in 3, 6 and 12 months;
  - a re-review prompt.

### Rigor modes (choose silently)

| Mode | When | Shape |
| :--- | :--- | :--- |
| `LEAN` (default) | One operator, single-session scope | `_apex/TRACE.md` + a compact spec (`_apex/SPEC.md`, ≤ 120 lines) or none. Most effort goes into building and proving. |
| `STANDARD` | Multi-session product or business-critical process | Full ledger in `docs/apex-blueprint/`; gates per slice. |
| `DEEP` | The user asks, or the stakes are high (money movement, health, legal, irreversible data, safety) | Adds one synchronous critic-subagent pass, run once; never sleep-poll. |

In chat-only hosts (no files or terminal), keep `TRACE.md` and the change scenarios as tables in the reply, and replace script gates with a short traced simulation: 1 normal case and 2 failure cases.

---

## Scripts (CLI/IDE hosts)

* **Scaffold:** `python "<skill_dir>/scripts/init_project.py" --dir "<target>" --name "<project>" --domain "<DOM-01..07 or any free-text field, e.g. 'dental clinic, Da Nang'>"`
  - It creates `docs/apex-blueprint/` (STANDARD/DEEP) and `TRACE.md`.
  - For LEAN, skip the scaffold and create only `_apex/TRACE.md` yourself.
* **Gate audit:** `python "<skill_dir>/scripts/fitness_audit.py" --dir "<target>" --gate <1..6> --scan-code "<code_dir>"`
* **How the gates judge:**
  - Documents contain `[[FILL: hint]]` markers; a gate is vetoed while any remain.
  - Gate 3 needs `TOTAL C-SUITE AUDIT SCORE` ≥ 85.
  - Gate 5 needs `--scan-code`, at least one proven slice in `STATE.json`, and a valid `TRACE.md` (no `DONE` without evidence).
  - Gate 6 needs all slices proven, no `OPEN` rows in `TRACE.md`, and at least 3 passed `change_scenarios`.
  - Never write a score, proof or status you did not actually obtain. Report results as plain outcomes, not gate numbers.

## Shortcuts the user may type

* `/idea-to-product [idea]` or `/apex [idea]`: start (Turn-1 rules above).
* `/apex-lean [idea]`: `LEAN` mode; build as early as possible.
* `/apex-redteam`: critique an idea, plan or codebase (critic subagent if available).
* `/apex-blueprint`: scaffold `docs/apex-blueprint/` and run Gate 4.
* `/apex-verify` or `/apex-audit`: run `fitness_audit.py` with `--scan-code`.
