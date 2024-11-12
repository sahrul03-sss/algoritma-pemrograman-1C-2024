sekor_jaka = 1100
ipk_jaka = 3.5
sekor_ida = 1000
ipk_ida = 3.5
 
skor_minimum = 1100
ipk_minimum = 3.0


input("masukan sekor jaka: ")
    input("masukan ipk jaka: ")
  input("masukan sekor ida: ")
    input("masukan ipk ida")
if sekor_jaka >= skor_minimum and ipk_jaka >= ipk_minimum:
    hasil_jaka = "Jaka lulus persyaratan beasiswa."
    print(hasil_jaka)
else:
    hasil_jaka = "Jaka tidak lulus persyaratan beasiswa."
    print(hasil_jaka)

if sekor_ida >= skor_minimum and ipk_ida >= ipk_minimum:
    hasil_ida = "Ida lulus persyaratan beasiswa."
    print(hasil_ida)
else:
    hasil_ida = "Ida tidak lulus persyaratan beasiswa."
    print(hasil_ida)
