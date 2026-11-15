Chào bạn, mình đã đọc hết 8 file trong `homestay_suongmai_dalat`, chạy thử `tinh_tien.py` và tự tính lại từng booking. Mình **chưa sửa, chưa di chuyển, chưa tạo file nào** trong thư mục của bạn.

**Tóm tắt nhanh**
1. **Có 2 phòng bị bán trùng đúng dịp cao điểm:** P3 đêm 25/12 và P2 đêm 31/12. Cả hai khách bị trùng đều đã chuyển cọc. Còn 41 ngày nữa là tới Noel, vẫn kịp xếp lại phòng.
2. **Chị Ngọc đang chờ hoàn cọc 600k và hôm qua đã dọa đánh giá xấu.** Theo chính sách bạn đã nói với khách thì homestay phải hoàn. Thêm nữa, đêm đó P6 đã bán cho đoàn chú Bảy từ trước.
3. **Script tính tiền đang báo thiếu khoảng 1/3 doanh thu.** Tiền Airbnb tính bằng USD bị cộng như tiền đồng, ngày nhập sai định dạng bị tách thành "tháng lạ", và hoa hồng Booking vẫn tính 12% thay vì 15%. Riêng tháng 12, doanh thu thật khoảng 29–30 triệu, script chỉ báo 18 triệu.
4. **Có 2 file đặt phòng lệch nhau ở 8 booking, và không file nào đầy đủ.**
5. **Ảnh CCCD/hộ chiếu của khách đang để công khai theo link, và mã hộp khóa 20 tháng chưa đổi.** Ngoài ra khai báo lưu trú đang chậm hoặc thiếu.
6. **Thuế 2026 chưa làm gì từ khi bỏ khoán**, mà năm 2026 sắp hết.

---

## Những điều mình tìm thấy (xếp theo mức rủi ro về tiền, dữ liệu và an toàn)

### 1. Bán trùng phòng dịp Noel và Tết Dương lịch
| Đêm | Phòng | Khách A | Khách B | Phòng còn trống đêm đó |
|---|---|---|---|---|
| 25/12 (T6) | P3 | BK-4520 Phạm Đức Anh (Booking, 24–26/12) | ZL-044 Anh Tùng (Zalo, 25–27/12, **đã CK 1 triệu**, chị Thảo xác nhận "phòng gia đình có ban công" ngày 12/11) | P2, P5, P6 |
| 31/12 (T5) | P2 | AG-9101 Wang Lei (Agoda, 30/12–2/1) | FB-024 Đỗ Minh Châu (Messenger 9/11, **cọc 500k**). Booking này **chỉ có trong `bookings_2026_final_v2.csv`**, file chính không có | P1, P3, P4 |

- **Bằng chứng:**
  - `bookings_2026.csv` dòng 13 và 15.
  - `bookings_2026_final_v2.csv` dòng 9, 10 và 11.
  - `lich_don_phong.txt` dòng 11 có ghi "?? hỏi lại", và lịch ngày 31/12 không có ai nhận P1.
- **Thiệt hại nếu để nguyên:** có khách tới nơi mà không có phòng đúng đêm lễ. Với khách đặt qua OTA, homestay thường phải tự lo phòng thay thế và có thể bị phạt hoặc tụt hạng (điều khoản cụ thể cần kiểm trong hợp đồng Booking). Với khách Zalo/FB thì phải hoàn tiền và gần như chắc chắn nhận đánh giá xấu.
- **Đề xuất (bạn làm được ngay, không cần chờ mình):**
  - Chuyển chị Châu sang **P1**, cùng loại phòng đôi view vườn.
  - Gọi anh Tùng, mời sang **P5 hoặc P6** (phòng 4 người, rộng hơn) với giá cũ. Hai phòng này không có ban công, nên cần nói rõ với anh.
  - Không nên đổi khách đặt qua Booking.
- **Nguyên nhân gốc:** khi nhận khách qua Zalo/FB, không có bước nào kiểm tra phòng còn trống hoặc đóng phòng trên Booking/Agoda.

### 2. Chị Ngọc (ZL-049) chờ hoàn 600k, đã 6 ngày
- **Diễn biến:** chị hủy lúc 20:14 ngày 08/11 cho đêm 1/1, tức là **trước 54 ngày**. Chính sách bạn nói với khách là "hủy trước 7 ngày hoàn 100%" (`gia_phong_va_chinh_sach.txt` dòng 24). Ý "dịp lễ khỏi hoàn" (`tin_nhan_coc_hoan.txt` dòng 7) chưa bao giờ được báo cho khách. Ngày 13/11 chị nhắn sẽ đánh giá lên Google Maps và group Đà Lạt.
- **Thêm một điểm quan trọng:** đêm 1/1, phòng P6 **đã bán cho đoàn chú Bảy (ZL-047, P5+P6, 31/12–2/1)** từ trước. Nghĩa là dù chị Ngọc không hủy thì homestay cũng không có phòng cho chị. Giữ cọc trong trường hợp này rất khó bảo vệ.
- **Đề xuất:** hoàn 600k hôm nay, kèm một tin nhắn xin lỗi ngắn. Mất 600k vẫn rẻ hơn một bài đánh giá xấu ngay trước mùa cao điểm.

