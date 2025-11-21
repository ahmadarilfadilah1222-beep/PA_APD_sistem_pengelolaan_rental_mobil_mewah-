# main.py
# Simpan sebagai main.py
from navigasi import menu_interaktif
from autentikasi import login_prompt, register_prompt
from menu_admin import menu_admin_loop
from menu_user import menu_user_loop
from utils import clear
from colorama import Fore, Style

def main_loop():
    while True:
        pilihan = menu_interaktif("SISTEM RENTAL MOBIL MAHAL", ["Login", "Register", "Keluar"])
        if pilihan == 0:
            username, role = login_prompt()
            if username:
                if role == "admin":
                    menu_admin_loop()
                else:
                    menu_user_loop(username)
        elif pilihan == 1:
            register_prompt()
        else:
            clear()
            print(Fore.CYAN + "Terima kasih telah menggunakan program rental mobil mahal ini!" + Style.RESET_ALL)
            input("Tekan Enter untuk keluar dari program...")
            break

if __name__ == "__main__":
    main_loop()