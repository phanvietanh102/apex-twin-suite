Chào bạn, mình đã đọc hết 8 file trong thư mục và chạy thử script tính tiền. Nói thẳng là "đang chạy ổn" chỉ đúng ở bề mặt. Có **2 phòng đang bị bán trùng ngay dịp Noel – Tết Dương**, một khách đang dọa đánh giá xấu, và con số doanh thu script in ra đang sai khá nhiều. Mình xếp theo mức gấp bên dưới.

Mình **không sửa file nào của bạn**. Mình chỉ viết thêm một script kiểm tra (`kiem_tra_dat_phong.py`) để tìm lỗi, và mọi phát hiện bên dưới đều lấy từ kết quả chạy script đó.

---

## 1. Việc gấp, nên xử lý trong tuần này

**a) Trùng phòng P3 đêm 25/12**
- Khách Booking **Phạm Đức Anh (BK-4520)** ở P3 từ 24 đến 26/12.
- Khách Zalo **anh Tùng (ZL-044)** cũng ở P3 từ 25 đến 27/12. Ngày 12/11 chị Thảo đã nhắn xác nhận "25 tới 27" với anh Tùng, và anh ấy đã chuyển 1 triệu.
- Ngày 25/12, P5 và P6 (phòng 4 người) đều còn trống.
- Cách xử lý mình đề xuất: gọi anh Tùng ngay, đề nghị chuyển sang P5 hoặc P6 (rộng hơn, giữ nguyên giá, có thể tặng thêm chút gì đó). Đổi phòng của khách Zalo dễ hơn nhiều so với đổi khách Booking.

**b) Trùng phòng P2 đêm 31/12** (chỉ thấy trong file `final_v2`)
- Khách Agoda **Wang Lei (AG-9101)** ở P2 từ 30/12 đến 2/1.
- Chị Thảo nhận khách Messenger **Đỗ Minh Châu (FB-024)** vào P2 đêm 31/12, khách đã cọc 500k. Đơn này **không có trong `bookings_2026.csv`**.
- Đêm 31/12 thì **P1 còn trống**, cũng là phòng đôi view vườn, nên chuyển chị Châu sang P1.
- Nhớ **đóng P1 đêm 31/12 trên Booking và Agoda**. Nếu không, phòng này có thể bị bán thêm lần nữa.

**c) Chị Ngọc đòi hoàn cọc 600k**
- Chị Ngọc hủy ngày 8/11 cho đêm 1/1, tức báo trước 54 ngày. Theo chính sách chính bạn đã nói với khách ("hủy trước 7 ngày hoàn 100%"), chị ấy được hoàn đủ.
- Thêm nữa, P6 đêm 1/1 **đã bán cho đoàn chú Bảy (P5+P6, 31/12 đến 2/1)**. Nghĩa là nếu chị Ngọc không hủy thì bạn cũng không có phòng cho chị ấy.
- Mình đề xuất hoàn 600k ngay hôm nay kèm một lời xin lỗi vì chậm. 600k rẻ hơn nhiều so với một bài chê trên Google Maps và group Đà Lạt ngay trước mùa cao điểm.

**d) Ảnh CCCD và hộ chiếu đang để công khai**
- Thư mục Drive có khoảng 600 ảnh giấy tờ khách, đang để chế độ "Bất kỳ ai có đường liên kết đều xem được".
- Ai có link là tải được hết. Ảnh CCCD bị lộ thường bị dùng để vay tiền online hoặc lừa đảo, và chủ homestay phải chịu trách nhiệm.
- Việc nên làm hôm nay: chuyển thư mục về "Bị hạn chế", rồi chia sẻ riêng cho Gmail của chị Mai.
- Sau đó nên xóa ảnh của khách đã trả phòng lâu rồi (ví dụ từ năm 2024).

**e) Có 2 file đặt phòng khác nhau, không biết file nào đúng**
- Có 21 chỗ lệch giữa `bookings_2026.csv` và `bookings_2026_final_v2.csv`. Ví dụ:
  - ZL-040: file chính ghi 2 đêm/1,6tr, nhưng 12 đến 15/12 là 3 đêm/2,4tr.
  - BK-4520: một file ghi giá 1,2tr, file kia ghi 1,1tr.
  - Chị Ngọc: một file ghi "Hủy", file kia ghi "Xác nhận".
  - Anh Tùng: một file ghi đã cọc 1tr, file kia ghi "Chờ cọc", cọc 0.
