# s1 grade: Homestay Sương Mai (A vs B)

Grader: independent blind grading against the hidden checklist (22 items). Both workbooks were recalculated in real Excel (COM) in `grader_tmp/`. The originals were not modified.

## Score table (1–10)

| Criterion | A | B |
|---|---|---|
| 1. Beyond-knowledge insight | 8 | 9 |
| 2. Correctness / no false precision / no invented law | 8 | 8 |
| 3. Fit to user constraints | 9 | 9 |
| 4. Progress (working artifacts after 2 turns) | 8 | 9 |
| 5. Low friction (10 = very low) | 7 | 7 |
| 6. Overall wow | 8 | 9 |
| **Total /60** | **48** | **51** |

## Checklist recall

| # | Item | A | B | Note |
|---|---|---|---|---|
| S1-01 | P3 double booking, Noel | ✓ | ✓ | Both: urgent first, move anh Tùng to P5/P6, overlap check in sheet. B also drafted the apology/move message. |
| S1-02 | Two diverging masters, P2 hidden conflict | ✓ | ✓ | A diffed 21 field differences. B gave line numbers, a 20-item merge log, a backup with SHA256 and version-history advice. |
| S1-03 | Airbnb USD summed as VND | ✓ | ✓ | Both spotted the "433" tail and sized it at ≈11tr. Both added a USD column and an actual-VND-received field. |
| S1-04 | "Huy" vs "Hủy"; non-refundable no-show | ✓ | ✓ | Both added dropdowns and said to check the Agoda payout. A also caught that "no-show" is impossible because check-in is still in the future. B noted P2 5–6/12 can be resold. |
| S1-05 | Mixed dates, month/occupancy logic, P5+P6 | ✓ | ✓ | Both use date validation, room-night occupancy and P5+P6 handling. Both still book revenue to the check-in month (no per-night split). |
| S1-06 | Booking 12% → 15% | ✓ | ✓ | Both quantified 340k. A uses a channel lookup with no effective date, so changing the rate rewrites past bookings. B uses an old%/new% plus effective date (tested). |
| S1-07 | ZL-040 nights, FB-019 discount | ✓ | ✓ | Both moved nights and totals to formulas. B added a "còn phải thu khách" column. |
| S1-08 | Lưu trú declaration non-compliant | ◐ | ✓ | A raised the right points but deferred "hỏi về khai báo" to after Tết. B cited Luật Cư trú 68/2020, TT 55/2021 (23h/8h), Luật 47/2014 (12h) and declaring every group member, all hedged. It also added a "Đã khai báo?" column and a pre-arrival ID template. |
| S1-09 | ~600 IDs on a public Drive link | ✓ | ◐ | A: restrict the link and delete old (2024) images. B: restrict, plus Decree 13/2023 and PDPL 2026 ("cần kiểm"), but no retention or deletion. B's pre-arrival template also routes IDs through Zalo. |
| S1-10 | Personal account, household money mixed, tax 2026 | ✓ | ✓ | Both: separate account, deposit/account columns, confirm tax with the tax office or an accountant. B cites NQ 68-NQ/TW and has a deposits-held / refunds-owed ledger. |
| S1-11 | Ngọc refund vs own policy | ✓ | ✓ | Both: refund now. Both noticed P6 1/1 was already sold to ZL-047. A drafted a written policy that includes a holiday rule. |
| S1-12 | Peak turnover, Sunday 27/12, Airbnb 13h | ✓ | ✓ | Both built a daily check-out/check-in view. B's DonPhong flags Sundays, writes Mai's message and mentions linen/laundry prep. A does not mention linen. |
| S1-13 | Key code, extinguisher, P3 heater | ✓ | ✓ | Both cover all three. |
| S1-14 | "20% cheaper than OTA" post | ✓ | ◐ | A: parity risk, the claim is false against real data, replace it with direct-booking perks. B: parity risk and check the contract, but no replacement offer. |
| S1-15 | Availability grid + iCal/channel manager | ◐ | ◐ | Both: grid with COUNTIFS and red highlight, plus a manual close-out rule. Channel sync is deferred (B names iCal in its log). Neither mentions sync delay. |
| S1-16 | Phone-first for Thảo, retire orphan script | ✓ | ✓ | Both replaced the script with Sheet formulas. A's calendar is vertical (fits a phone). B adds an auto-quote tab (ConPhong) for Thảo. |
| S1-17 | Hospitality KPIs / monthly P&L | ✓ | ✓ | Both: occupancy, net after commission, direct share vs 40%, monthly profit. Neither has ADR or RevPAR. |
| S1-18 | Tết 2027, effective-date changes | ◐ | ✓ | A: calendar runs to 31/3 only. B: Tết 6/2/2027, +80%, 2-night minimum, effective-date commission. |
| S1-19 | Messaging time / direct growth | ✓ | ✓ | A: 9 templates plus how to save them in Zalo and Meta. B: auto-generated quote, templates, review request, QR card. |
| S1-20 | Channel payout reconciliation | ✓ | ✓ | Both: gross/fee/net/actual-received/account. Airbnb 3% flagged unverified. |
| S1-21 | Overbooking playbook | ◐ | ✓ | A: close channels and re-room. B: also OTA relocation/penalty risk and a ready message script. No partner homestay from either. |
| S1-22 | Access control on the booking sheet | ✗ | ✓ | B: do not share the sheet with Mai (phones, revenue); she gets the DonPhong message instead. A shares with Thảo and says nothing on sheet access. |
| | **Recall** | **19/22 = 86%** | **20.5/22 = 93%** | |

