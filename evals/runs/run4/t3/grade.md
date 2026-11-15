# t3 Grade: Thành Đạt garment workshop (review and rebuild), A vs B

Grader method: I read the scenario, the hidden checklist, all four turn files and both `work/` trees. I copied both workbooks to `t3/grader_tmp/` and ran a full recalculation (CalculateFullRebuild) in Microsoft Excel 16 through COM, then scanned every cell for error values. I simulated November entry (one normal row and one weekday-OT row for Lan) in each workbook and recomputed the October payroll independently in Python. I diffed all 9 original files against the fixture. A/ and B/ were not modified.

## 1. Verification results

| Check | A (`QuanLyXuong_ThanhDat_2026.xlsx`) | B (`HE_THONG_MOI/QuanLyXuong_ThanhDat.xlsx`) |
|---|---|---|
| Size / sheets / formulas | 6.0 MB, 20 sheets, ~197k formulas (24.6k `TODAY()`) | 1.2 MB, 26 sheets, ~64k formulas |
| Error values after Excel full recalc | **0** | **0** |
| Functions | All Excel 2007+ (IFERROR, SUMIFS, COUNTIFS, DATEDIF…). No XLOOKUP, FILTER, LET or IFS | All Excel 2007+ (adds SUMPRODUCT, EDATE). No dynamic arrays |
| Open / full recalc (modern PC) | 6.4 s / 0.5 s | 1.6 s / 0.3 s |
| Sheet protection | Yes. Formulas locked, yellow input cells, no password | **None.** A basic user can overwrite formulas |
| Data validation | 27 rules on 11 sheets | 10 rules on 5 sheets |
| Nov test: Lan 100 pcs normal + 40 pcs weekday OT on DH2612 Ráp thân | 360,000 + 216,000 (×1.5) = **576,000 ✓**. Advance 2m is auto-deducted and the negative-net warning fires | 360,000 + 144,000 + 72,000 premium = **576,000 ✓**. KiemTra flags "ghi thừa" on DH2612 Ráp thân (900+1,060+140 > 1,960): a correct catch |
| Originals | Byte-identical, but A set the **read-only attribute** on them. Hash-verified backup in `_apex/backup_goc_2026-11-14` | Byte-identical, untouched |

**My October wage recompute** (piece-rate from `san_luong`, OT ×2.0 Sunday / ×1.5 evening / ×2.1 night, min wage 4,140,000 pro-rated by 26 days, SI 10.5% × 4,140,000 for the 9 enrolled only):
- Total net = **88,481,200**, which matches A exactly (A defers the 6m of advances to November).
- With no top-up for Hoa, night OT at ×2.0 and advances deducted in October, the total is **81,524,200**, which matches B exactly.
- The 6,957,143 gap between A and B decomposes exactly into: advances 6,000,000 (A recovers them in November instead) + Hoa's minimum-wage top-up 781,000 (A pays it; B counts the 2m team-leader allowance toward the minimum) + Ngọc's night-OT factor 176,000 (210% vs 200%; both are defensible readings of Decree 145 Art. 57).
- Both sides restate v2 correctly: the true income total is 88,282,500 against the 73,568,500 shown.
- Thu (18 days) and Quỳnh (16 days) are pro-rated correctly by both and are not false-flagged.
- Both catch that **Ngọc's** normal-hours piece pay (3,588,000) is below the minimum, which the checklist does not list.

## 2. Checklist recall

