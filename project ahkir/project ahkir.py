 #wisnu
import datetime
kendaraan = [
    {"tipe": "Bus",
        "merk": [
            "White House Deluxe Coach WEHA One Minivan", 
            "Toyota Hiace 15 seat", 
            "White Horse Deluxe Coach Premiere Medium", 
            "White Horse", 
            "Tetransport Tours Microbus Hi Ace Commuter Day", 
            "Bus Pariwisata SHD 45-47 Seats"
        ],
        "harga": [500000, 1000000, 1500000, 10000, 100000, 250000],  # Harga per hari
        "denda": [500000, 1000000, 1500000, 10000, 100000, 250000]},
    {"tipe": "Mobil",
        "merk": [
            "Toyota Calya", 
            "Suzuki Ertiga", 
            "Daihatsu Xenia", 
            "Toyota Grand New Innova"
        ],
        "harga": [25000, 30000, 25000, 40000],  # Harga per hari
        "denda": [25000, 30000, 25000, 40000]},
    {"tipe": "Motor",
        "merk": [
            "Honda Beat", 
            "Honda Beat Street", 
            "Honda Genio", 
            "Honda Vario 125cc", 
            "Honda Scoopy", 
            "Yamaha Fazzio", 
            "Honda Vario 160cc", 
            "Yamaha Grand Filano", 
            "Honda Stylo", 
            "Yamaha New Nmax", 
            "Honda PCX 160cc", 
            "Vespa LX 125cc"
        ],
        "harga": [15000, 17000, 17000, 20000, 22000, 25000, 27000, 30000, 20000, 35000, 40000, 45000],  # Harga per hari
        "denda": [15000, 17000, 17000, 20000, 22000, 25000, 27000, 30000, 20000, 35000, 40000, 45000]},
    {
"tipe": "Sepeda",
        "merk": ["Sepeda Lipat", "Sepeda Gunung", "Sepeda Balap"],
        "harga": [5000, 7000, 8000],  
        "denda": [5000, 7000, 8000]}
]

penyewa = {} 

def tampilkan_menu():
    print("="*50)
    print("  SISTEM PENYEWAAN KENDARAAN")
    print("="*50)
    print("1. lihat harga dan denda per item\n2. sewa kendaraan \n3. Lihat Penyewa\n4. Update Penyewa\n5. Hitung Keterlambatan\n6. Hapus Penyewa\n7. Keluar")
    print("="*50)

def menu():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1': lihat_harga_per_item()
        elif pilihan == '2': sewa_kendaraan()
        elif pilihan == '3': lihat_penyewa()
        elif pilihan == '4': update_penyewa()
        elif pilihan == '5': hitung_keterlambatan()
        elif pilihan == '6': hapus_penyewa()  
        elif pilihan == '7': break
        else: print("Pilihan tidak valid!")

#sahrul
def lihat_harga_per_item():
    print("="*50)
    print("HARGA DAN DENDA KENDARAAN PER-ITEM")
    print("="*50)

    # Menampilkan pilihan kendaraan
    for i, k in enumerate(kendaraan, 1):
        print(f"{i}. {k['tipe']}")  

    try:
        pilihan = int(input("Pilih kendaraan (nomor): "))
        if 1 <= pilihan <= len(kendaraan):
            kendaraan_terpilih = kendaraan[pilihan - 1]
            print(f"\nHarga untuk tipe kendaraan: {kendaraan_terpilih['tipe']}")
            print("-"*100)
            print(f"{'No':<5} {'Merk Kendaraan':<50} {'Harga per hari (Rp)':<20} {'Denda per hari (Rp)':<20}")
            print("-"*100)

            # Menampilkan merk, harga, dan denda sesuai tipe kendaraan
            for idx, merk in enumerate(kendaraan_terpilih['merk'], 1):
                harga = kendaraan_terpilih['harga'][idx - 1]
                denda = kendaraan_terpilih['denda'][idx - 1]  # Denda sesuai merk
                print(f"{idx:<5} {merk:<50} {harga:<20} {denda:<20}")
            print("-"*100)
        else:
            print("Pilihan kendaraan tidak valid.")
    except ValueError:
        print("Pilihan tidak valid!")


