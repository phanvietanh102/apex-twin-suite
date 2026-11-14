# 08. Traceability, Definition of Done & Change Scenarios

These three mechanisms turn "I think it's complete" into evidence. They constrain **what must be true at the end**, never how you think or in what order you work.

---

## 1. Traceability: `TRACE.md`

**Why:** in evals, the most damaging failures were silent drops: a requirement the user stated, or one the assistant itself raised, that never reached the deliverable. A visible ledger makes drops impossible to miss.

```markdown
| ID | Need | Source | Weight | Status | Evidence / Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Import marketplace orders on a phone | user | High (70% of volume) | DONE | tests/import.test.js 12/12; demo with sample export |
| R-02 | Lot & expiry per product | discovered (lens 12) | High (legal/safety) | DONE | stock sheet + block-expired test |
| R-03 | Daily reconciliation reminder | discovered (lens 6) | Medium | DEFERRED | needs the user's email provider; planned slice 3 |
| R-04 | Loyalty points | user | Low | DROPPED | user agreed in turn 3: "chưa cần" |
```

**Rules:**
- **What becomes a row:** every need the user stated, every need you discovered (lens findings), and every question you asked whose answer creates work.
- **Statuses:**
  - `OPEN` while working.
  - Final statuses: `DONE` (evidence required), `DEFERRED` (reason and when), `DROPPED` (only with the user's agreement; quote it) or `N/A` (why).
- **No silent deferral of high-weight rows.** Eval run 3 showed the ledger being gamed: important items such as product labelling, traceability, data retention, and even the owner's core vision got a one-line "DEFERRED: check later" instead of substance. A deferral is not coverage.
  - A row is **High** weight if it touches law/compliance, safety or health, money at risk, irreversible data, the user's stated root vision, or their #1 pain.
  - A High row may only end as `DONE` (at least a minimal working version, or concrete instructions the user can act on today, e.g. the exact label fields to print or the exact rule and who to call) or `DEFERRED` with the user's explicit agreement. Write that evidence as `agreed: "<user's words>"`.
  - If time is short, deliver the smallest version that removes the risk now, and defer only its polish.
- **Rows never disappear between turns.** When direction changes, update rows; do not delete them.
- **Order rows by weight** (lens 2). High-weight rows reach `DONE` before low-weight rows get polish.
- **At handover,** show the user a short version in their language: *"Bạn cần → Nằm ở đâu → Đã kiểm thế nào"*. This is often the single most reassuring thing they read.
- **Location:** `_apex/TRACE.md`. All process files (trace, spec, ledger, notes to yourself) live in a single `_apex/` folder, or in `docs/apex-blueprint/` / `docs/apex-review/` in STANDARD/DEEP mode, and never loose in the user's working folder.
- **In chat-only hosts,** keep the table in the reply instead of a file.

`fitness_audit.py` / `review_gate_audit.py` read `TRACE.md`:
- **Gate 5** blocks on `DONE` rows without evidence, on unfilled markers, and on `DROPPED` rows without a reason.
- **Gate 6** also blocks on any `OPEN` row.

---

## 2. Delivery: the daily operators' world decides the medium

This skill's users are comfortable with AI tools. Installing Python or a package for the agent's own work is one command and is **not a cost**: use code, scripts and tests freely to analyse, generate, transform and verify.

What decides the *deliverable's* medium is the people who will **operate it every day**. Sometimes that is the user. Often it is an accountant, a receptionist, a packer or a team lead. They live in their phone, Excel, Outlook or an existing platform.

Eval run 3 showed what goes wrong otherwise:
- an Excel-only accountant received a Python engine whose summary sheet showed `#NAME?` in real Excel;
- a bakery's shared order book depended on one laptop running a nightly script.

The tests passed and the operators still could not use it.

Pick the medium in this order of preference, choosing the first that does the job **for the daily operators**:

1. **Configure what they already have:** the existing platform's settings, built-in features or templates.
2. **Native artifacts in their tool:** spreadsheet formulas, data validation, conditional formatting, protected ranges, document templates, forms.
3. **Automation inside their tool:** Apps Script, Power Automate, macros, platform automations.
4. **A new app, script or service:** fine when it clearly earns its keep and someone (the user or the agent on request) can run and maintain it. Give it a one-command setup and a fallback for the operators.

Code that *generates or checks* a native artifact (a script that builds and verifies an Excel workbook, say) is often the best of both: the operators get their tool, and the user gets reproducibility.

Two further rules:
- **Shared workflows** (several people, several sites) must not depend on one person's machine being on.
- **Verify in the target app, not just in your sandbox:**
  - Spreadsheets: recalculate with a real engine when one is available (Excel, LibreOffice headless, Google Sheets) and confirm zero error values (`#NAME?`, `#REF!`, `#VALUE!`, `#DIV/0!`). Use only functions the user's version supports. When unsure, avoid newer functions such as `XLOOKUP`, `LET`, `LAMBDA`, `FILTER` and dynamic arrays.
  - Documents: open and check the rendering.
  - Mobile-first users: check that it is usable at phone width.
  - If you could not verify in the target app, say so plainly and give the user a 1-minute check to do.

---

## 3. Definition of Done by deliverable type

Pick every type that applies; most real projects mix two or three.

| Deliverable type | Done means |
| :--- | :--- |
| **Software / tool / automation** | Runs in the user's *actual* environment (or a faithful mock, stated honestly). Tests pass for the heaviest flow plus edge cases. No stubs. Data export/backup exists. Setup is ≤ ~10 steps a non-specialist can follow. Chosen by the native-first ladder (§2). |
| **Spreadsheet / document workflow** | Built natively in the user's tool. Formulas verified against worked examples **and recalculated in the target app with zero error values**. Inputs validated. Issued or historical records protected from later edits. A template plus a one-page how-to in the user's language. |
| **Plan / strategy / research** | Every number recomputed and the assumptions listed with how to verify them. Milestones carry "if not met → action". Week-1 actions are concrete. Top risks have early-warning triggers. |
| **Content / media / marketing system** | Calendar, templates, quality rubric, distribution channels, measurement, and compliance (disclosure, rights, platform rules). |
| **Physical project / event / operations / service process** | Timeline with buffers, checklists per role, vendor and contact list, a contingency for each critical risk, budget with a contingency %, and the permits, safety or legal steps. |
| **Personal goal** (career, study, health routine, finances) | Baseline, target, weekly routine that fits the stated time, review cadence, and a plan for when it slips. |
| **Anything replacing a live process** | A switchover plan: a parallel or shadow run, or a drill (e.g. "the key person is off sick this week"), before cut-over. Ownership by a role or shared account, not one person's login. An alarm if the automation silently stops. |
| **Review / upgrade of an existing system** | Everything above for the parts changed, plus a verified backup before changes, parity (old valid inputs still give the same results unless intentionally corrected and stated), and protected history. |

---

## 4. Change Scenarios: the 12-month promise made testable

**Why:** "lasts 12 months" is only a claim until something changes and the result still holds.

1. Derive 3–5 scenarios from lens 9 and the domain brief (09), chosen for *this* user. Examples:
   - a key price rises 15%;
   - a new channel or customer type is added;
   - a tax or regulatory rate changes;
   - volume triples;
   - the main operator is away for two weeks;
   - a vendor or API disappears.
2. For each, state the event, the expected behaviour, and how it was verified:
   - **Software:** an automated test, e.g. change a price; old documents keep their numbers; new ones use the new price.
   - **Non-software:** a written walk-through showing exactly which file, sheet or step changes and what stays untouched; or a rehearsal with sample data.
3. Record the results in `STATE.json` / `REVIEW-STATE.json` → `change_scenarios`:
   ```json
   {"id": "CS-1", "event": "steel price +15%", "expected": "old quotes unchanged, new quotes +X",
    "status": "pass", "proof": "test_price_change: old 823,237,800 unchanged; new +8,448,000"}
   ```
   Gate 6 requires at least 3 scenarios with status `pass` and a proof.
4. Tell the user in plain words what they can change safely and how, e.g. "đổi giá thép trong 1 file, báo giá cũ giữ nguyên".
