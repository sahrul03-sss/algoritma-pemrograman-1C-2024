import datetime
kendaraan = [
    {"tipe": "Mobil", "harga_per_hari": 300000},
    {"tipe": "Motor", "harga_per_hari": 100000},
    {"tipe": "Sepeda", "harga_per_hari": 50000}
]
penyewa = {}

def tampilkan_menu():
    print("="*50)
    print("  SELAMAT DATANG DI SISTEM PENYEWAAN KENDARAAN")
    print("="*50)
    print("Pilih menu untuk memulai transaksi penyewaan kendaraan:")
    print("1. Sewa Kendaraan")
    print("2. Lihat Daftar Penyewa")
    print("3. Update Data Penyewa")
    print("4. Hapus Data Penyewa")
    print("5. Keluar")
    print("="*50)

def menu():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            sewa_kendaraan()
        elif pilihan == '2':
            lihat_penyewa()
        elif pilihan == '3':
            update_penyewa()
        elif pilihan == '4':
            hapus_penyewa()
        elif pilihan == '5':
            print("Terima kasih! Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

def hitung_biaya(harga_per_hari, hari):
    return harga_per_hari * hari

def tampilkan_kendaraan():
    print("\nDaftar Kendaraan yang Tersedia untuk Disewa:")
    for i, kendaraan_item in enumerate(kendaraan, start=1):
        print(f"{i}. {kendaraan_item['tipe']} - Rp {kendaraan_item['harga_per_hari']}/hari")

def sewa_kendaraan():
    tampilkan_kendaraan()
    try:
        pilihan = int(input("Pilih kendaraan (1-3): "))
        if pilihan not in [1, 2, 3]:
            print("Pilihan tidak valid! Silakan pilih lagi.")
            return sewa_kendaraan() 

        kendaraan_terpilih = kendaraan[pilihan - 1]
        nama = input("Masukkan nama penyewa: ")
        hari = int(input("Berapa hari kendaraan disewa? "))
        biaya = hitung_biaya(kendaraan_terpilih["harga_per_hari"], hari)

        waktu_sewa = datetime.datetime.now()
        penyewa[nama] = {
            'kendaraan': kendaraan_terpilih['tipe'],
            'hari': hari,
            'biaya': biaya,
            'waktu_sewa': waktu_sewa
        }

        print(f"\nSewa {kendaraan_terpilih['tipe']} berhasil!")
        print(f"Nama Penyewa: {nama}")
        print(f"Durasi Sewa: {hari} hari")
        print(f"Total Biaya: Rp {biaya}")
        print(f"Waktu Sewa: {waktu_sewa.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")

def lihat_penyewa():
    if not penyewa:
        print("Belum ada penyewa.")
    else:
        print("\nDaftar Penyewa yang Telah Menyewa Kendaraan:")
        for nama, info in penyewa.items():
            print(f"\nNama Penyewa: {nama}")
            print(f"Kendaraan: {info['kendaraan']}")
            print(f"Durasi Sewa: {info['hari']} hari")
            print(f"Total Biaya: Rp {info['biaya']}")
            print(f"Waktu Sewa: {info['waktu_sewa'].strftime('%Y-%m-%d %H:%M:%S')}")

def update_penyewa():
    if not penyewa:
        print("Tidak ada penyewa yang terdaftar.")
        return

    nama = input("Masukkan nama penyewa yang ingin diperbarui: ")
    if nama not in penyewa:
        print(f"Penyewa dengan nama {nama} tidak ditemukan.")
        return

    print(f"Mengupdate data penyewa {nama}.")
    tampilkan_kendaraan()
    try:
        pilihan = int(input("Pilih kendaraan baru (1-3): "))
        if pilihan not in [1, 2, 3]:
            print("Pilihan kendaraan tidak valid.")
            return

        kendaraan_terpilih = kendaraan[pilihan - 1]
        hari = int(input("Berapa hari kendaraan disewa? "))
        biaya = hitung_biaya(kendaraan_terpilih['harga_per_hari'], hari)

        penyewa[nama] = {
            'kendaraan': kendaraan_terpilih['tipe'],
            'hari': hari,
            'biaya': biaya,
            'waktu_sewa': penyewa[nama]['waktu_sewa']  
        }

        print(f"\nData penyewa {nama} berhasil diperbarui!")
        print(f"Nama Penyewa: {nama}")
        print(f"Kendaraan: {kendaraan_terpilih['tipe']}")
        print(f"Durasi Sewa: {hari} hari")
        print(f"Total Biaya: Rp {biaya}")

    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")

def hapus_penyewa():
    if not penyewa:
        print("Tidak ada penyewa untuk dihapus.")
        return

    nama = input("Masukkan nama penyewa yang ingin dihapus: ")
    if nama not in penyewa:
        print(f"Penyewa dengan nama {nama} tidak ditemukan.")
        return

    del penyewa[nama]
    print(f"\nPenyewa {nama} berhasil dihapus.")

menu()
