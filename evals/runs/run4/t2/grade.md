# t2 grade: small English law firm (key dates / matters / comms)

Grader: independent, blind to configuration. Graded against `scenarios/t2/checklist.md` (23 items).
Inspection copies are in `t2/grader_tmp/` (A/ and B/ were not modified).

## 1. What was built

| | A | B |
|---|---|---|
| Turn 1 | Three routes (PMS, M365, custom), safety principles, an "every date in one list this week" step, 8 questions. Nothing built. | Recommended M365, gave 4 legal/system points (SRA systems and controls, conflict DB, DSAR, AML reg 40), **built and tested an interim register**, a limitation sweep, a 3-route table and 3 questions. |
| Turn 2 recommendation | Microsoft Lists + Power Automate (4 flows) + Outlook. An interim Excel register until Lists goes live on 4 Jan. | A single Excel "Practice Register" on a private SharePoint site + a Power Automate 8:00 email + a Forms/iPhone intake for Sue. No migration in the middle of the project. |
| Spreadsheet | `Key-Dates-Register.xlsx`: 7 sheets, classic functions only (INDEX/MATCH/SMALL/COUNTIFS/SUMPRODUCT), 3 EXAMPLE matters and 4 example dates | `Practice Register.xlsx`: 13 sheets, Excel tables, LET/FILTER/SORTBY/MINIFS (fine in M365 and Excel for the web), empty, with a separate test copy. Sheets: Today, Next 8 weeks, Matter card, Conflict search, Key Dates, Matters, Calls & post, Bank details checks, Undertakings, Wills & deeds held, Standard periods, Settings, Change log |
| Documents | 2 Markdown files: IT spec (1,814 words) and Procedures/Policy/Rollout (1,640 words) | 4 Word files: Plan (1,484), IT guide (1,893), Office routines (1,757), Insurer statement draft (392) |
| Tests claimed | "Tested its formulas in Excel" | 109 automated checks, 0 failures (`_apex/test-results.txt`), including 7 change scenarios and a volume test with 3,000 dates |

### Recalculation (real engine: desktop Excel via COM, CalculateFullRebuild)
- **A `Key-Dates-Register.xlsx`:** 0 error cells on any sheet (2,529 formulas).
- **B `Practice Register.xlsx`:** 0 error cells on any sheet, including the empty-state dynamic arrays. B's `test-practice-register.xlsx` (3,000 rows) timed out in my cell-by-cell scan, which is a limit of my COM script, not of the file. B's own log reports 0 error cells after the volume test.
- **Unsupported functions:** none. B needs Microsoft 365 Excel or Excel for the web for LET/FILTER/SORTBY. The firm has these, and B says so in its IT guide. B's turn-1 claim of "any Excel from 2010" applied to the deleted draft, not to the final register.
- **Latent defects found by inspection:**
  - A's *Next 8 Weeks* has 80 fixed slots and gives no warning when there are more items, so overflow would be silently truncated. With about 140 matters and several dates each this is unlikely but possible.
  - A's *Checks* ranges are fixed at rows 2–601.
  - B: a minor inconsistency on PI retention. Settings says 15 years; the plan's prose says 7 years for "others".

## 2. Checklist recall

