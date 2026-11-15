Cảm ơn anh Vinh, như vậy là đủ rõ rồi. Mình chốt phương án và đã làm xong phần chính.

## Phương án mình chọn: nâng cấp Google Sheet hiện tại, chi phí 0đ, xong trước Noel

**Lý do:**
- Chị Thảo vẫn dùng Google Sheet trên điện thoại như hiện nay.
- Không cần biết code. Script của em Duy được thay bằng công thức có sẵn trong Sheet, nên không ai phải chạy Python nữa.
- Không đụng vào giá trên Booking hay Agoda.

**Mình chưa đề xuất phần mềm đồng bộ lịch (channel manager) lúc này.** Lý do là cài phần mềm mới ngay trước mùa cao điểm dễ gây lỗi hơn là đỡ lỗi. Kết nối với các sàn cũng có thể ảnh hưởng tới cách đang bán, mà anh muốn giữ nguyên. Sau Tết mình sẽ cùng anh xem có loại nào dưới 500k/tháng không. Mình không tra giá được nên không dám hứa trước.

Phương án này giải quyết 3 nỗi đau của anh như sau:

| Nỗi đau | Giải pháp |
|---|---|
| 1. Trùng phòng | Tab **Lich** dạng lưới ngày × phòng, **tự tô đỏ khi trùng**. Kèm quy trình 3 bước mỗi khi nhận khách trực tiếp (bên dưới) |
| 2. Không biết lời bao nhiêu | Tab **Tong_ket** tự tính doanh thu, hoa hồng, chi phí, lời, công suất và **% đơn đặt trực tiếp** (để theo dõi mục tiêu 40% của anh). Có thêm cột ghi tiền về tài khoản nào |
| 3. Tin nhắn tốn thời gian | 9 mẫu trả lời nhanh để lưu sẵn vào Zalo và Facebook. Mẫu xác nhận đặt phòng có ghi chính sách hủy bằng chữ, để không còn kiểu "nói miệng" |

## Mình đã làm gì

**1. `SuongMai_QuanLy_v1.xlsx`** (nằm trong thư mục homestay), gồm 6 tab:
- **Huong_dan:** cách dùng hằng ngày, viết ngắn.
- **Dat_phong:** gộp cả 2 file CSV cũ thành **một danh sách duy nhất**.
  - Ô trắng là chỗ nhập tay, ô xám tự tính.
  - Kênh, phòng, trạng thái và tài khoản đều chọn từ danh sách. Ngày chọn trên lịch, nên không còn chuyện gõ lẫn "24/12/2026" với "2026-12-24".
  - Cột **CANH_BAO** báo đỏ khi trùng phòng, sai ngày, hoặc đơn Airbnb thiếu số USD.
- **Lich:** lịch từ 01/11/2026 đến 31/03/2027 (đã gồm Tết Nguyên Đán). Ô xanh là có khách, ô đỏ là trùng. Có thêm cột số phòng trả, nhận và còn trống mỗi ngày để chị Thảo nhắn chị Mai.
- **Thu_chi:** đã nhập sẵn chi phí tháng 10.
- **Tong_ket:** tổng kết theo tháng.
- **Cai_dat:** % hoa hồng (Booking 15%, Agoda 15%, Airbnb 3% còn cần kiểm tra), tỷ giá USD, danh sách tài khoản.

**2. `mau_tin_nhan_tra_loi_nhanh.txt`** gồm 9 mẫu: chào khách, báo giá, hướng dẫn cọc kèm chính sách hủy, xác nhận, chỉ đường, khách đến sau 22h, cảm ơn và mời quay lại, hoàn cọc, hết phòng.

