Cảm ơn anh Vinh. Anh đã giao cho mình chọn, nên mình chọn: **giữ nguyên Google Sheet và Zalo, gộp mọi thứ vào 1 file Google Sheet mới, ưu tiên chặn trùng phòng trước, rồi đến biết lãi thật, rồi bớt thời gian nhắn tin.** Chi phí 0đ, dùng được ngay trước Noel.

**Tóm tắt**
1. Đã làm xong file **`SuongMai_QuanLy.xlsx`**. Anh tải lên Google Drive rồi chọn "Lưu dưới dạng Google Trang tính" là chị Thảo dùng được trên điện thoại.
2. **Chống trùng phòng:** nhập booking nào trùng là dòng đó đỏ ngay, và tab Lịch hiện chữ TRÙNG. Sheet đã bắt đúng 2 vụ đang có là P3 đêm 25/12 và P2 đêm 31/12.
3. **Lãi thật:** tab LaiLo tính tổng doanh thu đang có là **45,15 triệu**, trong khi script cũ báo 32,15 triệu. Tab này cũng tách hoa hồng, thực nhận và lãi theo tháng, và đo % khách đặt trực tiếp: hiện là 35%, mục tiêu 40%.
4. **Bớt nhắn tin:** chị Thảo nhập ngày khách hỏi, sheet tự soạn tin nhắn có phòng trống, giá lễ và tiền cọc để copy gửi. Có thêm 9 mẫu tin nhắn và tin nhắn lịch dọn phòng cho chị Mai.
5. **Giữ nguyên:** file gốc (đã sao lưu và khóa), sheet cũ, giá trên Booking/Agoda/Airbnb, kênh Zalo.
6. **Đã kiểm:** 20/20 phép thử đạt, tính bằng Excel thật và đối chiếu với một cách tính riêng. Google Sheet thì mình chưa mở thử được ở đây.
7. **4 việc chỉ anh chị làm được, nên làm hôm nay:** hoàn 600k cho chị Ngọc, gọi đổi phòng cho anh Tùng và chị Châu, khóa thư mục ảnh CCCD trên Drive, đổi mã hộp khóa.

---

## Việc cần làm hôm nay (mình đã soạn sẵn tin nhắn)
| Việc | Cách làm |
|---|---|
| **Hoàn 600k cho chị Ngọc** | Chị đã hủy trước 54 ngày, và đêm 1/1 phòng P6 vốn đã bán cho đoàn chú Bảy. Chuyển khoản xong thì gửi tin ở tab MauTinNhan (dòng 8), rồi điền "Đã hoàn" = 600000. |
| **Anh Tùng (P3, 25–27/12)** | Đổi sang **P5 hoặc P6**: đều trống cả 2 đêm và rộng hơn, nhưng không có ban công. Tin nhắn ở dòng 9. |
| **Chị Châu (P2, đêm 31/12)** | Đổi sang **P1**: cùng loại phòng đôi view vườn, đêm đó đang trống. Tin nhắn ở dòng 10. |
| **Thư mục ảnh CCCD trên Drive** | Vào Chia sẻ, đổi "Bất kỳ ai có đường liên kết" thành **"Bị hạn chế"**, rồi chỉ thêm Gmail của chị Mai. |
| **Mã hộp khóa** | Đổi mã mới. Từ giờ gửi mã riêng cho từng khách. |

Sửa cột Phòng của anh Tùng và chị Châu xong thì chữ đỏ biến mất. Mình đã chạy thử đúng thao tác này: số booking trùng giảm từ 4 về 0.

## Cài đặt (1 lần, trên laptop, khoảng 5 phút)
1. Vào drive.google.com, chọn Mới, Tải tệp lên, rồi chọn `SuongMai_QuanLy.xlsx`.
2. Mở file, vào menu Tệp, chọn **Lưu dưới dạng Google Trang tính**.
3. **Phép thử:** tab **Lich** phải có đúng 2 chữ TRÙNG đỏ (P3 ngày 25/12, P2 ngày 31/12). Thấy vậy là sheet chạy đúng trên Google.
4. Chia sẻ quyền chỉnh sửa cho chị Thảo. **Không** chia sẻ cho chị Mai, vì sheet có số điện thoại khách và doanh thu; chị Mai nhận tin nhắn từ tab DonPhong.
5. Sheet cũ thì giữ nguyên làm lưu trữ, không nhập tiếp vào đó nữa.

