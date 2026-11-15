Chào anh, mình đã xem hết 9 file trong thư mục (đơn hàng, sản lượng, 2 bản bảng lương, nhân sự, NPL, giao hàng, ghi chú và `tinh_luong.py`). Nói thẳng: tháng nào cũng cãi nhau là có lý do, vì bảng lương đang sai thật chứ không phải do công nhân khó tính. Ngoài lương còn vài chuyện gấp hơn, mình để lên đầu.

## 1. Việc cần làm ngay trong tuần này

1. **Gỡ danh sách nhân sự (CCCD, số tài khoản) và bảng lương khỏi nhóm Zalo 38 người.** Cả nhóm đang xem được giấy tờ và lương của nhau, việc này vi phạm quy định bảo vệ dữ liệu cá nhân. Từ nay gửi cho chị Vân qua kênh riêng, còn phiếu lương thì gửi riêng từng người.
2. **Đơn DH2612 Hanbok, hạn giao 15/11 (ngày mai):** cuộn vải ghi **2.600 YDS, tức yard chứ không phải mét**, quy ra chỉ được **2.377 m**. Nếu định mức 1,2 là mét thì cần 2.400 m, tức là **thiếu khoảng 23 m (≈19 áo)** chứ không phải dư 200 m. Tháng 10 đã cắt 1.960 áo. Anh hỏi lại Hanbok định mức tính bằng mét hay yard rồi báo khách trước khi giao.
3. **Phan Thị Quỳnh chưa nhận đồng lương T10 nào.** Quỳnh bị gõ trùng mã NV09 với Ngô Thị Thảo, mà `tinh_luong.py` cộng theo mã, nên tiền công của Quỳnh (3.264.000đ) đã chuyển vào lương Thảo ngày 5/11. Anh nên trả Quỳnh trước, sau đó nói chuyện riêng với Thảo, cho xem sản lượng và thỏa thuận bằng giấy cách trả lại dần. Đừng tự ý trừ lương Thảo.
4. **Dừng tăng ca và ca đêm cho 2 người:**
   - Chị **Mai** đang mang thai, dự sinh 1/2027. Từ tháng thứ 7 luật cấm cho làm thêm giờ và làm đêm.
   - **Hoàng Thị Ngọc** sinh 15/03/2009, **mới 17 tuổi**, mà T10 đã làm ca đêm 22h–24h. Người dưới 18 tuổi chỉ được làm thêm hoặc làm đêm ở một số nghề theo danh mục của Bộ. Với đợt audit châu Âu, đây là lỗi rất nặng.
5. **Sao lưu ngay:** đưa thư mục lên Google Drive hoặc OneDrive và chép thêm ra USB. Tháng 3 đã mất dữ liệu một lần rồi.

## 2. Vì sao lương tháng nào cũng sai

| Lỗi | Hậu quả T10 |
|---|---|
| Trùng mã NV09 (Thảo và Quỳnh) | Thảo nhận 7.764.000 tiền khoán, đúng ra là 4.500.000. Quỳnh nhận 0 |
| File `final_v2` có công thức tổng `SUM(H2:H13)` | Sót Oanh và Quỳnh: tổng ghi 73.568.500 trong khi thật là 88.282.500. Đây là file đã gửi chị Vân kê khai |
| Huyền được cộng tay 500.000 vì "sổ ghi thiếu" | Công đoạn thùa khuy DH2611 đã ghi đủ 2.985 = số áo giao. Nếu Huyền bị ghi thiếu thì phải có người khác bị ghi thừa, cần dò sổ chứ không cộng tay |
| Tạm ứng ghi ở sổ đỏ, không có trong file | 6.000.000 tạm ứng (Lan, Hằng, Huyền, Ngọc, Thảo) chưa trừ |
| Trừ 10,5% BHXH cho cả tổ, tính trên toàn bộ thu nhập | Đã trừ 8.874.443, trong khi chị Vân chỉ nộp 10,5% × 4.140.000 cho 9 người có đóng (= 3.912.300). **Khoảng 4,96 triệu/tháng giữ lại "quỹ xưởng" là tiền lương của công nhân**, luật không cho trừ |
| Tăng ca trả bằng đơn giá thường | Luật quy định tối thiểu 150% ngày thường, 200% Chủ nhật, làm đêm cộng thêm, áp dụng cả với lương khoán. Công nhân "đồng ý" mức thấp hơn thì thỏa thuận đó cũng không có hiệu lực. T10 còn thiếu: Lan 1.560.000, Mai 1.200.000, Ngọc 1.760.000 |
| Giờ tăng ca gõ tay trên bảng lương, sổ sản lượng không ghi | 10 người có giờ tăng ca (Hoa 20h, Tú 24h...) nhưng sổ sản lượng không có dòng tăng ca nào, nên không biết phải trả phụ trội bao nhiêu |
| Lương khoán giờ thường dưới lương tối thiểu vùng | Huyền 2.294.000 và Ngọc 3.588.000 cho đủ 26 công, thấp hơn 4.140.000 (vùng III) |

