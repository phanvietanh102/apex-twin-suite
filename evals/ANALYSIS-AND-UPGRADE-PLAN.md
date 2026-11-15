# Phân tích toàn diện & Kế hoạch nâng cấp APEX (sau eval run 1–2)

> **Mục đích:** giải thích điểm số đo cái gì, cái gì chưa đo, và so sánh ưu điểm, nhược điểm, đánh đổi của 3 cấu hình (skill v3.7, skill v3.8, không skill). Từ đó đề xuất kiến trúc nâng cấp: bổ sung **tính cầu toàn và toàn diện** mà model mạnh còn thiếu, nhưng không khoá cứng cách model suy nghĩ.

---

## 1. Điểm số đại diện cho tiêu chuẩn nào?

Mỗi case được một người chấm độc lập (Opus 5.5) chấm mù A/B. Có 6 tiêu chí, thang 1–10, tối đa 60 điểm/case.

| # | Tiêu chí | Câu hỏi người chấm trả lời | Bằng chứng người chấm phải kiểm |
| :--- | :--- | :--- | :--- |
| 1 | **Insight vượt hiểu biết** | Có điểm nào cụ thể, đúng, không hiển nhiên, mà người dùng gần như chắc chắn chưa biết? | Liệt kê top 3 mỗi bên. Đối chiếu với checklist "cơ hội wow ẩn" (case 1, 3) hoặc "lỗi cài sẵn" (case 2). |
| 2 | **Độ đúng** | Có khẳng định nào sai hoặc không kiểm chứng được, nhất là luật, thuế, phí sàn? | Tính lại mọi phép toán. Đối chiếu nghị định. Gắn cờ "chính xác giả". |
| 3 | **Khớp ràng buộc** | Lượt 2 có bám đúng cái người dùng nói (ngân sách, kỹ năng, điện thoại, quy mô)? | So từng ràng buộc người dùng nêu. |
| 4 | **Tiến độ** | Sau 2 lượt có gì dùng được thật? | **Chạy code/test** trên bản sao, xuất PDF thật, kiểm file hoá đơn cũ bằng SHA-256. |
| 5 | **Ít ma sát** | Người dùng phải đọc, trả lời, cài đặt bao nhiêu? (10 = rất nhẹ) | Số câu hỏi, độ dài, số bước cài, có phải cài Python hay không. |
| 6 | **Wow tổng thể** | Người dùng có nghĩ "tự mình sẽ không có được cái này" không? | Tổng hợp cảm nhận dựa trên 1–5. |

### Những gì điểm số CHƯA đo, mà lại là lý do tồn tại của skill

| Giá trị cốt lõi skill hứa | Eval hiện tại đo chưa? | Hệ quả |
| :--- | :--- | :--- |
| Bền 12 tháng: đổi giá, thêm kênh, đổi luật mà không viết lại | ❌ Không có kịch bản "tháng thứ 3 có biến" | Lợi thế kiến trúc của skill gần như vô hình |
| Toàn diện: không bỏ sót yêu cầu nào | ◐ Chỉ đo gián tiếp qua checklist 7–9 mục | Mẫu nhỏ, chưa đo tỉ lệ bao phủ yêu cầu |
| Dự án nhiều phiên, không quên quyết định cũ | ❌ Chỉ có 2 lượt | Giá trị của STATE.json và ledger chưa được thử |
| Cải tiến liên tục workflow đang chạy | ❌ | Chưa có tình huống "đã tốt rồi, làm tốt hơn nữa" |
| Hoạt động trên Gemini Argon | ❌ | Chưa biết |
| Việc quan trọng nhất của người dùng | ◐ 3 tình huống thật nhưng ngắn | Đề bài còn gần với "task thường" |

**Kết luận về độ tin cậy:**
- Cùng một output (bản không skill) được 145 điểm ở lần chấm 1 và 131 ở lần chấm 2. Nhiễu khoảng ±7 điểm mỗi case.
- Chênh lệch 3–7 điểm mỗi case **không đủ** để kết luận "vượt trội". Bạn nhận xét đúng.
- Muốn chứng minh vượt trội cần eval v2 (mục 5): đề bài đúng tầm việc quan trọng, có kịch bản thay đổi, và nhiều lần chạy.

---

## 2. So sánh toàn diện 3 cấu hình (dựa trên 6 báo cáo chấm)

### 2.1 Bảng điểm theo tiêu chí (cộng 3 case, tối đa 30)