| ID | Wt | A | B | Notes |
|---|---|---|---|---|
| T2-01 heaviest flow | H | ◐ | ✓ | A covers only matter open → reminders → updates, with no conflict, AML, engagement or closure. B has "Opening a matter" (conflict search → Matters row with CDD date → standard dates → second check), closing with "Keep file until", and owners named |
| T2-02 medium/budget | H | ✓ | ✓ | Both build on M365 with a build-vs-buy comparison and costs inside £150/£2k |
| T2-03 limitation logic | H | ✓ | ✓ | A: PI 3y (ss.11/14), child, capacity, ET 3m−1d + ACAS, worked out by/how/checked by. B: also contract 6y, latent 3y/15y longstop, deed, fatal, s.33 warning, plus a cross-check against the standard period that works to the earlier date |
| T2-04 four-eyes + backup | H | ✓ | ✓ | A requires a *second solicitor* for limitation (stronger on that point). B requires a different person and keeps the diary as a copy with a Friday comparison |
| T2-05 escalation + sabbatical | H | ✓ | ✓ | A: 90/30/14/7/3/1/0 to responsible and back-up, overdue daily to both partners, 26 Feb handover. B: daily all-staff email until Done, Away dates flag BACKUP AWAY, 12 Feb handover, cover for David |
| T2-06 conveyancing dates | H | ✓ | ✓ | B adds LTT 30 days for Welsh-border property; A omits undertakings |
| T2-07 probate dates | M | ✓ | ✓ | Both have all four; B adds CGT 60-day and empty-property insurance |
| T2-08 AML | H | ✗ | ✓ | A never mentions AML or CDD. B: MLR 2017 reg 40 (5 years), CDD date and risk per matter, AML-in-scope by matter type, and the Check column flags missing CDD. No firm-wide risk assessment |
| T2-09 conflict check | H | ✗ | ✓ | B: Conflict search sheet across client and other parties, the 9-year closed matters loaded in January, result saved to file |
| T2-10 client care/transparency/LeO | M | ✗ | ◐ | B flags the April 2023 LeO time-limit change and asks for a client-care review. Neither covers the Transparency Rules or a template |
| T2-11 client money stays in accounts | M | ✓ | ✓ | Both leave the package alone. B adds a CLEARED gate agreed with the bookkeeper |
| T2-12 payment-fraud controls | H | ✓ | ✓ | Both have "never change by email", callback on an independent number, MFA, DMARC, forwarding block, CoP. B's Bank-details sheet enforces it in formula logic |
| T2-13 UK GDPR | H | ◐ | ◐ | A: device/MFA/misdirected-email basics only. B: DSAR 1 month, DUAA 2025, a retention schedule per matter type. Neither covers the ICO fee, 72h breach reporting or special-category access |
| T2-14 migration | H | ◐ | ✓ | A: open matters and both diaries, cross-checked, parallel run, but the 9-year history is ignored. B: open matters, diaries and Outlook calendars, prioritised PI/ET first, closed history imported for conflicts |
| T2-15 undertakings | M | ✗ | ✓ | B: Undertakings sheet plus a key-date row until discharge |
| T2-16 wills/deeds + closure | M | ✗ | ✓ | B: Wills & deeds held with an out/returned log, and "Keep file until" on closure |
| T2-17 written procedure for insurers | M | ✓ | ✓ | A: Key Dates Policy section. B: Insurer statement draft (send only if true after sign-off), COLP/COFA/MLRO cover |
| T2-18 client comms | M | ◐ | ◐ | Both have Sue's iPhone logging (A via the Lists app, B via Forms). B adds subject-line matter numbers and mailbox delegation. Neither has client update letters or no-contact chasers |
| T2-19 Margaret adoption | H | ✓ | ✓ | A: 3 habits, 3×30-minute sessions, "→P" tick. B: "you do not need to learn the register", tick Monday printout, email Priya, MFA set up in person |
| T2-20 measurement | M | ✓ | ✓ | A: Checks all zero, monthly audit, trusted checklist. B: Today counts, 10-day email streak, 12-month counts of misses, near misses and days post→diarised |
| T2-21 change without developer | M | ✓ | ✓ | B is stronger: Settings and Standard periods tables, Change log, change scenarios tested |
| T2-22 next 12–24 months | L | ◐ | ✓ | A: Cyber Essentials in one phrase, ID-verification service. B: Cyber Essentials budgeted and timed, ERA 2025, DUAA 2025, 3/6/12-month reviews |
| T2-23 phased plan + protected items | H | ✓ | ✓ | Both go register first (4 Dec), then a Feb drill, then sign-off before 1 Mar |

**Recall:** A = (13 + 0.5×5)/23 = **67%**. B = (20 + 0.5×3)/23 = **93%**.

### Valid points beyond the checklist
- **A:** the "Margaret is off sick" drill week. The Monday digest doubles as a dead-man alarm. Flows are owned by a service account or co-owners. Member delete permission is restricted ("Contribute without delete"). Inbox-rule alerting. Intune app protection. The "→P" tick in the paper diary.
- **B:**
  - ERA 2025 may extend ET limits to 6 months, so check before loading dates (correct to flag as of Nov 2026).
  - LTT for Welsh-border property (very apt for Shropshire).
  - CGT 60-day return on estate property sales; the empty-property insurance limit.
  - The flow reads a non-volatile key column, so the email doesn't depend on someone opening the workbook.
  - A failure-alarm branch, with acceptance test 12 deliberately breaking it.
  - A "FORMULAS DAMAGED" self-check.
  - Bank-check logic rejects a number taken from the email and the same person doing both checks.
  - The Christmas completion-rush check.
  - Cover for David in March/April; COLP/MLRO deputising.
  - Insurer statement to be sent only if true; ET "advised in writing – not acting" decision; mailbox delegation tested in the rehearsal.

## 3. Silent deferral check (High-weight concerns pushed to "later" with no substance and no user agreement)

| Concern | A | B |
|---|---|---|
| Limitation/key-dates reliability | addressed | addressed |
| Payment-fraud controls | addressed | addressed |
| SRA/insurer expectations | addressed (policy for insurers) | addressed (SRA 2.1, insurer statement) |
| Data protection | thin but not deferred | partial, not deferred |
| Root goal / #1 fear (Margaret not using it) | addressed | addressed |
| AML / conflict (High) | **omitted entirely** (an omission, not a deferral) | addressed |

**Silent deferrals: A = 0, B = 0.**
- B's open items have substance and a named owner and date: the ERA 2025 check (David, w/c 16 Nov), the retention-period confirmation, and the insurer renewal month.
- A's "IT should confirm UK data location" has substance.
- A has two **silent omissions** of High-weight regulatory items: AML/CDD (T2-08) and conflict checks (T2-09). For a firm doing 50% conveyancing and 30% probate, these are serious gaps.

