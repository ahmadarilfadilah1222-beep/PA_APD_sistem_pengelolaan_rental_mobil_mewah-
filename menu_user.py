# menu_user.py
# Simpan sebagai menu_user.py
from navigasi import menu_interaktif
from colorama import Fore, Style
from utils import mobil_list, transaksi_list, fmt_dt, clear
from sewa import sewa_mobil, kembalikan_mobil
from transaksi import lihat_transaksi

def tampilkan_daftar_mobil():
    from prettytable import PrettyTable
    clear()
    print(Fore.CYAN + "=== DAFTAR MOBIL ===" + Style.RESET_ALL)
    table = PrettyTable(["Plat","Nama","Harga","Status","Batas Waktu (jika disewa)"])
    for plat, d in mobil_list.items():
        table.add_row([plat, d["nama"], f"Rp{d['harga']}", d["status"], fmt_dt(d.get("batas_waktu"))])
    print(table)
    input("Enter...")

def menu_user_loop(username):
    while True:
        pilihan = menu_interaktif(f"MENU USER ({username})", [
            "Lihat Daftar Mobil",
            "Sewa Mobil",
            "Kembalikan Mobil",
            "Lihat Riwayat Transaksi Saya",
            "Logout"
        ])
        if pilihan == 0:
            tampilkan_daftar_mobil()
        elif pilihan == 1:
            sewa_mobil(username)
        elif pilihan == 2:
            kembalikan_mobil(username)
        elif pilihan == 3:
            # tampilkan transaksi milik user
            from prettytable import PrettyTable
            clear()
            print(Fore.CYAN + f"=== TRANSAKSI {username} ===" + Style.RESET_ALL)
            table = PrettyTable(["Plat","Mobil","Tgl Sewa","Batas","Tgl Kembali","Harga","Denda","Total"])
            import csv
            from utils import TRANSAKSI_CSV
            try:
                with open(TRANSAKSI_CSV, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row.get("username") == username:
                            table.add_row([
                                row.get("plat",""),
                                row.get("mobil",""),
                                row.get("tgl_sewa",""),
                                row.get("batas_waktu",""),
                                row.get("tgl_kembali",""),
                                row.get("harga",""),
                                row.get("denda",""),
                                row.get("total_bayar","")
                            ])
                print(table)
            except FileNotFoundError:
                print(Fore.YELLOW + "Belum ada transaksi." + Style.RESET_ALL)
            input("Enter...")
        else:
            break
