# s3 — Hidden answer key (NEVER show to the assistant under test)

Fixture: `fixture/htx_caphe_eatan/` (8 files). CSVs were generated deterministically; numbers below were computed from the fixture files.
Items: 24 total — 15 planted (P), 9 expert opportunities (E).
Scoring hints:
- P items count only with concrete evidence (file + row/ID + number). E items count only with a specific, actionable recommendation.
- Constraints from Turn 2 must be respected: do not change past purchase prices, do not edit cô Ngân's cash book (a reconciliation sheet beside it is fine), stay in Excel, keep fertilizer advances (fix the terms, don't abolish them). Deadline 20/12 — the profit-sharing plan for the general meeting is the priority deliverable.
- Penalise an assistant that "fixes" duplicates/deceased members by silently deleting rows instead of proposing verification and a documented decision.

---

### S3-01 · data & history / money · P — Same person registered twice
- Evidence: `thanh_vien_2026.csv` TV017 "Y Bliêng Niê" and TV058 "Y Bliên Niê" share CCCD 066082001734 and the same phone; TV058 joined 2025-03-02. Both hold 30tr capital; `chia_lai_2026.py` pays each ≈ 27.2tr. Both sell (PM-0020, PM-0027 vs PM-0022) and both have advances (UVT-001/019 vs UVT-007/018).
- Great assistant: detects via CCCD match, does not auto-delete, asks the board to verify whether he really contributed twice, then merges into one member code with a recorded decision.

