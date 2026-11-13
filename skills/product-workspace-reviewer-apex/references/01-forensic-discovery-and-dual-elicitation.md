# 01. Forensic X-Ray Recording, Root-Vision Elicitation & Vision-vs-Reality Gap Matrix

## 1. The Fatal Flaw of Traditional "Code/Workspace Reviewers" (`Sửa Ngọn Quên Gốc`)

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using, three fatal traps await naive AI agents:
1. **The "Premature Patching" Trap (`Sửa Ngọn Quên Gốc`):** Naive AI scans the existing folder and immediately proposes patches/refactoring for the files it sees—never realizing that the existing workspace only implemented 30–40% of the user's **Original Root Idea**, or built it in the wrong direction because the previous AI didn't know how to elicit requirements!
2. **The "Arrogant Rewrite" Trap:** Naive AI deletes or overwrites working files, accidentally destroying historical customer records (`Red Zone`) or sacred muscle-memory habits.
3. **The "Cosmetic Praise" Trap:** Naive AI skims 3 files, gives 5 generic textbook tips, and fails to run a true A-to-Z `idea-to-product` evolution.

To defeat all three traps, `product-workspace-reviewer-apex` strictly separates **Phase 1 (Turn 1: Objective X-Ray Recording + Root-Vision Interview ONLY)** from **Phase 2 (Turn 2: Vision-vs-Reality Gap Matrix + Full A-to-Z Evolution Blueprint)**.

---

## 2. Phase 1 (Turn 1): Silent/Factual X-Ray Recording + Root-Vision Interview (NO FIXES ALLOWED!)

### Step 1A: Objective Non-Destructive X-Ray Recording
Run `scripts/xray_scanner.py` (or inspect the workspace structure) and output ONLY the **Objective Baseline Telemetry**:
1. **Asset & Module Inventory:** Total files, directory depth, existing modules/scripts/templates, and what workflows are currently present.
2. **Entropy & Version Chaos Index:** Any duplicated or manually versioned files (`v1`, `v2`, `final_copy`, `.bak`).
3. **Blast-Radius Zoning (Green / Yellow / Red Zones):**
   * 🟢 **Green Zones:** Docs, static UI/assets, export templates.
   * 🟡 **Yellow Zones:** Existing logic/scripts/templates that can be refactored under test protection.
   * 🔴 **Red Zones:** Historical invoices/orders, customer databases, live credentials (100% read-only snapshot protection).

> **⛔ IRON GATE 1A:** Right after showing this factual inventory, explicitly tell the user:
> *"I have recorded the current state of your workspace above. I am **not** proposing any fixes yet—first, I want to interview you from the root of your original idea so we can compare what you truly wanted from A-to-Z against what this workspace currently does."*

### Step 1B: Root-Vision A-to-Z Elicitation Interview (From Scratch)
Ask the user **3 to 4 open, root-level questions** (mirroring `idea-to-product-apex`) before designing any solution:
1. **Q1 — Original Root Vision & Ultimate North Star:**
   *"Temporarily set aside the limitations of the current files in this workspace: when you first started this project, what was the complete, ideal product or outcome you wanted it to achieve from A to Z?"*
2. **Q2 — Open-Canvas Unbuilt Ambitions & Outside-the-Box Ideas:**
   *"What features, workflows, or secret ideas did you originally want (or recently think of) that the current workspace completely missed, left half-finished, or built the wrong way?"*
3. **Q3 — Real-World Friction & Disappointments:**
   *"When operating the current workspace in real life, what frustrates you the most or wastes the most time compared to your initial expectation?"*
4. **Q4 — Sacred Assets & Habits to Preserve:**
   *"Which specific data, files, or working parts in the current workspace are already serving you well and must be preserved 100%?"*

> **🛑 HARD STOP AT THE END OF TURN 1:** Stop immediately after asking Q1–Q4 and wait for the user's response! Never output repair options or code edits on Turn 1.

---

## 3. Phase 2 (Turn 2 — After User Replies): The 4-Column Vision-vs-Reality Gap Matrix & A-to-Z Expansion

Once the user shares their **Original Root Vision**, cross-examine **Root Vision** against **Current Workspace Reality** in a mandatory **4-Column Gap Matrix**:

| Gap Bucket | Definition | Action in A-to-Z Pipeline |
| :--- | :--- | :--- |
| **1. 🟢 Met & Healthy (`KEEP & PROTECT`)** | Parts of the current workspace that already fulfill the user's Root Vision accurately and reliably. | Lock & preserve 100%; wrap cleanly into the upgraded architecture. |
| **2. 🟡 Built Wrong / Drifted (`REALIGN & REFACTOR`)** | Existing files/code that attempted to solve a requirement from the Root Vision, but built it poorly, hardcoded it, or drifted from the user's true intent. | Split into **15-Min Quick-Win Patches** and **Surgical 3-Tier Refactors** with regression parity tests. |
| **3. 🔵 Unbuilt Core Vision (`MISSING A-TO-Z BUILD`)** | Core features, workflows, or desires from the user's Root Vision that the current workspace **never built at all**! | Execute full **Greenfield A-to-Z Idea-to-Product Engineering** to build these missing pillars from scratch! |
| **4. 🚀 30% Beyond-Expectation Expansion (`KANO DELIGHTERS + 4 SILENT LEAKS`)** | High-ROI industry capabilities (`DOM-01..07`) and 4 Johari Silent Leak remedies that the user didn't even know to ask for. | Inject 20–30% asymmetric delight features that elevate the product far beyond the user's original expectation. |

