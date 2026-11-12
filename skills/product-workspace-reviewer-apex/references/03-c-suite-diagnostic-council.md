# 03. C-Suite Forensic Diagnostic Council, Competency Standards & Deduction Scoring (Hội Đồng 6 Giám Đốc Chẩn Đoán & Kiểm Toán Chuyên Sâu)

## 1. Twin-Parity Model Competency & Subagent Critic Policy

To maintain **100% parity** with `idea-to-product-apex`:
1. **Frontier High-Reasoning Model Required (Phases 1, 3, 4):**
   * Forensic architecture auditing and root-cause analysis require a **High-Reasoning Model** (`Claude Opus / Sonnet Thinking`, `Gemini Pro / Argon High`). Warn the user if running on a lightweight model.
2. **Isolated Subagent Forensic Critic (Chống "Nhận Xét Nể Nang / Bề Nổi"):**
   * When subagents are supported (`invoke_subagent` / Task tool), spawn an **isolated Forensic Auditor Subagent** to inspect the target product/workspace with fresh, ruthless eyes.

---

## 2. Hard Competency Standards & Mandatory Forensic Proof per Executive Role

Every member of the 6-Role Diagnostic Council must produce a **Mandatory Quantitative Forensic Proof** (generic advice is strictly rejected):

| Persona | Diagnostic Role | Mandatory Forensic Deliverable Proof | Veto / Block Condition |
| :--- | :--- | :--- | :--- |
| **1. CPO (Giám đốc Sản phẩm & UX Auditor)** | Cognitive Walkthrough & Conversion Leak Hunter | **Step-by-Step Friction & Drop-Off Map:** Counts exact steps, clicks, and manual copy-pastes required to complete the core workflow Today vs. After Upgrade, plus **30% Kano Modernization Table**. | Upgrade fails to cut manual friction by $\ge 40\%$ or breaks a Sacred User Habit. |
| **2. CTO / Principal Legacy Architect** | Technical Debt, Blast-Radius & Coupling Forensics | **Green/Yellow/Red Zone Map + Hardcoded Volatility Inventory:** Lists exact file paths and line numbers where volatile data (prices, rules, URLs, prompts) is hardcoded or where files are duplicated. | Refactor touches a Red Zone without a verified snapshot backup or leaves hardcoded volatility in Tier A. |
| **3. VP of Domain & Benchmark Strategy (`DOM-01`..`07`)** | Industry Gap & Competitive Moat Auditor | **Domain Benchmark Gap Table:** Compares current product/workspace against Top 1% industry standards (SEO/AIO schema, construction BOQ standards, invoice accuracy, etc.). | Leaves major industry blind spots unaddressed. |
| **4. CFO / FinOps & Time-Bleed Director** | Unit Economics & Operational Waste Auditor | **Annualized Time & Money Leak Calculation:** Quantifies exact hours/year wasted on manual repetition + API/infra/margin leaks ($\text{Hours Saved/Yr} \times \text{Value}$). | Upgrade adds recurring cost or increases daily maintenance time. |
| **5. CRO / CISO / COO (Giám đốc Rủi ro & Vận hành)** | Entropy, Data Loss & Disaster Recovery Auditor | **Single-Point-of-Failure & Entropy Audit:** Quantifies workspace clutter index (duplicate `v1/v2` files, missing backups, unvalidated inputs) and verifies the **1-Click Rollback & 5-Min Manual SOP**. | No rollback mechanism exists before modifying existing files, or historical records risk overwrite. |
| **6. Frustrated Daily Operator / End-User** | Real-World Muscle-Memory & Edge-Case Tester | **Pain-Point Walkthrough Log:** Simulates daily high-stress usage (rushed edits, typos, mobile viewing, messy real-world data). | New upgrade feels more complicated or slower to use than the old system. |

---

## 3. Dual-Scorecard Protocol: "Before (Baseline)" vs. "After (Upgraded)"