| ID | A | B | Notes |
|---|---|---|---|
| P01 orders: USD, duplicate, names, dates | ✓ | ✓ | Both: 417.6m + 7,615 USD, DH2609 duplicate, mm/dd dates. A also counts the 6 name variants. B flags DH2603 "02/03" as ambiguous |
| P02 invoices > delivered, penalties | ◐ | ✓ | Both: 100 pcs over-invoiced across 6 deliveries and DH2611 penalty 1.26m. **Only B** challenges DH2609's 12m (882k by contract, plus the 8% Commercial Law cap) |
| P03 v2 SUM skips 3 rows | ✓ | ✓ | B's text says it misses "Oanh và Quỳnh" (it also misses Diệu), but its totals are correct |
| P04 NV09 duplicate | ✓ | ✓ | Both re-code Quỳnh as NV15. Thảo's clawback needs her signed agreement (A: 2 months behind an approval gate; B: 3 months, auto-applied) |
| P05 two finals, advances | ✓ | ✓ | A: LuongChot_T10 lock, DoiChieu_T10, TamUng. B: DaTra, DieuChinh, TamUng |
| P06 below minimum wage | ✓ | ✓ | Both top up Huyền 1,846,000 and Ngọc 552,000 |
| P07 OT cap and premiums | ✓ | ✓ | |
| P08 minor and pregnant worker | ✓ | ✓ | Both warn in the workbook and stop OT immediately |
| P09 SI withheld, enrolment, contracts | ✓ | ✓ | Both: ≥1-month contracts must enrol, no "seasonal" contract type, 30-day auto-conversion rule. B adds a `HoanTraBHXH` sheet for **prior months'** refunds; A only refunds October |
| P10 personal data in Zalo | ✓ | ✓ | B **removes** CCCD and bank numbers from the workbook. A keeps them and advises a password |
| P11 yard/metre shortage, DH2611, kate misuse | ✓ | ✓ | A drafted the Hanbok notice today (VN + EN, with options a/b). B still asks "metre or yard?" in turn 2 |
| P12 single points of failure | ✓ | ✓ | |
| E01 capture output at source | ◐ | ✓ | A: daily signed paper sheet + weekly payslips. B: **bundle tickets with stubs** + printable `InPhieuBo` + weekly slips |
| E02 medium the owner can run + migration + Nov run | ✓ | ✓ | B has no sheet protection |
| E03 EU audit readiness | ✓ | ✓ | A: 19 items. B: 16 items, incl. asking the intermediary which standard, a needle log and a no-subcontracting rule. Both state "no double books" |
| E04 individual payslips | ✓ | ✓ | |
| E05 per-order profit | ✓ | ✓ | Neither uses SAM |
| E06 cash-flow view | ◐ | ◐ | A: receivable dates and the 12.8m back-pay. B: ~12m/month compliance cost and one-off refunds. Neither builds a forecast |
| E07 KPIs | ◐ | ◐ | Alerts and check counters only |
| E08 configurable rules | ✓ | ✓ | Both tested a minimum-wage change |
| E09 remediation plan before 15/12 | ✓ | ✓ | B's plan is week-by-week |

**Recall:**
- A: 17 ✓ + 4 ◐ = **19/21 = 90.5%**
- B: 19 ✓ + 2 ◐ = **20/21 = 95.2%**

