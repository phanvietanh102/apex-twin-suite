# 01. Dual-Mode Elicitation Engineering & The Pros/Cons Decision Matrix

## 1. Why Bare "3-Option Multiple Choice" Fails the User

When an AI presents 3 bare options (`Option A`, `Option B`, `Option C`) without asking the user personal open questions and without analyzing the **Pros, Cons, and Best-Fit** of each option, two critical failures occur:
1. **No Space for Personal Desires ("Không có phần hỏi riêng người dùng"):** When options A/B/C are merged directly into the question, the user's own secret ideas, personal workflow preferences, and unique domain insights (*outside* AI's 3 options) are never excavated.
2. **Blind Choice Paralysis ("Không có Ưu/Nhược điểm nên không biết chọn gì"):** Listing 3 brief titles or 1-sentence descriptions leaves the user guessing which option actually matches their personal goals, budget, and operating habits.

---

## 2. When to Use the 2-Section Format (and When Not To)

The 2-section format solves two real problems: personal open questions so the user's own ideas surface, and pros/cons/best-fit so options are never chosen blindly. But eval run 1 showed it hurting when applied mechanically. It cost the most points when it was shown *again* after the user had already said "just pick and continue".

Use it only when all three hold:
1. There is a **genuine fork**: 2–3 viable paths that differ in ways only the user can weigh (cost vs. speed, manual vs. automated, scope).
2. The user has **not delegated** the decision ("cứ chọn phương án bạn thấy hợp nhất", "you decide", "làm luôn").
3. You have **already led with value**: Turn 1 opens with 2–4 concrete domain findings, and the questions and table come after them.

Otherwise, recommend one path in a sentence, say what would change your mind, and keep going. When the user delegates, convert their answers into decisions and build in the same reply.

Always keep **one open question** for the user's own idea, even when you skip the table. That is where knowledge the model does not have comes from.

```
[Turn 1]  2–4 concrete findings for this user's domain  →  recommended direction (+ draft if cheap)
          →  ≤ 3 questions that change the build (one of them open)  →  options table ONLY if a real fork exists
[Turn 2+] user delegated?  → decide in one line, build slice 1 (the biggest flow) now
          user chose/mixed? → acknowledge how their own idea changed the plan, then build
```

### 2-Section Template (when a genuine fork exists; translate naturally into the user's language; add a "Khuyến nghị của tôi" line):

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

## 3. The 2-Pass Discovery Loop (Pass 1: Value + Questions $\rightarrow$ Pass 2: Decide & Build)

* **Pass 1:** Lead with findings. Then ask the personal questions, plus the options table if a genuine fork exists (see §2).
* **Pass 2:** Once the user replies:
  * Say briefly how their own ideas changed the plan.
  * Resolve the remaining edge cases **yourself** with sensible defaults and list them as assumptions they can override. Do not open another question round unless an edge case is truly blocking and only the user can answer it.
  * Start building slice 1, the flow carrying most of their volume or pain.

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