| Tiêu chí | v3.7 (run 1) | Không skill (run 1) | v3.8 (run 2) | Không skill (chấm lại ở run 2) |
| :--- | :---: | :---: | :---: | :---: |
| Insight | **23** | 22 | **26** | 19 |
| Độ đúng | 22 | **24** | **25** | 23 |
| Khớp ràng buộc | 21 | **27** | **26** | 24 |
| Tiến độ | 20 | **25** | **26** | 23 |
| Ít ma sát | 14 | **24** | 19 | **22** |
| Wow | 20 | **23** | **26** | 20 |
| **Tổng** | 120 | **145** | **148** | 131 |

### 2.2 Bao phủ checklist ẩn (đây là thước đo "toàn diện" gần nhất)

| Case | v3.7 | Không skill | v3.8 |
| :--- | :--- | :--- | :--- |
| 1. App đơn hàng (7 mục) | ~6/7 nhưng **bỏ sót Shopee = 70% đơn** | 5/7 (run 1); 5 + ½ (run 2), **bỏ mất lô/HSD dù đã hỏi** | **6 + ½ /7** |
| 2. Báo giá (9 lỗi cài) | 7,5/9 | 7,5/9 | **9/9** |
| 3. Affiliate (9 mục) | 8,5/9 | 7,5/9 (run 1); 7 + 2½ (run 2) | **9/9** |

### 2.3 Ưu điểm, nhược điểm, đánh đổi

| | **Không skill** (Opus 5.5 trần) | **v3.7** (quy trình cứng) | **v3.8** (gọn, ưu tiên giá trị) |
| :--- | :--- | :--- | :--- |
| ✅ **Ưu điểm** | Nhanh, gọn, ít ma sát (24/30 ở run 1). Làm ngay khi được giao. Chọn công cụ quen thuộc (Sheets, plugin WordPress, không phải cài gì). | Phát hiện điểm mù sâu (phần thô báo giá thấp, AI Overviews, link chết). Kỹ thuật kỹ (lô/HSD, dán lại sao kê an toàn). | **Toàn diện nhất** (9/9, 9/9, 6,5/7). Insight đúng luật hiện hành (VAT 8% đến hết 2026, NĐ 70/2025, NĐ 117/2025). Luôn ship test (18+13, 10, 22). Có backup, khoá file hoá đơn cũ. Tìm ra góc độc đáo (tiền điện theo bậc EVN). |
| ⚠️ **Nhược điểm** | **Bỏ sót im lặng**: hỏi về lô/HSD rồi bỏ; có lần không có test. Có chỗ sai luật (ghi VAT 8% là "từng có"). Ý tưởng chung chung hơn. Bỏ qua một số rủi ro tiền bạc. | Ép hỏi thêm khi người dùng đã giao quyền. Thuật ngữ và điểm tự chấm lọt ra ngoài. 7 file tiếng Anh trong workspace. **Bỏ mất luồng chính** (Shopee). Tốn 2 lần token, 3 lần thời gian. | Vẫn dài. Bắt người mới cài Python (case 3, ma sát 5/10). Câu hỏi lượt 1 còn rộng, khó trả lời (case 2). Vài lỗi lặt vặt (đường dẫn sai, tiêu đề lệch năm). Tốn khoảng 1,4 lần token. |
| ⚖️ **Đánh đổi** | Tốc độ và sự dễ chịu, đổi lấy độ sâu và độ toàn diện. | Độ sâu, đổi lấy sự tôn trọng người dùng và tiến độ. | Độ toàn diện và kiểm chứng, đổi lấy độ dài và gánh nặng cài đặt. |
| 🎯 **Hợp nhất khi** | Việc nhỏ, cần nhanh, người dùng tự biết mình cần gì. | (Không nên dùng nữa.) | **Việc quan trọng nhất của người dùng**, nơi một lỗi bỏ sót tốn tiền thật: báo giá, thuế, dữ liệu khách. |

### 2.4 Bài học then chốt

1. **Model mạnh không thiếu thông minh, mà thiếu sự kiên trì rà soát.** Bản không skill *biết* lô/HSD (đã hỏi), *biết* VAT 8%, nhưng không mang chúng tới cuối cùng. Đúng như bạn nhận định: model thiếu tính cầu toàn và toàn diện.
2. **Quy trình cứng không sửa được điều đó, còn làm tệ hơn** (v3.7 bỏ sót cả Shopee). Thứ sửa được là **rà soát bao phủ và truy vết yêu cầu tới cuối cùng**. v3.8 thắng chủ yếu nhờ "biggest flow first", "honest certainty" và test.
3. **Ma sát là điểm yếu còn lại.** Người dùng quan trọng thường bận. Kết quả phải đến tay họ trên nền tảng họ đã có, kèm một bản tóm tắt ngắn.

