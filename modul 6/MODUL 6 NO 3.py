data_barang = []

def tambah_barang(data_barang):
    nama_barang = input("Nama Barang: ")
    id_barang = input("ID Barang: ")
    
    while True:
        prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")
        if prioritas in ["Darurat", "Biasa", "Non-Darurat"]:
            break
        else:
            print("Prioritas tidak valid! pilih Darurat, Biasa, atau Non-Darurat.")

    if prioritas == "Darurat":
        data_barang.insert(0, (nama_barang, id_barang, prioritas)) 
    elif prioritas == "Biasa":
        data_barang.insert(len(data_barang) // 2, (nama_barang, id_barang, prioritas))  
    elif prioritas == "Non-Darurat":
        data_barang.append((nama_barang, id_barang, prioritas)) 

    data_barang.sort(key=lambda x: {"Darurat": 0, "Biasa": 1, "Non-Darurat": 2}[x[2]])

def tampilkan_barang(data_barang):
    if not data_barang:
        print("Belum ada data barang.")
    else:
        print("\nData Barang yang telah diinputkan:")
        for barang in data_barang:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

def main():
    while True:
        tambah_barang(data_barang)
        tampilkan_barang(data_barang)

        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (iya/tidak): ")
        if lagi != 'iya':
            break

main()