#wisnu
def pilih_kendaraan():
    for i, k in enumerate(kendaraan, 1):
        print(f"{i}. {k['tipe']}")  # Menampilkan tipe kendaraan
    
    try:
        pilihan = int(input("Pilih kendaraan (nomor): "))
        if 1 <= pilihan <= len(kendaraan):
            kendaraan_terpilih = kendaraan[pilihan - 1]
            if kendaraan_terpilih['merk']:  # Jika kendaraan memiliki merk (seperti motor atau mobil)
                print("-" * 100)
                print(f"{'No':<5} {'Merk Kendaraan':<50} {'Harga per Hari (Rp)':<30}")
                print("-" * 100)
                for idx, merk in enumerate(kendaraan_terpilih['merk'], 1):
                    harga = kendaraan_terpilih['harga'][idx - 1]  # Mengambil harga sesuai merk
                    print(f"{idx:<5} {merk:<50} {harga:<30}")
                print("-" * 100)
                
                merk_pilihan = int(input("Pilih merk kendaraan (nomor): "))
                if 1 <= merk_pilihan <= len(kendaraan_terpilih['merk']):
                    harga_terpilih = kendaraan_terpilih['harga'][merk_pilihan - 1]
                    return kendaraan_terpilih, kendaraan_terpilih['merk'][merk_pilihan - 1], harga_terpilih
                else:
                    print("Pilihan merk tidak valid.")
                    return None
            # Jika kendaraan tidak memiliki merk, ambil harga pertama
            return kendaraan_terpilih, None, kendaraan_terpilih['harga'][0]  # Tidak ada merk
    except ValueError:
        pass
    return None

#sahrul
def sewa_kendaraan():
    kendaraan_terpilih, merk_terpilih, harga_terpilih = pilih_kendaraan()
    if not kendaraan_terpilih:
        print("Pilihan kendaraan tidak valid.")
        return
    nama = input("Masukkan nama penyewa: ")
    
    if nama not in penyewa:
        penyewa[nama] = [] 

    while True:
        try:
            hari = int(input("Berapa hari disewa? "))  
            break
        except ValueError:
            print("Masukkan angka yang valid untuk durasi sewa.")
    
    biaya = harga_terpilih * hari 
    waktu_sewa = datetime.datetime.now()
    waktu_pengembalian = waktu_sewa + datetime.timedelta(days=hari) 

    penyewa[nama].append({
        'kendaraan': kendaraan_terpilih['tipe'] + (" " + merk_terpilih if merk_terpilih else ""),
        'hari': hari,
        'biaya': biaya, 
        'waktu_sewa': waktu_sewa,
        'waktu_pengembalian': waktu_pengembalian
    })
    
    print(f"\nSewa {kendaraan_terpilih['tipe']} {merk_terpilih if merk_terpilih else ''} berhasil!")
    print(f"Nama Penyewa: {nama}")
    print(f"Durasi Sewa: {hari} hari")
    print(f"Total Biaya: Rp {biaya}")
    print(f"Waktu Sewa: {waktu_sewa.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Waktu Pengembalian: {waktu_pengembalian.strftime('%Y-%m-%d %H:%M:%S')}")

#wisnu
def lihat_penyewa():
    if not penyewa:
        print("Tidak ada penyewa yang tercatat.")
    else:
        print("-"*150)
        print(f"{'No':<5} {'Nama Penyewa':<30} {'Kendaraan':<50} {'Durasi (hari)':<15} {'Biaya (Rp)':<20}")
        print("-"*150) 
        
        nomor = 1
        for nama, daftar_kendaraan in penyewa.items():
            for kendaraan in daftar_kendaraan:
                print(f"{nomor:<5} {nama:<30} {kendaraan['kendaraan']:<50} {kendaraan['hari']:<15} {kendaraan['biaya']:<20}")
                nomor += 1
        print("-"*150)