Nguyên nhân gốc: sản lượng do công nhân tự báo cuối ngày, qua 3 lần chép (sổ tay → máy → script → dán Excel), không đối chiếu với số sản phẩm thật, và cả bảng lương bị đưa lên nhóm chung.

**Lương T10 tính lại** (sheet `BangLuong` trong file mới):

| Người | Đã chuyển 5/11 | Đúng ra | Chênh lệch | Lý do chính |
|---|---:|---:|---:|---|
| Quỳnh | 0 | 3.264.000 | **+3.264.000** | chưa được trả |
| Ngọc | 5.054.960 | 7.460.000 | +2.405.040 | phụ trội ca đêm, bù lương tối thiểu, không trừ BHXH, trừ tạm ứng |
| Mai | 6.282.900 | 7.785.300 | +1.502.400 | phụ trội tăng ca, BHXH trừ đúng mức |
| Huyền | 2.321.630 | 3.440.000 | +1.118.370 | bù lương tối thiểu, trừ tạm ứng |
| Thu | 3.332.532 | 3.723.500 | +390.968 | không đóng BHXH nên không được trừ |
| 8 người có đóng BHXH còn lại | | | +91.980 đến +261.030 mỗi người | trước bị trừ BHXH quá mức (riêng Lan: được thêm phụ trội tăng ca, bị trừ tạm ứng 2 triệu) |
| Hằng | 4.457.100 | 3.480.000 | −977.100 | trừ tạm ứng 1,5 triệu |
| Thảo | 7.217.280 | 3.800.000 | **−3.417.280** | đã nhận tiền của Quỳnh, trừ tạm ứng |
| **Tổng** | **75.644.057** | **81.524.200** | **+5.880.143** | |

Bảng này tính theo các giả định: vùng III, mức đóng BHXH = lương tối thiểu như chị Vân đang làm, ca đêm của Ngọc rơi vào ngày thường, tạm ứng trừ hết một lần.

## 3. Đơn hàng, vải, giao hàng

