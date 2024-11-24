klub_basket = {"Ucup", "Ucok", "Amba", "Adit", "Agus"}
klub_renang = {"Yanto", "Adit", "Rangga", "Adi", "Amba", "Bagus"}

siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)
print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
