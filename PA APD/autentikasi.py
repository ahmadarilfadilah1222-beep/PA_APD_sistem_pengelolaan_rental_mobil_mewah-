# autentikasi.py
# Simpan sebagai autentikasi.py
from utils import users, append_customer_to_csv, clear
from navigasi import menu_interaktif
from colorama import Fore, Style

# Fungsi validasi
def hanya_huruf(teks):
    return teks.replace(" ", "").isalpha()

def hanya_angka(teks):
    return teks.isdigit()

# LOGIN

def login_prompt():
    while True:   # tetap di menu login sampai benar
        clear()
        print(Fore.CYAN + "=== LOGIN ===" + Style.RESET_ALL)

        username = input("Username (username di isi hanya berupa huruf saja): ").strip()
        password = input("Password (password di isi hanya berupa angka saja): ").strip()

        # -------- Validation --------
        if not username:
            print(Fore.RED + "Username tidak boleh kosong!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if not hanya_huruf(username):
            print(Fore.RED + "Username hanya boleh huruf!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if not password:
            print(Fore.RED + "Password tidak boleh kosong!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if not hanya_angka(password):
            print(Fore.RED + "Password hanya boleh angka!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        user = users.get(username)

        if not user:
            print(Fore.RED + "Username tidak ditemukan!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if user["password"] != password:
            print(Fore.RED + "Password salah!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        # Jika login berhasil
        print(Fore.GREEN + "Login berhasil!" + Style.RESET_ALL)
        input("Tekan Enter...")
        return username, user.get("role", "user")


# REGISTER
def register_prompt():
    while True:
        clear()
        print(Fore.CYAN + "=== REGISTER ===" + Style.RESET_ALL)

        username = input("Username baru (username di isi hanya berupa huruf saja): ").strip()

        if not hanya_huruf(username):
            print(Fore.RED + "Username hanya boleh huruf!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if username in users:
            print(Fore.YELLOW + "Username sudah terpakai!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        password = input("Password (8 digit angka): ").strip()

        if not hanya_angka(password):
            print(Fore.RED + "Password hanya boleh angka!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        if len(password) != 8:
            print(Fore.RED + "Password harus tepat 8 angka!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        nama = input("Nama lengkap (nama lengkang di isi hanya berupa huruf saja): ").strip()

        if not hanya_huruf(nama):
            print(Fore.RED + "Nama hanya boleh huruf!" + Style.RESET_ALL)
            input("Enter untuk ulang...")
            continue

        append_customer_to_csv(username, password, nama)

        print(Fore.GREEN + "Registrasi berhasil! Data pelanggan tersimpan." + Style.RESET_ALL)
        input("Enter...")
        break