## Hằng ngày
**Chị Thảo, trên điện thoại:**
- Khách hỏi phòng: mở **ConPhong**, nhập ngày đến, ngày đi, số khách, khách quen hay không, rồi copy ô tin nhắn gửi khách.
- Có booking mới (OTA báo về, hoặc khách chốt qua Zalo/FB): thêm 1 dòng vào **DatPhong** ngay. Cột CẢNH BÁO phải trống.
- Khách Zalo/FB chốt phòng: **đóng phòng đó trên Booking, Agoda và Airbnb**, rồi điền "Rồi". Bước này chặn trùng phòng từ gốc. Hiện có 7 booking trực tiếp đang chờ chị Thảo xác nhận đã đóng phòng.
- Buổi tối: mở **DonPhong**, copy tin nhắn gửi chị Mai. Ngày Chủ nhật có phòng trả thì sheet tự nhắc.

**Anh Vinh, mỗi tuần khoảng 10 phút:**
- Xem **LaiLo**: tiền cọc đang giữ, số tiền còn nợ hoàn khách (phải bằng 0), % khách đặt trực tiếp.
- Nhập chi phí vào **ChiPhi**. Cuối tháng, dòng của tháng đó chính là lãi thật.

## So với mong muốn ban đầu của anh
- **Giữ:** Google Sheet, Zalo cho khách quen, giá và thứ hạng trên OTA.
- **Từng làm lệch, nay đã sửa:**
  - Script tính sai: cộng USD như VND, sai định dạng ngày, hoa hồng Booking 12% thay vì 15%.
  - 2 file đặt phòng chạy song song.
  - Giá lễ cho khách trực tiếp phải tính tay.
- **Chưa từng có, nay đã có:** chặn trùng phòng, lãi theo tháng, sổ cọc, đo % khách đặt trực tiếp.
- **Thêm ngoài mong đợi:**
  - Báo giá tự soạn sẵn.
  - Lịch dọn phòng cho chị Mai.
  - Nhắc khai báo lưu trú, và mẫu tin xin giấy tờ của tất cả khách *trước* khi đến.
  - Mẫu tin "sau khi trả phòng" để mời khách quay lại đặt trực tiếp.

**Hai điều mình phát hiện thêm khi gộp dữ liệu:**
- Booking AG-9035 là loại hủy không hoàn tiền, nên **P2 hai đêm 5–6/12 đang trống và có thể bán lại**, khoảng 1,5 triệu. Anh kiểm trên Agoda xem tiền có về không và phòng đã mở bán lại chưa.
- 6 booking ngày 20–30/11 ghi "Đã ở" dù chưa tới ngày. Mình đã đổi thành "Xác nhận"; tiền không thay đổi.
  - Vì vậy cần đính chính một con số ở lần trước: tiền cọc đang giữ là **4,8 triệu, cộng 600 nghìn phải hoàn cho chị Ngọc**.

## Đã kiểm thế nào
| Anh cần | Nằm ở đâu | Đã kiểm |
|---|---|---|
| Không trùng phòng | DatPhong, Lich | 720/720 ô lịch khớp với cách tính riêng; bắt đúng 2 vụ thật; thử nhận nhầm 1 khách Zalo vào phòng đã bán thì sheet báo ngay |
| Biết lãi thật | LaiLo | 21/21 booking và từng tháng khớp với cách tính riêng. Phần chênh so với script cũ (+13 triệu) giải thích đủ 100%: tiền Airbnb USD, 1 đêm bị sót của ZL-040, giảm khách quen của FB-019, và booking FB-024 trước đây chỉ có trong file v2 |
| Không mất gì cũ | `_sao_luu/` | 8 file gốc khớp mã kiểm tra (hash). 15 booking không cần sửa vẫn giữ nguyên đúng số tiền |
| Đổi giá về sau an toàn | tab CauHinh | Đã thử: Booking tăng hoa hồng lên 18%, tỷ giá USD đổi, tăng bảng giá 10%, Tết +80% (tối thiểu 2 đêm), gõ sai ngày. Booking cũ đều giữ nguyên số tiền |

