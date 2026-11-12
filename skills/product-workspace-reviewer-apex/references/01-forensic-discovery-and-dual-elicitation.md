# 01. Forensic X-Ray Discovery & Dual-Mode Pain Excavation (Quét X-Quang Hiện Trạng & Khai Thác Kép Cho Sản Phẩm/Workspace Đang Vận Hành)

## 1. Why Reviewing an Existing Product/Workspace Is Fundamentally Harder Than Building From Scratch

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using for months or years, two fatal traps await naive AI agents:
1. **The "Arrogant Rewrite" Trap (Đập đi xây mới phá hỏng di sản):** Naive AI looks at an old workspace or codebase, calls it messy, and rewrites it from scratch—accidentally destroying unwritten business rules, historical customer records, SEO rankings, or muscle-memory habits the owner relies on daily!
2. **The "Cosmetic Praise" Trap (Nhận xét hời hợt bề nổi):** Naive AI skims 3 files, gives a generic list of 5 textbook tips, and misses the **silent financial, operational, and structural leaks** killing the system from the inside.

---

## 2. Step 1: Automated Non-Destructive X-Ray Scan (Chụp X-Quang Tự Động Trước Khi Hỏi)

Before asking the user a single question, run `scripts/xray_scanner.py` (or inspect the workspace structure) to gather objective forensic facts:
1. **Asset & File Topology:** Total files, directory depth, file formats (code, spreadsheets, PDFs, images, markdown, configs).
2. **Entropy & Version Chaos Index:** Detect duplicated or manually versioned files (e.g., `baogia-v1.xlsx`, `baogia-v2-final.xlsx`, `copy of ...`, `.bak`, `old/`) which prove that the user is suffering from **manual versioning pain**.
3. **Blast-Radius Zoning (Phân Vùng Rủi Ro Xanh / Vàng / Đỏ):**
   * 🟢 **Green Zones (Vùng Xanh — An toàn tối ưu ngay):** UI polish, new export templates, documentation, isolated helper scripts, static asset organization.
   * 🟡 **Yellow Zones (Vùng Vàng — Cần kiểm thử tương đương khi nâng cấp):** Core workflow scripts, search/filter logic, SEO/AIO schema templates, folder restructuring.
   * 🔴 **Red Zones (Vùng Đỏ — Dữ liệu sống / Tài chính / Lịch sử bất biến):** Historical invoices/orders, customer databases, payment/billing formulas, live production URLs, authentication keys. *(Rule: Never mutate Red Zones without a verified backup snapshot and Strangler-Fig wrapper!)*

---

## 3. Step 2: The 3-Layer "Dual-Mode Hybrid Elicitation" for Existing Systems

Once the X-Ray scan completes, interview the user (max 3–4 questions per turn) combining **Open Pain/Habit Excavation + Brutal Diagnostic Grilling + A/B/C/D Modernization Paths**:

### Layer 1: Open Excavation of "Sacred Habits" & "Secret Ambitions" (Khai Thác Mở)
* Ask what **MUST NOT CHANGE** (*"Phần nào trong công cụ/workspace hiện tại bạn đang cực kỳ ưng ý hoặc đã quen tay đến mức không muốn bị xáo trộn?"*).
* Ask for the user's **Own Upgrade Vision** (*"Trong quá trình dùng thực tế bấy lâu nay, có ý tưởng nâng cấp hay tính năng tự động hóa nào bạn từng nghĩ tới mà chưa làm được không?"*).

### Layer 2: Brutal Diagnostic Stress-Test ("Gắt Gao Chuyên Sâu")
* Point directly to concrete evidence found in the X-Ray scan:
  * *"Qua quét X-Quang, tôi phát hiện [X file bị trùng phiên bản v1/v2 / Y tham số giá đang đóng cứng / Z bước đang phải copy-paste thủ công]. Mỗi tuần bạn đang mất bao nhiêu phút cho khâu này, và đã từng xảy ra nhầm lẫn số liệu nào chưa?"*

### Layer 3: AI Benchmark Modernization Paths (Options A/B/C + Wildcard D)
Always provide 3 calibrated modernization options plus Option D so the user controls the exact blast radius:
* **Phương án A (Surgical Polish & Hygiene — An toàn 100%, giữ nguyên luồng cũ):** Dọn dẹp cấu trúc, vá lỗi ngầm, tách bảng cấu hình Tier B, tự động hóa sao lưu.
* **Phương án B (Khuyến nghị — Evolutionary 3-Tier Upgrade + 30% Kano Delighters):** Giữ nguyên toàn bộ dữ liệu lịch sử (Red Zone), nâng cấp lõi xử lý, thêm 3 tính năng thông minh vượt kỳ vọng, bảo chứng chạy nhàn 12 tháng.
* **Phương án C (10x System Transformation via Strangler Fig):** Xây dựng giao diện/hệ thống tự động hóa thế hệ mới bọc ngoài dữ liệu cũ, chuyển đổi mượt mà không gián đoạn.
* **Phương án D (Ý tưởng nâng cấp riêng của bạn / Kết hợp tùy chỉnh):** Ưu tiên tuyệt đối góc nhìn thực tế của người vận hành!

---

## 4. Mapping the "4 Silent Leaks" (Tương Đương Johari Quadrant 4 Của Bản A-Z)

Just as `idea-to-product-apex` injects 4 Unknown-Unknown industry blind spots, `product-workspace-reviewer-apex` MUST uncover **4 Silent Leaks** that the user has grown numb to ("Quen khổ mà không biết mình đang mất tiền/thời gian"):

1. **Leak 1 — Cognitive & Time Bleed (Rò rỉ Thời gian & Thao tác thừa):**
   Manual copy-pasting between files, repetitive formatting, or hunting for files across chaotic folders.
2. **Leak 2 — Unit Economics & Revenue Bleed (Rò rỉ Doanh thu & Biên lợi nhuận):**
   Slow response time to leads, outdated unit prices in quotes/invoices, unmonetized follow-ups, or excessive API/hosting waste.
3. **Leak 3 — Structural & Volatility Rot (Lão hóa Kiến trúc & Đóng cứng Tham số):**
   Hardcoded prices, tax rates, prompts, or file paths that require manual editing in multiple places whenever the market shifts.
4. **Leak 4 — Catastrophic Fragility (Rủi ro Mất trắng / Sập ngầm):**
   Lack of immutable historical snapshots (editing a template overwrites old customer records), zero automated validation on input errors, or single-device lock-in without 1-click export.
