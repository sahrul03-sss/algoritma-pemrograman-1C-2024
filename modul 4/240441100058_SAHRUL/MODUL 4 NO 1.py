ukuran = int(input("masukkan ukuran : "))
karakter = input("masukkan bentuk (X/O) : ")

for i in range(1, ukuran +1):
  for k in range (ukuran - i):
    print(' ', end=" ")
  for b in range (1, i+ 1):
    print(karakter, end="   ")
  print()

for i in range(1, ukuran +1):
  for k in range (1, i +1):
    print(' ',end=" ")
  for b in range (ukuran - i):
    print(karakter, end="   ")
  print()