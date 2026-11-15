# s3 grade: HTX cà phê Ea Tân (A vs B)

## Score table

| Criterion | A | B |
|---|---|---|
| 1. Beyond-knowledge insight | 8 | 8 |
| 2. Correctness | 8 | 7 |
| 3. Fit to constraints | 9 | 6 |
| 4. Progress (working artifacts) | 9 | 8 |
| 5. Low friction | 7 | 5 |
| 6. Overall wow | 8 | 7 |
| **Total /60** | **49** | **41** |

## Checklist recall (24 items)

| # | Item | A | B | Notes |
|---|---|---|---|---|
| 01 | Duplicate TV017/TV058 | ✓ | ✓ | Both found the shared CCCD and phone number. Both hold TV058 without deleting it. |
| 02 | Deceased/withdrawn paid | ✓ | ✓ | Both exclude TV033 and hold TV041 for the heirs. |
| 03 | 100% by capital, no funds | ✓ | ✓ | Both split 70/30 by kg and capital, with fund % as parameters, and say to verify against the charter and the provincial co-op alliance. |
| 04 | GM paperwork/timeline | ✓ | ✓ | A: Word report, 7 pages, 8 resolutions, plus per-household slips. B: Excel report, per-household slips, voice script. Neither gives a minutes template. |
| 05 | x vs X double deduction | ✓ | ✓ | B quantified 37,586,400 đ over 7 households. A listed 6 of the 7 (missed TV047). |
| 06 | 2%/month interest | ✓ | ✓ | Both cap at 20%/yr (Civil Code art. 468), keep advances and propose a new rate. |
| 07 | Moisture inconsistency | ✓ | ✓ | Both found 118.5M overpaid to TV009/TV012 and 15.27M underpaid on Ngân's slips, priced kept. B also holds the overpaid amount from those payouts. |
| 08 | 8.35 t missing | ✓ | ✓ | A gives 7,345 kg after moisture correction and catches the "bán vét kho" contradiction. B gives 8,352 kg / 880M with a 0.5–1% normal-loss benchmark. |
| 09 | 380M receivable | ✓ | ✓ | Both withhold it from the distribution. B adds a debt-acknowledgement template. |
| 10 | Scales unverified | ✓ | ✓ | |
| 11 | Segregation / cash book | ✓ | ✓ | A: weekly reconciliation sheet where Ngân types her own total. B: monthly cash comparison next to her book. Neither edits her book. |
| 12 | Non-member (KN) | ✓ | ✓ | Both take KN profit into the fund. |
| 13 | CCCD on Zalo | ✓ | ✓ | Both give a public list without CCCD/phone. |
| 14 | Capital change TV023 / time-weighting | ◐ | ◐ | A time-weights TV060 but pays TV023's full 50M. B holds the 30M increment but does not time-weight. Neither proposes a capital ledger. |
| 15 | Purchase list (bảng kê) | ◐ | ◐ | Both flag it; B names form 01/TNDN. Neither generated one. |
| 16 | EUDR | ✓ | ✓ | B adds a plot GPS/EUDR sheet and a date caveat. |
| 17 | Price risk | ✗ | ✗ | |
| 18 | Per-household statement + KPIs | ✓ | ✓ | KPIs are partial in both (loss %, receivables). |
| 19 | Built for Ngân's Excel / Ê Đê | ✓ | ◐ | A: live-formula workbook, no Python needed. B: the engine is Python + .bat + CSV config, so a script still has to be maintained. |
| 20 | Cheaper working capital | ✗ | ✗ | |
| 21 | Quality/storage failure | ◐ | ◐ | |
| 22 | Charter / 2023 law | ◐ | ◐ | A: amend the charter at the GM if it differs. B: ask the provincial co-op alliance. |
| 23 | Harvest-peak workflow | ✓ | ✓ | A: 2-copy signed slips, daily close, USB backup. B: slip stub numbers, photo of slip sent to the seller on Zalo, moisture-meter ID, locked formulas. |
| 24 | Path to export/certification | ◐ | ◐ | |

**Recall:** A = (17 + 0.5·5)/24 = **81.3%**. B = (16 + 0.5·6)/24 = **79.2%**.

