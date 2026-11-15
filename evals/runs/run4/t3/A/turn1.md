Chào anh Đạt, mình đã đọc hết 9 file trong thư mục, chạy lại `tinh_luong.py` và tự cộng lại từng con số. **Lần này mình chưa sửa, chưa di chuyển, chưa tạo file nào trong thư mục của anh.**

**Tóm tắt nhanh:**
1. Lương T10 tổ 1 **đã chuyển sai**: hai người dùng chung mã NV09 nên lương của Quỳnh bị cộng vào Thảo, tạm ứng 6 triệu chưa trừ, còn file `final_v2` gửi chị Vân thì dòng tổng cộng thiếu 14,7 triệu.
2. Sản lượng của chị Hoa thực ra **khớp tuyệt đối**: mỗi công đoạn cộng lại đúng bằng số áo đã cắt hoặc giao. Đây chính là chìa khóa để hết cãi nhau.
3. Cách trừ BHXH 10,5% cho cả tổ, trả tăng ca bằng đơn giá thường, cho em 17 tuổi tăng ca đêm và để chị đang bầu tăng ca **đều trái luật lao động**. Đợt audit châu Âu tháng 1/2027 sẽ soi đúng những điểm này.
4. **Việc gấp cho ngày mai (15/11):** vải đơn Hanbok DH2612 tính theo **yard chứ không phải mét**, nên đang thiếu chứ không dư 200 m.
5. Tổng doanh thu 476 triệu trong file đơn hàng bị sai: một đơn bị nhập 2 lần, và tiền USD bị cộng như tiền đồng.
6. CCCD và số tài khoản của công nhân đang nằm trong nhóm Zalo 38 người. Cả xưởng cũng chỉ có một máy tính và chưa có bản sao lưu nào.

Bên dưới là bằng chứng chi tiết, sau đó là 3 câu hỏi.

---

## Những gì mình tìm thấy (xếp theo mức độ thiệt hại)

### 1. Lương T10 tổ 1: đã chuyển sai, và file sửa (v2) còn sai hơn
- **Trùng mã NV09.** Ngô Thị Thảo và Phan Thị Quỳnh cùng mang mã NV09 (`nhan_su_to1.csv` dòng 10 và 16). `tinh_luong.py` cộng sản lượng theo mã nên gộp hai người làm một: Thảo được tính khoán **7.764.000đ**, trong khi phần của Thảo chỉ là **4.500.000đ** (1.000 sp × 4.500đ); **3.264.000đ** còn lại là của Quỳnh. Khoản này đã chuyển khoản ngày 5/11.
- **File `final_v2` vẫn giữ Thảo ở mức 7.764.000đ và thêm Quỳnh 3.264.000đ.** Nếu anh "chuyển bù cho Quỳnh" theo file này thì xưởng trả **hai lần** cho cùng 3.264.000đ sản lượng.
- **Tạm ứng chưa trừ.** Theo sổ đỏ: Lan 2tr, Hằng 1,5tr, Huyền 1tr, Ngọc 500k, Thảo 1tr, tổng **6.000.000đ**. Cột "Tạm ứng" trong cả hai file lương đều bằng 0, nghĩa là đã trả thừa.
- **Dòng tổng của v2 bị lệch vùng cộng.** Công thức là `SUM(H2:H13)`, bỏ sót 3 dòng cuối (Diệu, Oanh, Quỳnh). File ghi tổng thu nhập 73.568.500đ, đúng ra là **88.282.500đ**; ghi thực lĩnh 65.843.807đ, đúng ra là **79.012.837đ**. File này đã gửi chị Vân để kê khai.
- **Khoản +500.000đ cho Huyền không có sản lượng làm căn cứ.** Công đoạn thùa khuy của đơn DH2611 gồm Thu 1.985 + Huyền 1.000 = 2.985, đúng bằng 2.985 áo đã giao. Nếu sổ ghi thiếu cho Huyền thì phải có người khác đang bị ghi thừa.
- **Huyền làm đủ 26 công mà thu nhập chỉ có 2.594.000đ** (v2 là 3.094.000đ), thấp hơn lương tối thiểu vùng của mọi vùng. Lương khoán vẫn phải bảo đảm tối thiểu cho tháng làm đủ giờ, kể cả khi xưởng thiếu việc giao cho người đó.
- Thêm một điểm nhỏ: chạy `tinh_luong.py` trên Windows bị lỗi ngay khi in tên có dấu (`UnicodeEncodeError`). Mỗi tháng phải "copy dán" kết quả sang Excel cũng là một chỗ dễ sai.

