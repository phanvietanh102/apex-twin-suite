# Phân tích ngược: bản KHÔNG skill làm được gì mà bản CÓ skill không làm được?

**Nguồn dữ liệu:** 6 báo cáo chấm mù của run 3 (homestay, tiệm bánh ở Đức, HTX cà phê) và run 4 (SaaS, văn phòng luật ở Anh, xưởng may). Mọi mục dưới đây là chỗ bản không skill được chấm **cao hơn** bản có skill, hoặc là ý hay chỉ bản không skill có. Mỗi mục có nguyên nhân gốc và cách sửa. Tất cả cách sửa đều **tổng quát cho mọi ngành**, không viết riêng cho tình huống test.

## Bảng tổng hợp

| # | Thiếu sót của bản có skill (bằng chứng) | Nguyên nhân gốc | Sửa ở đâu (v4.2) |
| :--- | :--- | :--- | :--- |
| 1 | **Bảo vệ dữ liệu cá nhân kém:** CCCD và số tài khoản công nhân nằm trong file lương dùng chung (xưởng may); không có thời hạn lưu hay xoá ảnh CCCD khách, lại gửi CCCD qua Zalo (homestay); không tối thiểu hoá dữ liệu sức khoẻ (tiệm bánh) | **Thiên lệch "giữ nguyên dữ liệu".** Luật Red-Zone ("bảo toàn 100% lịch sử") khiến model sao chép toàn bộ dữ liệu sang sản phẩm mới. Lăng kính 5 chỉ nói chung chung "kept private" | Lăng kính 5: **tối thiểu hoá**. Mọi thứ skill tạo ra chỉ mang dữ liệu cần thiết; định danh nhạy cảm được che hoặc để ở nguồn hạn chế; có quy tắc lưu và xoá. "Giữ lịch sử không phải lý do để lan nó ra" |
| 2 | **Chỉ cảnh báo, không đưa phương án thay thế:** cảnh báo bài quảng cáo "rẻ hơn 20%" có rủi ro nhưng không đưa nội dung thay thế (homestay) | Sổ truy vết coi "đã nêu rủi ro" là xong | Quy tắc **đóng phát hiện**: chỉ coi là xong khi có cách sửa hoặc nội dung thay thế dùng được ngay |
| 3 | **Không soát yêu sách của đối tác:** chấp nhận khoản phạt 12 triệu của khách mà không đối chiếu hợp đồng (882 nghìn) và trần phạt 8% của Luật Thương mại (xưởng may); điều khoản dịch vụ của SaaS không có giới hạn trách nhiệm (SaaS) | Skill chỉ kiểm lỗi **của người dùng**, không kiểm những gì **người khác đòi người dùng**, cũng không kiểm người dùng đã tự bảo vệ chưa | Lăng kính 3 (tiền): **soát cả đối tác**: phạt, phí, khấu trừ đều đối chiếu hợp đồng và trần luật định; kiểm điều khoản, giới hạn trách nhiệm, bảo hiểm của chính người dùng |
| 4 | **Tự chế cách làm thay vì dùng công cụ chuẩn của nghề:** đề xuất "sổ ký tay hằng ngày", trong khi nghề may dùng **phiếu bó** để ghi sản lượng ngay tại chuyền (xưởng may) | Hồ sơ ngành chỉ hỏi "người trong nghề kiểm tra gì", chưa hỏi "nghề này dùng **công cụ** gì cho đúng bước này" | 09: **Công cụ chuẩn của nghề trước**. Với mỗi quy trình lõi, hỏi nghề đã dùng công cụ gì, rồi áp dụng và cải tiến trên đó |
| 5 | **Không kéo theo hệ quả bậc hai của việc sửa:** không hoàn lại BHXH đã trừ sai các tháng trước; không tính chi phí tuân thủ (khoảng 12 triệu/tháng) vào giá báo cho đơn xuất khẩu EU; không họp toàn xưởng trước khi đổi cách tính lương (xưởng may) | Skill sửa lỗi **từ nay về sau**, nhưng không hỏi việc sửa đó ảnh hưởng gì đến quá khứ, giá cả và con người | **Lượt rà hệ quả bậc hai:** kỳ trước (khắc phục hồi tố), chi phí (điều chỉnh giá), con người (báo trước, tin nhắn soạn sẵn) |
| 6 | **Không kiểm tính hợp lý của dữ liệu:** bỏ sót trạng thái "no-show" cho một lượt lưu trú chưa diễn ra, và câu quảng cáo "rẻ hơn 20%" mà chính bảng giá chứng minh là sai (homestay); bỏ sót năng suất 5,7 tấn/ha cao bất thường, "bán vét kho" vượt tồn kho, và xung đột lợi ích khi chủ nhiệm tự duyệt phần chia lãi của mình (HTX) | Lăng kính 6 chỉ nói "lỗi và ngoại lệ", chưa có **soát dữ liệu với chính nó và với định mức của nghề**. Lăng kính 7 chưa có quản trị và xung đột lợi ích | Lăng kính 6: **kiểm hợp lý** (ngày không thể có, trạng thái mâu thuẫn, vượt định mức vật lý, tồn kho không thể có). Lăng kính 7: thêm **xung đột lợi ích** |
| 7 | **Hệ thống không tự bảo vệ chính nó:** không diễn tập kịch bản "luật sư chính nghỉ ốm", không có cảnh báo khi luồng tự động ngừng, quyền xoá quá rộng, luồng gắn với tài khoản cá nhân (văn phòng luật); không chạy song song tuần đầu (SaaS) | Định nghĩa "xong" có test và kịch bản thay đổi, nhưng thiếu **quy trình chuyển đổi** và **tình huống chính hệ thống hỏng** | Định nghĩa "xong" thêm loại "**thay thế quy trình đang chạy**": chạy song song hoặc diễn tập, sở hữu theo vai trò, cảnh báo khi không có hoạt động |
| 8 | *(Đã sửa ở v4.1)* Hoãn tầm nhìn gốc, phụ thuộc 1 laptop, bắt kế toán chỉ biết Excel dùng Python, lỗi `#NAME?` (run 3) | Kẽ hở hoãn trong sổ truy vết; "phải có test" đẩy model sang viết code | v4.1: cấm hoãn mục High và kiểm tra trong ứng dụng thật. Run 4 xác nhận không lặp lại |