Unlike a Greenfield project (which only scores the proposed blueprint), a Brownfield Review MUST produce a **Comparative Delta Scorecard (Thang Điểm Đối Chiếu Trước & Sau Nâng Cấp)** across all 6 dimensions (100 points total):

```markdown
| Tiêu chí Kiểm toán C-Suite (Thang 100) | Điểm Hiện Trạng (Before) | Lỗ hổng Thực tế Phát hiện (Evidence) | Điểm Sau Nâng Cấp (After) | Cơ chế Khắc phục Triệt để |
| :--- | :---: | :--- | :---: | :--- |
| **1. Hiệu suất Luồng việc & UX (20đ)** | [X]/20 | [Số bước thừa / điểm nghẽn] | [Y]/20 | [Rút gọn luồng + Preset 1-Click] |
| **2. Giá trị Đột phá Kano 30% (15đ)** | [X]/15 | [Thiếu tính năng thông minh] | [Y]/15 | [Bổ sung 3 Delighters tự động] |
| **3. Chuẩn mực Chuyên ngành (15đ)** | [X]/15 | [Thiếu chuẩn ngành DOM-0X] | [Y]/15 | [Chuẩn hóa theo Top 1% ngành] |
| **4. Kiến trúc 3 Tầng & Tách Cấu hình (20đ)**| [X]/20 | [Đóng cứng giá/luật ở file X] | [Y]/20 | [Tách Tier-B sửa trong 2 phút] |
| **5. Tối ưu Chi phí & Thời gian (15đ)** | [X]/15 | [Mất X giờ/tuần làm thủ công] | [Y]/15 | [Tự động hóa tiết kiệm 80% giờ] |
| **6. An toàn Dữ liệu, Chuẩn hóa & Sao lưu (15đ)**| [X]/15 | [Trùng file v1/v2, thiếu backup]| [Y]/15 | [Snapshot bất biến + Rollback] |
| **TỔNG ĐIỂM SỨC KHỎE HỆ THỐNG** | **[Before]/100** | **Chênh lệch: +[Delta] điểm** | **[After >= 85]/100** | **BẢO CHỨNG 12 THÁNG** |
```

---

## 4. Built-In Defenses Against 7 Brownfield Review Meta-Risks

| # | Brownfield Meta-Risk (Rủi ro khi Review & Nâng cấp) | Naive AI Failure | APEX v3.5 Built-In Defense |
| :--- | :--- | :--- | :--- |
| **1** | **Destructive Refactoring (Sửa lợn lành thành lợn què)** | Deletes or overwrites working files/data. | **Mandatory Pre-Flight Snapshot Backup** + Red-Zone Quarantine before any edit. |
| **2** | **Breaking Muscle Memory (Đổi giao diện/luồng làm người dùng bỡ ngỡ)** | Changes familiar shortcuts/layouts unnecessarily. | **Sacred Habit Lock** in `00-PRESERVATION-CONSTITUTION.md`. |
| **3** | **Broken Internal Links / Imports After Reorganization** | Moving messy files breaks scripts, formulas, or HTML links. | Automated path-reference scan & update verification in Gate 5. |
| **4** | **Silent Regression in Calculation / Output** | New code produces slightly different numbers on old invoices/data. | **Behavioral Parity Test:** Run old inputs through new engine and assert 100% match. |
| **5** | **Superficial "Consultancy Talk" Without Action** | Writes a long critique report but doesn't actually fix the workspace/code. | Phases 5–6 execute the actual surgical upgrades and verify with `review_gate_audit.py`. |
| **6** | **Context Bloat During Large Workspace Audits** | Tries to read 500 files into context at once and crashes/hallucinates. | Uses `xray_scanner.py` to map metadata first; reads only targeted files per slice. |
| **7** | **Relapse into Chaos After 60 Days (Tái phát bừa bộn)** | Cleaned workspace gets messy again next month. | Leaves behind an automated **Hygiene/Validation Script** & 2-Minute SOP. |
