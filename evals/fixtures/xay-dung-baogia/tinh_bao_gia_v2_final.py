# ban moi - dung cai nay!!! (sua gia thep thang 3)
import sys

GIA = {"XM": 92000, "THEP": 17500, "CAT": 450000, "DA": 380000, "GACH": 1350}
DINH_MUC = {"XM": 1.2, "THEP": 32, "CAT": 0.18, "DA": 0.15, "GACH": 95}
LOAI_HOAN_THIEN = {"co_ban": 2500000, "kha": 3800000, "cao_cap": 5500000}

def bao_gia(dien_tich, loai="co_ban"):
    tong = 0
    for ma, dm in DINH_MUC.items():
        tong += dien_tich * dm * GIA[ma]
    tong += dien_tich * 1500000
    tong += dien_tich * LOAI_HOAN_THIEN[loai]
    vat = round(tong * 0.1, 2)
    return round(tong + vat, 2)

if __name__ == "__main__":
    print(bao_gia(float(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else "co_ban"))
