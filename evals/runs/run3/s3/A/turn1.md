Chào anh, em đã đọc hết 8 file trong thư mục và tính lại từng dòng. Em nói thẳng trước: **chưa nên đem bảng chia lãi hiện tại ra Đại hội.** Có ba lý do: script của cháu Khoa tính sai, con số 1,46 tỷ chưa chắc là tiền thật có để chia, và cách chia 100% theo vốn góp nhiều khả năng không đúng Luật HTX, lại đúng vào chỗ bà con đang thắc mắc.

Em không sửa file gốc nào. Em viết một script mới, chạy ra bảng cảnh báo và bảng chia lãi nháp (danh sách ở cuối).

---

## 1. Script chia lãi cũ sai ở đâu

| Lỗi | Hậu quả |
|---|---|
| Cột `da_tru` có hộ ghi "x" thường (cô Ngân), có hộ ghi "X" hoa (anh Hùng). Script chỉ nhận "X" hoa | 8 phiếu ứng **đã trừ rồi lại bị trừ lần nữa**, cộng thêm lãi tới 31/12. Chị Lê Thị Thắm (TV053) bị tính ra **âm 7,8 triệu**. TV017, TV009, TV012, TV022, TV050 bị trừ oan 3–11 triệu mỗi hộ |
| Ghi cứng 1,46 tỷ | Số tạm của cô Ngân, chưa đối chiếu (xem mục 2) |
| Chia cả cho anh Mai Văn Bảo (TV033), người đã rút từ 08/2025 | Anh Bảo được 13,6 triệu tiền lãi, trong khi việc phải làm là hoàn 15 triệu vốn cho anh ấy |
| Không trích quỹ nào, chia hết sạch | Trái Luật HTX (mục 4) |
| Anh Lộc (TV060) vào HTX tháng 2/2026 vẫn được tính đủ 12 tháng vốn | Thiệt cho người góp vốn cả năm |
| File kết quả ghi không có BOM | Mở bằng Excel thì tiếng Việt bị lỗi font |

## 2. Lãi thật để chia: khoảng 0,88–1,06 tỷ, không phải 1,46 tỷ

| | Số tiền (đ) |
|---|---|
| Lãi tạm tính (cô Ngân) | 1.458.794.000 |
| − Anh Phát còn nợ, không hợp đồng, gọi không nghe máy | −380.000.000 |
| − Tiền HTX còn nợ bà con (6 phiếu cô Ngân quy đổi theo chuẩn 12,5% thay vì 13%) | −15.271.000 |
| − Hoàn phần lãi ứng phân vượt trần (mục 5) | −1.495.633 |
| **= Lãi sau điều chỉnh** | **1.062.027.367** |
| − Quỹ đầu tư phát triển 10% (tạm tính) | −106.202.737 |
| − Phần lãi đến từ cà phê người ngoài HTX (8,4% sản lượng) | −80.614.426 |
| **= Lãi đem chia thành viên** | **≈ 875 triệu** |

Khi nào thu được nợ anh Phát thì chia bổ sung. Bảng này **chưa tính** thuế TNDN, giá trị 3.200 kg tồn kho (cà phê bị ẩm mốc), tiền mua phân để cho ứng (gốc 119 triệu) và tiền lãi ứng thu về. Anh hỏi cô Ngân giúp em mấy khoản này đã nằm trong con số 600 triệu chi phí chưa.

## 3. Những việc Ban kiểm soát phải làm rõ trước Đại hội

Em không kết luận ai sai. Nhưng nếu không giải trình được thì tới Đại hội sẽ bị hỏi.

