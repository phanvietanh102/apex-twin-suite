# tinh_luong.py - chau Minh (con anh chu) viet thang 6/2026
# Chay: python tinh_luong.py san_luong_to1_T10.csv
# In ra luong khoan tung nguoi de chi Hoa copy vao Excel
import csv
import sys

BHXH_RATE = 0.105  # tru het cho ca xuong cho don gian, chi Hoa bao vay

def main(path):
    tong = {}
    ten = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ma = row["Mã NV"].strip()
            sl = int(row["Số lượng"])
            gia = int(row["Đơn giá (đ/sp)"])
            # cot "Ca" khong dung, tang ca cung tinh theo don gia khoan
            tong[ma] = tong.get(ma, 0) + sl * gia
            ten.setdefault(ma, row["Họ tên"])
    print("Ma NV,Ho ten,Luong khoan,BHXH tru,Con lai")
    for ma in sorted(tong):
        lk = tong[ma]
        bh = round(lk * BHXH_RATE)
        print(f"{ma},{ten[ma]},{lk},{bh},{lk - bh}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "san_luong_to1_T10.csv")
