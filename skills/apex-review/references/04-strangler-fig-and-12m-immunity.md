# 04. Upgrading in Place: Strangler-Fig Steps, Organisation, 12-Month Roadmap

Load this when planning the upgrade architecture (any mode). SKILL.md and references 07–09 take precedence over anything here.

## 1. Upgrade around what works; never rip and replace

A system in daily use must keep working while it is improved. Work in this order:

1. **Protect history where it is.** Finished records (issued invoices, completed projects, signed contracts, closed periods) stay **in place**: take a verified backup, record a hash, and set them read-only where that does not disturb the system. Do not move, rename or edit them. Live data the system still writes to (a running database, the current working sheet) is backed up but not set read-only; change it only with a tested rollback. A file the owner's people open by habit, or that other files link to, breaks when moved. If the owner asks for an archive folder, copy first, verify the copy, update every reference, and only then retire the old location with their agreement.
2. **Pull volatile values into one editable place.** Find every price, rate, tax percentage, rule, template or contact detail hard-coded across files and consolidate them into a single source the operators can edit (a config sheet or file in their own tool).
3. **Wrap and upgrade the core flows.** Connect the cleaned logic to that config and add the improvements agreed in the gap matrix, heaviest flow first.
4. **Prove parity, then switch over.** Old valid inputs must give the same results unless a correction is intended and stated. Keep a one-step rollback to the pre-upgrade state.

## 2. Reorganising folders is optional

Reorganise only when clutter is one of the owner's stated pains or they agree to it. Clutter that nobody trips over is not worth the risk of broken links and lost habits.

When you do reorganise:
- Apply the new structure to **new** files first; leave existing ones where people expect them unless the owner agrees to move them.
- Keep one canonical template per document type instead of `v1 / v2 / final_copy` duplicates; generate dated outputs from it.
- Prefer names that sort chronologically, such as `<YYYY-MM-DD>_<client-or-project>_<type>`.
- After any move, scan scripts, formulas and links for broken paths.

A layout that has worked for small businesses, offered as an example, not a requirement:

```text
<root>/
├── config/          # prices, rates, rules, master templates (the one editable place)
├── active/          # current work
├── tools/           # scripts, workbooks, automations
├── archive/         # finished, read-only records (only if the owner wants history gathered here)
└── exports/         # what is sent to clients
```

Process files belong in `_apex/` (LEAN) or `docs/apex-review/` (STANDARD/DEEP), never loose in the owner's working folders.

## 3. Twelve-month roadmap (adapt to the owner's context)

Give the owner a short schedule of what to expect and what each step costs them. Fill it with their real events; the rows below are a starting shape.

| Horizon | What happens | What protects them | Owner effort |
| :--- | :--- | :--- | :--- |
| Day 1 | Upgrade in use; history untouched | Verified backup, parity checks passed | None beyond normal use |
| Day 30 | First price or rule change | Edit the one config place | A few minutes |
| Day 90 | A quarter of new records | Backup routine; optional tidy-up | A few minutes |
| Day 180 | A rule, platform or volume change | The change scenarios already tested (08 §4) | A short review |
| Day 365 | Year-end review | Annual summary and backup export | A short review |