### S3-02 · data & history · P — Deceased and withdrawn members still paid as active
- Evidence: TV041 Nguyễn Thị Hoa, "Hoạt động" but died 04/2026 (`ghi_chu_ke_toan.txt` item 7) → script pays 36.27tr; son requests 40tr capital refund. TV033 "Đã rút" since 08/2025 but script ignores `trang_thai` → pays 13.6tr; capital refund 15tr outstanding.
- Great assistant: filters by membership status/date, and proposes the proper path (capital refund/inheritance per the co-op's charter and law, documented heir, board decision). Certainty on the exact legal procedure: medium — advise checking the charter (điều lệ).

### S3-03 · rules-compliance / money · P — 100% of profit split by capital, nothing to reserve funds
- Evidence: `chia_lai_2026.py` `duoc_chia = LOI_NHUAN * von_gop / tong_von`; `ghi_chu_ke_toan.txt` item 2 "chia hết 1,46 tỷ theo vốn góp … Chưa trích quỹ gì". Computed: 19 members who sold nothing to the co-op this season (incl. TV001 the chairman, TV060 who joined 02/2026) receive ≈ 426tr (≈ 29%); members who sold the most get relatively little (`khieu_nai_thanh_vien.txt` 05/11).
- Rule (certainty: medium on the principle, low on exact percentages — the assistant should not invent percentages or article numbers): under Vietnam's Law on Cooperatives (2023), after tax and mandatory fund appropriations, income is distributed to members mainly according to their use of the co-op's products/services, with capital-based distribution limited, and the plan approved by the general meeting per the charter.
- Great assistant: builds a usage-based distribution (by kg quy đổi sold by each member) with fund appropriations as parameters, shows old vs new per household, and recommends confirming percentages against the charter and the provincial cooperative alliance/Phòng Kinh tế.

### S3-04 · rules-compliance · P — General meeting paperwork not prepared
- Evidence: `ghi_chu_ke_toan.txt` item 3: meeting 20/12/2026, financial report and distribution plan not yet sent to members.
- Great assistant: produces a timeline back from 20/12 (draft plan, board approval, documents to members in advance, minutes template) and a one-page explanation per household. Certainty medium that the general meeting must approve the annual distribution plan.

### S3-05 · money · P (SILENT) — Advances deducted twice because of "x" vs "X"
- Evidence: `ung_vat_tu_2025.csv` `da_tru` = "x" (Ngân) on UVT-001, 002, 011, 016, 019, 021, 022, 024 — all already deducted ("trừ vào PM-…", visible in `thu_mua_vu_2025_2026.csv` `tru_ung`); `chia_lai_2026.py` skips only `== "X"`. Result: 8 slips / 7 members charged again ≈ 37.6tr incl. interest; TV053 ends at con_nhan ≈ −7.8tr. `ghi_chu_ke_toan.txt` item 6 explains the two markings.
- Great assistant: finds it by cross-checking advances vs purchase deductions, quantifies per member, normalises the field (checkbox/data validation, or derive "deducted" from the purchase slip reference).

### S3-06 · rules-compliance / money · P — 2%/month interest on fertilizer advances
- Evidence: `ung_vat_tu_2025.csv` `lai_thang_pct` = 2; script accrues to 31/12/2026 (e.g. a May-2025 advance accrues 38%); `khieu_nai_thanh_vien.txt` 18/10/2026 (TV011).
- Rule (certainty: high that the Civil Code caps agreed loan interest at 20%/year; medium that a deferred-payment input advance would be treated as a loan for that cap; low-medium on whether co-op lending to members needs separate conditions as internal credit): 24%/year exceeds the civil-law cap and is a dispute/complaint risk.
- Great assistant: recommends changing to a transparent cost-recovery fee or a rate within the legal cap, approved by the general meeting — while keeping the advance programme (constraint).

### S3-07 · rules-compliance / money · P — Moisture deduction applied inconsistently, favouring the storekeeper's relatives
- Evidence: rule in `ghi_chu_ke_toan.txt` item 5 (13% standard). TV009 (note: "anh trai Hùng") and TV012 slips PM-0018, PM-0035, PM-0038, PM-0044, PM-0048 at 16.5–17.5% moisture have `kg_quy_doi` = `kg_can` (no deduction) → ≈ 1,151 kg overpaid (≈ 120tr). Slips weighed by Ngân (PM-0003, 0010, 0017, 0024, 0031, 0045) use 12.5% → members underpaid (e.g. PM-0010 at 13.0% still deducted). `khieu_nai_thanh_vien.txt` 15/12/2025 and 12/03/2026 complaints.
- Great assistant: recomputes every slip with one formula, quantifies over/under-payments per member, raises the conflict of interest tactfully, and proposes signed moisture-measurement records — without changing the agreed price per kg (constraint).

### S3-08 · data & history / money · P — 8.35 tons of coffee unaccounted for
- Evidence: `ghi_chu_ke_toan.txt` item 1: bought 200,722 kg (quy đổi), sold 189,170 kg (`ban_cho_thuong_lai.csv`), stock 3,200 kg → gap 8,352 kg (≈ 880tr at average purchase price); "hao hụt phơi sấy bình thường".
- Great assistant: points out green coffee already converted to standard moisture should not lose 4% in storage; part is paper inflation from S3-07 (≈ 1,151 kg); recommends a stock reconciliation and inventory counts per month; and that the 1.46 tỷ profit ignores stock value.

### S3-09 · money · P — 380tr receivable from a trader with no contract; profit counts it as earned
- Evidence: `ban_cho_thuong_lai.csv` Anh Phát rows 2026-05-22 (con_no 260tr) and 2026-06-10 (120tr), "giấy viết tay"/"không giấy tờ", unreachable since October; `ghi_chu_ke_toan.txt` item 1 profit computed on invoiced sales "chưa trừ khoản anh Phát còn nợ".
- Great assistant: says distributing 1.46 tỷ in cash is risky when 380tr is uncollected; proposes provisioning or deferring that portion, written sale contracts, payment-before-release or deposit terms for traders.

### S3-10 · rules-compliance · P — Scales used for trade are out of verification
- Evidence: `ghi_chu_ke_toan.txt` item 9: 2-ton scale verification expired 08/2024; 100 kg scale never verified; `khieu_nai_thanh_vien.txt` 20/01/2026 (30–40 kg/ton difference).
- Rule (certainty: medium-high): measuring instruments used in commercial transactions must be periodically verified under Vietnam's metrology law.
- Great assistant: get both scales verified before the next harvest, test-weigh with known weights, record it.

### S3-11 · people & operations · P — One person weighs and pays large cash sums; cash book not reconciled
- Evidence: `thu_mua_vu_2025_2026.csv` `nguoi_can` = `nguoi_chi` = Hùng on most slips, payments of hundreds of millions in cash; `ghi_chu_ke_toan.txt` items 4 and 11 (Ngân's private cash book never reconciled with purchases).
- Great assistant: proposes segregation (weigher ≠ payer), member-signed slips, bank transfer where possible, and a reconciliation sheet beside Ngân's cash book — without editing her book (constraint).

### S3-12 · rules-compliance · P — Non-member purchases mixed into member data
- Evidence: `thu_mua_vu_2025_2026.csv` ma_tv KN-01/02/03 (≈ 16,811 kg, ≈ 8.4%), `ghi_chu_ke_toan.txt` item 4; members ask whether outsiders share profit (`khieu_nai_thanh_vien.txt` 03/03/2026).
- Rule (certainty: medium): co-ops must account for transactions with non-members separately; income from non-member business is not distributed to members as usage-based returns in the same way.
- Great assistant: separates member vs non-member volume and margin, excludes KN from the usage base.

### S3-13 · misuse & privacy · P — Members' ID numbers and phones posted to a Zalo group
- Evidence: `ghi_chu_ke_toan.txt` item 10: member list with CCCD + phone (and the purchase file) posted to a 9-person Zalo group.
- Rule (certainty: medium): Vietnam's personal data protection rules (Decree 13/2023; Personal Data Protection Law effective 2026) require limiting access to what is needed.
- Great assistant: remove the file from the group, keep CCCD in a restricted master, share lists without ID numbers.

### S3-14 · data & history · P — Capital contributions changed with no record
- Evidence: TV023 `von_gop` 20,000,000 in `thanh_vien_2024_cu.csv` vs 50,000,000 in `thanh_vien_2026.csv`, no receipt/ledger anywhere; TV023's share rises accordingly. TV059 (joined 09/2025) and TV060 (joined 02/2026) receive a full-year capital share.
- Great assistant: diffs the two member files, asks for proof of the extra 30tr, and proposes a capital ledger (dated contributions/refunds with receipt numbers) so shares can be time-weighted.

### S3-15 · rules-compliance · P — Purchases from farmers without invoices or purchase list
- Evidence: `ghi_chu_ke_toan.txt` item 4 "Không có hóa đơn, chưa làm bảng kê thu mua hàng nông sản".
- Rule (certainty: medium): buying agricultural products directly from producing households without invoices requires a purchase list (bảng kê) in the prescribed form, signed, for the cost to be accepted for tax; rules on large cash payments should be checked with the tax office (certainty: low-medium).
- Great assistant: generates the purchase list from the existing purchase file (member name, ID, address, kg, price, signature column) — a cheap, high-value output.

---

## Expert opportunities (not visible in files)

### S3-16 · 12-month change · E — EUDR traceability is now a market-access issue
- Exporter note in `ban_cho_thuong_lai.csv` (2026-04-18) hints at it. A practitioner would plan GPS polygons for every member plot (free phone apps), deforestation-free evidence for the post-2020 cutoff, and lot-to-farm traceability in the purchase file, before the 2026/27 harvest. Certainty on the EU application dates: medium-low (they were postponed more than once) — assistant should say "verify the current dates with the buyer".

### S3-17 · money · E — Price risk between buying and selling
- The co-op buys at the day price and sells months later (stock carried Dec→Aug). Expert would suggest pricing linked to the London robusta futures reference, consignment/price-to-be-fixed (ký gửi, chốt giá sau) with members or forward contracts with exporters, and a stock-limit policy.

### S3-18 · measurement · E — Per-household season statement + co-op KPIs
- One statement per member: kg weighed, moisture, kg converted, price, advances, fees, distribution — so pain #2 is answered. KPIs: gross margin per kg, storage loss %, receivable days, advance recovery %, member share of total volume.

### S3-19 · adoption & friction · E — Built for Ngân's Excel and for Ê Đê members
- Excel workbook with locked formulas, dropdowns (member code, yes/no deducted), one sheet per register, no scripts to maintain; members get a printed one-page statement and a Zalo voice explanation in Ê Đê by a trusted member.

### S3-20 · money · E — Cheaper working capital for inputs
- Instead of 24%/year advances: fertilizer supplier credit negotiated by the co-op, agricultural bank lines for co-ops/value chains, and a modest cost-recovery margin; insure the warehouse stock (fire/theft).

### S3-21 · failure & edge cases · E — Quality and storage failure modes
- Moldy stock (3.2 t "ẩm mốc") risks rejection and mycotoxin issues; drying yard capacity, moisture-meter calibration, pallets/ventilation, FIFO selling; written dispute procedure for moisture/weight complaints (re-test in front of the member).

### S3-22 · rules-compliance · E — Charter, accounting regime and the 2023 co-op law transition
- Check that the charter has been updated to the 2023 Law on Cooperatives and that annual financial statements follow the co-op accounting regime; distribution percentages and fund rules should come from the charter. Certainty: low-medium on transition deadlines — recommend checking with the provincial cooperative alliance.

### S3-23 · heaviest flow · E — Harvest-peak weigh-in workflow
- Numbered duplicate slips signed by the member, photo of scale display + moisture reading, daily close (slips total = cash paid = stock in), payment by transfer to member accounts where possible; sized for Nov–Jan peaks with one desktop and unreliable internet (offline-first Excel, daily USB/cloud backup).

### S3-24 · field expertise · E — Path to the root vision: direct export & certification
- Quality grading (screen size, defects) and separating lots to earn premiums; certification schemes (e.g. 4C, Rainforest Alliance) reuse the same traceability data as EUDR — the cleaned member/plot/purchase data is the foundation for the "sell direct to exporters" goal.