### 3. `tinh_tien.py` báo 32,15 triệu, con số thật khoảng 44 triệu
Kết quả chạy script: tổng `32,150,433`, trong đó có 2 "tháng" lạ là `24/12/2` và `12/01/2`.

| Lỗi | Bằng chứng | Ảnh hưởng |
|---|---|---|
| Tiền Airbnb tính bằng USD bị cộng như VND | `tinh_tien.py` dòng 17. Các booking AB-2210, AB-2244, AB-2291 có `tong_tien` lần lượt là 95, 128 và 210 | 433 USD bị tính thành 433đ, **thiếu khoảng 10,8–11,3 triệu** (tỷ giá 25–26k; số chính xác lấy theo sao kê VCB) |
| Ngày nhập dạng dd/mm/yyyy | BK-4533 (dòng 14), FB-023 (dòng 20) | Tháng 12 thiếu 2,4 triệu, tháng 1 thiếu 1,4 triệu |
| Số đêm sai | ZL-040 ở 12→15/12 là 3 đêm, file ghi 2 | Thiếu 800k (file v2 thì ghi đúng) |
| Hoa hồng Booking vẫn 12% (chưa sửa, như ghi chú dòng 12–13 đã nhắc) | 6 booking Booking, tổng 11,35 triệu | **Báo thiếu hoa hồng 340.500đ** |
| Giảm giá khách quen chưa trừ | FB-019 "chưa trừ" | Báo dư 140k |
| Trạng thái gõ "Huy" thay vì "Hủy" | AG-9035 | Script vẫn tính 1,7 triệu. Booking này là giá không hoàn hủy và khách no-show, nên có thể Agoda vẫn trả tiền; cần kiểm trên trang quản lý của Agoda |
| Công suất phòng chia cố định cho 180 | dòng 27–29 | Đêm P5+P6 chỉ được tính là 1 phòng, nên con số 12,2% của tháng 12 không có ý nghĩa |

Tính lại theo từng tháng:

| Tháng | Script báo | Tính lại |
|---|---|---|
| 11 | 6,35 triệu | 6,21 triệu + 95 USD |
| 12 | 18,0 triệu | **khoảng 29–30 triệu** (21,2 triệu + 338 USD) |
| 1 | 4,0 triệu | 5,4 triệu |

### 4. Hai file đặt phòng lệch nhau, và không file nào đúng hoàn toàn
`bookings_2026_final_v2.csv` nghe tên thì giống bản mới hơn, nhưng thực ra là bản cũ hơn. Trong đó ZL-049 vẫn "Xác nhận" dù khách đã hủy ngày 8/11, và ZL-044 vẫn "Chờ cọc" dù anh Tùng đã chuyển 1 triệu ngày 12/11. Ngược lại, chỉ file v2 có FB-024 và có số đêm đúng của ZL-040. Hai file còn ghi giá khác nhau cho BK-4520 (1,2 triệu và 1,1 triệu một đêm).

Script chỉ đọc file `bookings_2026.csv`. Tiền cọc của 5 booking Zalo/FB, cộng thêm khoản phải hoàn cho chị Ngọc, tổng cộng **4,9 triệu**, đang nằm trong tài khoản Techcombank cá nhân của chị Thảo, chung với tiền chợ. Sổ cọc chỉ có trong app Ghi chú trên điện thoại.

### 5. Giấy tờ khách: lộ dữ liệu, khóa cửa và khai báo lưu trú
- **Lộ dữ liệu:** thư mục Drive chứa khoảng 600 ảnh CCCD/hộ chiếu đang để chế độ **"Bất kỳ ai có đường liên kết"** (`giay_to_khach_ghi_chu.txt` dòng 6–8). Đây là dữ liệu cá nhân thuộc phạm vi Nghị định 13/2023/NĐ-CP (hiệu lực 1/7/2023). Theo mình biết thì từ 1/1/2026 còn có thêm Luật Bảo vệ dữ liệu cá nhân 2025, *cần kiểm số hiệu và mức phạt*.
  - Việc nên làm ngay (khoảng 5 phút): chỉ chia sẻ thư mục cho tài khoản Google của chị Mai.