- **Dòng "TỔNG DOANH THU 2026" 476.407.615 bị sai:** DH2609 nhập 2 dòng (thừa 58,8 triệu), và 7.615 USD của Hanbok bị cộng như 7.615 đồng. Con số đúng là **417.600.000đ + 7.615 USD** (giá trị đơn đặt, chưa trừ khoản bị phạt).
- **DH2611 An Phát:** phiếu xuất của khách ghi 4.000 m, xưởng đếm được 3.950 m nhưng **chưa báo khách**. Định mức 1,32 × 3.000 = 3.960 m, nghĩa là ngay từ đầu đã thiếu vải cho khoảng 8 áo. Điều này giải thích một phần chuyện giao thiếu 15 áo. Anh nên báo bằng văn bản ngay, kẻo lúc quyết toán bị trừ tiền.
- **DH2609 bị trừ 12 triệu:** nếu hợp đồng cũng phạt 0,5%/ngày như DH2611 thì trễ 3 ngày chỉ khoảng **882.000đ**. Luật thương mại cũng giới hạn mức phạt tối đa 8%. Anh xin An Phát bảng tính và chứng từ phí đổi tàu. DH2611 trễ 4 ngày, theo hợp đồng phạt khoảng 1.260.000đ.
- **140 m vải kate của An Phát đang dùng may đơn Mộc Miên:** vải dư vẫn là tài sản của khách. Anh cần văn bản An Phát đồng ý hoặc mua lại. Khi audit mà bị phát hiện thì rất khó giải thích.
- **Hóa đơn xuất theo số đặt:** có 6 lần giao mà hóa đơn ghi dư tổng cộng 100 sản phẩm so với thực giao, 7 lần giao không có biên bản ký nhận. Hóa đơn phải ghi đúng số giao thực tế.
- Ngày của các đơn Hanbok ghi kiểu tháng/ngày lẫn với ngày/tháng. Mình đã đổi về cùng một kiểu. Riêng DH2603 ghi "02/03" không chắc là ngày nào, anh kiểm tra lại giúp.

## 4. Hợp đồng và BHXH (audit tháng 1 sẽ xem đúng mấy chỗ này)

- **Hợp đồng đã hết hạn:** Hằng, Thu, Huyền hết 31/10. Ngọc hết 30/09, đã quá 30 ngày mà vẫn làm nên theo luật hợp đồng thành không thời hạn. Thảo đã ký 2 lần, lần tới phải ký không thời hạn. Những người "12 tháng" làm từ 2016–2023 nhiều khả năng cũng đã phải chuyển sang không thời hạn.
- **BHXH:** câu "thời vụ dưới 3 tháng không phải đóng" là không đúng. Hợp đồng từ đủ 1 tháng đã phải đóng, mà hợp đồng 3 tháng cũng không phải "dưới 3 tháng". Hiện có 6 người chưa đóng. Ngoài ra đóng theo lương tối thiểu trong khi thực trả 5–11 triệu dễ bị truy thu, và chị Mai sắp nghỉ sinh cũng chỉ được hưởng theo mức đóng thấp đó.
- **Giờ tăng ca:** giới hạn là 40 giờ/tháng và 300 giờ/năm (ngành may). T10 Lan làm 52h, Mai 48h, và năm nay cả hai đã quá 300h.
- **Lương tối thiểu vùng:** sau đợt sáp nhập tỉnh/xã, vùng có thể đã đổi. Nhờ chị Vân xác nhận. Trong file mình để 4.140.000 (vùng III, theo NĐ 293/2025), đổi ở một ô là mọi chỗ tự cập nhật.

*Mình không phải luật sư. Các mốc luật trên (Bộ luật Lao động 2019, Luật BHXH, NĐ 293/2025...) anh nhờ chị Vân hoặc luật sư lao động xác nhận trước khi áp dụng, nhất là phần truy đóng BHXH.*

## 5. Mình đã làm lại gì

File mới: `xuong_may_thanh_dat/HE_THONG_MOI/QuanLyXuong_ThanhDat.xlsx`. Mình **không sửa file gốc nào**.

Gom tất cả về **1 file Excel**, đã chuyển sẵn dữ liệu tổ 1 tháng 10 vào:

| Sheet | Dùng để |
|---|---|
| `ViecCanXuLy` | 20 việc ở trên, có hạn, người làm, ô đánh dấu xong |
| `KiemTra` | 13 phép kiểm tra. Trước khi chốt lương tất cả phải về 0 |
| `NhanSu` | Mỗi người 1 mã (Quỳnh đổi thành **NV15**). Tự cảnh báo trùng mã, dưới 18 tuổi, hợp đồng hết hạn, chưa đóng BHXH. **Không chứa CCCD và số tài khoản** |
| `DonGia` | Đơn giá theo đơn và công đoạn, chốt trước khi may |
| `SanLuong` | Mỗi dòng là 1 người × 1 công đoạn × 1 ngày. Chỉ cần chọn mã NV và loại ca, tên, đơn giá, tiền tăng ca tự ra. Gõ sai tên công đoạn là báo đỏ ngay |
| `ChamCong`, `TamUng`, `DaTra` | Ngày công, tạm ứng (thay cho sổ đỏ), số đã chuyển khoản |
| `BangLuong` | Đổi ô tháng là tự tính. Dòng tổng cộng đủ mọi người, không còn kiểu sót dòng như `final_v2`. **Không cần chạy `tinh_luong.py` và copy-dán nữa** |
| `PhieuLuong` | Chọn mã NV là ra phiếu lương có chi tiết từng dòng sản lượng, để in hoặc gửi riêng |
| `DoiChieu` | Tổng số lượng mọi người ghi cho 1 công đoạn so với số sản phẩm của đơn. **Ai kêu thiếu thì mở sheet này ra trước** |
| `DonHang`, `NPL`, `QuyetToanVai`, `GiaoHang` | Mỗi đơn 1 dòng, VND và USD cộng riêng, vải yard tự quy ra mét, tính thiếu/dư vải theo định mức, cảnh báo hóa đơn dư, giao trễ, khoản phạt bị trừ quá mức |
| `ThamSo` | Lương tối thiểu, tỷ lệ BHXH, hệ số tăng ca. Sửa một chỗ là cả file cập nhật |

Mình đã mở file bằng Excel trên máy và tính lại: không có ô nào báo lỗi, số liệu khớp với các con số ở trên. Mình cũng thử nhập sản lượng tháng 11 thì bảng lương tự lên, gõ sai tên công đoạn thì sheet `KiemTra` báo lỗi.

**Còn thiếu:**
- Chưa có tổ 2 và tổ 3.
- Sản lượng T10 không có ngày cụ thể.
- Chấm công mới là tổng cả tháng, chưa theo từng ngày.
- Các đơn cũ chưa có định mức vải nên chưa quyết toán vải được.

**Để hết cãi nhau về lâu dài**, mình gợi ý thêm 2 việc:
- **Phiếu bó hàng:** mỗi bó 10–20 sản phẩm đi kèm một phiếu có cuống cho từng công đoạn. Làm xong công đoạn nào thì xé cuống nộp tổ trưởng. Như vậy sản lượng có bằng chứng, không còn dựa vào lời khai cuối ngày.
- **Gửi phiếu sản lượng riêng cho từng người mỗi tuần**, để chỗ nào sai thì sửa ngay trong tuần, không dồn tới cuối tháng.

## Anh trả lời giúp mình mấy câu để làm tiếp

1. **Lương T10:** anh có trả bù và thu lại theo bảng tính lại ở trên không, hay chỉ sửa từ T11? Khoản tạm ứng của Hằng (đang âm 977.100) trừ hết một lần hay chia ra?
2. **Tăng ca và BHXH:** anh có đồng ý tính theo luật từ T11 không? Khoản 10,5% trừ thừa bỏ vào "quỹ xưởng" bắt đầu từ tháng nào và hiện còn bao nhiêu, để mình tính số hoàn lại cho từng người?
3. **DH2612:** định mức 1,2 là mét hay yard? Hiện đã xong bao nhiêu áo?
4. **Tổ 2, tổ 3:** tổ trưởng ghi trên giấy hay dùng được điện thoại? Nếu dùng được điện thoại, mình có thể chuyển file sang Google Sheets để các tổ nhập trực tiếp, anh xem từ xa, lại tự sao lưu luôn.
5. Máy văn phòng đang dùng Excel bản nào? File mình làm chạy được từ Excel 2010 trở lên.

## Files created

- `<scratch>/eval4/t3/B/work/xuong_may_thanh_dat/HE_THONG_MOI/QuanLyXuong_ThanhDat.xlsx`: file quản lý mới (17 sheet, đã có dữ liệu T10 và bảng lương T10 tính lại)
- `<scratch>/eval4/t3/B/work/_build/tao_file_quan_ly.py`: script mình dùng để tạo file Excel từ các CSV cũ (chỉ đọc, không sửa file gốc). Anh không cần dùng script này
