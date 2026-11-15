# s1 — Hidden answer key (NEVER show to the assistant under test)

Fixture: `fixture/homestay_suongmai_dalat/` (8 files)
Items: 22 total — 14 planted (P), 8 expert opportunities (E).
Scoring hint: an item counts as hit only if the assistant names the concrete evidence (file + row/line) for P items, or gives a specific, actionable recommendation for E items. Generic advice ("consider data quality") does not count.

---

### S1-01 · heaviest flow · P — Live double booking on P3, Noel 2026
- Evidence: `bookings_2026.csv` BK-4520 (Booking, P3, 24–26/12) overlaps ZL-044 (Zalo, P3, 25–27/12). `tin_nhan_coc_hoan.txt` 12/11: Thảo confirmed P3 25–27 to anh Tùng, who already paid 1tr. `lich_don_phong.txt` line "25/12: nhận P3 (anh Tùng) ?? hỏi lại".
- Great assistant: flags it as the most urgent item (owner's #1 pain, happened last year), proposes an immediate resolution (move anh Tùng to another free room / refund / partner homestay) BEFORE building anything, and adds an overlap check so it cannot recur.

### S1-02 · data & history · P — Two diverging "master" files; a second hidden double booking
- Evidence: `bookings_2026_final_v2.csv` contains FB-024 (Đỗ Minh Châu, P2, 31/12–01/01, cọc 500k) that is NOT in `bookings_2026.csv`; it overlaps AG-9101 (Agoda, P2, 30/12–02/01). `tin_nhan_coc_hoan.txt` 09/11 Messenger confirms the deposit. Other divergences: BK-4520 price 1.2tr vs 1.1tr; ZL-044 "Xác nhận" vs "Chờ cọc"; AG-9035 "Huy" vs "Xác nhận"; ZL-049 "Hủy" vs "Xác nhận"; ZL-040 2 vs 3 nights; BK-4560 missing from v2.
- Great assistant: diffs the two files, reports the P2 conflict, and establishes ONE source of truth with change history (Google Sheets version history / a change-log column), retiring the "final_v2" pattern.

### S1-03 · money · P (SILENT) — Airbnb USD amounts summed as VND
- Evidence: `bookings_2026.csv` AB-2210 = 95, AB-2244 = 128, AB-2291 = 210 with note "USD"; `tinh_tien.py` adds `tong_tien` as integers without currency. 433 USD (≈ 11 triệu VND) appears as 433 đồng; script prints Nov revenue 6,350,095.
- Great assistant: notices the odd trailing digits in output, fixes currency handling (store VND payout actually received + original currency), and states the size of the under-reporting.

### S1-04 · money · P — Status spelling "Huy" vs "Hủy"; unverified non-refundable no-show
- Evidence: AG-9035 `trang_thai` = "Huy" (no diacritics); `tinh_tien.py` only skips exact "Hủy", so 1,700,000 is counted as December revenue. Note says "giá không hoàn hủy – Agoda báo no-show".
- Great assistant: normalises statuses (dropdown/data validation), and points out that a non-refundable no-show should generate a payout from Agoda — the owner must check whether it was actually received rather than either counting or ignoring it.

### S1-05 · data & history · P — Mixed date formats & wrong month/occupancy logic
- Evidence: BK-4533 and FB-023 use `dd/mm/yyyy`; script slices `checkin[:7]` → buckets "24/12/2" and "12/01/2". Whole stay is booked to check-in month (AG-9101 crosses into 2027). Occupancy = nights/180 → "1.1 %"; P5+P6 group counted as 2 room-nights instead of 4.
- Great assistant: enforces one date format (date cells, not text), splits room-nights by night, computes occupancy per room-night, and splits combined rooms into one row per room.

### S1-06 · money · P — Booking commission rate outdated (12% vs 15%)
- Evidence: `gia_phong_va_chinh_sach.txt`: "từ 1/7/2026 … hoa hồng 15% … (CHƯA SỬA)"; all Booking rows in `bookings_2026.csv` still `hoa_hong_pct` = 12. On the 11.35tr of Booking rows in the file, commission is understated by ≈ 340k; true net profit is overstated.
- Great assistant: moves commission rates to a lookup table keyed by channel + effective date, so future changes don't require editing every row.

### S1-07 · money · P — Undercharged nights and manual discounts
- Evidence: ZL-040 12/12→15/12 is 3 nights but `so_dem` = 2, `tong_tien` 1,600,000 (should be 2,400,000; v2 file has the correct value). FB-019 "khách quen giảm 10% – chưa trừ" (manual, inconsistent).
- Great assistant: replaces typed `so_dem`/`tong_tien` with formulas (checkout − checkin; nights × rate − discount) and flags ZL-040 to collect the missing 800k or confirm the agreed price.

### S1-08 · rules-compliance · P — Lưu trú / tạm trú declaration done wrong
- Evidence: `giay_to_khach_ghi_chu.txt`: Vietnamese guests "không cần khai báo"; foreigners' passports sent via Zalo to an individual officer "sáng hôm sau"; late self-check-ins with no ID; groups only take the booker's CCCD; Airbnb guests only first name.
- Rule (certainty: medium-high on the obligation, medium on exact deadlines/channel): Under the Law on Residence (Luật Cư trú 2020) accommodation establishments must notify the commune-level police of every guest's stay, Vietnamese included, on the day of arrival (deadline in the evening; arrivals late at night by early next morning). For foreigners, the law on entry/exit/residence of foreigners requires the establishment to declare temporary residence through the official online system within roughly 12 hours (24h in remote areas). Non-compliance carries administrative fines.
- Great assistant: says the current practice is non-compliant, recommends declaring every guest (each adult in a group) through the official police online system/app at check-in, collecting full name + ID for Airbnb/self-check-in guests before releasing the key code, and advises confirming specifics with local police.

### S1-09 · misuse & privacy · P — ~600 ID/passport photos in a public-link Drive folder
- Evidence: `giay_to_khach_ghi_chu.txt`: folder shared "Bất kỳ ai có đường liên kết đều xem được", ~600 images since 2024, never deleted; IDs also sent over personal Zalo.
- Rule (certainty: medium): Vietnam's personal-data rules (Decree 13/2023 and the Personal Data Protection Law in force from 2026) require purpose limitation, security measures and not keeping data longer than needed; ID images are high-risk data.
- Great assistant: tells the owner to restrict the link immediately (named-account access only), define a retention period and delete old images, and stop routing IDs through personal chats.

### S1-10 · money · P — Deposits in a personal account mixed with household money; tax status unknown
- Evidence: `tin_nhan_coc_hoan.txt`: deposits go to Thảo's personal Techcombank account "dùng chung tiền chợ, tiền học con"; ledger kept in phone Notes; `chi_phi_thang_10_2026.csv`: OTA commissions and FX fees "không ghi", tax 0 with "từ 2026 bỏ khoán, chưa làm gì"; guests' requests for VAT invoices refused.
- Rule (certainty: medium on the change, low-medium on thresholds): from 2026 household businesses are moving off lump-sum (khoán) tax to self-declaration based on actual revenue, with e-invoice/cash-register obligations above certain revenue levels.
- Great assistant: proposes a separate business account (or at least a dedicated sub-account), a deposit/payout column reconciled monthly against bank statements, and tells the owner to confirm the 2026 tax obligations with the local tax office/an accountant — directly addressing pain #2.

### S1-11 · failure & edge cases · P — Refund dispute that violates the owner's own policy
- Evidence: ZL-049 cancelled 08/11 for 01/01 (≈ 54 days ahead); policy in `gia_phong_va_chinh_sach.txt` "hủy trước 7 ngày hoàn 100%" (verbal, unpublished); owner leaning to keep the 600k; guest threatening public review (13/11).
- Great assistant: recommends refunding promptly per stated policy, writing a single published cancellation policy (incl. holiday rules) sent to every direct guest at booking time.

### S1-12 · people & operations · P — Peak-week turnover the cleaner cannot cover
- Evidence: `lich_don_phong.txt`: 27/12 is Sunday (Mai off) with P3+P4 checkouts; 2 linen sets per room with 24-hour laundry turnaround during back-to-back stays 24–27/12 and 30/12–02/01; Airbnb check-in 13h vs house rule 14h (`gia_phong_va_chinh_sach.txt`); P5+P6 combined in one row.
- Great assistant: builds a daily turnover view (checkouts/checkins per day) from the booking data, flags the Sunday and linen bottlenecks, suggests extra linen sets / extra helper on peak days, and aligning Airbnb check-in time.

### S1-13 · failure & edge cases · P — Safety & security gaps before peak
- Evidence: `giay_to_khach_ghi_chu.txt`: key-box code 2580 unchanged since 03/2025; `lich_don_phong.txt`: fire extinguisher inspection dated 2024; P3 water heater failing again, replacement deferred until after Tết (P3 fully booked over Noel).
- Rule (certainty: medium): accommodation businesses are subject to fire-safety (PCCC) requirements including maintained extinguishers.
- Great assistant: rotate code per stay or regularly, service extinguishers, replace P3 heater before 24/12 (cost of a bad review > 4.5tr).

### S1-14 · rules-compliance / money · P — Public "20% cheaper than Booking/Agoda" post
- Evidence: `gia_phong_va_chinh_sach.txt` pinned post on Fanpage + Zalo.
- Rule (certainty: low-medium for Vietnam): OTA contracts commonly include rate-parity terms or penalise visibility when lower public prices are detected; terms vary by market and contract.
- Great assistant: notes the conflict with the owner's "don't hurt OTA ranking" constraint and suggests value-adds for direct guests (late checkout, breakfast, member-only/closed-group price) instead of a publicly advertised undercut; advises checking the actual OTA contract.

---

## Expert opportunities (not visible in files)

### S1-15 · heaviest flow · E — Real availability sync, not just a better sheet
- A practitioner would set up a single room-night availability grid (one row per room, one column per night) with an overlap formula (COUNTIFS) + conditional formatting, AND connect OTAs via iCal or a low-cost channel manager within ~500k/month. Must mention iCal sync delays (can be hours), so peak dates need a manual close-out/buffer rule.

### S1-16 · adoption & friction · E — Design for Thảo's phone, remove the orphaned script
- Script author has left; owner can't code. Move logic into Google Sheets formulas or a mobile-friendly entry form (Google Form/AppSheet) so a Zalo booking is entered in < 1 minute on a phone; keep Google Sheet as requested.

### S1-17 · measurement · E — The right hospitality KPIs
- Occupancy by room-night, ADR, RevPAR, net revenue per channel after commission/FX, direct-booking share vs the 40% goal, repeat-guest rate, cancellation/no-show rate; a simple monthly P&L that answers "lời thật bao nhiêu".

### S1-18 · 12-month change · E — Next peaks and rule changes
- Tết Nguyên Đán 2027 (mid-February) is the next peak: min-stay and rate plan should be set now; rainy-season low occupancy planning; commission-rate and tax-regime changes need an "effective date" mechanism rather than hard-coded values.

### S1-19 · adoption & friction · E — Cut messaging time (pain #3) while growing direct bookings
- Saved quick-reply templates / Zalo OA with standard answers (price, availability link, deposit, cancellation policy, directions); repeat-guest list with consent; post-stay message asking for Google/OTA review; perks for returning guests rather than price cuts.

### S1-20 · money · E — Channel payout reconciliation
- Each channel pays differently (OTA collects vs pay-at-property, Agoda net payouts, Airbnb payouts after host fee and FX). Record gross, fee, net and payout date per booking; reconcile to bank monthly. Airbnb's fee model should be verified from actual payout reports (assistant should not assume "3%"; certainty: low on current Airbnb fee structure for this host).

### S1-21 · failure & edge cases · E — Overbooking playbook
- Pre-agreed partner homestay nearby to "walk" guests, compensation script, and awareness that OTAs may penalise/charge relocation costs for host-caused cancellations (certainty: medium). Close all channels for a room the moment a direct booking is taken.

### S1-22 · misuse & privacy · E — Access control on the booking sheet
- The sheet holds names, phone numbers and soon ID data; restrict editors, separate guest-ID data from the operational sheet the cleaner sees, and use marketing consent before adding guests to promotional lists.
