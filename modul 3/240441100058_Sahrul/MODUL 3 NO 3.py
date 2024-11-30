def hitung_denda(lama_sewa):
    
    keterlambatan = lama_sewa - 1
    denda = 0

    if keterlambatan > 0:
        denda += keterlambatan * 500000
        if keterlambatan > 10:
            denda += ((keterlambatan - 10) // 5 + 1) * 5500

    return denda
while True:
    lama_sewa = int(input("Masukkan lama sewa: "))
    total_denda = hitung_denda(lama_sewa)
    print(f"Total denda keterlambatan: Rp {total_denda}")
    ulang = input("Ingin menghitung kembali? (ya/tidak): ")
    if ulang != 'ya':
        break
