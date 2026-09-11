import sqlite3, hashlib

# 1. Inisialisasi Database & Tabel
conn = sqlite3.connect('user.db')
conn.execute('CREATE TABLE IF NOT EXISTS akun (username TEXT PRIMARY KEY, password TEXT)')
conn.commit()

# Fungsi untuk mengubah password menjadi hash aman (SHA-256)
def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 2. Display Menu Utama di Terminal
print("=" * 35)
print("     SISTEM LOGIN & REGISTER     ")
print("=" * 35)
print("1. Register (Daftar Akun Baru)")
print("2. Login (Masuk Ke Sistem)")
pilihan = input("\nPilih menu (1/2): ")

# --- MENU 1: REGISTER ---
if pilihan == "1":
    print("\n--- MENU REGISTER ---")
    usn = input("Masukkan Username Baru : ").strip()
    pw = input("Masukkan Password Baru : ").strip()
    
    try:
        conn.execute('INSERT INTO akun VALUES (?, ?)', (usn, hash_pw(pw)))
        conn.commit()
        print(f"\n[✓] Akun '{usn}' BERHASIL didaftarkan!")
    except sqlite3.IntegrityError:
        print(f"\n[!] GAGAL: Username '{usn}' sudah dipakai user lain.")

# --- MENU 2: LOGIN ---
elif pilihan == "2":
    print("\n--- MENU LOGIN ---")
    input_usn = input("Masukkan Username : ").strip()
    input_pw = input("Masukkan Password : ").strip()

    # Cek ke database
    res = conn.execute('SELECT * FROM akun WHERE username=? AND password=?', (input_usn, hash_pw(input_pw))).fetchone()

    if res:
        print(f"\n[✓] LOGIN BERHASIL! Selamat datang, {input_usn}.")
    else:
        print("\n[!] LOGIN GAGAL! Username atau Password salah.")

else:
    print("\n[!] Pilihan tidak valid.")

conn.close()
