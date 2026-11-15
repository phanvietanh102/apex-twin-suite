<div align="center">

<img src="./assets/logo.svg" alt="APEX Twin Suite Logo" width="110" height="110" />

# APEX Twin Suite `v4.4`
### Strong models are smart. They are not always thorough. APEX adds the missing layer.
*Two skills for Claude Code, Claude Desktop, Codex, Cursor and Google Antigravity: one turns an idea into a working result, the other makes an existing system better. Works in any field, country or context.*

[![Version](https://img.shields.io/badge/version-4.4.0-6366F1?style=for-the-badge)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)](./LICENSE)
[![Evals](https://img.shields.io/badge/evals-blind_%26_pre--registered-F59E0B?style=for-the-badge)](./evals/EVAL-RESULTS.md)

[**Install**](#install) • [**How it works**](#how-it-works) • [**Evidence**](#evidence-blind-pre-registered-evals) • [**When to use it**](#when-to-use-it-and-when-not-to) • [**Changelog**](./CHANGELOG.md)

</div>

---

## Why this exists

Today's frontier models already ask sensible questions and write good code. In our blind evals, though, they kept failing in the same few ways on people's *most important* work:

- **They raise a critical point, then drop it.** One asked about lot/expiry tracking for a cosmetics shop and never built it.
- **They polish a minor flow while the main one is missing.** One shipped an order app without the marketplace channel that carried 70% of the orders.
- **They state rules they have not checked.** One called a VAT reduction "past" while it was still in force.
- **They say "done" without proof that it works where the user will actually use it.** One shipped a summary sheet that showed `#NAME?` when opened in real Excel.

None of these is a knowledge gap. They are gaps in **thoroughness that survives to the end**, and that is the gap APEX fills.

> **Design principle:** *free in how the model thinks, strict in coverage and proof.*
> APEX never scripts the model's reasoning. It defines **what must be true at handover**: every relevant angle considered, every need traced to a final status, everything proven where it will be used.

---

## The two skills

| Skill | Use it when | Starts with |
| :--- | :--- | :--- |
| **`idea-to-product-apex`** | You have an idea, goal or vague problem and want a complete, working result: an app, tool, business process, content system, event, project or personal plan | 2–4 concrete findings for *your* field and situation, a recommended direction, then at most 3 questions you can answer in one line |
| **`product-workspace-reviewer-apex`** | You already use something (an app, a folder of spreadsheets and scripts, a workflow) and want it assessed and made better, even if it "already works" | A read-only first pass with 3–6 evidence-backed findings ranked by money, data and safety risk, then at most 3 root-vision questions. Nothing is changed until you have said what is sacred |

Both skills reply in your language. When you say "you decide" or *"cứ chọn phương án bạn thấy hợp nhất và làm tiếp"*, they pick an option, state their assumptions and **build in the same reply**: no extra round of option tables.

---

## How it works

### 1. Context profile: tailor before acting
Not every rule fits every situation. Before any sweep, the model answers nine quick questions about the context:
- Does money change hands with other parties?
- Is there personal data about others?
- Is the work regulated?
- Do other people operate it?
- Does someone control money or data on behalf of others?
- Does it replace something that already exists?
- Is it long-lived?
- Is there an established trade with standard practices?
- What are the stakes?

**Applicability comes from these features, not from the industry label.** A rule that does not apply is marked `N/A` with a one-line reason: never forced, never silently skipped. Depth scales with the stakes.

### 2. Domain brief for *any* field
There is no fixed list of supported industries. For each context the model builds a short brief:
- jurisdiction;
- value chain;
- money norms;
- the rules that apply, each with an identifier, a date and a certainty tag;
- **what a 15-year practitioner would notice in five minutes**;
- the field's **standard instruments** (bundle tickets in garment piece-rate work, a key-dates register in a law firm, and so on);
- typical failure modes;
- **the next 12–24 months**: scheduled mandates, price risk and hedging, financing, the growth path.

### 3. Twelve completeness lenses, then a second-order sweep
The lenses are run after drafting, as a checklist rather than a script:
1. stakeholders;
2. every flow ranked by weight;
3. money, including **auditing what counterparties claim against you**;
4. rules;
5. records, including **data minimisation**;
6. failure and **plausibility checks**;
7. misuse and governance;
8. people;
9. 12-month change;
10. adoption;
11. measurement;
12. field expertise.

Every fix then gets a second-order check: past periods to remedy, cost and repricing, people to tell first, and how the system itself could fail.

### 4. Traceability: `TRACE.md`
Every need you state, and every need the model discovers, becomes a row that must end in one of these states:
- `DONE`, with evidence;
- `DEFERRED`, with a reason;
- `DROPPED`, with your agreement;
- `N/A`, with a reason.

**High-weight items** (law, safety, money at risk, irreversible data, your root vision, your #1 pain) cannot be deferred without your agreement. A "check later" line is not coverage. A finding is closed by a fix or a ready-to-use replacement, never by a warning alone.

### 5. Definition of done and 12-month change scenarios
Each deliverable type (software, spreadsheet workflow, plan, content system, physical project or event, personal goal, review of an existing system, replacement of a live process) has a concrete definition of done.

"Lasts 12 months" is proven with change scenarios that are actually tested, for example: *"steel price +15%: old quotes keep their numbers, new quotes use the new price"*. How many scenarios are required depends on the context profile.

### 6. The daily operators decide the medium
Installing Python or packages for the agent's own work is one command and is not a cost. What the **people who use it every day** receive, though, must run where they already live: their phone, Excel, Outlook or existing platform. It must also be **verified there**: spreadsheets recalculated in a real engine with zero error values. Code that *builds and checks* a native workbook gives you both.

### 7. Projects built with an older APEX version
If a project already contains `docs/apex-blueprint/` or `docs/apex-review/` from an older version, the skills read it for the original vision and decisions but do not trust its scores or "approved" lines, because older templates were pre-filled. The gate scripts refuse to audit such a ledger and continue with a fresh trace in `_apex/`.

### 8. Respectful conversation
- Every substantial reply opens with a summary of 10 lines or fewer and is meant to be read in about two minutes; details go in files.
- Process files live in a single `_apex/` folder.
- Gates, scores and tiers stay backstage; you see plain outcomes and a short "you asked → where it is → how it was checked" table.

---

## Evidence: blind, pre-registered evals

Everything is in [`evals/`](./evals/): results, pre-registrations, the run 1–2 prompts and fixture, a [gap analysis](./evals/GAP-ANALYSIS.md), and the raw evidence for runs 3–4 in [`evals/runs/`](./evals/runs/) (scenarios, hidden checklists, both assistants' replies and the graders' reports).

**Method (runs 3–4):**
- **Scenarios** are drawn at random, with a logged seed, from a pool of 12 diverse cases, in Vietnamese and English, business and personal, greenfield and existing.
- **An independent agent writes each scenario,** including a messy fixture workspace where needed and a **hidden weighted checklist of 21–24 items**, without seeing the skill.
- **Each scenario runs twice:** once with the skill and once with the same model without it, for 2 turns, with the user delegating in turn 2.
- **Blind A/B graders** run the code, recalculate workbooks in real Excel, and score 6 criteria from 1 to 10 plus checklist recall.
- **Pass criteria are written down before any run.**

| Run | Version | Scenarios | With skill | Without skill | Recall (with / without) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| 1 | v3.7 | 3 fixed cases | 120 | **145** | n/a |
| 2 | v3.8 | same 3 cases | **148** | 131 | n/a |
| 3 | v4.0 | 3 random, unseen (homestay, German bakery, coffee co-op) | 140 | 139 | 85.2% / 82.9% |
| **4** | **v4.1** | 3 fresh random (B2B SaaS, English law firm, garment workshop) | **147** | 130 | **91.75% / 81.75%** |

**Run 4 passed all six pre-registered criteria:**
- completeness at least +10 percentage points: met at exactly +10.0;
- friction not worse than before;
- at least 2 of 3 scenarios won (it won 3 of 3);
- no correctness regression;
- zero spreadsheet errors in the target app;
- zero silent deferrals of high-weight items.

**Honest caveats:**
- **n = 1 run per scenario.** Grader noise is about ±7 points per scenario, so only one run-4 scenario (the law firm, +10) is a win on its own.
- **The skill costs about 1.9× the tokens** of a plain model and takes longer.
- **Everything after v4.1 is not yet re-evaluated.** v4.2 and v4.3 add the fixes from the [gap analysis](./evals/GAP-ANALYSIS.md) and context-based applicability; later changes reconcile the older references, make the gates work in `LEAN` mode and in any language, and handle projects built with older versions. v4.1 is the last version with eval evidence.
- **Only Claude Opus 5.5 has been tested** so far. A Gemini (Antigravity) run is pending.

---

## When to use it (and when not to)

**Use it for the work that matters most to you:**
- building something new that you will rely on;
- turning a fuzzy goal into a plan you can execute;
- reviewing a system you depend on: an invoicing or quoting workflow, a booking sheet, a payroll file, a product codebase, a content operation;
- finding out how something that "already works" could be much better.

**Skip it for** quick questions, single bug fixes, or reviewing one pull request. A plain model is faster there, and the reviewer skill deliberately does not trigger on PR or diff reviews.

---

## Install

### Recommended: install from the GitHub link (auto-updates)
In **Claude Code** (CLI, VS Code extension, or the Claude Desktop Code tab):
```text
/plugin marketplace add phanvietanh102/apex-twin-suite
/plugin install apex-twin-suite@apex-twin-suite
```
For **Codex**, **Cursor** and **Antigravity** the repo includes manifests (`.codex-plugin/`, `.cursor-plugin/`, `.antigravity-plugin/`), but installing from the GitHub link has only been verified in Claude Code. On those hosts, use the local installer below, which copies the skills into each host's skills folder.

### Alternative: local installer (copies the skills into every host on this machine)
**Windows (PowerShell):**
```powershell
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
powershell -ExecutionPolicy Bypass -File .\install-skills.ps1
```
**macOS / Linux / WSL:**
```bash
git clone https://github.com/phanvietanh102/apex-twin-suite.git
cd apex-twin-suite
chmod +x ./install-skills.sh && ./install-skills.sh
```

Only if you use the **claude.ai chat**, which accepts skills as `.zip` uploads only, under *Settings → Capabilities → Skills*: the Windows installer also writes upload-ready archives to a local `dist/` folder. No archives are stored in the repo, so they can never be out of date.

---

## Using it

Just describe what you want: *"Build an order app for my shop that sells on Facebook and Shopee"* or *"Review this workspace: ./my-quotes-folder"*. The skills trigger on intent. The repo also ships slash commands in [`commands/`](./commands/) that only point at the skills: the local installer copies them to `~/.claude/commands`, and a plugin install exposes them under the plugin's namespace. The other phrases below work as part of your message.

| Phrase | What happens |
| :--- | :--- |
| `/idea-to-product [idea]`, `/apex [idea]` | Start from an idea |
| `/apex-lean [idea]` | Small scope: build as early as possible |
| `/apex-redteam` | Critique an idea, plan or codebase |
| `/review-product [path]`, `/apex-review` | Review and upgrade an existing system |
| `/apex-improve` | It works; make it better (baseline → ROI-ranked improvements → improvement log) |
| `/audit-workspace` | Organisation and risk clean-up with protected history |

**Rigor modes** are chosen automatically:
- `LEAN` (default): `_apex/TRACE.md` and `_apex/STATE.json`, plus a compact spec if useful;
- `STANDARD`: a full ledger and gates per slice;
- `DEEP`: adds one isolated critic subagent pass when the stakes are high.

---

## Repository layout

```text
skills/
  idea-to-product-apex/
    SKILL.md
    references/01..09   # elicitation, domain examples, red-team, 12-month architecture, templates,
                        # gates, completeness lenses (07), traceability & definition of done (08),
                        # domain discovery protocol (09)
    scripts/            # init_project.py (scaffold), fitness_audit.py (gates + stub scan)
  product-workspace-reviewer-apex/
    SKILL.md
    references/01..10   # same shared 07–09, plus continuous improvement (10)
    scripts/            # xray_scanner.py (--scan-only inventory / scaffold), review_gate_audit.py
commands/               # slash commands that point at the two skills
tests/test_gates.py     # end-to-end checks for scaffolders, gates, commands and installers
evals/                  # eval pack, fixtures, pre-registrations, results, gap analysis, raw run evidence
.github/workflows/      # CI: runs tests/test_gates.py on Linux and Windows
docs/archive/           # v3.5-v3.7 whitepaper and pitch deck, kept for history
.claude-plugin/ .codex-plugin/ .cursor-plugin/ .antigravity-plugin/   # host manifests
```

### What the gate scripts actually check
The scripts check structure and evidence. They cannot judge quality, and they say so.
- **Scaffolds contain only `[[FILL: hint]]` markers.** A document with an unresolved marker, or with almost no content, vetoes its gate. The check is structural, so documents can be written in any language.
- **`TRACE.md` is checked at every gate.** A `DONE` row needs evidence, and a High-weight row can be `DEFERRED` only with `agreed: "<user's words>"`. Headers may be translated; the status and weight codes stay in English.
- **Gate 3** needs a recorded critique score of 85 or more. The script reads the number the critique produced; it cannot verify that the critique was honest.
- **Gate 5** needs a stub scan of the built product and, in ledger modes, a proven slice.
- **Gate 6** needs no `OPEN` rows and the required number of passed change scenarios. Fewer than 3 needs a stated waiver.
- **`LEAN` mode works too.** With only `_apex/TRACE.md` (created by `--lean`), the trace, stub-scan and change-scenario checks still run.
- The stub scanner matches only real `TODO`/`FIXME` comments and `raise NotImplementedError`, so names like `todo-list` do not trip it.
- All scripts print UTF-8, so non-ASCII paths work on Windows.

Run the checks with `python tests/test_gates.py` (standard library only).

---

## Contributing and re-running the evals

Changes to the prompts should be measured, not argued. See [`evals/EVAL-PROMPTS.md`](./evals/EVAL-PROMPTS.md) and the pre-registration files for the protocol:
1. pre-register the pass criteria;
2. draw fresh random scenarios;
3. have an independent author write the checklists;
4. run with and without the skill;
5. grade blind;
6. report failures as plainly as wins.

The v3.5–v3.7 whitepaper and pitch deck are archived in [`docs/archive/`](./docs/archive/). They describe an older design; where they disagree with this README, this README wins.

<div align="center">
  <b>MIT License</b>
</div>
