# 01. Forensic X-Ray Recording, Root-Vision Elicitation & Vision-vs-Reality Gap Matrix

## 1. The Fatal Flaw of Traditional "Code/Workspace Reviewers" (`Sửa Ngọn Quên Gốc`)

When a user brings an existing app, website, Excel/invoice workflow, SEO content folder, or project workspace they have been using, three fatal traps await naive AI agents:
1. **The "Premature Patching" Trap (`Sửa Ngọn Quên Gốc`):** Naive AI scans the existing folder and immediately proposes patches/refactoring for the files it sees—never realizing that the existing workspace only implemented 30–40% of the user's **Original Root Idea**, or built it in the wrong direction because the previous AI didn't know how to elicit requirements!
2. **The "Arrogant Rewrite" Trap:** Naive AI deletes or overwrites working files, accidentally destroying historical customer records (`Red Zone`) or sacred muscle-memory habits.
3. **The "Cosmetic Praise" Trap:** Naive AI skims 3 files, gives 5 generic textbook tips, and fails to run a true A-to-Z `idea-to-product` evolution.

To defeat all three traps, `product-workspace-reviewer-apex` separates **Turn 1 (read-only: evidence-backed findings + root-vision questions)** from **Turn 2+ (gap matrix, then build)**.

---

## 2. Turn 1: Findings First, Then Root-Vision Questions (Read-Only)

Eval run 1 showed that a Turn 1 containing only an inventory plus an interview feels like homework to a busy owner. Findings come first: they prove the review is worth reading. File changes still wait until the owner has said what is sacred.

### Step 1A: Read the Workspace and Report Findings
1. Run `scripts/xray_scanner.py --scan-only` for the inventory: file counts, duplicate/version files, and zones. It writes nothing. Then **open the actual files**: run what is safe to run, recompute the numbers, and read the records.
2. Report **3–6 findings ranked by money and data risk**, each with evidence (file:line, the computed number, the affected record) and what it costs the owner. Typical findings: an under- or over-pricing formula, money in float, the same price kept in several places, an unpaid balance hidden in an archive, duplicate outputs, missing validity dates or payment terms.
3. Mark the zones in plain words:
   * **Safe to change:** docs, static assets.
   * **Change only with tests:** logic, scripts, templates.
   * **Never touch:** historical invoices, customer data, credentials. These are read-only and get snapshot protection.
4. Proposing *what* to fix is fine. **Do not edit, move or create files in the workspace on Turn 1.**

### Step 1B: Root-Vision Questions (≤ 3, after the findings)
1. **Original vision:** *"Setting aside what is built now: what did you originally want this to do, from start to finish?"*
2. **Pain and gaps:** *"Where does it break down or waste your time, and what did you want that it never did?"*
3. **Sacred assets:** *"Which files, data or habits must stay exactly as they are?"*

Drop or merge any question the workspace already answers. Then stop and wait for the reply.

---

## 3. Turn 2 (After the Owner Replies): The 4-Column Vision-vs-Reality Gap Matrix & A-to-Z Expansion

Show the matrix to the owner in short, plain language. The bucket labels below are internal names.

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

### Selecting the Evolution Path (Only When the Choice Is Genuinely the Owner's)
**If the owner delegated** ("cứ chọn phương án bạn thấy hợp nhất và làm tiếp", "you decide", "làm luôn"), skip the table. Pick the path in one line, list your assumptions, and start building slice 1 (verified backup and Red-Zone lock), then their biggest pain.

Otherwise, after the gap matrix, present the two parts below. Never give bare one-line choices, and always add your recommendation.

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
