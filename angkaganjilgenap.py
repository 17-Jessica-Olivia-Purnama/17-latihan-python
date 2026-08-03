# Program Mengecek Angka Ganjil atau Genap

try:
    # Meminta input dari pengguna dan mengubahnya menjadi integer
    angka = int(input("Masukkan sebuah angka: "))

    # Memeriksa apakah angka habis dibagi 2 (sisa bagi adalah 0)
    if angka % 2 == 0:
        print(f"Angka {angka} adalah bilangan GENAP.")
    else:
        print(f"Angka {angka} adalah bilangan GANJIL.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka bulat.")