# APEX Skill Eval Pack (with vs. without skill)

Goal: measure whether the skill turns a **short, ordinary request** into a result that makes the user say "wow". That means insights beyond the user's own knowledge, a better product, and low friction.

Each case is 2 turns:

1. Send **Turn 1** exactly as written.
2. Whatever the assistant answers, send the **Turn 2** reply exactly as written.

Run each case twice in a fresh chat: once **with** the skill enabled and once **without** it. Run the same pack on every model and host (Claude Code / Claude Desktop / Antigravity with Gemini Argon).

---

## Case 1 — Greenfield, e-commerce (DOM-04), skill: `idea-to-product-apex`

**Turn 1**
> Tạo app quản lý đơn hàng cho shop mỹ phẩm online của tôi, bán qua Facebook và Shopee. Tôi muốn có: nhập đơn, theo dõi giao hàng, xuất hoá đơn.

**Turn 2**
> Shop có tôi + 1 bạn đóng gói part-time. Khoảng 40 đơn/ngày, 70% Shopee, 30% inbox Facebook (ship COD qua GHTK). Doanh thu khoảng 1,5 tỷ/năm, đăng ký hộ kinh doanh. Hiện tôi dùng Google Sheets, không rành code, ngân sách dưới 200k/tháng. Hay bị nhầm đơn inbox và quên đối soát tiền COD. Muốn dùng được trên điện thoại. Cứ chọn phương án bạn thấy hợp nhất và làm tiếp.

*Hidden "wow" opportunities (for the grader, not shown to the model):*
- E-invoice obligations for a household business with revenue ≥ 1 billion VND (invoices generated from a cash register; the lump-sum tax regime is ending).
- Cosmetics batch/expiry tracking.
- Return/refund handling across channels.
- COD reconciliation.
- Avoiding Shopee double-entry.

## Case 2 — Brownfield review, construction quoting (DOM-02), skill: `product-workspace-reviewer-apex`

Fixture: `evals/fixtures/xay-dung-baogia/`. Copy it to a fresh folder for every run.

**Turn 1**
> review giùm tôi workspace này: `<path to the copy>`

**Turn 2**
> Đây là workspace làm báo giá xây nhà phố của công ty nhỏ của tôi (3 người). Mong muốn ban đầu: nhập diện tích + loại hoàn thiện → ra báo giá chi tiết gửi khách bằng PDF đẹp, giá vật tư cập nhật dễ, lưu lịch sử báo giá đã gửi. Hiện hay bị: sửa file v2 rồi không biết file nào đúng, giá thép đổi liên tục, báo giá cũ bị tính lại sai khi đổi giá. Giữ nguyên file hoá đơn cũ trong archive. Cứ chọn phương án bạn thấy hợp nhất và làm tiếp.

*Planted issues (for the grader):*
- Prices are duplicated in 2 `.py` files and the CSV is unused.
- Money is computed in `float` with `round(…, 2)`.
- VAT is hard-coded at 10% and also applied to labour, with no question raised about which rate applies.
- No wastage factor (`hao hụt`), although a customer asked for it.
- The v1 output is missing the finishing tier.
- `(1)` duplicate files.
- An archived invoice has an unpaid balance of 112,400,000.
- No quote validity date or payment milestones.
- No snapshot of prices per quote.

## Case 3 — Greenfield, content/affiliate (DOM-03), skill: `idea-to-product-apex`

**Turn 1**
> Tôi muốn xây 1 website review đồ gia dụng để kiếm tiền affiliate, giúp tôi lên kế hoạch.

**Turn 2**
> Tôi làm 1 mình, tối khoảng 2 tiếng/ngày, ngân sách 3 triệu cho năm đầu, biết WordPress cơ bản. Thị trường Việt Nam, muốn kiếm từ affiliate Shopee/Lazada/TikTok Shop. Mục tiêu 10 triệu/tháng sau 12 tháng. Cứ chọn phương án bạn thấy hợp nhất và làm tiếp.

*Hidden "wow" opportunities (for the grader):*
- AI-overview / zero-click search eating review traffic, so GEO/AIO optimisation is needed.
- Google's site-reputation and scaled-content policies.
- Affiliate commission caps and cookie windows on Vietnamese platforms.
- A realistic traffic → revenue funnel showing whether 10M/month is plausible.
- Short-video distribution.
- First-hand testing as the moat.
- Disclosure requirements.

---

## Grading rubric (blind A/B; score each 1–10)

1. **Beyond-knowledge insight:** specific, correct, non-obvious points this user probably did not know. List them.
2. **Correctness:** penalise wrong or unverifiable factual claims, especially legal, tax or platform claims.
3. **Fit:** after Turn 2, does the answer match what this user actually said, including budget, skills and phone use?
4. **Progress:** how far toward a usable result after 2 turns? Count real artifacts and concrete next steps.
5. **Friction:** effort the user must spend reading or answering. Higher means less friction.
6. **Wow (overall):** which one would make this user say "wow, I would not have gotten this by myself"?
