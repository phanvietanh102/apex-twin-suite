Cảm ơn anh Đạt. Anh đã giao cho mình chọn, nên mình chọn cách này: **gom tất cả vào một file Excel, cộng thêm phiếu giấy có chữ ký mỗi ngày, rồi gửi phiếu lương riêng cho từng người qua Zalo.** Lý do: không tốn tiền, không cần biết lập trình, máy cũ vẫn chạy được, và chị Hoa vẫn ghi sản lượng như mọi khi. Mình đã làm xong luôn.

**Tóm tắt:**
1. File mới là `QuanLyXuong_ThanhDat_2026.xlsx`. Lương, sản lượng, tạm ứng, đơn hàng, vải khách, giao hàng, lãi/lỗ từng đơn và danh sách việc chuẩn bị audit đều nằm trong file này. Bảng lương tự tính và tự báo khi có chỗ lệch.
2. Lương tháng 10 đã tính lại. Tháng 10 xưởng đã chuyển khoản **75.644.057đ**, trong khi đúng ra phải là **88.481.200đ**, tức xưởng **còn nợ công nhân 12,84 triệu** (chi tiết từng người ở sheet `DoiChieu_T10`).
3. Lương tháng 11 (trả ngày 5/12) đã sẵn sàng tính theo cách mới. Phần tạm ứng 6 triệu sẽ tự trừ vào lương tháng 11.
4. Mỗi công nhân có phiếu lương riêng, ghi từng dòng: ngày, mã đơn, công đoạn, số lượng, đơn giá. Ai kêu thiếu sản lượng thì mở sheet `KiemKhop` là biết thiếu ở đâu.
5. Có thêm file `SaoLuu_1Cham.bat`: bấm đúp một lần là sao lưu cả thư mục ra Desktop và USB. Mình đã chạy thử, chạy được.
6. Có file `TIN_NHAN_MAU.txt` gồm các tin nhắn soạn sẵn gửi Hanbok, An Phát, chị Vân và nhóm công nhân. **Mình chưa gửi gì cho ai cả.**
7. Mình đã chạy 26 bài kiểm tra trên Excel thật và đạt cả 26. File không có ô nào báo lỗi.
8. Mình không xóa hay sửa file cũ nào. 9 file cũ được khóa ở chế độ chỉ đọc, và có bản sao gốc kèm mã kiểm tra trong thư mục `_apex`.

---

## Việc anh cần làm, theo thứ tự gấp

| Khi nào | Việc | Ở đâu |
| :--- | :--- | :--- |
| **Hôm nay** | Gửi Hanbok tin báo thiếu vải đơn DH2612. Hạn giao là ngày mai, vải là 2.600 **yard**, tức 2.377 m, nên thiếu khoảng 23 m, tương đương khoảng 19 áo | TIN_NHAN_MAU mục 1 (có sẵn bản tiếng Anh) |
| **Hôm nay** | Xóa hoặc thu hồi danh sách CCCD, số tài khoản và bảng lương trong nhóm Zalo 38 người, rồi gửi thông báo mới | TIN_NHAN_MAU mục 4 |
| **Từ ngày mai** | Không cho Ngọc (17 tuổi) và chị Mai (đang bầu khoảng tháng thứ 7) tăng ca hay làm đêm nữa | ChuanBiAudit việc 1–2 |
| Tuần này | Gửi chị Vân 8 câu cần xác nhận. Quan trọng nhất là vùng lương tối thiểu và mức đóng BHXH, vì số tiền truy lĩnh phụ thuộc hai con số này | TIN_NHAN_MAU mục 3 |
| **Trước 30/11** | Ký hợp đồng mới cho Hằng, Thu, Thảo, Huyền (hợp đồng của 4 người đã hết hạn từ 31/10) | NhanSu: cột cảnh báo đỏ |
| Trước 23/11 | Đối chiếu với An Phát: thiếu 50 m vải, giao trễ 4 ngày, còn khoản 63 triệu chưa thu | TIN_NHAN_MAU mục 2 |
| **Trước 5/12** | Duyệt các khoản truy lĩnh tháng 10: đổi "Chờ duyệt" thành "Đã duyệt" | sheet DieuChinh |
| Trước 15/12 | Làm hết 19 việc chuẩn bị audit | sheet ChuanBiAudit (đỏ = trễ hạn) |

