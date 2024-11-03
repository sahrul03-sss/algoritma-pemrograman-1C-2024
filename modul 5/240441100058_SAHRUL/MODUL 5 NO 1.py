def calculate_discount():
    total_belanja = int(input("Masukkan harga belanja: "))
    member = input("Apakah anda punya member? jawab (ya) jika punya: ")
    diskon = 0

    if member == "ya":
        keanggotaan = input("Apa member kamu? (gold/silver/bronze): ")
        if keanggotaan == "gold":
            print("Karena anda memiliki member gold, selamat mendapatkan diskon 15%")
            diskon += 0.15
        elif keanggotaan == "silver":
            print("Karena anda memiliki member silver, selamat mendapatkan diskon 10%")
            diskon += 0.10
        elif keanggotaan == "bronze":
            print("Karena anda memiliki member bronze, selamat mendapatkan diskon 5%")
            diskon += 0.05
        else:
            print("Maaf, keanggotaan tidak valid.")

    if total_belanja > 1000000:
        print("Selamat, anda mendapatkan diskon tambahan 5%, karena anda belanja lebih dari 1jt.")
        diskon += 0.05

    harga_setelah_diskon = total_belanja * (1 - diskon)
    print(f"Total belanja anda adalah Rp. {total_belanja}")
    print(f"Total setelah diskon adalah Rp. {harga_setelah_diskon}")

calculate_discount()