---

## 3. Nguyên tắc thiết kế cho bản nâng cấp (v4)

> **"Tự do trong cách nghĩ, nghiêm ngặt trong độ bao phủ và bằng chứng."**

Skill không quy định *các bước suy nghĩ*. Nó quy định 3 thứ model hay làm thiếu:

| Lớp | Skill cung cấp | Model tự do quyết định |
| :--- | :--- | :--- |
| **Bao phủ (Completeness)** | Bộ "lăng kính rà soát" kiểu checklist DO-CONFIRM: làm xong mới rà, không bắt làm theo thứ tự | Cách phân tích, thứ tự, kiến trúc, công nghệ |
| **Truy vết (Traceability)** | Sổ truy vết: mọi yêu cầu người dùng nêu và mọi nhu cầu phát hiện ra đều phải có trạng thái cuối (đã làm và test / hoãn có lý do) | Làm yêu cầu nào trước, làm thế nào |
| **Bằng chứng (Proof)** | Định nghĩa "xong" theo loại sản phẩm, cộng các kịch bản thay đổi 12 tháng **chạy được như test** | Viết test gì, công cụ gì |

Cộng thêm hai yếu tố hỗ trợ:
- **Kiến thức ngành có ngày kiểm chứng** (thứ model hay sai hoặc hay quên).
- **Ngân sách ma sát** (giao kết quả trên nền tảng người dùng đã có, kèm tóm tắt 10 dòng).

---

## 4. Kế hoạch nâng cấp chi tiết

### 4.1 Lớp bao phủ: `references/07-completeness-lenses.md` (có ở cả 2 skill)

12 lăng kính để rà **sau khi** làm xong bản nháp. Chỉ ghi ra những lăng kính có phát hiện.

1. Dòng tiền: thu, chi, công nợ, hoàn tiền, làm tròn, kiểu số tiền.
2. Pháp lý, thuế, nền tảng: luật hiện hành kèm ngày kiểm chứng, nghĩa vụ hoá đơn, khấu trừ thuế, điều khoản sàn.
3. Mọi kênh, vai trò, thiết bị: luồng nào chiếm nhiều khối lượng nhất, ai dùng, dùng trên máy gì.
4. Vòng đời dữ liệu: nhập, sửa, lịch sử bất biến, sao lưu, xoá, quyền riêng tư.
5. Lỗi và ngoại lệ: nhập sai, trùng, thiếu, mất mạng, phụ thuộc bên ngoài chết.
6. Lạm dụng và bảo mật: chèn công thức, lộ dữ liệu, quyền truy cập.
7. Quy mô và chi phí: tới mức nào thì cần nâng cấp.
8. Vận hành con người: thói quen hằng ngày, người mới vào, người nghỉ việc.
9. Thay đổi 12 tháng: giá, luật, kênh mới, mùa vụ, tăng khối lượng.
10. Học và dùng: thiết lập trong N bước, không cài đặt nếu có thể.
11. Đo lường: chỉ số nào cho thấy sản phẩm đang tốt lên hay xấu đi.
12. Đặc thù ngành: lấy từ bộ kiến thức ngành.

### 4.2 Lớp truy vết: `TRACE.md` + kiểm bằng script

- Bảng: `ID | Yêu cầu / nhu cầu | Nguồn (người dùng nói / phát hiện) | Trạng thái (Làm-Test / Hoãn-Lý do / Bỏ-Người dùng đồng ý) | Bằng chứng`.
- Khi bàn giao, cho người dùng xem một bảng ngắn: "Bạn yêu cầu → nằm ở đâu, đã kiểm chưa".
- `fitness_audit.py` / `review_gate_audit.py` chặn nếu còn dòng không có trạng thái cuối, hoặc dòng "Làm" mà không có bằng chứng.
- Hai lỗi đã gặp sẽ bị chặn cứng: bỏ lô/HSD sau khi hỏi, và bỏ luồng Shopee.

### 4.3 Lớp bằng chứng: `references/08-definition-of-done.md` + kịch bản thay đổi

