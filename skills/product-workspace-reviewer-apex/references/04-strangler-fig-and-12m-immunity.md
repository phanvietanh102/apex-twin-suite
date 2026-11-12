# 04. Agentic Strangler-Fig Evolution & 12-Month Immunity Architecture (Kiến Trúc Nâng Cấp Không Gián Đoạn & Miễn Dịch Lão Hóa 1 Năm)

## 1. Why "Rip-and-Replace" Rewrites Fail — And How the Strangler Fig Pattern Wins

When upgrading a product, app, or workspace that is actively being used:
* **Never do a Big-Bang Rewrite** that breaks current operations while the new version is being built.
* **Use the Agentic Strangler-Fig Pattern (Mô Hình Cây Đa Bọc Ngoài Nâng Cấp Dần):**
  1. **Step 1 — Quarantine & Freeze Historical Data (Đóng Băng Bảo Toàn Dữ Liệu Lịch Sử - Red Zone):**
     Move all historical invoices, completed projects, old contracts, and raw archives into an immutable `archive/` or `history/` vault so they remain 100% untouched and readable forever.
  2. **Step 2 — Extract Hardcoded Volatility into Tier B (Rút Ruột Các Tham Số Đóng Cứng Ra Bảng Cấu Hình):**
     Locate every hardcoded price, rate, tax percentage, product SKU, prompt template, or contact detail scattered across the old files, and consolidate them into a single, clean **Tier-B Configuration Source of Truth** (`config.json`, `settings.yaml`, or Master Config Sheet).
  3. **Step 3 — Wrap & Upgrade Core Workflows (Bọc Lõi Xử Lý & Cắm Thêm 30% Kano Delighters):**
     Connect the cleaned core logic (Tier A) to the new Tier-B Config and attach modern Tier-C outputs (1-click PDF/Excel generators, automated SEO/AIO checkers, interactive dashboards).
  4. **Step 4 — Verify Behavioral Parity & Switch Over:**
     Prove that historical test cases produce accurate results in the upgraded system, while keeping a 1-click rollback path to the pre-upgrade state.

---

## 2. Universal Workspace Hygiene & Anti-Entropy Architecture (Chuẩn Hóa Thư Mục Chống Tái Phát Bừa Bộn 12 Tháng)

When auditing a messy project folder or business workspace (e.g., scattered PDFs, Excels, images, scripts, and drafts), transform it into the **Immutable 5-Zone Workspace Taxonomy**:

```text
<Project-Or-Business-Root>/
├── 00-CONFIG-AND-TEMPLATES/    # Tier B: Bảng giá chuẩn, cấu hình, mẫu chuẩn (Sửa ở đây áp dụng toàn cục)
├── 01-ACTIVE-OPERATIONS/       # Công việc / dự án đang chạy (Đặt tên chuẩn: YYYY-MM-DD_MaDuAn_Ten)
├── 02-CORE-SYSTEM-AND-TOOLS/   # Tier A & C: Source code, scripts tự động hóa, công cụ xử lý
├── 03-IMMUTABLE-ARCHIVE/       # Red Zone: Hóa đơn đã chốt, dự án đã bàn giao (Bất biến, phân theo Năm/Quý)
├── 04-EXPORTS-AND-DELIVERABLES/# File xuất ra gửi khách (PDF/XLSX/Ảnh đã đóng gói)
└── docs/apex-review/           # Hồ sơ Kiểm toán Sức khỏe, Sổ tay SOP & STATE.json
```

### The 3 Laws of Workspace Immunity (Chống Tái Phát Rác Suốt 1 Năm):
1. **Zero `v1 / v2 / final_copy` Rule:** Never duplicate code or template files to change a number. Keep 1 canonical template in `00-CONFIG-AND-TEMPLATES/` and generate dated snapshots into `03-IMMUTABLE-ARCHIVE/` or `04-EXPORTS-AND-DELIVERABLES/`.
2. **ISO-8601 & Slug Naming Convention:** Standardize filenames as `<YYYY-MM-DD>_<Entity-Or-ProjectCode>_<DocType>_v<SemVer>.<ext>` so sorting alphabetically always sorts chronologically.
3. **Automated Hygiene Guard (`review_gate_audit.py`):** A single command checks if stray temporary files, duplicate copies, or unarchived items have accumulated.

---

## 3. The 365-Day Post-Upgrade Immunity Roadmap (Day 1 $\rightarrow$ Day 365)

Every upgraded product/workspace includes a 12-month operational immunity schedule in `04-ZERO-DOWNTIME-MIGRATION-ROADMAP.md`:

| Horizon | System State After Review & Upgrade | Built-In Immunity Mechanism | Operator Effort |
| :--- | :--- | :--- | :--- |
| **Day 1 (Surgical Upgrade Complete)** | Clutter eliminated; Tier-B Config extracted; 30% Delighters live; old data 100% preserved. | Pre-upgrade snapshot archived + Behavioral Parity tests passed. | 0 downtime; use upgraded flow immediately. |
| **Day 30 (1-Month Drift Check)** | First month of new operations; operator adjusts prices/templates. | Edit Tier-B Config in 2 minutes; zero need to duplicate files. | 5 mins config calibration. |
| **Day 90 (Quarterly Hygiene Sweep)** | New client/project files accumulated over Q1. | Run 1-click Archive move from `01-ACTIVE` to `03-IMMUTABLE-ARCHIVE/2026-Q1`. | 5 mins quarterly cleanup. |
| **Day 180 (Mid-Year Evolution)** | Business expands or external API/market rule shifts. | Adapter layer & schema versioning (`schema_version`) absorb changes without touching core. | 15 mins Mid-Year AI Audit. |
| **Day 365 (1-Year Evergreen Proof)** | 12 months of zero-rewrite operation and clean historical records. | 1-Click Annual Summary & Backup Export. | Ready for Year 2 with zero tech debt. |