- Trong khi đó script tính tiền và chị Mai lại đọc theo file chính.

## 2. Số doanh thu script đang in ra là sai

Chạy `tinh_tien.py` thì ra tổng **32.150.433đ**. Số lẻ "433" đã cho thấy có vấn đề. Các lỗi mình tìm được:

| Lỗi | Hậu quả |
|---|---|
| Tiền Airbnb ghi bằng USD (95, 128, 210) nhưng bị cộng thẳng như tiền VND | Thiếu khoảng **11 triệu** (433 USD, tính theo tỷ giá khoảng 26.000) |
| AG-9035 ghi trạng thái "Huy" không dấu, script chỉ nhận "Hủy" | Đơn hủy vẫn bị cộng 1,7tr |
| BK-4533 và FB-023 ghi ngày kiểu 24/12/2026 | Doanh thu rơi vào hai "tháng" lạ là `24/12/2` và `12/01/2` |
| Hoa hồng Booking vẫn ghi 12%, trong khi từ 1/7/2026 là 15% (ghi chú cũng nói "CHƯA SỬA") | Hoa hồng bị tính thiếu khoảng 340k trên các đơn Booking trong file |
| Giảm 10% cho khách quen phải trừ tay (FB-019 ghi "chưa trừ") | Doanh thu bị tính dư |
| Công suất phòng chia cố định cho 180 đêm và tính theo tháng nhận phòng. Đoàn P5+P6 chỉ được tính là 1 phòng | Tỷ lệ lấp đầy không đúng |

Bên chi phí cũng ghi "Hoa hồng OTA tự trừ – không ghi" và "phí đổi ngoại tệ không rõ". Vì vậy hiện tại **bạn chưa biết thực sự mỗi tháng lời bao nhiêu**.

## 3. Nên làm trước 24/12

- **Bình nóng lạnh P3:** thợ đã khuyên thay, bạn định để sau Tết. Nhưng P3 kín khách từ 24/12 đến 3/1, Đà Lạt tháng 12 lại lạnh. Thay ngay với giá 4,5tr vẫn rẻ hơn mấy review 1 sao trên Booking.
- **Phòng P2 từ 5 đến 7/12 (AG-9035):** cần kiểm tra trên trang quản lý Agoda xem đơn này đã hủy thật chưa. Đây là loại không hoàn hủy, nên có thể bạn vẫn được Agoda trả tiền. Nếu đã hủy thì phòng đang trống vào cuối tuần, mở bán lại được. Ghi chú "no-show" cũng lạ, vì ngày nhận phòng còn chưa tới.
- **Airbnb:** đổi giờ nhận phòng từ 13h thành 14h. Đồng thời kiểm tra lại phí host 3% bằng cách mở một lần chi trả cụ thể.
- **Mã hộp khóa 2580:** mã này chưa đổi từ 03/2025 và đang ghi trong file text. Nên đổi mã.
- **Bình chữa cháy:** hạn kiểm định ghi năm 2024, đã quá hạn.
- **Ngày 27/12 là Chủ nhật,** chị Mai nghỉ. Hôm đó có 2 phòng trả (P4 và P3, hoặc P5/P6 nếu anh Tùng đổi phòng). Nên sắp xếp người dọn từ bây giờ.

## 4. Những điều nên hỏi lại cho chắc