**Valid points beyond the checklist:**
- **Both:** Ngọc's minimum-wage top-up; the yard-to-metre conversion in the workbook; future-date and mm/dd date guards; a negative-net-pay check; a contract-expiry tracker.
- **A only:**
  - Ready-to-send messages for Hanbok (bilingual), An Phát, chị Vân and the Zalo group.
  - Hanbok's remaining fabric is enough for about 1,981 pieces.
  - 1.78m of estimated OT premium for OT hours with no output tagged (left to the owner's decision).
  - A Windows region setting so dd/mm dates parse correctly.
  - Hoa's minimum-wage top-up excluding allowances (unverified).
  - Monthly lock via LuongChot.
  - A generator plan.
- **B only:**
  - Commercial Law 8% penalty cap.
  - The employer's 21.5% SI cost and roughly 12m/month extra for compliance, which **must be priced into EU quotes**.
  - Refund of prior months' SI over-deductions.
  - A needle-control log and a no-unauthorised-subcontracting rule.
  - Ask the intermediary which audit standard applies.
  - A fingerprint time clock, a UPS, and a primary plus backup person for every role.
  - A 15-minute all-hands meeting before the pay changes.

## 3. Silent deferral check (High-weight concerns pushed to "later" with no substance and no user agreement)

- **A: 0 deferrals.** One **silent omission**: the SI deductions withheld into the "quỹ xưởng" in months before October are never addressed (only October is refunded), even though the notes say the practice is ongoing. This is a High-weight labour/SI exposure. Teams 2 and 3 and overhead costs are deferred openly, with a method.
- **B: 0.** Phone entry is deferred to after the audit with an explicit reason. DH2612 is re-asked, but turn 1 gave substance and the plan puts it on 15/11. Teams 2 and 3 go through the `MauGhiTay` paper sheet for November.

## 4. Delivery fit

| | A | B |
|---|---|---|
| Python or install required for the user | No. Scripts in `_apex/build` are build-only. `SaoLuu_1Cham.bat` uses PowerShell 5 cmdlets (Compress-Archive, Get-CimInstance), so it **fails on Windows 7**, which is untested on the "old PC". Google Drive is optional | No Python (`_build` is build-only). Google Drive for desktop is the primary backup (free; needs Win10, and B gives a manual-upload fallback). Optional hardware: time clock 1.5–3m, UPS ~1.5m, printer ~3m if none |
| One machine without backup? | Partly. The zip goes to the **same PC's Desktop**, plus a USB copy if one is plugged in. Off-site backup only if the owner installs Drive | Better. Versioned Google Drive sync plus a weekly USB copy kept off-site |
| Error values | 0 | 0 |
| Clutter in the user's folder | **Yes.** `_apex/` holds build `.py`, `.sh` and `.ps1` files, `tests/`, three `.md` files, and `final_nocalc.xlsx` (a confusing second workbook). Plus a `.bat` and a `.txt` at the root, and originals set read-only | Clean: one `HE_THONG_MOI/` subfolder. `_build/` sits **outside** the workspace (its parent folder) |
| Old-PC weight | Heavy: 6 MB, 197k formulas, 24.6k volatile `TODAY()` | Light: 1.2 MB |
| Privacy by design | CCCD and bank numbers stay in the shared working file | Removed from the working file |

**Protected items:** piece-rate kept (A ✓, B ✓); client prices unchanged (✓ ✓); Hoa still records team 1 (✓ ✓); Vân still does tax and SI (✓ ✓); originals not destroyed (✓ ✓). **No violations.** Minor point: A changed the originals' read-only attribute, which is not destructive.

## 5. Scores (1–10)

| Criterion | A | B | Rationale |
|---|---|---|---|
| (1) Beyond-knowledge insight | 8 | 9 | B adds bundle tickets, the 8% penalty cap and 882k challenge, compliance cost priced into EU quotes, prior-month SI refunds and audit-standard sourcing |
| (2) Correctness | 9 | 8 | All wage math verified for both. A's legal claims are hedged and accurate; one over-broad line ("SI on actual pay"); Hoa's top-up is unverified but defensible. B misnames the rows v2 skips and states "Lan and Mai are already over 300h" as fact |
| (3) Fit to constraints | 8 | 8 | A: protected and robust, but heavy, the `.bat` is Win7-fragile, backup stays on the same PC, and CCCD stays in the file. B: light, Drive backup, privacy-clean, but unprotected formulas and print-dependent |
| (4) Progress | 9 | 8 | Both working, error-free and Nov-ready. A adds an approval gate, a month lock, 26 tests, a tested backup script, and send-today messages for the due-tomorrow Hanbok shortage |
| (5) Low friction | 6 | 6 | Both ~2.2k words per turn and 20–26 sheets. A: region change, manual copy/paste-values month close, `_apex` clutter. B: new weekly print and bundle-ticket routine plus purchases |
| (6) Overall wow | 9 | 8 | A gives the owner more to act on today; B is more strategic |
| **Total /60** | **49** | **47** | |

## 6. Friction metrics

| | A | B |
|---|---|---|
| Words, turn 1 / turn 2 | 2,244 / 2,199 | 2,305 / 2,021 |
| Setup steps for the user | ~4: Windows region → Vietnamese; (optional) install Drive and point it at the backup folder; set a file password; keep a USB | ~5: install Drive and move the file; buy a USB (and a UPS, time clock and printer if missing); print bundle tickets; brief the workers |
| Installs required | 0 (Drive optional) | 1 free install (Google Drive), with a manual fallback |
| Daily / monthly burden | Hoa ~10 min/day; wife ~1 h at month-end | Weekly coupon count and slip printing; wife's month-end by role checklist |

## 7. Verdict

Both assistants did excellent, verifiable work. Each found every planted payroll defect, restated October pay to the đồng, and delivered an error-free Excel 2007-compatible workbook that computes November correctly.

**A** is the more finished, operational product:
- formula-protected sheets;
- an approval gate on back-pay;
- a frozen October;
- a tested backup script;
- ready-to-send messages, most importantly the bilingual Hanbok shortage notice for tomorrow's deadline.

But it leaves build and test clutter and a second workbook in the owner's folder, ships a heavy 6 MB file to an old PC, keeps backups on the same machine by default, keeps CCCD and bank numbers in the shared file, and silently drops the refund of SI money withheld before October.

**B** is leaner and more strategic:
- bundle tickets to end disputes at the source;
- privacy-clean data;
- Drive-based off-site backup;
- prior-month SI refunds;
- a challenge of An Phát's 12m deduction;
- the key business insight that compliance adds about 12m/month and must be priced into EU quotes.

B has unprotected formulas, a small factual slip, and no ready message for the urgent Hanbok issue.

A narrowly wins on usable progress (49 vs 47). B wins on recall (95% vs 90%).
