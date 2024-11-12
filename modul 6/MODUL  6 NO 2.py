data_peminjaman = []

def main():
    while True:
        print("\n---PEMINJAMAN BUKU---")
        print("1. Tambah Data Peminjaman")
        print("2. Tampilkan Data Peminjaman")
        print("3. Update Data Peminjaman")
        print("4. Hapus Data Peminjaman")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_peminjaman()
        elif pilihan == "2":
            tampilkan_peminjaman()
        elif pilihan == "3":
            update_peminjaman()
        elif pilihan == "4":
            hapus_peminjaman()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. coba lagi.")

def tambah_peminjaman():
    id_peminjaman = input("ID Peminjaman: ")
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("DD/MM/YYYY: ")

    peminjaman_baru = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    data_peminjaman.append(peminjaman_baru)
    print("\nData peminjaman berhasil ditambahkan!")

def tampilkan_peminjaman():
    if data_peminjaman:
        print("\nDaftar Peminjaman Buku:")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("\nData tidak valid.")

def update_peminjaman():
    id_peminjaman = input("ID Peminjaman yang akan diupdate: ")
    for i in range(len(data_peminjaman)): #berapa banyak elemen yang ada dalam list
        if data_peminjaman[i][0] == id_peminjaman:
            nama_peminjam = input("Nama Peminjam baru: ")
            judul_buku = input("Judul Buku baru: ")
            tanggal_peminjaman = input("Tanggal Peminjaman baru (DD-MM-YYYY): ")
            data_peminjaman[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("\nData peminjaman berhasil diupdate!")
            return
    print("\nID Peminjaman tidak ditemukan.")

def hapus_peminjaman():
    id_peminjaman = input("ID Peminjaman yang akan dihapus: ")
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id_peminjaman:
            del data_peminjaman[i]
            print("\nData peminjaman berhasil dihapus!")
            return
    print("\nID Peminjaman tidak ditemukan.")


main()