### The 4 Silent Leaks (Injected into Bucket 4)
1. **Leak 1 — Cognitive & Time Bleed:** Manual copy-pasting, repetitive steps, or hunting across `v1/v2` files.
2. **Leak 2 — Unit Economics & Revenue Bleed:** Slow quote/response turnaround, unguarded margin drops, or wasted API/hosting cost.
3. **Leak 3 — Structural & Volatility Rot:** Hardcoded prices, tax rates, rules, or prompts scattered inside logic files instead of a 2-Minute Editable Tier-B Config.
4. **Leak 4 — Catastrophic Fragility:** Risk of overwriting historical Red-Zone records, zero input validation, or lack of 1-click export/backup.

### Selecting the Strategic A-to-Z Evolution Archetype (End of Phase 2 — Mandatory 2-Section Format)
After presenting the **4-Column Vision-vs-Reality Gap Matrix**, you MUST present **Section 1 (Personal Priority & Customization Questions)** and **Section 2 (The 3-Option Pros/Cons/Best-Fit Decision Table + Hybrid Option D)**—never bare 1-line choices!

#### 1. Dedicated Personal Customization Questions ("Phần Hỏi Riêng Bạn"):
* Ask the user directly: *"Looking at the 4-Column Gap Matrix above, is there any personal requirement, workflow habit, or custom idea of your own that you want to add, remove, or prioritize differently before we lock the upgrade plan?"*

#### 2. Strategic A-to-Z Evolution Decision Matrix (With Explicit Pros ✅, Cons ⚠️ & Best-Fit 🎯):

| Phương án nâng cấp | Cơ chế cốt lõi | ✅ Ưu điểm (Pros) | ⚠️ Nhược điểm / Đánh đổi (Cons) | 🎯 Hợp nhất với mong muốn của bạn nếu... (Best Fit) |
| :--- | :--- | :--- | :--- | :--- |
| **Option A (Surgical Realignment & Hygiene)** | Giữ Cột 1 (`KEEP`), sửa Cột 2 (`REALIGN`), tách file Config Tier-B & khóa an toàn Vùng Đỏ | • Nhanh nhất, rủi ro bằng 0<br>• Không làm xáo trộn thói quen cũ | • **Chưa xây mới** các tính năng còn thiếu ở Cột 3 (`MISSING A-TO-Z`) | Bạn chỉ muốn **dọn sạch, sửa lỗi hiện tại và dùng ổn định ngay** mà chưa cần bổ sung tính năng mới. |
| **Option B (Khuyên dùng — Full Root-Vision A-to-Z + 30% Kano Delighters)** | Giữ Cột 1 + Sửa Cột 2 + **Xây mới A-Z toàn bộ Cột 3 (`MISSING A-TO-Z`)** + **Bơm 30% Cột 4 (`KANO`)** | • Đạt 100% mong muốn gốc ban đầu + vượt kỳ vọng 30%<br>• Bền vững 12 tháng không cần viết lại | • Thời gian thi công dài hơn Option A (chia làm 4 chặng kiểm thử) | Bạn muốn **biến workspace hiện tại thành đúng sản phẩm hoàn chỉnh từ A–Z như ước muốn ban đầu** của bạn. |
| **Option C (10x Next-Gen Platform via Strangler-Fig)** | Xây dựng kiến trúc thế hệ mới bao bọc lấy dữ liệu cũ, tự động hóa toàn diện quy mô lớn | • Sức mạnh và khả năng mở rộng gấp 10 lần bản cũ<br>• Chuẩn hóa cấp độ Enterprise | • Thay đổi nhiều cấu trúc bên dưới<br>• Tốn nhiều token và bước kiểm thử nhất | Bạn muốn **lột xác hoàn toàn dự án lên quy mô lớn/tự động hóa tối đa** cho 1–2 năm tới. |
| **Option D (Lai ghép / Theo ý riêng của bạn)** | Tuỳ biến tự do theo câu trả lời riêng của bạn | • Khớp 100% với ý muốn cá nhân (ví dụ: lấy Option B nhưng chỉ chọn một số tính năng Cột 3 & 4) | • Cần chốt danh sách tính năng cụ thể cùng bạn trước khi chạy | Bạn muốn **tự chọn những mảnh ghép hợp ý nhất từ A, B, C cộng với ý riêng của bạn**. |

Once the user confirms their personal adjustments and chosen path, proceed seamlessly through **Phase 3 (6-Role C-Suite Red-Team Council)** $\rightarrow$ **Phase 4 (Unified A-to-Z Evergreen Architecture)** $\rightarrow$ **Phase 5 (Full A-to-Z Build of Missing Features + Surgical Refactoring of Existing Assets)** $\rightarrow$ **Phase 6 (Before/After Vision-Fulfillment Delta & 365-Day Handover)**.
