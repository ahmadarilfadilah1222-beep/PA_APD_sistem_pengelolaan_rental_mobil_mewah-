# navigasi.py
# Simpan sebagai navigasi.py
import os
try:
    import msvcrt
    WINDOWS = True
except Exception:
    WINDOWS = False

from colorama import Back, Fore, Style, init
init(autoreset=True)

def menu_interaktif(judul, opsi):

    if not WINDOWS:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN + "=" * 60)
            print(Fore.YELLOW + judul.center(60))
            print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
            for i, o in enumerate(opsi, 1):
                print(f"{i}. {o}")
            pilih = input("Pilih (angka): ").strip()
            if pilih.isdigit() and 1 <= int(pilih) <= len(opsi):
                return int(pilih) - 1
            print("Pilihan tidak valid. Tekan Enter...")
            input()
    posisi = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + judul.center(60))
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        for i, o in enumerate(opsi):
            if i == posisi:
                print(Fore.BLACK + Back.YELLOW + f"> {o}" + Style.RESET_ALL)
            else:
                print(f"  {o}")
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        key = msvcrt.getch()
        if key == b'\xe0':
            arah = msvcrt.getch()
            if arah == b'H':  # up
                posisi = (posisi - 1) % len(opsi)
            elif arah == b'P':  # down
                posisi = (posisi + 1) % len(opsi)
        elif key == b'\r':
            return posisi
