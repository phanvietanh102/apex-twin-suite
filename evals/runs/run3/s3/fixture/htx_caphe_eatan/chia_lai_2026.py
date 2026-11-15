# Bang chia lai cuoi nam cho thanh vien HTX - chau Khoa viet 11/2025, sua 11/2026
# Chay: python chia_lai_2026.py  -> ra file chia_lai_2026_ketqua.csv de in cho Dai hoi
import csv
from datetime import date

LOI_NHUAN = 1_460_000_000      # so co Ngan bao
NGAY_CHOT = date(2026, 12, 31)

def doc(file):
    with open(file, encoding="utf-8") as f:
        return list(csv.DictReader(f))

thanh_vien = doc("thanh_vien_2026.csv")
ung = doc("ung_vat_tu_2025.csv")

tong_von = sum(int(tv["von_gop"]) for tv in thanh_vien)

# tien ung chua tru (+ lai 2%/thang den ngay chot)
no_ung = {}
for u in ung:
    if u["da_tru"] == "X":
        continue
    d = date.fromisoformat(u["ngay"])
    so_thang = (NGAY_CHOT.year - d.year) * 12 + NGAY_CHOT.month - d.month
    tien = int(u["thanh_tien"]) * (1 + float(u["lai_thang_pct"]) / 100 * so_thang)
    no_ung[u["ma_tv"]] = no_ung.get(u["ma_tv"], 0) + tien

ket_qua = []
for tv in thanh_vien:
    duoc_chia = LOI_NHUAN * int(tv["von_gop"]) / tong_von     # chia theo von gop nhu nam ngoai
    tru = no_ung.get(tv["ma_tv"], 0)
    ket_qua.append({
        "ma_tv": tv["ma_tv"],
        "ho_ten": tv["ho_ten"],
        "von_gop": tv["von_gop"],
        "duoc_chia": int(duoc_chia),
        "tru_ung_phan": int(tru),
        "con_nhan": int(duoc_chia - tru),
    })

with open("chia_lai_2026_ketqua.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ket_qua[0].keys())
    w.writeheader()
    w.writerows(ket_qua)

print("Da chia", f"{sum(k['duoc_chia'] for k in ket_qua):,}", "cho", len(ket_qua), "thanh vien")
am = [k for k in ket_qua if k["con_nhan"] < 0]
print("So ho con nhan am:", len(am))