1. **Thiếu 7,3 tấn cà phê, khoảng 775 triệu, bằng nửa số lãi.** Cà phê mua vào đã quy đổi về 13% ẩm được 199.715 kg, bán ra 189.170 kg, tồn 3.200 kg, vậy thiếu 7.345 kg (3,7%). Cà phê đã quy về ẩm chuẩn rồi thì hao hụt "phơi sấy bình thường" không thể lớn tới mức đó. Còn một chỗ vô lý nữa: lô bán ngày 20/8 ghi "bán vét kho" mà tháng 11 lại đếm được 3.200 kg tồn.
2. **5 phiếu cân không trừ ẩm.** Đó là 3 phiếu của anh Lê Văn Tư (TV009, anh trai anh Hùng) và 2 phiếu của chị Lê Thị Hạnh (TV012). Độ ẩm 17–17,5% mà vẫn ghi đủ ký, HTX trả dư **118,5 triệu**. Như vậy khiếu nại của ông Y Wăn Niê là có cơ sở. Riêng hộ anh Tư bán 14,3 tấn trên 2,5 ha, tức 5,7 tấn/ha, cao gấp đôi mặt bằng chung.
3. **Anh Hùng một mình cân, ghi sổ, chi tiền mặt và giữ kho**, áp dụng cho cả 49/49 phiếu, không có chữ ký người bán, không có biên bản đo ẩm. Sổ quỹ tiền mặt cũng chưa đối chiếu với file thu mua.
4. **TV017 Y Bliêng Niê và TV058 Y Bliên Niê trùng cả số CCCD lẫn số điện thoại.** TV058 mới vào năm 2025, có 30 triệu vốn và nhận ứng phân 8,5 triệu. Cộng hai mã lại thì 2 ha bán 14,5 tấn. Em đã để TV058 ở trạng thái *tạm giữ, chưa chi*.
5. **Vốn góp của anh Nguyễn Văn Sáu (TV023) tăng từ 20 lên 50 triệu** so với danh sách năm 2024, cần có phiếu thu.
6. **Bà Hoa (TV041) đã mất.** Phần lãi cùng 40 triệu vốn phải trả cho **những người thừa kế** theo giấy tờ thừa kế. Không nên trả riêng cho anh Bình khi chưa có văn bản các đồng thừa kế thống nhất.

## 4. Chia theo cách nào

Luật HTX 2023 đặt nguyên tắc: **trích quỹ trước, sau đó chia lãi chủ yếu theo mức độ thành viên sử dụng dịch vụ**, tức là lượng cà phê bán qua HTX. Chia theo vốn góp chỉ là phần phụ. Lãi đến từ cà phê người ngoài HTX không chia như lãi của thành viên. Đây cũng đúng là điều tổ 2 và bà con đang hỏi. Mức % cụ thể em nhớ không chắc, anh nhờ cô Ngân đối chiếu Điều lệ HTX hoặc hỏi Liên minh HTX tỉnh. Em đã để sẵn các mức này thành tham số trong script.

Ví dụ một vài hộ, chia trên 875 triệu:

| Hộ | Vốn góp | Cà phê bán qua HTX | PA1: 100% theo vốn | PA2: 50/50 | PA3: 70% sản lượng / 30% vốn |
|---|---|---|---|---|---|
| TV001 (anh) | 50 tr | 0 kg | 27,5 tr | 13,7 tr | 8,2 tr |
| TV023 Nguyễn Văn Sáu | 50 tr | 0 kg | 27,5 tr | 13,7 tr | 8,2 tr |
| TV029 Y Wăn Niê | 30 tr | 5.651 kg | 16,5 tr | 21,8 tr | 23,9 tr |
| TV032 Phạm Văn Yên | 15 tr | 5.832 kg | 8,2 tr | 18,1 tr | 22,0 tr |

Có một điều tế nhị em xin nói thật với anh. Anh là người góp vốn cao nhất và vụ này không bán cà phê qua HTX. Vì vậy nếu anh đề xuất giữ cách chia theo vốn thì rất dễ bị hiểu là có lợi cho mình. Anh nên đưa 2–3 phương án ra để **Đại hội biểu quyết**. Ngoài ra, sản lượng của TV009 cần được làm rõ trước (mục 3.2), vì theo PA3 hộ này nhận nhiều nhất.

## 5. Rủi ro khác cần xử lý sớm

