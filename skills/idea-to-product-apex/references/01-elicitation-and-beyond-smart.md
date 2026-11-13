# 01. Dual-Mode Elicitation Engineering & The Pros/Cons Decision Matrix

## 1. Why Bare "3-Option Multiple Choice" Fails the User

When an AI presents 3 bare options (`Option A`, `Option B`, `Option C`) without asking the user personal open questions and without analyzing the **Pros, Cons, and Best-Fit** of each option, two critical failures occur:
1. **No Space for Personal Desires ("Không có phần hỏi riêng người dùng"):** When options A/B/C are merged directly into the question, the user's own secret ideas, personal workflow preferences, and unique domain insights (*outside* AI's 3 options) are never excavated.
2. **Blind Choice Paralysis ("Không có Ưu/Nhược điểm nên không biết chọn gì"):** Listing 3 brief titles or 1-sentence descriptions leaves the user guessing which option actually matches their personal goals, budget, and operating habits.

---

## 2. The APEX v3.7 Mandate: Strict 2-Section Discovery Format

Every discovery turn in Phase 1 & Phase 2 MUST be explicitly divided into **Two Mandatory Sections** in visible chat output (even if the host IDE also has a multiple-choice UI tool):

```
[SECTION 1: Dedicated Personal Open-Canvas Questions (No A/B/C Attached!)]
  --> Excavates the user's personal desires, custom ideas, and Socratic edge cases
                                   +
[SECTION 2: AI 3-Option Decision Matrix (With Pros ✅ / Cons ⚠️ / Best-Fit 🎯 + Hybrid Option D)]
  --> Gives clear trade-offs so the user knows exactly which option (or mix) fits their true desire
```

### Canonical 2-Section Discovery Template (Translate Naturally into the User's Language):

```markdown
### 💬 PHẦN 1: Câu Hỏi Riêng Khai Thác Mong Muốn & Ý Tưởng Cá Nhân Của Bạn (Personal Open Excavation)
*(Trước khi chọn các phương án gợi ý bên dưới, hãy chia sẻ góc nhìn riêng của bạn để hệ thống phục vụ đúng ý bạn nhất)*

1. **Mong muốn cốt lõi & Dấu ấn riêng của bạn:**
   Theo đúng gu cá nhân hoặc kinh nghiệm thực tế của bạn, kết quả lý tưởng nhất bạn muốn sản phẩm này làm được là gì? Có ý tưởng hay tính năng "độc" nào bạn đang ấp ủ mà chưa thấy ai làm không?
2. **Thực tế vận hành & Thói quen cá nhân (Socratic Check):**
   Khi sản phẩm đi vào hoạt động hàng ngày, ai sẽ là người trực tiếp bấm nút/vận hành nó, bạn muốn tốn tối đa bao nhiêu phút mỗi ngày cho nó, và điều gì dễ làm bạn (hoặc khách hàng) nản nhất nếu gặp phải?

---

### 🧭 PHẦN 2: Bảng Phân Tích 3 Gợi Ý Chiến Lược Của AI (Kèm Ưu Điểm, Nhược Điểm & Độ Phù Hợp)
*(Dưới đây là 3 hướng tiếp cận chuẩn ngành. Mỗi phương án đều có mặt mạnh và sự đánh đổi riêng để bạn dễ dàng cân nhắc hoặc lấy ý tưởng)*

| Phương án gợi ý | Cơ chế cốt lõi | ✅ Ưu điểm (Pros) | ⚠️ Nhược điểm / Đánh đổi (Cons) | 🎯 Hợp nhất với mong muốn của bạn nếu... (Best Fit) |
| :--- | :--- | :--- | :--- | :--- |
| **Phương án A (Khuyên dùng — Cân bằng & Tự động hóa cao)** | [Mô tả rõ cơ chế A] | • [Ưu điểm 1]<br>• [Ưu điểm 2] | • [Nhược điểm / Đánh đổi 1]<br>• [Giới hạn cần lưu ý] | Bạn muốn **ra sản phẩm nhanh, tự động hóa 80% thao tác lặp lại và bền vững 12 tháng** mà không phức tạp hóa hệ thống. |
| **Phương án B (Tối giản / Tinh gọn tốc độ cao)** | [Mô tả rõ cơ chế B] | • [Ưu điểm 1]<br>• [Ưu điểm 2] | • [Nhược điểm / Đánh đổi 1]<br>• [Tính năng bị lược bỏ] | Bạn muốn **ưu tiên sự đơn giản tuyệt đối, dùng được ngay trong ngày** và chấp nhận làm thủ công một vài bước phụ. |
| **Phương án C (Cao cấp / Quy mô lớn / Toàn diện 10x)** | [Mô tả rõ cơ chế C] | • [Ưu điểm 1]<br>• [Ưu điểm 2] | • [Nhược điểm / Đánh đổi 1]<br>• [Chi phí/thời gian cao hơn] | Bạn muốn **xây dựng hệ thống quy mô lớn, đa tác vụ chuyên sâu ngay từ đầu** và sẵn sàng đầu tư thêm thời gian cấu hình. |
| **Phương án D (Lai ghép / Theo ý riêng của bạn ở Phần 1)** | Kết hợp tự do | • Giữ trọn vẹn ý tưởng riêng của bạn ở Phần 1 + nhặt phần hay nhất của A/B/C | • Cần 1 vòng phản biện Socratic để chốt biên giới kỹ thuật | Bạn muốn **lấy ý tưởng riêng ở Phần 1 làm gốc, cộng thêm [ưu điểm của A] và [ưu điểm của C]**. |

👉 **Cách bạn phản hồi nhanh nhất:** Bạn hãy trả lời tự do **Phần 1 (Mong muốn riêng của bạn)** kèm theo lựa chọn ở **Phần 2** (ví dụ: *"Chọn A nhưng thêm ý riêng X của tôi"*, hoặc *"Lai giữa A và C"*).
```

