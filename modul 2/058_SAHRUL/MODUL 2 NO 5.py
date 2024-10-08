nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: ")) 
total_harga = float(input("Masukkan total belanja: "))
kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")

if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    diskon = 0
    if kartu_member == "ya":
        diskon += 15
    if total_harga >= 500000:
        diskon += 10
    total_diskon = (diskon / 100) * total_harga
    total_harga_setelah_diskon = total_harga - total_diskon

    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_harga}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:.2f}")