### Valid points beyond the checklist
- **Both:** the 6 Nov bookings marked "Đã ở" for future dates; shared electricity meter; Mai has no labour contract (A in reply, B in TRACE R-38); "khách quen không cần cọc" contradicts the 50% deposit rule.
- **A only:** the "no-show" note is impossible because the stay is still in the future. The "20% cheaper" claim is false against actual data (P2 same price).
- **B only:** holiday rates on the OTAs are below the owner's own +40% list. B explicitly left them alone because of the OTA-price constraint.
- **B only:** a forfeited deposit counts as revenue (cọc − phải hoàn). Deposit liability is 4.8tr plus 600k owed.
- **B only:** an auto quote with the holiday surcharge and minimum-night warning, and an auto message to Mai.
- **B only:** do not solicit direct bookings inside OTA apps (ToS risk).

## Artifact verification (grader_tmp)
- **A `SuongMai_QuanLy_v1.xlsx`** (6 tabs, about 5,100 formulas, data validation on channel/room/status/account/date).
  - Excel recalculation matches A's own stated check values exactly: Dec 29,588,000; commission 1,838,640; direct 45%.
  - The Lich tab shows 2 at P3 25/12 and P2 31/12.
  - CANH_BAO flags all 4 overlapping rows.
  - `kiem_tra_dat_phong.py` (turn 1) runs and correctly lists the conflicts and diffs. It needs Python, which this owner cannot run.
- **B `SuongMai_QuanLy.xlsx`** (9 tabs, about 8,000 formulas).
  - Recalculation gives total revenue 45,151,500, deposits held 4.8tr, refunds owed 600k and 4 bookings in conflict, which matches B's report.
  - B's own `ket_qua_kiem_thu.txt` reports 20/20 PASS on an Excel recalculation.
  - ConPhong correctly lists P2/P5/P6 free on 24–26/12, priced with +40%.
  - DonPhong produces the Sunday warning.
  - DatPhong has 40 columns and Lich has 120 day-columns. That is heavier on a phone.
- Neither assistant tested in real Google Sheets. Both said so honestly and gave in-sheet check points. All functions used (COUNTIFS, SUMIFS, SUMPRODUCT, SEARCH, FIXED, TODAY) exist in Google Sheets.

## Protected items
- OTA prices: untouched by both. B consciously declined to "fix" holiday rates.
- Zalo: kept by both.
- Google Sheets: both deliver an xlsx to import into Sheets.
- No paid software: both cost 0đ, channel manager deferred.
- Original files: byte-identical to the fixture in both A/work and B/work. B also made a SHA256-verified backup.
- **No violations.**

## Friction metrics

| | A | B |
|---|---|---|
| Words turn 1 / turn 2 | 1,839 / 1,631 (3,470) | 1,994 / 1,667 (3,661), plus 3 optional handover .md files (3,842 words) |
| Questions asked in turn 1 | 5 (one technical) | 3 |
| One-time setup steps | 4 (upload, convert, verify 3 points, share), about 15 min on laptop | 5 (upload, convert, verify, share, archive old), about 5 min on laptop |
| Install required? | No for the deliverable. Turn 1 suggested running a Python command. | No. The `_cong_cu` Python/PowerShell tools are optional and grader-facing. |
| Manual to-dos handed back | about 16 checklist items | 5 "today" items plus about 8 dated items (in TRACE.md) |
| Workbook size | 6 tabs, 25 columns | 9 tabs, 40 columns |

## Evidence summary / verdict
Both assistants were strong and nearly on par. Both:
- found both live double bookings with concrete re-rooming;
- found the USD/"Huy"/date/commission/nights errors;
- urged the Ngọc refund and the Drive lockdown;
- delivered a working, Excel-verified, 0đ Google-Sheets-ready workbook;
- respected every constraint.

**B edges ahead** on depth and durability:
- effective-dated commissions;
- a Tết 2027 rule;
- an auto-quote tab aimed at Thảo's messaging pain;
- a deposits/refunds-owed ledger;
- precise, hedged lưu trú law with a tracking column;
- keeping the cleaner off the sheet;
- 20 regression tests.

**A is leaner and more phone-friendly** (vertical calendar, fewer columns). It made sharper catches on the bogus "no-show" and the false "20% cheaper" claim. But it deferred guest-declaration compliance until after Tết and hard-wired commission rates retroactively.
