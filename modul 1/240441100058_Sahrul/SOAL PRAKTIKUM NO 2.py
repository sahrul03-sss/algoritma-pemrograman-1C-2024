suku_ke_5=int(input("masukan nilai dari suku_ke_5: ")) #11
jumlah_suku_8_12=int(input("masukn nilai jumlah_suku_8_12: "))  #52

#hitung beda
b=(jumlah_suku_8_12-2*suku_ke_5)/ 10

# cari suku pertama
a=suku_ke_5-4*b

n=8
jumlah_8_suku= n*(2*a+(n-1)*b)/2

print("hasil suku pertama adalah: ",a)
print("bedanya: ", b)
print(f"jumlah 8 suku pertama{jumlah_8_suku}")