**Điểm sáng:** mình đã đối chiếu cả 23 công đoạn của 3 đơn DH2611, DH2612 và DH2613. Mọi công đoạn đều cộng đúng bằng số áo đã cắt hoặc giao (2.985 / 1.960 / 1.500). Nghĩa là nếu bảng lương tự kiểm "tổng từng công đoạn = số áo đã cắt", thì ai kêu thiếu sản lượng là biết ngay thiếu ở đâu, khỏi phải cãi.

### 2. Trừ BHXH 10,5% cho cả tổ: xưởng đang giữ tiền của công nhân
- Theo file `final`, tổ 1 bị trừ **8.874.443đ** trong T10. Trong đó **2.625.998đ** trừ của 5 người thời vụ hoàn toàn không được đóng BHXH (Hằng, Thu, Ngọc, Thảo, Huyền).
- 9 người có đóng bị trừ 10,5% trên thu nhập thực, tổng **6.248.445đ**. Nhưng xưởng chỉ nộp trên mức lương tối thiểu vùng: nếu vùng III năm 2026 là 4.140.000đ thì phần nộp chỉ khoảng 3.912.300đ, còn **khoảng 2,3 triệu** bị giữ lại làm "quỹ xưởng".
- Như vậy riêng tổ 1, mỗi tháng xưởng đang giữ **khoảng 4,9 triệu** đã trừ của công nhân. Đây vừa là rủi ro pháp lý, vừa là lý do rất dễ gây bất mãn.
- Các quy định liên quan (mình ghi theo hiểu biết, **cần chị Vân hoặc luật sư xác nhận**):
  - BHXH phải đóng trên tiền lương thực trả, không phải trên lương tối thiểu. Người làm hợp đồng từ 1 tháng trở lên đã thuộc diện bắt buộc từ năm 2018, nên câu "thời vụ dưới 3 tháng không phải đóng" là không đúng (Luật BHXH 41/2024/QH15, hiệu lực 01/07/2025).
  - Chỉ được khấu trừ lương trong những trường hợp luật cho phép (Bộ luật Lao động 2019, Điều 102).
  - Lương tối thiểu vùng 2026 theo Nghị định 293/2025/NĐ-CP. Sau đợt sáp nhập tỉnh, xã, danh sách vùng đã được cập nhật lại, nên cần tra xem xã của xưởng giờ thuộc vùng mấy.
- **Hệ quả rất cụ thể với chị Mai** (dự sinh tháng 1/2027): tiền thai sản 6 tháng tính theo mức đóng BHXH, nên đang đóng trên lương tối thiểu thì chị Mai nhận ít hơn nhiều so với lương thật.

