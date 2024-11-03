def fibonacci(n): 
    if n == 0:
        return 0    
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    n = int(input("Masukkan nilai n (bilangan bulat non-negatif): "))
    if n < 0:
        print("Error: n harus bilangan bulat non-negatif. Silakan coba lagi.")
    else:
        print(f"Fibonacci ke-{n}: {fibonacci(n)}")
        break

      #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