#sahrul
def update_penyewa():
    nama = input("Masukkan nama penyewa yang ingin diupdate: ")
    if nama not in penyewa:
        print(f"Penyewa {nama} tidak ditemukan.")
        return
    
    print(f"Penyewa {nama} memiliki kendaraan sebagai berikut:")
    for idx, info in enumerate(penyewa[nama], 1):
        print(f"{idx}. {info['kendaraan']} - Durasi: {info['hari']} hari")
    
    try:
        kendaraan_index = int(input("Pilih kendaraan yang ingin diupdate (nomor): ")) - 1
        if 0 <= kendaraan_index < len(penyewa[nama]):
            print("Pilih aksi yang ingin dilakukan:")
            print("1. Ubah durasi sewa")
            print("2. Ganti kendaraan")
            aksi = input("Pilih aksi: ")

            if aksi == '1': 
                while True:
                    try:
                        hari_baru = int(input("Masukkan durasi sewa baru (hari): "))
                        break
                    except ValueError:
                        print("Masukkan angka yang valid.")
                
                biaya_baru = penyewa[nama][kendaraan_index]['biaya'] / penyewa[nama][kendaraan_index]['hari'] * hari_baru
                penyewa[nama][kendaraan_index]['hari'] = hari_baru
                penyewa[nama][kendaraan_index]['biaya'] = biaya_baru
                waktu_sewa = datetime.datetime.now()
                penyewa[nama][kendaraan_index]['waktu_sewa'] = waktu_sewa
                penyewa[nama][kendaraan_index]['waktu_pengembalian'] = waktu_sewa + datetime.timedelta(days=hari_baru)
                print(f"Durasi sewa berhasil diubah menjadi {hari_baru} hari.")

            elif aksi == '2':  
                kendaraan_terpilih, merk_terpilih, harga_terpilih = pilih_kendaraan()
                if kendaraan_terpilih:
                    biaya_baru = harga_terpilih * penyewa[nama][kendaraan_index]['hari']
                    penyewa[nama][kendaraan_index] = {
                        'kendaraan': kendaraan_terpilih['tipe'] + (" " + merk_terpilih if merk_terpilih else ''),
                        'hari': penyewa[nama][kendaraan_index]['hari'],
                        'biaya': biaya_baru,
                        'waktu_sewa': datetime.datetime.now(),
                        'waktu_pengembalian': datetime.datetime.now() + datetime.timedelta(days=penyewa[nama][kendaraan_index]['hari'])
                    }
                    print(f"Kendaraan berhasil diganti menjadi {kendaraan_terpilih['tipe']} {merk_terpilih if merk_terpilih else ''}.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Kendaraan yang dipilih tidak valid.")
    except ValueError:
        print("Pilihan tidak valid.")

#wisnu
def hitung_keterlambatan():
    nama = input("Masukkan nama penyewa untuk menghitung keterlambatan: ")
    
    if nama not in penyewa:
        print(f"Penyewa {nama} tidak ditemukan.")
        return
    
    print(f"Penyewa {nama} memiliki kendaraan sebagai berikut:")
    for idx, info in enumerate(penyewa[nama], 1):
        print(f"{idx}. {info['kendaraan']} | Waktu Pengembalian: {info['waktu_pengembalian'].strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        kendaraan_index = int(input("Pilih kendaraan yang ingin dihitung keterlambatannya: ")) - 1
        if 0 <= kendaraan_index < len(penyewa[nama]):
            kendaraan = penyewa[nama][kendaraan_index]
            harga_per_hari = kendaraan['biaya'] / kendaraan['hari']
            tanggal_input = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
            try:
                # Mengonversi tanggal input menjadi objek datetime
                waktu_pengembalian_input = datetime.datetime.strptime(tanggal_input, "%Y-%m-%d")
                
                waktu_pengembalian_sebenarnya = kendaraan['waktu_pengembalian']
                
                if waktu_pengembalian_input < waktu_pengembalian_sebenarnya:
                    print("Tanggal pengembalian lebih awal dari yang seharusnya. Tidak ada denda.")
                    return
                keterlambatan = (waktu_pengembalian_input - waktu_pengembalian_sebenarnya).days

                if keterlambatan > 0:
                    denda = keterlambatan * harga_per_hari
                    print(f"Keterlambatan: {keterlambatan} hari")
                    print(f"Denda keterlambatan: Rp {denda:,.2f}")
                else:
                    print("Tidak ada keterlambatan (pengembalian tepat waktu atau lebih awal).")
            
            except ValueError:
                print("Format tanggal salah! Harap masukkan tanggal dengan format YYYY-MM-DD.")
        else:
            print("Kendaraan yang dipilih tidak valid.")
    
    except ValueError:
        print("Pilihan tidak valid!")

#sahrul
def hapus_penyewa():
    nama = input("Masukkan nama penyewa yang ingin dihapus: ")
    if nama in penyewa:
        del penyewa[nama]
        print(f"Penyewa {nama} berhasil dihapus.")
    else:
        print(f"Penyewa {nama} tidak ditemukan.")

menu()