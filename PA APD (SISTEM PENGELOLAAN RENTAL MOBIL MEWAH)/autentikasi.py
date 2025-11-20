# autentikasi.py
# Simpan sebagai autentikasi.py
from utils import users, append_customer_to_csv, clear
from navigasi import menu_interaktif
from colorama import Fore, Style

def login_prompt():
    clear()
    print(Fore.CYAN + "=== LOGIN ===" + Style.RESET_ALL)
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = users.get(username)
    if user and user["password"] == password:
        print(Fore.GREEN + "Login berhasil!" + Style.RESET_ALL)
        input("Tekan Enter...")
        return username, user.get("role","user")
    print(Fore.RED + "Username atau password salah!" + Style.RESET_ALL)
    input("Tekan Enter...")
    return None, None

def register_prompt():
    clear()
    print(Fore.CYAN + "=== REGISTER ===" + Style.RESET_ALL)
    username = input("Username baru: ").strip()
    if username in users:
        print(Fore.YELLOW + "Username sudah terpakai!" + Style.RESET_ALL)
        input("Enter...")
        return
    password = input("Password: ").strip()
    nama = input("Nama lengkap: ").strip()
    # simpan ke CSV & memory
    append_customer_to_csv(username, password, nama)
    print(Fore.GREEN + "Registrasi berhasil! Data pelanggan tersimpan di customers.csv" + Style.RESET_ALL)
    input("Enter...")