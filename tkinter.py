import tkinter as tk
from tkinter import messagebox

def login():
    if user_entry.get() == "admin" and pass_entry.get() == "12345":
        messagebox.showinfo("Sukses", "Login Berhasil!")
    else:
        messagebox.showerror("Gagal", "Username/Password Salah!")

root = tk.Tk()
root.title("Login")
root.geometry("280x150")

BG_COLOR = "#2c3e50"  
FG_COLOR = "#ffffff"  
root.configure(bg=BG_COLOR)

tk.Label(root, text="Username", bg=BG_COLOR, fg=FG_COLOR).pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
