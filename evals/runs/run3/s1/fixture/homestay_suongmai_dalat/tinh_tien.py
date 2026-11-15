# Tinh doanh thu theo thang - em Duy viet giup (2025)
# Cach dung: xuat sheet "Dat phong" ra bookings_2026.csv roi chay: python tinh_tien.py
import csv
from collections import defaultdict

FILE = "bookings_2026.csv"

doanh_thu = defaultdict(int)
hoa_hong = defaultdict(int)
so_dem = defaultdict(int)

with open(FILE, encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["trang_thai"] == "Hủy":
            continue
        thang = r["checkin"][:7]          # vd 2026-12
        tien = int(r["tong_tien"].replace(".", "").replace(",", "") or 0)
        pct = int(r["hoa_hong_pct"] or 0)
        doanh_thu[thang] += tien
        hoa_hong[thang] += tien * pct // 100
        so_dem[thang] += int(r["so_dem"] or 0)

print("THANG       DOANH THU      HOA HONG     THUC NHAN   DEM")
for t in sorted(doanh_thu):
    print(f"{t:<9} {doanh_thu[t]:>12,} {hoa_hong[t]:>12,} {doanh_thu[t]-hoa_hong[t]:>12,} {so_dem[t]:>5}")
print("TONG:", f"{sum(doanh_thu.values()):,}")
# Cong suat phong = so dem / (6 phong * 30)
for t in sorted(so_dem):
    print(t, "cong suat", round(so_dem[t] / 180 * 100, 1), "%")