**Định nghĩa "xong" theo loại sản phẩm:**
- App/tool:
  - test pass;
  - chạy trên môi trường của người dùng;
  - thiết lập tối đa 10 bước;
  - có backup;
  - luồng lớn nhất hoạt động.
- Workflow: so sánh trước/sau bằng số liệu (phút/việc, tỉ lệ lỗi, tiền rò rỉ).
- Kế hoạch: phép tính kiểm lại được, mốc có hành động "nếu không đạt thì…".

**Kịch bản 12 tháng thành test:** ít nhất 3 kịch bản "tháng 3, 6, 12" theo ngành, chạy được như test. Ví dụ: đổi giá thép, sao cho báo giá cũ giữ nguyên số; thêm kênh TikTok Shop; thay đổi thuế suất. STATE.json lưu kết quả các kịch bản này.

### 4.4 Kiến thức ngành cho MỌI lĩnh vực: giao thức hồ sơ ngành (`09-domain-discovery-protocol.md`) ✅ đã làm

> **Điều chỉnh theo phản hồi:** skill là khung tổng quát cho mọi ngành, quốc gia và hoàn cảnh, kể cả việc cá nhân. 3 tình huống eval chỉ là mẫu thử. Vì vậy **không** viết sẵn bộ kiến thức cho vài ngành, vì làm thế vừa khớp đề vừa nhanh lỗi thời.

Thay vào đó, model **tự dựng hồ sơ ngành** cho đúng bối cảnh người dùng:
- lĩnh vực và khu vực pháp lý;
- chuỗi giá trị;
- mô hình tiền và định mức;
- luật kèm số hiệu, ngày và mức chắc chắn;
- **checklist của người 15 năm trong nghề**;
- kiểu thất bại và mùa vụ;
- công cụ ngành đang dùng;
- những gì cần xác minh.

Hồ sơ này cấp dữ liệu cho phát hiện ở lượt 1, lăng kính 12 và các kịch bản thay đổi. 7 nhóm ngành cũ trong `02-*` chuyển thành ví dụ về độ sâu cần đạt, không còn là giới hạn. `--domain` của script nhận tên lĩnh vực viết tự do (ví dụ "phòng khám nha khoa, Đà Nẵng").

### 4.5 Ngân sách ma sát và chọn nền tảng giao hàng

- Mỗi câu trả lời mở đầu bằng **tóm tắt tối đa 10 dòng**: phát hiện chính, đã làm gì, bạn cần làm gì tiếp. Chi tiết để trong file.
- Ưu tiên nền tảng người dùng đã có: Sheets/Apps Script, Excel, web tĩnh, plugin sẵn. Chỉ yêu cầu cài Python/Node khi người dùng là người kỹ thuật hoặc không có cách nào khác, và khi đó phải có file `.bat` chạy một chạm.
- Câu hỏi phải **trả lời được trong 1 dòng**, có ví dụ câu trả lời mẫu.

### 4.6 Chế độ "Cải tiến liên tục" cho reviewer

Dành cho trường hợp "workflow tưởng đã tốt nhưng vẫn có thể tốt hơn mỗi ngày":
- Đo baseline: phút/việc, số lỗi/tháng, tiền rò rỉ.
- Xếp hạng cải tiến theo ROI.
- Thêm chỉ số đo vào chính workflow.
- Sổ cải tiến `IMPROVEMENT-LOG.md`.
- Prompt tái kiểm hằng quý, so sánh với baseline.

### 4.7 Dọn dẹp repo

- Đưa `commands/` vào repo (các lệnh `/apex`, `/review-product`… theo v4) để người cài plugin có đủ lệnh.
- Đồng bộ phiên bản thành 4.0.0 trên mọi manifest.
- Script build lại `dist/`.
- Cập nhật README theo kết quả eval thật.

---

## 5. Eval v2: đo **tính tổng quát** và đúng tầm "việc quan trọng nhất"

**Nguyên tắc chống khớp đề:** bộ eval phải là **mẫu ngẫu nhiên từ một kho tình huống đa dạng**, gồm nhiều ngành, nhiều quốc gia, có cả việc cá nhân, và có cả tiếng Việt lẫn tiếng Anh. Một phần tình huống được **giữ kín** (không dùng khi thiết kế skill) để đo skill trên bối cảnh nó chưa từng thấy.