## Điều chỉnh theo phản hồi của bạn: cài đặt không phải rào cản

Người dùng repo này biết dùng AI, nên cài Python hay package là một câu lệnh. v4.2 bỏ quy tắc "chỉ viết code nếu người dùng đã chạy code". Tiêu chí mới:
- **Phía agent:** dùng code thoải mái để phân tích, tạo và kiểm tra sản phẩm.
- **Phía người vận hành hằng ngày** (kế toán, lễ tân, tổ trưởng…): sản phẩm phải chạy trong công cụ họ đang dùng (điện thoại, Excel, Outlook, Zalo), và phải được kiểm tra trong chính ứng dụng đó.
- **Cách tốt nhất thường là kết hợp:** dùng code để *dựng và kiểm tra* một file Excel thuần. Người vận hành vẫn dùng Excel, còn người dùng có quy trình tái lập được.

## Ý nghĩa

Bảy thiếu sót trên **không phải thiếu kiến thức**: bản không skill dùng cùng model mà vẫn làm được. Đó là **điểm mù do chính khung quy trình gây ra** (thiên lệch giữ dữ liệu, cảnh báo được coi là xong, chỉ soát người dùng mà không soát đối tác), hoặc **những góc mà khung chưa phủ** (công cụ chuẩn của nghề, hệ quả bậc hai, tính hợp lý của dữ liệu, độ bền của chính hệ thống). v4.2 vá cả hai loại bằng quy tắc tổng quát.

**Chưa được kiểm chứng:** các sửa đổi v4.2 chưa qua eval. Lần eval sau nên bốc tình huống mới và đặt tiêu chí trước: "thiếu sót loại 1–7 không còn xuất hiện ở bản có skill".