## Trước và sau

| | Trước | Bây giờ |
| :--- | :--- | :--- |
| Lương tháng 10 | 2 file khác nhau. Bản v2 cộng thiếu 3 dòng (tổng ghi 73,57 triệu, đúng là 88,28 triệu). Quỳnh bị cộng vào Thảo do trùng mã NV09. Tạm ứng không trừ | 1 bảng lương, 1 bản chốt không sửa được. Quỳnh có mã riêng NV15. Mã trùng sẽ báo đỏ |
| Phát hiện sai sót | Không ai biết, cuối tháng mới cãi nhau | Ô "Kiểm tra tổng" phải hiện **KHỚP**. KiemKhop bắt ghi trùng sản lượng. Cột CẢNH BÁO hiện chữ đỏ |
| Tăng ca | Trả bằng đơn giá thường | Chọn loại ca thì file tự nhân 150%, 200%, 300% hoặc mức ca đêm |
| Trừ BHXH | Trừ 10,5% thu nhập của cả tổ, kể cả người không đóng, phần dư để "quỹ xưởng" | Chỉ trừ đúng số xưởng nộp cho người có đóng |
| Lương tối thiểu | Huyền làm đủ 26 công mà khoán chỉ được 2,29 triệu | File tự bù cho đủ mức tối thiểu vùng |
| Doanh thu năm | Ghi 476,4 triệu, sai vì đơn DH2609 nhập 2 lần và tiền USD bị cộng như tiền đồng | **417,6 triệu + 7.615 USD**, khoảng 615 triệu theo tỷ giá tạm 26.000 (anh sửa lại tỷ giá thực) |
| Lãi/lỗ | Không biết | Lãi gộp, chưa trừ chi phí chung: DH2611 khoảng 33,6% (đã trừ khoản phạt trễ ước tính), DH2613 khoảng 47,9% |
| Sao lưu | 1 máy, đã từng mất dữ liệu | 3 nơi: máy, file zip trên Desktop, USB (có thêm Google Drive nếu anh cài) |

**Lương tháng 10 chênh 12,84 triệu ở đâu** (chi tiết ở sheet DoiChieu_T10):
- Quỳnh chưa nhận đồng nào: +3.264.000đ.
- Thảo nhận thừa phần của Quỳnh. Sau khi trừ đi số BHXH đã trừ sai của Thảo, Thảo còn nhận thừa 2.417.280đ. Mình chia ra 2 tháng để thu lại, và **chỉ thu khi Thảo ký đồng ý**.
- Phụ trội tăng ca của Lan, Mai, Ngọc: +4.696.000đ.
- Hoàn lại tiền trừ BHXH sai.
- Bù cho đủ lương tối thiểu: chị Hoa 781.000đ, Ngọc 552.000đ, Huyền 1.846.000đ. Khoản 500.000đ chị Hoa định cộng cho Huyền không có sản lượng làm căn cứ, nên mình thay bằng khoản bù lương tối thiểu này.
- Ngoài ra có **1,78 triệu ước tính** phụ trội cho 9 người có giờ tăng ca, nhưng sản lượng không ghi là làm tăng ca. Khoản này mình để riêng, anh tự quyết.

## Dùng hằng ngày (chi tiết ở sheet `HuongDan`)
- **Mỗi ngày (chị Hoa, khoảng 10 phút):**
  - In sheet MauPhieuNgay. Cuối ngày ghi sản lượng, mỗi công nhân **ký** vào dòng của mình.
  - Tối nhập vào sheet SanLuong, mỗi dòng gồm: ngày, mã NV, mã đơn, công đoạn, số lượng, ca.
  - Ô màu vàng là ô được gõ. Thấy chữ đỏ thì sửa ngay.
