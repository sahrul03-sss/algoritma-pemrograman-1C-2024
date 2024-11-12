data_karyawan = []

def tambah_karyawan():
    data_karyawan.append((
        input("\nMasukkan NIP: "),
        input("Masukkan Nama: "),
        input("Masukkan Alamat: "),
        input("Masukkan Departemen: "),
        input("Masukkan Jabatan: ")
    ))
    print("\nData karyawan berhasil ditambahkan!")

def tampilkan_karyawan(karyawan):
    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(atribut, nilai):
    hasil_cari = [karyawan for karyawan in data_karyawan if nilai in karyawan[atribut]]
    if hasil_cari:
        for karyawan in hasil_cari:
            tampilkan_karyawan(karyawan)
    else:
        print("\nkaryawan tidak valid.")

def main():
    print("------DATA KARYAWAN------")
    
    while input("\nTambah karyawan? (ya/tidak): ") == 'ya':
        tambah_karyawan()

    while True:
        print("\nPilih pencarian berdasarkan:")
        print("1. NIP\n2. Nama\n3. Alamat\n4. Departemen\n5. Jabatan\n6. Tampilkan Semua\n7. Keluar")
        
        pilihan = input("Masukkan pilihan (1-7): ")
        
        if pilihan == "1":
            cari_karyawan(0, input("Masukkan NIP: "))
        elif pilihan == "2":
            cari_karyawan(1, input("Masukkan Nama: "))
        elif pilihan == "3":
            cari_karyawan(2, input("Masukkan Alamat: "))
        elif pilihan == "4":
            cari_karyawan(3, input("Masukkan Departemen: "))
        elif pilihan == "5":
            cari_karyawan(4, input("Masukkan Jabatan: "))
        elif pilihan == "6":
            if data_karyawan:
                for karyawan in data_karyawan:
                    tampilkan_karyawan(karyawan)
            else:
                print("\nKaryawan tidak valid.")
        elif pilihan == "7":
            break
        else:
            print("Pilihan tidak valid.")

main()