---

## 3. The 2-Pass Discovery Loop (Pass 1: Personal + Trade-Off Matrix $\rightarrow$ Pass 2: Convergent Grill-Me)

* **Pass 1 (Divergent Personal Excavation + Trade-Off Matrix):** Present **Section 1 (Personal Open Questions)** and **Section 2 (Pros/Cons/Best-Fit Table for Options A/B/C/D)** using the template above.
* **Pass 2 (Convergent "Grill-Me" Stress-Test):** Once the user replies with their personal answers and chosen/hybrid direction:
  * Explicitly acknowledge how their **personal desires from Section 1** modify or override the standard options in Section 2.
  * Stress-test any remaining operational edge cases (*"To make sure your custom combination of [Option A + Personal Idea X] runs for 12 months without breaking, let's lock down 2 final edge cases..."*) — and again provide Pros/Cons for each resolution!

---

## 4. The Johari Window Protocol (Quadrant-4 Unknown-Unknowns)

Map project knowledge into 4 quadrants and **dedicate 50% of advisory energy to Quadrant 4**:
1. **Quadrant 1 (Known Knowns):** What the user stated.
2. **Quadrant 2 (Known Unknowns):** What the user asked AI to solve.
3. **Quadrant 3 (Hidden Personal Context — User knows, AI doesn't know yet):** The user's private business secrets, personal preferences, local market habits, or novel ideas outside AI's training average. *(Extracted via **Section 1: Dedicated Personal Open Questions**!)*
4. **Quadrant 4 (Unknown Unknowns — User doesn't know, AI Council injects):**
   * Industry landmines, legal/compliance traps, unit-economics killers, schema corruption risks, and **30% Kano Asymmetric Delighters** (each presented with clear **Pros, Cons, and ROI**!).

---

## 5. Upgrading SMART to SMART-ER at Gate 4

Only after Discovery (Gate 1), Kano Delight (Gate 2), and C-Suite Red-Team (Gate 3) are complete, lock every specification into **SMART-ER**:
* **S**pecific (Exact input, processing logic, output format, and explicit *Non-Goals*)
* **M**easurable (Quantifiable numeric threshold)
* **A**chievable (Realistic for the operator's budget and Bus Factor)
* **R**elevant (Directly drives core JTBD & protects unit margins)
* **T**ime-bound (Mapped to Vertical Slices 1..4)
* **E**valuated (Backed by an automated verification script or test command at that exact step)
* **R**esilient 12M (12-month durability: Tier-B config isolation + immutable historical snapshots)