**Đổi giá hay quy định:** chỉ sửa ô vàng ở tab **CauHinh**. Booking đã nhập giữ nguyên số tiền. Hoa hồng mới chỉ áp cho ngày đến sau ngày anh điền.

**Sao lưu:** dùng Google Sheet → Tệp → Lịch sử phiên bản. Đầu mỗi tháng, tải file .xlsx về và cất vào `_sao_luu/`.

## Việc còn lại, mình không làm thay được
Tất cả đã ghi trong `TRACE.md`, mỗi dòng có hạn và người làm.

- **Tuần này:**
  - Hỏi công an phường về khai báo lưu trú: theo mình hiểu thì khách Việt Nam cũng phải khai, khách nước ngoài khai trong vòng 12 giờ. Cần xác nhận.
  - Đổi giờ nhận phòng trên Airbnb từ 13h sang 14h.
  - Cài tin nhắn nhanh cho Zalo và câu trả lời lưu sẵn cho Facebook Page.
- **Trước Noel:**
  - Thay bình nóng lạnh P3 (P3 kín phòng từ 24/12 đến 3/1).
  - Kiểm định bình chữa cháy.
  - Mở 1 tài khoản ngân hàng riêng cho homestay.
- **Trước cuối năm:** gặp kế toán hoặc thuế phường về thuế 2026, vì đã bỏ thuế khoán. Tab LaiLo và ChiPhi có sẵn số liệu cần thiết.
- **Một việc mình đã bỏ theo ý anh:** giá dịp lễ trên Booking/Agoda thấp hơn bảng giá của anh, nhưng anh dặn không đổi giá OTA nên mình để nguyên.

**Một nhờ nhỏ:** chị Thảo ước giúp mình hiện mất mấy phút để trả lời một tin hỏi giá, và mỗi ngày bao nhiêu tin. Mình ghi số đó vào `IMPROVEMENT-LOG.md` để sau 2 tuần so lại xem tiết kiệm được bao nhiêu.

## Files created
Tất cả nằm trong `homestay_suongmai_dalat/`. Các file cũ không bị sửa.
- `SuongMai_QuanLy.xlsx`: file chính để tải lên Google Sheet. Gồm 9 tab: HuongDan, DatPhong, ConPhong, Lich, DonPhong, LaiLo, ChiPhi, MauTinNhan, CauHinh.
- `TRACE.md`: 38 nhu cầu và phát hiện, mỗi dòng có trạng thái và bằng chứng.
- `APEX-COMPACT-REVIEW.md`: bàn giao gọn, gồm cách dùng, đổi giá, sao lưu, kiểm thử.
- `IMPROVEMENT-LOG.md`: mốc đo ban đầu, nhật ký cải tiến, 3 cải tiến tiếp theo, câu lệnh để rà lại sau này.
- `_sao_luu/2026-11-14_ban_goc/`: bản sao chỉ đọc của 8 file gốc, kèm `SHA256SUMS.txt`.
- `_cong_cu/` (dành cho laptop, chị Thảo không cần mở):
  - `tao_bang_tinh.py`: dựng lại file từ dữ liệu gốc.
  - `kiem_thu.py`: chạy lại 20 phép thử.
  - `excel_tinh_lai.ps1`: dùng Excel để tính lại khi kiểm thử.
  - `ket_qua_kiem_thu.txt`: kết quả 20/20 PASS.
  - `nhat_ky_gop_du_lieu.txt`: 20 điều chỉnh khi gộp 2 file, mỗi điều chỉnh có lý do.
  - `baseline_tinh_tien_cu.txt`: kết quả của script cũ, giữ để đối chiếu.
