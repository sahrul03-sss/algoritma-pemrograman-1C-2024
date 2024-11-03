def faktorial(n): 
    if n == 0 or n == 1:
        return 1
    else:   
        hasil = n * faktorial(n - 1)
        print(f"{n} x ", end="")
        return hasil
while True:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan < 0:
        print(f"Faktorial dari {bilangan} tidak dapat dihitung. Silakan coba lagi.")
    else:
        print(f"Faktorial dari {bilangan} adalah ", end="")
        hasil_faktorial = faktorial(bilangan)
        print(f"1 = {hasil_faktorial}")
        break  

