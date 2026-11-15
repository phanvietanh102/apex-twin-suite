Cảm ơn anh, giờ mình đã đủ thông tin. Mình đã chọn phương án, chốt luôn những chỗ anh để mình quyết, và làm tiếp vào file `QuanLyXuong_ThanhDat.xlsx`.

## Phương án mình chọn

**Excel trên máy văn phòng là sổ chính, Google Drive lo sao lưu, và giấy tờ (phiếu bó có cuống, phiếu in) là bằng chứng.** Không mua phần mềm, không cần ai biết lập trình.

| Anh cần / anh lo | Cách làm | Chi phí |
|---|---|---|
| Lương rõ ràng, hết cãi nhau | **Phiếu bó hàng có cuống:** mỗi bó kèm 1 phiếu, mỗi công đoạn 1 cuống. Công nhân làm xong ghi mã NV lên cuống và giữ lại. Mỗi bó chỉ có đúng 1 cuống cho 1 công đoạn nên không ai ghi trùng hay ghi thừa được. Cuối tuần tổ trưởng đếm cuống theo người. File tự tính lương | Giấy in |
| Công nhân tự xem phần của mình | Thứ Hai in **phiếu sản lượng tuần** cho cả xưởng (bấm in 1 lần, 3 phiếu/trang), phát tận tay. Có sai thì sửa trước thứ Tư. Cuối tháng in **phiếu lương riêng** từng người. Ai muốn thì chụp gửi Zalo riêng | 0đ |
| Xưởng không phụ thuộc anh và chị Hoa | Mỗi việc có 1 người chính và 1 người dự phòng. Sheet `HuongDan` viết rõ ai làm gì, ngày nào. Bằng chứng nằm ở cuống phiếu, không nằm trong trí nhớ ai. Không còn file Python nữa | 0đ |
| Biết đơn nào lời, đơn nào lỗ | Sheet `LaiLoDon` lấy doanh thu trừ khoản khách trừ, tiền công khoán và chi phí chung chia theo tỷ lệ tiền công | 0đ |
| Đoàn kiểm tra hoặc audit xuống | Sheet `ChuanBiAudit` (16 mục, có hạn, có người làm) và kế hoạch tới 15/12 | Xem mục Tiền |
| Máy hỏng mất hết dữ liệu | File để trong thư mục Google Drive (tự lưu bản cũ), thứ Bảy chép thêm ra USB, mua UPS cho máy | ~1,5 triệu, mua 1 lần |
| Khách bắt đền thiếu vải, thiếu hàng | Đếm vải và ký biên bản khi nhận, quyết toán vải từng đơn, hóa đơn theo số giao thực tế (đã có trong file) | 0đ |

**Những cách mình không chọn:**
- **ERP:** vượt ngân sách.
- **App riêng cho công nhân:** phải có người lập trình bảo trì, mà cháu anh đã đi học xa.
- **Chuyển ngay sang Google Sheets trên điện thoại:** văn phòng chỉ có 1 máy cũ, hạn lại gấp. Mình để việc này sau audit, khi đó cho tổ trưởng nhập bằng Google Form miễn phí.

Những điều anh dặn không đổi thì mình giữ nguyên: lương khoán theo công đoạn, đơn giá với khách, chị Hoa ghi sản lượng tổ 1, chị Vân làm thuế và BHXH.

## Những việc mình đã chốt thay anh

1. **Lương T10:**
   - Trả ngay cho Quỳnh 3.264.000.
   - Phần chênh lệch của những người khác trả hoặc thu cùng lương T11 ngày 5/12. Mình đã ghi sẵn ở sheet `DieuChinh`, nên lương T11 tự cộng hoặc trừ.
   - Thảo trả lại 3.417.280, chia 3 tháng (T11, T12, T1), có giấy thỏa thuận ký tên.
   - Hằng trừ hết 977.100 tiền tạm ứng trong T11.
2. **Từ lương T11:**
   - Trả tăng ca theo luật (150% ngày thường, 200% Chủ nhật, ca đêm cao hơn).
   - Chỉ trừ BHXH với người có đóng, theo đúng mức đóng.
   - Ai lương giờ thường dưới mức tối thiểu thì bù cho đủ.
   - Bỏ hẳn "quỹ xưởng".
3. **Tiền BHXH đã trừ thừa các tháng trước:** hoàn lại cho công nhân trước 15/12, lấy từ quỹ xưởng. Vợ anh nhập số đã trừ từ bảng lương cũ vào sheet `HoanTraBHXH`, file tự ra số phải hoàn cho từng người.
4. **Người hợp đồng 3 tháng:** chị Vân đăng ký BHXH từ tháng 12 và ký lại hợp đồng đúng loại.
5. **Phiếu bó:** tổ 1 dùng thử với 1 đơn mới cuối tháng 11, tổ 2 và tổ 3 chuyển sang trong tháng 12. Riêng tháng 11, tổ 2 và tổ 3 vẫn ghi sổ tay, nhưng chép tổng tuần ra tờ mẫu (`MauGhiTay`) để vợ anh nhập. Như vậy lương T11 của cả xưởng tính trong cùng một file.

