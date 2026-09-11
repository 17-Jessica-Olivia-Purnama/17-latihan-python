import sqlite3, time

conn = sqlite3.connect('timer.db')
conn.execute('CREATE TABLE IF NOT EXISTS siswa (nama TEXT, kelas TEXT, menit INT)')
conn.execute('INSERT INTO siswa VALUES ("Budi", "XI TKJ 1", 10)')

print ("Timer Budi (XI TKJ 1) - Durasi: 10 Menit\n")
for s in range(120, 0, -1):
    print(f"Sisa Waktu: {s//60:02d} Mnt {s%60:02d} Detik")
    time.sleep(1)

print("\n\n[!] WAKTU HABIS!")