- **Lãi ứng phân 2%/tháng tức 24%/năm**, cao hơn mức trần 20%/năm của Bộ luật Dân sự (Điều 468). Ngoài ra có 8 phiếu ứng của những hộ đã bán cà phê cho HTX mà HTX quên trừ, lãi vẫn chạy (như trường hợp anh Y Sơn Êban). Script mặc định áp trần 20%/năm. Em đề nghị thêm: tính lãi chỉ đến ngày hộ đó bán cà phê, và Đại hội quyết lãi suất mới cho năm sau.
- **Cân hết hạn kiểm định từ 08/2024**, cân 100 kg chưa từng kiểm định. Đi mua bán mà dùng cân như vậy là sai quy định đo lường, và khi chị Hằng khiếu nại thiếu cân thì HTX không có gì để chứng minh. Anh cho kiểm định trước khi cân vụ mới.
- **File có CCCD và số điện thoại của 60 hộ đang nằm trên nhóm Zalo.** Theo quy định bảo vệ dữ liệu cá nhân, anh nên gỡ xuống. Em đã làm sẵn bản danh sách bỏ hai cột đó (file 05) để gửi nhóm.
- **21 tỷ tiền mua cà phê trả bằng tiền mặt, không có bảng kê thu mua nông sản có chữ ký người bán.** Khoản này dễ bị cơ quan thuế không chấp nhận là chi phí. Anh hỏi Thuế cơ sở giúp em.
- **Rất gấp: Tây Nguyên Green**, khách mua khoảng 40% sản lượng của HTX, đã báo từ vụ 2026–2027, tức vụ đang bắt đầu, phải có **tọa độ vườn của từng hộ và cam kết không phá rừng (EUDR)**. Nếu không có thì bị trừ 3.000đ/kg, với 75 tấn là khoảng 225 triệu, hoặc công ty không mua nữa. Nên đi lấy tọa độ cho 60 hộ ngay bây giờ.
- 6/11 lô bán (gần 10 tỷ) không có hợp đồng. Từ nay chỉ nên bán khi có hợp đồng, và không giao hàng gối đầu khi chưa nhận tiền.

## 6. Em đã làm gì và cách dùng

Em viết `kiem_tra_va_chia_lai_2026.py` để thay script cũ (file cũ vẫn giữ nguyên để đối chiếu). Chạy `python kiem_tra_va_chia_lai_2026.py` thì ra thư mục `ket_qua_2026/`, mở thẳng bằng Excel được:

- 00: tóm tắt kho, công nợ, lãi
- 01: 38 cảnh báo, trong đó 15 mức CAO
- 02: các phiếu bị quy đổi ẩm sai
- 03: nợ ứng phân, tính lại từng phiếu
- 04: bảng chia lãi nháp theo 3 phương án, có trừ nợ ứng. Hộ không đủ lãi để trừ nợ thì ghi 0 chứ không ghi âm
- 05: danh sách thành viên không có CCCD và số điện thoại

Mọi con số cần quyết định (tỷ lệ quỹ, tỷ lệ chia, lãi suất ứng, dự phòng nợ anh Phát, các hộ xử lý riêng) nằm gọn ở đầu file. Anh hoặc cháu Khoa chỉ cần sửa ở đó rồi chạy lại.

## Anh cho em biết thêm mấy điều

1. Điều lệ HTX quy định trích quỹ bao nhiêu và chia theo vốn hay theo sản lượng? Anh chụp gửi em điều khoản đó.
2. TV017 và TV058 là một người hay hai người? Khoản 30 triệu vốn của TV058 có phiếu thu không?
3. Anh Nguyễn Văn Bình (TV059) có phải con bà Hoa không? Bà Hoa còn những người thừa kế nào?
4. Con số 600 triệu chi phí đã có chứng từ chưa? Đã gồm tiền mua phân cho ứng chưa?
5. 3.200 kg tồn kho là cà phê vụ nào, khi lô 20/8 đã ghi "bán vét kho"?
6. Bước tiếp theo anh muốn em làm phần nào: **phiếu báo chia lãi riêng cho từng hộ**, viết đơn giản để đọc to hoặc ghi âm gửi Zalo cho bà con Ê Đê, **báo cáo tài chính và phương án chia lãi trình Đại hội**, hay **mẫu phiếu cân mới** (có độ ẩm, chữ ký người bán, người cân khác người chi)?

## Files created
- `htx_caphe_eatan/kiem_tra_va_chia_lai_2026.py`
- `htx_caphe_eatan/ket_qua_2026/00_tom_tat.txt`
- `htx_caphe_eatan/ket_qua_2026/01_canh_bao.csv`
- `htx_caphe_eatan/ket_qua_2026/02_dieu_chinh_do_am.csv`
- `htx_caphe_eatan/ket_qua_2026/03_no_ung_phan_bon.csv`
- `htx_caphe_eatan/ket_qua_2026/04_phuong_an_chia_lai.csv`
- `htx_caphe_eatan/ket_qua_2026/05_danh_sach_tv_cong_khai.csv`
