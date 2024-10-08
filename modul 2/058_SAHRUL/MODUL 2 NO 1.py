nama = input("masukan nama mahasiswa: ")
nim = int(input("masukan nim mahasiswa: "))
nilai_uts = int(input("masukan nilai uts: "))
nilai_uas = int(input("masukan nilai uas: ")
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

# Menentukan grade berdasarkan nilai rata-rata
if nilai_rata_rata >= 81:
    grade = "A"
elif nilai_rata_rata >= 71:
    grade = "B"
elif nilai_rata_rata >= 61:
    grade = "C"
elif nilai_rata_rata >= 41:
    grade = "D"
else:
    grade = "E"


print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Nilai UTS: {nilai_uts}")
print(f"Nilai UAS: {nilai_uas}")
print(f"Nilai rata-rata anda: {nilai_rata_rata}")
print(f"Anda mendapatkan nilai: {grade}")