Phần này mình không phải luật sư hay kế toán. Đây là các điểm mình thấy **có khả năng đang làm sai quy định**, bạn nên xác nhận với cơ quan liên quan:
- **Thuế:** theo mình biết, từ 2026 hộ kinh doanh bỏ thuế khoán và chuyển sang tự kê khai theo doanh thu thật. Ghi chú của bạn nói "chưa làm gì", trong khi đã gần hết năm 2026. Nên hỏi cơ quan thuế ở phường hoặc một kế toán dịch vụ sớm. Nếu được xuất hóa đơn thì cũng trả lời được chuyện khách xin hóa đơn công ty.
- **Khai báo lưu trú:** khách nước ngoài thường phải khai báo trong khoảng 12 giờ, việc "sáng hôm sau mới gửi" có thể bị trễ. Theo mình hiểu, Luật Cư trú cũng yêu cầu thông báo lưu trú cho **cả khách Việt Nam**. Nên hỏi anh Tuấn cách khai báo online cho chuẩn.
- **Chị Mai:** chị làm 6 ngày một tuần nhưng không có hợp đồng. Nên hỏi về hợp đồng lao động và bảo hiểm xã hội.
- **Bài ghim "Rẻ hơn Booking/Agoda 20%":** dữ liệu thực tế không đúng như vậy. P2 đêm 31/12 khách Agoda và khách Messenger cùng giá 1,3tr. P3 khách Zalo chỉ rẻ hơn khoảng 8%. Khách so giá thì sẽ thấy ngay. Hợp đồng với các sàn cũng thường có điều khoản cấm quảng cáo giá rẻ hơn công khai. Ngoài ra, bài ghim nói "khách quen không cần cọc", trong khi chính sách lại là cọc 50%.

## 5. Gốc rễ của vấn đề

Hầu hết lỗi ở trên xuất phát từ cùng vài nguyên nhân:

1. **Có nhiều chỗ ghi đặt phòng:** Sheet, file `final_v2`, Messenger, Zalo và app Ghi chú. Khách Zalo/FB không được nhập vào cùng một chỗ với khách từ các sàn.
2. **Không có lịch xem theo phòng và theo ngày,** nên không thấy được phòng nào đã bán trùng.
3. **Tiền cọc chảy vào tài khoản cá nhân dùng chung tiền chợ, tiền học con.** Sổ cọc nằm trong app Ghi chú. Cuối tháng phải đọc lại tin nhắn để cộng.
4. **Chính sách chỉ "nói miệng",** nên khi có tranh chấp như vụ chị Ngọc thì không có căn cứ.

Hướng cải thiện mình đề xuất, từ đơn giản đến đầy đủ:
- **Bước 1 (gần như miễn phí):**
  - Chốt **một** Sheet duy nhất.
  - Thêm tab lịch dạng lưới phòng × ngày, tự tô đỏ khi trùng phòng.
  - Đặt danh sách chọn sẵn cho trạng thái, kênh, phòng, và định dạng ngày.
  - Thêm cột "tiền thực về (VND)".
  - Viết lại script tính tiền cho đúng.
  - Mở một tài khoản ngân hàng riêng cho homestay.
  - Đăng chính sách hủy và cọc thành văn bản.
- **Bước 2 (nếu muốn):** dùng phần mềm quản lý kèm đồng bộ lịch giữa các sàn (channel manager). Với 6 phòng bán trên 5 kênh như bạn, loại phần mềm này sinh ra để chặn đúng kiểu trùng phòng ở trên.

---

## Mình cần bạn trả lời vài câu để làm tiếp

1. Hiện tại **file nào là bản đúng**, `bookings_2026.csv` hay `final_v2`? Hay Google Sheet gốc đang khác cả hai?
2. Anh Tùng đã thực sự chuyển 1 triệu cọc chưa? (Hai file ghi khác nhau.)
3. Với đơn Airbnb, bạn muốn ghi **số VND thực tế về Vietcombank** (chính xác nhất) hay quy đổi theo một tỷ giá cố định?
4. "Tốt hơn" với bạn là gì nhất: **bớt sót, bớt trùng phòng**, **số liệu lời/lỗ rõ ràng** (và để làm thuế), hay **tăng doanh thu**?
5. Ai sẽ dùng hệ thống hằng ngày? Chị Thảo dùng trên điện thoại hay máy tính? Bạn có sẵn sàng trả phí hằng tháng cho phần mềm không?

Trong lúc chờ, bạn có thể tự kiểm tra bất kỳ lúc nào bằng lệnh:
`python kiem_tra_dat_phong.py bookings_2026.csv bookings_2026_final_v2.csv`
Script sẽ in ra các phòng trùng, ngày sai định dạng, số đêm hoặc tổng tiền lệch, và những chỗ khác nhau giữa 2 file.

## Files created
- `homestay_suongmai_dalat/kiem_tra_dat_phong.py`: script chỉ đọc, kiểm tra trùng phòng, số đêm và tổng tiền, định dạng ngày, trạng thái lạ, hoa hồng Booking, và so sánh 2 file CSV. Không ghi đè file nào.