**Valid points beyond the checklist**
- A: the "bán vét kho" on 20/8 vs 3,200 kg stock contradiction; TV009's 5.7 t/ha yield anomaly; the conflict of interest for the chairman's own share (8.2M vs 27.5M); a per-kg / per-million rule of thumb for oral explanation in Ê Đê.
- B: a per-household "nhận thêm khi thu được nợ" amount; a regression test against the old script (≤1 đ difference); parsing of Vietnamese-locale numbers; 50 đ lost to rounding in the old script; Zalo voice script; slip photo sent on Zalo; SHA-256 backup of originals.

## Protected items
- Past prices: unchanged by both (only kg is recomputed; neither claws back the overpayment). OK.
- Ngân's cash book: not edited by either; both only add a comparison beside it. OK.
- Excel stays: A is fully Excel. B's outputs are Excel, but regenerating them needs Python and the .bat. Not a violation, but a weaker fit.
- Fertilizer advances: kept by both. OK.
- Original data: all 8 files are byte-identical to the fixture in both work folders. B also keeps a SHA-256 backup, which verifies OK.
- **No violations.**

## Artifact verification (grader_tmp)
- **A:** `kiem_tra_va_chia_lai_2026.py` and `xuat_bao_cao_dai_hoi.py` run and regenerate the outputs.
  - Under a piped cp1252 console they crash at the final `print`. This needs `PYTHONIOENCODING=utf-8`; it is not an issue in a normal Windows console.
  - `Chia_lai_2026_DU_THAO.xlsx` was recalculated in real Excel (COM): 485 formulas, 0 errors. Totals match: 875,210,204 to share, 815.7M paid now, 31.7M held.
  - `So_thu_mua` template: formulas, dropdowns, same-person and wrong-code warnings, interest stops on the deduction date. The sheets are **not locked**.
  - The xlsx files as delivered had no cached values. Excel computes them on open, but A's claim that it "opened in Excel" is not reflected in the saved files.
- **B:** `kiem_thu.py` passes 21/21 and `chia_lai_dai_hoi.py` runs: 742,345,535 to share, 608.2M paid, 106.3M held.
  - **Bug:** on the "Tóm tắt" sheet, the labels in A8, A13 and A18 ("=Lãi trên giấy", etc.) are written as formulas and show **#NAME?** in real Excel. These are the three headline rows of the report going to the GM. B admits it never opened the file in Excel.
  - On "Công nợ - Hàng - Tiền", the numbers are stored as text.
  - The template is locked, with dropdowns and an EUDR sheet.
  - B says "4 households" were never deducted; there are actually 8 slips across 6 households.
- Recomputed figures:
  - Double deduction: 37,586,400 đ (matches B).
  - Weigher = payer on 49/49 slips, split 43 Hùng and 6 Ngân. A's line "anh Hùng ... 49/49 phiếu" is imprecise.
  - 8 un-deducted advance slips after a sale (matches A).

## Friction metrics

| | A | B |
|---|---|---|
| Words, turn 1 | 1,868 | 1,844 |
| Words, turn 2 | 1,700 | 1,668 |
| Extra files to read | none (2 Word, 2 Excel) | APEX-COMPACT-REVIEW.md (1,552 w) + TRACE.md (1,450 w), with jargon |
| Setup steps for Ngân | ~3: open the xlsx, edit the yellow cells, print the docx/sheet or copy the Zalo text | ~5: edit the CSV config in Excel, save as CSV UTF-8, double-click the .bat, open the xlsx, print |
| Install required | No (Python only to regenerate the docx, optional) | Python + openpyxl on the office PC ("nhờ cháu Khoa cài") |

## Verdict
Both found nearly all the planted problems with concrete numbers, protected every item the owner said must not be touched, and proposed a usage-based distribution with the 380M withheld. A wins on fit and readiness:
- Its distribution workbook is pure live Excel. Ngân can change costs, fund % and holds herself, and it recalculates without errors in real Excel.
- It adds a Word report with 8 resolutions for the general meeting, printed slips, and an unprotected but sensible new-season ledger.

B shows stronger engineering and calibration:
- 21 regression tests, legal claims hedged with confidence levels, a debt-acknowledgement template, an EUDR sheet, and prudent holds on TV009/TV012/TV023.
- But it makes a co-op with one shaky PC and an Excel-only accountant depend on Python, a .bat and CSV editing.
- It ships #NAME? errors on the headline rows of the GM summary, and it leaves jargon-heavy review files in the user's folder.
