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
    
    # Program Cek Ganjil Genap Interaktif (Looping)

print("=== PROGRAM CEK GANJIL / GENAP ===")
print("Ketik 'keluar' atau 'q' kapan saja untuk menghentikan program.\n")

while True:
    # Meminta input dari pengguna
    user_input = input("Masukkan angka: ").strip()

    # Memeriksa perintah untuk keluar dari program
    if user_input.lower() in ['keluar', 'q', 'exit']:
        print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
        break  # Menghentikan perulangan (loop)

    try:
        # Mengubah input menjadi angka bulat
        angka = int(user_input)

        # Memeriksa apakah angka genap atau ganjil
        if angka % 2 == 0:
            print(f"-> Angka {angka} adalah bilangan GENAP.\n")
        else:
            print(f"-> Angka {angka} adalah bilangan GANJIL.\n")

    except ValueError:
        # Penanganan jika pengguna memasukkan karakter yang bukan angka
        print("[!] Input tidak valid! Harap masukkan angka bulat yang benar.\n")
