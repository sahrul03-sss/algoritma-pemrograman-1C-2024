def cek_palindrom(kata):
    return kata.lower() == kata[::-1].lower()
while True:
    kata_input = input("Masukkan sebuah kata: ")
    if cek_palindrom(kata_input):
        print(f'"{kata_input}" adalah palindrom.')
        break 
    else:
        print(f'"{kata_input}" bukan palindrom. Silakan Coba lagi.')