## Đã làm thêm trong file

Đường dẫn vẫn là `xuong_may_thanh_dat/HE_THONG_MOI/QuanLyXuong_ThanhDat.xlsx`, giờ có 26 sheet. Nghe thì nhiều, nhưng **hằng ngày chỉ đụng tới 5 sheet**: `SanLuong`, `TamUng`, `ChamCong`, `InPhieuTuan`, `InPhieuLuong`. Anh thì xem 3 sheet: `KiemTra`, `LaiLoDon`, `ViecCanXuLy`. Các sheet còn lại làm một lần rồi để đó.

Các sheet mới:
- `InPhieuTuan`, `InPhieuLuong`: in phiếu cho tất cả mọi người một lần, cắt rời ra phát.
- `InPhieuBo`: chọn mã đơn là in được 8 phiếu bó mỗi trang, cuống ghi sẵn công đoạn lấy từ bảng đơn giá.
- `MauGhiTay`: tờ mẫu in ra cho tổ 2 và tổ 3 ghi tay.
- `DieuChinh`, `HoanTraBHXH`: xử lý tiền T10 và tiền BHXH trừ thừa.
- `ChiPhiChung`, `LaiLoDon`: tính lời lỗ theo đơn.
- `ChuanBiAudit`: danh sách việc chuẩn bị audit.
- `HuongDan`: viết lại theo từng người. `ViecCanXuLy`: viết lại thành kế hoạch theo tuần.

Bảng lương có thêm cột "Điều chỉnh kỳ trước". Nếu ai bị trừ nhiều hơn thu nhập (thực lĩnh âm), `KiemTra` sẽ báo. Người không đi làm ngày nào trong tháng (ví dụ chị Mai lúc nghỉ sinh) thì không bị trừ BHXH.

**Mình đã chạy thử trong Excel:**
- Không có ô nào báo lỗi công thức.
- Nhập thử sản lượng ngày 15/11 cho Lan (100 sản phẩm giờ thường, 40 sản phẩm tăng ca): phiếu tuần hiện đúng 2 dòng, tổng 576.000.
- Phiếu lương T11 của Lan tự tính phụ trội tăng ca 150% và tự cộng khoản điều chỉnh 202.705 từ T10.

## Kế hoạch đến 15/12

Kế hoạch chi tiết có hạn và người làm nằm ở sheet `ViecCanXuLy`. Tóm tắt:

- **15–17/11:**
  - Xử lý DH2612.
  - Gỡ dữ liệu cá nhân khỏi nhóm Zalo.
  - Trả lương cho Quỳnh.
  - Dừng tăng ca cho Mai và Ngọc.
  - Cài Google Drive.
- **16–22/11:**
  - Họp toàn xưởng 15 phút, báo trước các thay đổi về lương. Làm vậy để công nhân yên tâm, không ai bỏ đi.
  - Nhập danh sách tổ 2, tổ 3 và đơn giá các đơn đang chạy.
  - Chị Hoa nhập sản lượng T11.
  - Chị Vân làm hợp đồng và BHXH.
  - Xin công ty trung gian bộ tiêu chí audit.
- **23–29/11:**
  - Mua máy chấm công, chạy từ 1/12.
  - Thử phiếu bó ở tổ 1.
  - Gửi An Phát văn bản (thiếu vải, khoản trừ 12 triệu, vải kate).
  - Gom bảng lương cũ để tính số BHXH phải hoàn.
- **30/11–5/12:**
  - Ngày 3/12: `KiemTra` về 0, in phiếu lương phát cho công nhân dò.
  - Ngày 5/12: trả lương T11 theo cách mới.
- **6–15/12:**
  - Làm xong `ChuanBiAudit`.
  - Hoàn tiền BHXH trừ thừa.
  - Tổ 2, tổ 3 chuyển sang phiếu bó.
  - Nhập chi phí chung, xem lời lỗ.
  - Ngày 12–13/12: anh và chị Vân tự đi kiểm tra một vòng theo danh sách.

**Một nguyên tắc rất quan trọng khi audit:** không làm lại sổ sách cũ cho đẹp và không giữ 2 bộ sổ. Auditor đối chiếu chấm công, phiếu lương, sao kê chuyển khoản và danh sách BHXH với nhau. Phát hiện hồ sơ giả là trượt ngay. Anh cứ nói thật: hồ sơ được số hóa từ T11/2026, các lỗi cũ xưởng đã tự phát hiện và đã khắc phục, có chứng từ kèm theo. Cách này được đánh giá tốt hơn hẳn.