## 4. Delivery fit and protected items

- **A:** everything runs on M365 (Lists, Power Automate standard connectors, Outlook, the Lists iPhone app), with zero spreadsheet errors.
  - The deliverable documents are Markdown, which is awkward for a non-technical firm; A offers Word versions.
  - Two-stage change: Excel until 4 Jan, then Lists. That is a second migration 8 weeks before the sabbatical, and the IT man has to build 3 lists and 4 flows in about one day.
  - The 80-row cap on the printout is silent.
- **B:** everything runs on M365 (Excel tables on SharePoint, Power Automate, Forms on an iPhone home-screen shortcut), with zero spreadsheet errors. The documents are Word.
  - Single tool throughout.
  - Risks: Excel as a multi-user database is more fragile than Lists. B mitigates with version history, the health check, Monday backup copies, "don't sort the shared sheets" and sheet views.
  - The flow expressions are advanced. They are fine for the IT man, but Priya could not maintain them.
- **Protected items:** Outlook kept, accounts package untouched, paper diary allowed alongside, files left on the shared drive. **No violations by either side.**
  - B adds a "Practice Register backups" folder on the shared drive and mailbox delegation, but moves nothing.
  - Both recommend the Business Premium upgrade, which is within budget.

## 5. Correctness notes (no law invented; "unverified" where unsure)

- **A:** headline periods are correct (SDLT 14d, OS1 30 working days, IHT 6th-month/12-month, IA 1975 6 months, s.27 2 months, PI 3y, child, capacity, CPR 7.5). The ET "3 months less one day" is stated **without** any caveat about the Employment Rights Act 2025 extension to 6 months, which was expected to start around Oct 2026. Commencement is unverified, so A may be out of date. No false precision elsewhere.
- **B:** periods and citations are checked and correct (LA 1980 ss.2, 4A, 5, 8, 10, 11, 12, 14, 14A/B, 28; CPR 7.5/54.5; FA 2003 s.76; IHTA ss.216/226; I(PFD)A 1975 ss.4/20; TA 1925 s.27; MLR 2017 reg 40; SRA Code for Firms 2.1; Code for Solicitors 6.2; LeO April 2023 change).
  - LTT 30 days is marked "verify". The CGT 60-day reference to FA 2019 Sch 2 is plausible but unverified.
  - The 15-year retention is a firm-policy suggestion and labelled as such.
  - Licence pricing (~£7–8/user uplift) is labelled "verify".

## 6. Scores (1–10)

| Criterion | A | B |
|---|---|---|
| (1) Beyond-knowledge insight | 6 | 9 |
| (2) Correctness | 7 | 8 |
| (3) Fit to constraints | 7 | 8 |
| (4) Progress (working artifacts after 2 turns) | 6 | 9 |
| (5) Low friction | 7 | 6 |
| (6) Overall wow | 6 | 9 |
| **Total /60** | **39** | **49** |

## 7. Friction metrics

| | A | B |
|---|---|---|
| Words: turn1 / turn2 | 841 / 1,163 (total 2,004) | 1,391 / 1,458 (total 2,849) |
| Supporting docs | 3,454 words (2 .md) | 5,526 words (4 .docx) |
| IT setup steps | 11 security items + site + 3 lists + 4 flows + 7 tests (~2 days) | 11 security tasks + 7 site steps + 13-step flow + form flow + 13 acceptance tests (~2–3 days) |
| Firm-side effort | Priya loads the register by 4 Dec, then imports to Lists in December; Margaret has 3×30 min sessions | Priya loads it in 4–6 days by 4 Dec, plus 1 day for history in January; Margaret learns nothing new |
| Installs | None beyond M365 (Authenticator; Lists app on Sue's iPhone) | None beyond M365 (Authenticator; Excel app on Sue's iPhone) |

## 8. Verdict

B delivers far more value to this firm. It built and verified a working register (0 errors in a real Excel recalculation, 109 self-tests). The register already covers what a conveyancing and probate practice is regulated on:
- conflict search across 9 years
- CDD tracking
- undertakings
- wills held
- bank-details clearance with tamper-resistant logic
- retention dates

It also adds sharp local insight (LTT for the Welsh border, the ERA 2025 tribunal limits, CGT 60-day) and an insurer statement that may be sent only once it is true. Its Margaret plan asks almost nothing of her.

A is sound on the core near-miss fix: second-solicitor checks, staged reminders to the responsible person and a back-up, the drill week, and a clean architecture on Lists. But it silently omits AML and conflict checking, which are High-weight duties for a firm that is 80% conveyancing and probate. It adds a second migration in January, and it ships Markdown documents.

B's costs are more reading, more advanced flows, and Excel-as-database fragility. Its mitigations make that acceptable for a 5-person firm.
