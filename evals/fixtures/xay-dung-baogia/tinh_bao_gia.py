# Tinh bao gia xay nha pho - ban cu
import csv, sys

GIA = {"XM": 85000, "THEP": 16000, "CAT": 420000, "DA": 350000, "GACH": 1200}

# dinh muc vat tu tren 1 m2 san xay dung (phan tho)
DINH_MUC = {"XM": 1.2, "THEP": 32, "CAT": 0.18, "DA": 0.15, "GACH": 95}

def bao_gia(dien_tich, nhan_cong_m2=1500000):
    tong = 0.0
    dong = []
    for ma, dm in DINH_MUC.items():
        sl = dien_tich * dm
        tien = sl * GIA[ma]
        dong.append((ma, sl, GIA[ma], tien))
        tong += tien
    nhan_cong = dien_tich * nhan_cong_m2
    tong = tong + nhan_cong
    vat = tong * 0.1
    return dong, nhan_cong, vat, tong + vat

if __name__ == "__main__":
    dt = float(sys.argv[1])
    dong, nc, vat, tong = bao_gia(dt)
    for d in dong:
        print(d)
    print("Nhan cong:", nc)
    print("VAT:", vat)
    print("TONG:", tong)
