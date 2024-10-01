panjang = int(input("masukan nilai panjang balok")) #20cm
lebar = int(input("masukan nilai lebar balok")) #13cm
tinggi = int(input("masukan nilai tinggi balok")) #7cm

volume_balok = panjang * lebar * tinggi
print("jadi nilai dari volume balok adalah: ",volume_balok)

diameter = int(input("/nmasukan nilai diameter balok: ")) #14cm
luas_selimut = int(input("masukan nilai luas selimut")) #440cm
phi = 22/7
a = 2
jari_jari = diameter/2
print("hasil nilai dari jari_jari tabung adalah: ",jari_jari)

tinggi_tabung = luas_selimut / (a * phi * jari_jari)
print("hasil nilai dari tinggi tabung adalah: ",tinggi_tabung)

volume_tabung = phi * jari_jari ** a * tinggi_tabung
print("jadi nilai dari volume tabung: ",volume_tabung)