**Những gì mình đã tự quyết khi gộp dữ liệu.** Anh xem lại giúp. Các dòng cần xử lý đều có ghi chú trong cột `ghi_chu`.
- **ZL-040:** sửa thành 3 đêm (từ 12 đến 15/12).
- **Chị Ngọc:** để "Hủy", theo tin nhắn.
- **Anh Tùng:** ghi đã cọc 1tr, theo tin nhắn. Anh nên đối chiếu sao kê cho chắc.
- **Đoàn chú Bảy:** tách thành 2 dòng P5 và P6. Mỗi phòng một dòng thì lịch mới tính đúng.
- **FB-019:** đã trừ 10% giảm giá khách quen (140k).
- **Hoa hồng Booking:** tất cả đơn tính 15%.
- **Đơn Airbnb:** tạm quy đổi theo **tỷ giá 26.000**. Khi tiền về Vietcombank, anh ghi số VND thực nhận vào cột `tien_ve_thuc_te`.
- **6 đơn tháng 11:** file cũ ghi "Đã ở" dù chưa tới ngày, mình đổi thành "Xác nhận".
- **BK-4520 (giá 1,2tr hay 1,1tr)** và **AG-9035 (đã hủy thật chưa):** mình chưa biết đúng sai. Mình để ghi chú "KIỂM TRA" để anh xem trên trang của Booking và Agoda.
- **2 vụ trùng phòng:** mình **cố ý để nguyên**, chưa đổi phòng giùm anh, vì còn phải gọi khách trước. Sau khi nhập vào Sheet, anh sẽ thấy ngay 2 ô đỏ.

**File gốc của anh không bị sửa gì.**

## Cách đưa lên Google Sheet (khoảng 15 phút, làm trên laptop)

1. Mở Google Drive, bấm **Mới → Tải tệp lên**, chọn `SuongMai_QuanLy_v1.xlsx`.
2. Bấm đúp vào file, chọn **Mở bằng Google Trang tính**. Sau đó vào **Tệp → Lưu dưới dạng Google Trang tính**.
3. **Kiểm tra xem file đã chạy đúng chưa.** Mình chưa thử được trên Google Sheet thật, nên anh xem giúp 3 điểm sau:
   - Tab Lich: ô **P3 ngày 25/12** và ô **P2 ngày 31/12** phải **màu đỏ, hiện số 2**.
   - Tab Tong_ket, dòng 12/2026, phải ra khoảng: 11 dòng đặt, doanh thu bán **29.588.000**, hoa hồng **1.838.640**, đơn trực tiếp **45%**.
   - Tab Dat_phong: bấm vào ô ngày phải hiện lịch để chọn, bấm vào ô kênh phải hiện danh sách.

   Nếu kết quả không khớp, anh chụp màn hình gửi mình để mình sửa.
4. Chia sẻ file cho chị Thảo với quyền **Người chỉnh sửa**. Từ đó **chỉ dùng file này**, không xuất CSV ra nữa.

## Quy trình chống trùng phòng

Nên dán quy trình này lên tường quầy và gửi chị Thảo.

**Mỗi khi nhận khách Zalo hoặc Facebook:**
1. Mở tab **Lich** và kiểm tra ngày đó còn ô trắng.
2. **Nhập ngay** vào tab Dat_phong, trạng thái "Chờ cọc". Không ghi tạm vào app Ghi chú hay để trong tin nhắn.
3. **Đóng phòng đó** trên app Booking (Pulse) và Agoda (YCS). Riêng P4 thì đóng trên Airbnb.

   Việc này là đóng phòng trống, **không phải đổi giá**, nên không ảnh hưởng thứ hạng như anh lo.

**Mỗi khi có đơn từ các sàn:** nhập vào Sheet trong ngày.

**Mỗi tối:** chị Thảo mở tab Lich, nhìn xem có ô đỏ không, rồi nhắn chị Mai lịch trả và nhận phòng ngày mai.

**Từ 20/12 đến 3/1:** anh kiểm tra thêm một lần mỗi tuần khi lên Đà Lạt.

## Việc anh chị cần tự làm (mình không làm thay được)