Kho tình huống đề xuất (khoảng 12). Mỗi lần chạy bốc ngẫu nhiên 4–5 tình huống, trong đó ít nhất 2 thuộc phần giữ kín:

| # | Bối cảnh | Loại | Ngôn ngữ / quốc gia |
| :--- | :--- | :--- | :--- |
| 1 | Phòng khám nha khoa gia đình muốn số hoá lịch hẹn và hồ sơ | Ý tưởng → sản phẩm | VI / Việt Nam |
| 2 | Hợp tác xã nông nghiệp quản lý thu mua và chia lợi nhuận xã viên | Workspace đang chạy | VI / Việt Nam |
| 3 | Trung tâm dạy thêm 120 học sinh, Excel học phí đang rối | Review và cải tiến liên tục | VI / Việt Nam |
| 4 | Tổ chức đám cưới 300 khách, ngân sách giới hạn | Dự án vật lý / sự kiện | VI / Việt Nam |
| 5 | Indie developer ra mắt SaaS B2B nhỏ | Ý tưởng → sản phẩm | EN / quốc tế |
| 6 | Small bakery in Germany, ordering and allergen compliance | Workspace đang chạy | EN / EU |
| 7 | Nonprofit quản lý tình nguyện viên và quyên góp | Ý tưởng → sản phẩm | EN / US |
| 8 | Kế hoạch tài chính cá nhân và đầu tư cho gia đình trẻ | Mục tiêu cá nhân | VI |
| 9 | Xưởng may 40 công nhân, quản lý đơn gia công | Workspace đang chạy | VI / Việt Nam |
| 10 | Luận văn thạc sĩ: thu thập dữ liệu và kế hoạch phân tích | Nghiên cứu | VI hoặc EN |
| 11 | Homestay 6 phòng, đặt phòng qua nhiều OTA | Workspace "đã ổn", làm tốt hơn | VI / Việt Nam |
| 12 | Văn phòng luật nhỏ, quản lý hồ sơ vụ việc và thời hạn | Ý tưởng → sản phẩm | EN / UK |

| Thay đổi | Lý do |
| :--- | :--- |
| Tình huống **dài**, 4–5 lượt, có **biến cố giữa chừng** phù hợp từng bối cảnh (giá tăng, luật đổi, thêm kênh, mất nhân sự) | Đo độ bền 12 tháng và khả năng xử lý thay đổi |
| Mỗi tình huống có checklist ẩn 15–25 mục, chia theo 12 lăng kính, do người soạn đề viết **trước** và không cho skill thấy | Đo **tỉ lệ bao phủ** (recall), không chỉ cảm nhận |
| Chỉ số khách quan: % lỗi tìm ra, % yêu cầu được truy vết tới cuối, % test pass, số kịch bản thay đổi sống sót, số bước thiết lập, số từ, token | Giảm phụ thuộc vào chấm chủ quan |
| 3 lần chạy mỗi cấu hình, 2 người chấm, đảo vị trí A/B | Hạ nhiễu ±7 xuống mức tin được |
| Thêm 1 tình huống "workflow đang chạy tốt, làm tốt hơn" | Đúng với mục đích cải tiến liên tục |
| Chạy trên cả Opus 5.5 và Argon | Đúng với nền tảng người dùng dùng |

**Chi phí ước tính:** khoảng 2–3 triệu token cho một vòng đầy đủ trên Claude. Có thể chạy bản rút gọn (1 lần chạy, 2 người chấm) trước.

---

## 6. Thứ tự thực hiện

1. ✅ 12 lăng kính (`07`), truy vết, định nghĩa "xong" và kịch bản thay đổi (`08`), ngân sách ma sát: đã đưa vào cả 2 SKILL.md (v4.0).
2. ✅ Chế độ cải tiến liên tục (`10`, reviewer, lệnh `/apex-improve`).
3. ✅ Giao thức hồ sơ ngành cho mọi lĩnh vực (`09`); `--domain` nhận tên lĩnh vực viết tự do.
4. ✅ Script gate kiểm `TRACE.md` (gate 5–6) và đủ 3 kịch bản thay đổi (gate 6). Bộ kiểm thử 25/25 qua.
5. ⏳ Dọn dẹp repo: đưa `commands/` vào, đồng bộ phiên bản 4.0.0, build lại dist, cập nhật README.
6. ⏳ Eval v2 lấy mẫu ngẫu nhiên từ kho tình huống ở mục 5, so với v3.8 và bản không skill.