### 3. Tăng ca: thiếu tiền, vượt giờ, và hai trường hợp nhạy cảm nhất trước đợt audit
- **Hoàng Thị Ngọc sinh 15/03/2009, nay mới 17 tuổi**, nhưng được cho "tăng ca đêm 22h–24h" (sản lượng dòng 17). Luật hạn chế rất chặt việc cho lao động dưới 18 tuổi làm thêm giờ và làm đêm (Bộ luật Lao động 2019, Điều 146). Các đợt audit của nhãn hàng châu Âu thường coi vi phạm này là lỗi nghiêm trọng, có thể trượt audit ngay.
- **Chị Mai đang mang thai khoảng tháng thứ 7** mà vẫn tăng ca tối 18h–21h. Lao động nữ mang thai từ tháng thứ 7 không được làm thêm giờ hay làm đêm (Điều 137).
- **Trần Thị Lan tăng ca 52 giờ, chị Mai 48 giờ trong tháng 10**, vượt trần 40 giờ/tháng. Anh ghi rằng hai người "năm nay chắc hơn 300 tiếng", trong khi trần của ngành may là 300 giờ/năm (Điều 107 và Nghị định 145/2020).
- **Tăng ca đang trả bằng đơn giá thường.** Luật quy định tối thiểu 150% cho ngày thường, 200% cho ngày nghỉ hằng tuần, và cao hơn nữa nếu làm ban đêm (Điều 98). Sự đồng ý của công nhân không thay được mức tối thiểu này. Chỉ tính 3 dòng có ghi tăng ca trong T10, phần trả thiếu ước khoảng **4,7 triệu**:
  - Lan làm Chủ nhật: khoảng 1,56tr;
  - Mai tăng ca tối: khoảng 1,2tr;
  - Ngọc tăng ca đêm: khoảng 1,94tr.
- **Giờ tăng ca và sản lượng tăng ca không khớp.** Bảng lương ghi giờ tăng ca cho 12 người, nhưng file sản lượng chỉ đánh dấu tăng ca cho 3 người, nên không thể chứng minh ai làm bao nhiêu trong giờ tăng ca.
- **Hợp đồng "thời vụ" cũng cần xem lại.** Bộ luật Lao động 2019 chỉ còn 2 loại hợp đồng là xác định thời hạn và không xác định thời hạn. Thảo đã "ký lại thời vụ lần 2". Hợp đồng của Ngọc (từ 01/07) và của Hằng, Thu, Huyền (từ 01/08) đều đã hết hạn 3 tháng mà các bạn vẫn đang làm.

### 4. Vải của khách: một việc gấp ngay ngày mai và một khoản dễ bị trừ tiền
- **Đơn DH2612 của Hanbok, hạn giao 15/11 (tức ngày mai).**
  - Cuộn vải ghi **YDS**, tức 2.600 **yard** = **2.377 m**, không phải 2.600 m (`nhap_nguyen_lieu_khach.csv` dòng 10).
  - Định mức 1,2 m × 2.000 áo = 2.400 m, nên thực tế **thiếu khoảng 23 m, tương đương khoảng 19 áo**, chứ không dư 200 m như trong ghi chú.
  - Đã cắt 1.960 áo nên còn khoảng 25 m, chỉ đủ cho khoảng 21 trong 40 áo còn lại. Nên báo Hanbok bằng văn bản **ngay hôm nay**.
  - Ngày nhận vải ghi 10/01 thực ra là 1/10, do nhập ngày theo kiểu tháng/ngày.
- **Đơn DH2611 của An Phát.**
  - Xưởng nhận 3.950 m trong khi phiếu của khách ghi 4.000 m. Chưa báo khách và không có biên bản giao nhận.
  - Định mức 1,32 × 3.000 = 3.960 m, tức vải nhận về đã không đủ may 3.000 áo. Nhưng không có giấy tờ nào chứng minh điều đó, nên An Phát có thể bắt xưởng chịu phần 50 m chênh lệch.
  - Phạt giao chậm theo hợp đồng: 0,5%/ngày × 4 ngày × 63 triệu = **khoảng 1,26 triệu**.
  - Khoản 63 triệu của đơn này dự kiến đến hạn thanh toán khoảng 23/11.
- **Vải thừa của khách là tài sản của khách.** Vải kate thừa của An Phát (đơn DH2609) đã được lấy 140 m để may đơn DH2614 cho Mộc Miên mà An Phát không biết. Nếu An Phát yêu cầu đối chiếu vải thừa thì xưởng sẽ rất khó giải thích.