- **Thứ Bảy:**
  - Mở KiemKhop xem có dòng "GHI THỪA" không.
  - Gửi phiếu lương theo tuần, nhắn riêng từng người.
  - Bấm SaoLuu_1Cham.bat.
- **Cuối tháng (vợ anh, khoảng 1 giờ cho 40 người):**
  - Nhập ChamCong, TamUng, rồi duyệt các khoản ở DieuChinh.
  - Đổi tháng ở CaiDat ô C4.
  - Kiểm tra BangLuong phải hiện **KHỚP**.
  - In phiếu từng người, chuyển khoản, rồi **chốt tháng** theo hướng dẫn (chốt rồi thì tháng đó không bao giờ đổi nữa).
- **Tổ 2 và tổ 3:** dùng cùng mẫu phiếu giấy. Vợ anh nhập danh sách người của hai tổ vào NhanSu, dùng mã mới từ NV16 trở đi, không bao giờ dùng lại mã cũ.

## Đổi giá, đổi luật mà không hỏng gì
- **Lương tối thiểu tăng:** sửa ô CaiDat C7. Mình đã thử tăng lên 4.730.000: Huyền được bù đúng thêm, còn tháng đã chốt giữ nguyên.
- **Hệ số tăng ca, phụ cấp, tỷ lệ BHXH:** sửa trong CaiDat. Mức đóng BHXH của từng người ghi ở NhanSu cột M, theo số chị Vân báo.
- **Đơn mới:** thêm dòng mới ở DonGia. Đơn giá của đơn cũ giữ nguyên. Đã thử: tiền công của đơn cũ không đổi.
- **Tỷ giá:** đơn đã nhận tiền thì gõ tỷ giá thực nhận ở DonHang cột H, khi đó đơn đó không đổi theo tỷ giá tạm nữa.

## Sao lưu và khôi phục
- Bấm đúp SaoLuu_1Cham.bat **sau khi đã đóng Excel**. File zip có ngày giờ nằm trong Desktop\SaoLuu_XuongMay, và được chép thêm sang USB nếu đang cắm.
- Nên cài Google Drive cho máy tính (miễn phí) để thư mục đó tự đưa lên mạng.
- **Khôi phục:** giải nén bản sao lưu gần nhất. Các file cũ của xưởng vẫn còn nguyên, kèm bản gốc trong `_apex\backup_goc_2026-11-14`.
- File có số CCCD và số tài khoản, nên anh đặt mật khẩu mở file: File → Info → Protect Workbook → Encrypt with Password.

## Bạn cần → Nằm ở đâu → Đã kiểm thế nào
| Bạn cần | Nằm ở đâu | Đã kiểm thế nào |
| :--- | :--- | :--- |
| Lương rõ ràng, hết cãi nhau | BangLuong, KiemKhop, MauPhieuNgay | Khi để hệ số tăng ca 100%, lương khoán khớp đúng từng đồng với file python cũ (78.618.500đ). Lương tháng 10 tính trong Excel khớp với một lần tính độc lập bằng Python. Thử ghi trùng 100 sản phẩm thì bị bắt |
| Công nhân tự xem phần của mình | PhieuLuong | Phiếu của Huyền tháng 10 và tháng 11 khớp bảng lương, thực lĩnh hiện ngay đầu phiếu |
| Không phụ thuộc anh và chị Hoa | HuongDan, CaiDat | Thử cho anh Tú nhập sản lượng cho một người mới ở tổ 2: bảng lương vẫn đúng |
| Biết đơn lời hay lỗ | LaiLo | Đơn mới có giá mới không làm đổi số của đơn cũ |
| Qua audit châu Âu | ChuanBiAudit + cảnh báo ở NhanSu, SanLuong | Người dưới 18 tuổi hay người đang mang thai mà làm tăng ca đều bị báo đỏ. Hợp đồng quá hạn bị báo |
| Không bị khách bắt đền | CanDoiVai, VaiKhach, DonHang | Bắt được vải yard ghi nhầm thành mét, tiền phạt giao trễ, hóa đơn xuất nhiều hơn số giao, mã đơn trùng |
| Không mất dữ liệu | SaoLuu_1Cham.bat, `_apex\backup_goc_2026-11-14` | Đã chạy thử ra file zip. Bản gốc đã so mã kiểm tra, khớp 100% |
| Lương tháng 11 tính theo cách mới | BangLuong (đang để tháng 11/2026) | Đã chạy thử cả tháng mới: người mới, tạm ứng, khoản đã duyệt, mã nhân viên sai |