**Tuần này:**
- [ ] Gọi **anh Tùng**, đề nghị chuyển sang **P5 hoặc P6** cho đêm 25 đến 27/12 (giữ nguyên giá). Sau đó sửa cột `phong`.
- [ ] Nhắn **chị Đỗ Minh Châu**, chuyển sang **P1** đêm 31/12. Sau đó sửa cột `phong` và **đóng P1 đêm 31/12 trên Booking và Agoda**.
- [ ] **Hoàn 600k cho chị Ngọc** hôm nay. Đã có mẫu `/hoancoc`.
- [ ] Google Drive: chuyển thư mục giấy tờ khách về **"Bị hạn chế"**, rồi chia sẻ riêng cho Gmail của chị Mai.
- [ ] Mở **một tài khoản ngân hàng riêng cho homestay** (thường miễn phí). Từ nay cọc và tiền phòng đều về tài khoản này. Đây là việc quan trọng nhất cho nỗi đau số 2.
- [ ] Trên Agoda: kiểm tra AG-9035. Trên Booking: kiểm tra giá BK-4520.

**Trước 20/12:**
- [ ] Thay bình nóng lạnh P3. Phòng này kín khách từ 24/12 đến 3/1.
- [ ] Đổi giờ nhận phòng trên Airbnb từ 13h thành 14h.
- [ ] Đổi mã hộp khóa. Từ nay chỉ gửi mã cho khách trong ngày khách đến.
- [ ] Kiểm định lại bình chữa cháy.
- [ ] Sắp người dọn phòng ngày 27/12 (Chủ nhật).
- [ ] Chốt chính sách hủy, xem phần [ĐỀ XUẤT] trong file mẫu tin nhắn. Mình gợi ý dịp lễ thì hủy trước 14 ngày mới hoàn cọc. Chính sách mới chỉ áp dụng cho khách đặt từ nay về sau.
- [ ] Sửa bài ghim "rẻ hơn Booking 20%". Câu này không đúng thực tế, và anh lại không muốn đổi giá trên các sàn. Nên đổi thành **ưu đãi khi đặt trực tiếp**, ví dụ nhận phòng sớm, cà phê sáng, giảm 10% cho khách quen và người được giới thiệu. Cách này vẫn kéo khách về Zalo mà không đụng giá trên sàn.

**Sau Tết** (mình làm cùng anh được):
- Xem có channel manager nào dưới 500k/tháng không.
- Hỏi cơ quan thuế về việc bỏ thuế khoán năm 2026. Tab Tong_ket sẽ có sẵn doanh thu để kê khai.
- Hỏi về khai báo lưu trú online.
- Làm hợp đồng cho chị Mai.

**Lưu ý nhỏ:**
- Doanh thu được tính theo **tháng nhận phòng**.
- Tiền điện đang ghi cả phần dùng chung với nhà ở, nên tiền lời sẽ hơi thấp hơn thực tế. Nếu anh ước được homestay dùng khoảng bao nhiêu %, mình chỉnh lại.
- File `tinh_tien.py` cũ không cần dùng nữa.

Anh nhập lên Google Sheet xong, nhờ anh báo lại 3 điểm kiểm tra ở trên có khớp không. Mình sẽ chỉnh tiếp nếu có chỗ nào chưa đúng hoặc chị Thảo thấy khó dùng trên điện thoại.

## Files created
- `homestay_suongmai_dalat/SuongMai_QuanLy_v1.xlsx`: file quản lý mới, để tải lên Google Drive và mở bằng Google Trang tính.
- `homestay_suongmai_dalat/mau_tin_nhan_tra_loi_nhanh.txt`: 9 mẫu tin nhắn trả lời nhanh cho Zalo và Facebook.
- `_build/tao_file_quan_ly.py`: script mình dùng để tạo file xlsx. Anh không cần dùng, chỉ để sau này tạo lại file khi cần.