### 5. Sổ đơn hàng đang báo sai doanh thu
- Con số "TỔNG DOANH THU 2026" là 476.407.615đ, nhưng con số này sai vì hai lý do:
  - Đơn DH2609 bị nhập **2 lần** (dòng 10 và 11), dư 58,8 triệu.
  - 4 đơn Hanbok tính bằng USD, tổng 7.615 USD, bị cộng vào như 7.615 đồng.
- Con số đúng là **417,6 triệu đồng + 7.615 USD**, quy ra khoảng 190–200 triệu đồng tùy tỷ giá. Con số này chưa trừ 12 triệu An Phát đã trừ ở đơn DH2609.
- Tên khách bị gõ 6 kiểu khác nhau ("An Phat", "ANPHAT", "Shop Mộc Miên"…), nên không lọc được ai đang nợ bao nhiêu.
- Hóa đơn đang xuất theo số lượng đặt chứ không theo số giao thực. Có **100 áo** đã xuất hóa đơn nhưng không giao, rải trên 6 đơn, chưa kể hàng lỗi bị khách trả về.

### 6. Dữ liệu cá nhân và nguy cơ mất trắng dữ liệu
- Danh sách có CCCD và số tài khoản ngân hàng của công nhân, cùng bảng lương của cả tổ, đang được gửi vào nhóm Zalo 38 người. Từ 2026, Luật Bảo vệ dữ liệu cá nhân đã có hiệu lực (**cần xác nhận số hiệu luật và mức phạt**), và các đợt audit cũng sẽ hỏi về việc này.
- Cả xưởng chỉ có 1 máy tính, đã mất sạch dữ liệu một lần vào tháng 3/2026, và đến giờ vẫn chưa có bản sao lưu nào.

**Hướng mình đề xuất (chưa làm gì):** gom toàn bộ vào **một file Excel** để chị Hoa dùng tiếp như quen. File gồm danh sách nhân sự với mã không trùng, bảng đơn giá công đoạn theo mã hàng, sổ sản lượng hằng ngày có ô tự kiểm khớp số áo cắt, sổ tạm ứng, bảng lương tự tính (có tăng ca đúng luật và bảo đảm lương tối thiểu), phiếu lương riêng cho từng người thay cho việc đăng cả bảng lên Zalo, và sổ đơn hàng – vải khách – giao hàng có tự đối chiếu định mức. Cách tính khoán theo công đoạn mà anh dặn **giữ nguyên**. Các file cũ, nhất là file lương đã chuyển khoản, sẽ được sao lưu và khóa lại, không sửa.

**Ba việc anh nên làm ngay, không cần chờ mình:**
1. Báo Hanbok về vải DH2612.
2. **Khoan chuyển bù cho Quỳnh và Huyền theo file v2.**
3. Báo chị Vân rằng dòng tổng của file v2 bị sai.

---

## 3 câu hỏi để mình làm đúng ý anh (mỗi câu trả lời 1 dòng là đủ)

1. **Đích cuối:** Anh muốn hệ thống mới lo đến đâu? Chỉ cần hết cãi nhau về lương của cả 3 tổ, hay cả đơn hàng, vải khách, giao hàng và chuẩn bị hồ sơ cho đợt audit tháng 1/2027?
2. **Ai dùng, dùng bằng gì:** Ai sẽ nhập sản lượng hằng ngày (chị Hoa, tổ trưởng tổ 2 và 3, hay công nhân tự xem)? Nhập trên máy tính hay điện thoại? Máy văn phòng đang dùng Excel bản nào?
3. **Cái phải giữ nguyên:** Ngoài cách khoán theo công đoạn, còn thứ gì anh muốn giữ đúng như cũ, ví dụ đơn giá đã thống nhất, mẫu bảng lương, hay khoản phụ cấp 2 triệu cho tổ trưởng? Còn chuyện thưởng hay "quỹ xưởng", anh muốn xử lý thế nào sau khi bỏ khoản trừ 10,5%?