- **Mã hộp khóa 2580 chưa đổi từ 03/2025:** mọi khách từng tự nhận phòng đều biết mã này.
- **Khai báo lưu trú:**
  - Ghi chú hiện tại viết "Khách Việt Nam không cần khai báo". Điều này *có lẽ không đúng*: Luật Cư trú 2020 (68/2020/QH14) và Thông tư 55/2021/TT-BCA yêu cầu thông báo lưu trú cho mọi khách, thường là trước 23h, còn khách đến sau 23h thì trước 8h sáng hôm sau.
  - Với khách nước ngoài, thời hạn khai báo thường là **12 giờ** (Luật 47/2014/QH13, sửa đổi năm 2019). Cách hiện tại là để sáng hôm sau mới gửi, và đôi khi quên, nên dễ trễ hạn.
  - Với đoàn khách, quy định thường yêu cầu khai báo từng người chứ không chỉ người đặt.
  - *Tất cả các điểm trên cần xác nhận với công an phường.* Sau đợt sắp xếp hành chính năm 2025, đầu mối liên hệ có thể đã thay đổi.

### 6. Thuế 2026
`chi_phi_thang_10_2026.csv` dòng 11 ghi: thuế = 0, "nghe nói từ 2026 bỏ khoán, chưa làm gì". Theo mình biết, từ 2026 hộ kinh doanh chuyển từ thuế khoán sang tự kê khai theo doanh thu (chủ trương trong Nghị quyết 68-NQ/TW, 5/2025). *Mức ngưỡng doanh thu, kỳ kê khai và việc có phải xuất hóa đơn điện tử hay không thì mình không chắc, cần hỏi cơ quan thuế phường hoặc một kế toán dịch vụ.* Đã 10,5 tháng chưa kê khai thì có thể bị tính tiền chậm nộp.

Hiện có ba điều làm việc kê khai khó hơn:
- tiền cọc chảy vào tài khoản cá nhân;
- điện dùng chung đồng hồ với nhà ở;
- hoa hồng OTA và phí đổi ngoại tệ không được ghi lại.

Cũng vì vậy, con số chi phí tháng 10 là 16,24 triệu đang thấp hơn chi phí thật.

---

## Vài điểm nhỏ hơn (mình sẽ đưa vào kế hoạch)
- **Bình nóng lạnh P3 hư lại từ tháng 10 nhưng định để sau Tết.** P3 kín phòng từ 24/12 đến 3/1, đúng lúc Đà Lạt lạnh nhất.
- **Giá dịp lễ đang thấp hơn bảng giá của chính bạn (+40%).** Ví dụ P3 của BK-4520 là 1,2 triệu và ZL-044 là 1,1 triệu, trong khi theo bảng giá phải từ 1,26 triệu. P5+P6 đoàn chú Bảy là 1,1 triệu/phòng, theo bảng giá phải từ 1,12 triệu. Nếu đây là giá ưu đãi có chủ ý thì không sao.
- **Tết Nguyên Đán 2027 rơi vào khoảng 6/2/2027.** Nên kiểm tra mức +80% và quy định ở tối thiểu 2 đêm đã được cài trên Booking/Agoda/Airbnb chưa.
- **Airbnb để giờ nhận phòng 13h, các kênh khác là 14h.** Bài ghim "rẻ hơn Booking/Agoda 20%" có thể vướng điều khoản ngang giá (parity) của OTA, cần kiểm hợp đồng. Bài ghim còn ghi "khách quen không cần cọc", mâu thuẫn với chính sách cọc 50%.
- **Bình chữa cháy ở hành lang có hạn kiểm tra ghi năm 2024.**

## Bạn giúp mình 3 câu (mỗi câu trả lời 1 dòng là đủ)
1. **Mong muốn ban đầu:** từ lúc khách nhắn đặt phòng đến cuối tháng biết lãi bao nhiêu, bạn muốn hệ thống này lo được những phần nào?
2. **Chỗ mất thời gian nhất:** khâu nào hay sai hoặc tốn công nhất, và có việc gì bạn từng muốn nó làm mà chưa làm được (ví dụ tự báo trùng phòng, sổ cọc, lịch dọn phòng cho chị Mai)?
3. **Những thứ cần giữ nguyên:** điều gì phải giữ đúng như hiện tại (Google Sheet, cách chị Thảo nhắn chị Mai qua Zalo, các cột trong sheet…)? Và bản sheet nào là bản bạn đang dùng thật?

Khi có câu trả lời, mình sẽ làm theo thứ tự này:
1. Sao lưu và khóa dữ liệu cũ.
2. Gộp 2 file thành một nguồn duy nhất và thêm bước tự báo trùng phòng.
3. Sửa script tính tiền, kiểm lại bằng chính các số ở trên.
4. Thêm sổ cọc.
5. Lịch dọn phòng tự tạo.

Mọi thứ vẫn chạy trên Google Sheet bạn đang dùng.