## Tiền

**Thiết bị và công cụ: nằm trong ngân sách.** Giá dưới đây là giá tham khảo, anh hỏi lại cửa hàng:

| Khoản | Giá | Mua |
|---|---|---|
| Máy chấm công vân tay | ~1,5–3 triệu | 1 lần |
| UPS cho máy tính | ~1–1,5 triệu | 1 lần |
| USB | ~150 nghìn | 1 lần |
| Máy in laser (nếu xưởng chưa có) | ~3 triệu | 1 lần |
| Giấy in | dưới 200 nghìn | mỗi tháng |
| Google Drive | miễn phí | — |

Lưu ý: phần mềm Google Drive cho máy tính cần Windows 10 trở lên. Nếu máy văn phòng chạy Windows 7 thì mỗi tuần vào drive.google.com tải file lên bằng tay.

**Chi phí làm đúng luật thì không nằm trong 2–3 triệu kia, và không bỏ qua được.** Nếu không làm thì vừa không qua audit, vừa bị phạt khi có đoàn kiểm tra. Ước tính riêng tổ 1 theo số liệu T10:

| Khoản | Mỗi tháng |
|---|---|
| BHXH phần xưởng đóng cho 6 người mới đăng ký (21,5% × 4,14 triệu) | ~5,3 triệu |
| Phụ trội tăng ca | ~4,5 triệu |
| Bù cho đủ lương tối thiểu | ~2,4 triệu |
| **Cộng** | **~12 triệu** |

Thêm một khoản phải trả một lần: tiền BHXH đã trừ thừa, khoảng 5 triệu cho mỗi tháng đã áp dụng (chỉ tính tổ 1).

Cả xưởng sẽ cao hơn con số này, nhập xong tổ 2 và tổ 3 là biết chính xác. Phụ trội tăng ca sẽ giảm khi giữ tăng ca dưới 40 giờ/tháng.

**Khi báo giá cho nhãn hàng châu Âu, anh phải tính đủ các khoản này vào giá.** Sheet `LaiLoDon` sẽ cho anh con số đó.

## Lời lỗ: đọc sơ bộ

Hiện file mới có sản lượng tổ 1 tháng 10, chưa nhập tiền thuê xưởng, điện..., nên các con số dưới đây chỉ để tham khảo:

| Đơn | Tiền công khoán / doanh thu | Tiền công mỗi sản phẩm | Ghi chú |
|---|---|---|---|
| DH2611 An Phát | 35,3 / 62,7 triệu (56%) | 11.823đ trên giá 21.000đ | Chưa trừ khoản phạt trễ |
| DH2613 Mộc Miên | 21,6 / 48 triệu (45%) | 14.373đ trên giá 32.000đ | |
| DH2612 Hanbok | | 13.144đ trên giá 0,95 USD | Chưa có tỷ giá |

Đơn của An Phát mỏng lãi hơn hẳn đơn của shop. Muốn biết chắc đơn nào lời, đơn nào lỗ thì cần nhập đủ chi phí chung và dữ liệu của cả 3 tổ.

## Anh gửi giúp mình (không có vẫn làm tiếp được)

1. **DH2612 giao ngày mai:** định mức 1,2 là mét hay yard? Hiện đã xong bao nhiêu áo? Việc này gấp nhất.
2. Danh sách công nhân tổ 2, tổ 3: mã, tên, ngày sinh, ngày vào làm, loại hợp đồng. Không cần CCCD hay số tài khoản.
3. Đơn giá công đoạn của các đơn đang may.
4. Chi phí chung T10 và T11 (thuê xưởng, điện, nước, sửa máy...), tỷ giá các đơn Hanbok đã nhận tiền.
5. Máy văn phòng chạy Windows mấy? Xưởng đã có máy in chưa?

Gửi được phần nào thì mình nhập luôn phần đó và tính lại lương T11, lời lỗ cho anh.

*Phần luật (tăng ca, BHXH, hợp đồng, lương tối thiểu) anh vẫn nhờ chị Vân xác nhận trước khi áp dụng, đặc biệt là chuyện vùng lương sau sáp nhập và số tiền phải truy đóng.*

## Files created

- `<scratch>/eval4/t3/B/work/xuong_may_thanh_dat/HE_THONG_MOI/QuanLyXuong_ThanhDat.xlsx`: cập nhật lên 26 sheet, đã tính lại trong Excel
- `<scratch>/eval4/t3/B/work/_build/phan_mo_rong.py`: phần tạo các sheet mới (mới)
- `<scratch>/eval4/t3/B/work/_build/tao_file_quan_ly.py`: script tạo file (đã sửa: thêm cột điều chỉnh lương, hướng dẫn theo vai trò, kế hoạch mới). Anh không cần dùng script này