## Còn phải nói thật với anh
- **Mấy con số luật cần chị Vân xác nhận:** lương tối thiểu vùng III năm 2026 là 4.140.000đ (theo Nghị định 293/2025, nhưng xưởng thuộc vùng nào sau sáp nhập thì phải tra lại), hệ số tăng ca đêm 210%, và mức trần 300 giờ tăng ca/năm. Mức 300 giờ chỉ áp dụng khi làm hàng xuất khẩu và xưởng đã gửi thông báo, nếu không thì trần là 200 giờ. Mọi chỗ cần xác nhận đều có ghi chú bên cạnh trong file.
- Mình kiểm tra trên Excel bản mới. **Mình chưa thử trên chính máy văn phòng của anh.** Anh kiểm tra trong 1 phút như sau:
  1. Mở file, vào sheet BangLuong. Ô C3 phải hiện chữ "KHỚP".
  2. Làm theo HuongDan mục 0 để chắc chắn máy hiểu ngày theo kiểu ngày/tháng/năm (gõ 05/11/2026 thì máy phải hiểu là tháng 11).
- File nặng khoảng 6 MB vì có sẵn công thức cho 20.000 dòng sản lượng, tức đủ dùng khoảng 1 năm cho cả 3 tổ. Máy cũ mở có thể chậm vài giây.
- Ngày dự sinh của chị Mai mình tạm ghi là 15/01/2027. Anh hỏi lại chị Mai rồi sửa ở NhanSu cột N.
- Giờ tăng ca từ tháng 1 đến tháng 9 bị mất, nên file chưa cảnh báo được ai đã vượt trần cả năm. Ở ChamCong có sẵn dòng "SỐ DƯ ĐẦU NĂM" cho từng người. Anh nhập theo sổ, nhất là cho Lan và Mai.

Khi rảnh, anh gửi mình danh sách người của tổ 2, tổ 3, kèm chi phí điện, thuê xưởng, sửa máy mỗi tháng. Có hai thứ đó thì bảng lãi/lỗ sẽ ra số thật cho mọi đơn.

## Files created
- `xuong_may_thanh_dat/QuanLyXuong_ThanhDat_2026.xlsx`: file quản lý chính, 20 sheet
- `xuong_may_thanh_dat/SaoLuu_1Cham.bat`: sao lưu 1 chạm
- `xuong_may_thanh_dat/TIN_NHAN_MAU.txt`: tin nhắn soạn sẵn gửi Hanbok, An Phát, chị Vân và nhóm Zalo
- `xuong_may_thanh_dat/_apex/TRACE.md`: 35 việc, mỗi việc kèm bằng chứng đã kiểm
- `xuong_may_thanh_dat/_apex/REVIEW.md`: bản rà soát gọn, có phần 12–24 tháng tới
- `xuong_may_thanh_dat/_apex/IMPROVEMENT-LOG.md`: nhật ký cải tiến, kèm câu lệnh dùng để rà lại sau 1–3 tháng
- `xuong_may_thanh_dat/_apex/SHA256_goc_2026-11-14.txt` và thư mục `_apex/backup_goc_2026-11-14/` (9 file gốc, chỉ đọc)
- `xuong_may_thanh_dat/_apex/build/` (build.py, finalize.py, oracle.py, peek.py, recalc.ps1, recalc_many.ps1, make_all.sh, final_nocalc.xlsx): dùng để dựng lại file từ dữ liệu gốc
- `xuong_may_thanh_dat/_apex/tests/` (test_workbook.py, results.json): 26 bài kiểm tra chạy trên Excel thật
