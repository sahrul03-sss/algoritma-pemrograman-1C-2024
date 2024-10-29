gaji_harian = 100000
max_lembur_per_hari = 8
max_lembur_mingguan = 40
total_gaji_mingguan = 0
total_lembur_mingguan = 0
total_gaji_lembur = 0

for hari in range(1, 8):
    lembur_harian = int(input(f"Masukkan jam lembur untuk hari ke-{hari}: "))

    if lembur_harian > max_lembur_per_hari:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur_harian = max_lembur_per_hari 
    elif total_lembur_mingguan + lembur_harian >= max_lembur_mingguan:
        lembur_harian = max_lembur_mingguan - total_lembur_mingguan
        print("Lembur mingguan telah mencapai batas, lembur di hari ini dibatasi.")

    if lembur_harian == 0:
        gaji_lembur = 0
    elif 1 <= lembur_harian < 4:
        gaji_lembur = lembur_harian * 25000
    elif lembur_harian == 4:
        gaji_lembur = 100000
    elif lembur_harian == 6:
        gaji_lembur = 200000
    elif lembur_harian == 8:
        gaji_lembur = 300000

    total_lembur_mingguan += lembur_harian
    total_gaji_lembur += gaji_lembur
    total_gaji_mingguan += gaji_harian + gaji_lembur

    print(f"Lembur hari ke-{hari}: {lembur_harian} jam")
    print(f"Gaji lembur hari ke-{hari}: Rp{gaji_lembur}")
    print("-" * 30)

total_gaji_tanpa_lembur = gaji_harian * 7
print(f"Total lembur selama satu minggu: {total_lembur_mingguan} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")