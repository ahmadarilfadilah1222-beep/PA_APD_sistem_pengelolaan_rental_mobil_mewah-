# menu_admin.py
# Simpan sebagai menu_admin.py
from navigasi import menu_interaktif
from colorama import Fore, Style
from utils import mobil_list, clear, users, append_transaksi_csv
from transaksi import lihat_transaksi

def lihat_mobil_admin():
    from prettytable import PrettyTable
    clear()
    print(Fore.CYAN + "=== DAFTAR MOBIL (ADMIN) ===" + Style.RESET_ALL)
    table = PrettyTable(["Plat","Nama","Harga","Status","Penyewa","Batas Waktu"])
    for plat, d in mobil_list.items():
        table.add_row([plat, d["nama"], f"Rp{d['harga']}", d["status"], d.get("penyewa","-"), d.get("batas_waktu","-")])
    print(table)
    input("Enter...")

def tambah_mobil_admin():
    clear()
    print(Fore.CYAN + "=== TAMBAH MOBIL ===" + Style.RESET_ALL)
    plat = input("Plat mobil (misal KT8888XX): ").upper().strip()
    if plat in mobil_list:
        print(Fore.YELLOW + "Plat sudah terdaftar!" + Style.RESET_ALL)
    else:
        nama = input("Nama mobil: ").strip()
        harga = input("Harga per hari: ").strip()
        if not harga.isdigit():
            print(Fore.RED + "Harga harus angka!" + Style.RESET_ALL)
        else:
            mobil_list[plat] = {"nama": nama, "harga": int(harga), "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None}
            print(Fore.GREEN + "Mobil berhasil ditambahkan!" + Style.RESET_ALL)
    input("Enter...")

def update_mobil_admin():
    clear()
    print(Fore.CYAN + "=== UPDATE MOBIL YANG INGIN DITAMBAHKAN ===" + Style.RESET_ALL)
    for plat, d in mobil_list.items():
        print(f"{plat} - {d['nama']} - Rp{d['harga']} - {d['status']}")
    plat = input("Plat yang diupdate: ").upper().strip()
    if plat not in mobil_list:
        print(Fore.YELLOW + "Plat tidak ditemukan!" + Style.RESET_ALL)
    else:
        nama = input("Nama baru (kosong=tidak ubah): ").strip()
        harga = input("Harga baru (kosong=tidak ubah): ").strip()
        status = input("Status (Tersedia/Disewa): ").strip()
        if nama:
            mobil_list[plat]["nama"] = nama
        if harga.isdigit():
            mobil_list[plat]["harga"] = int(harga)
        if status in ["Tersedia","Disewa"]:
            mobil_list[plat]["status"] = status
        print(Fore.GREEN + "Update berhasil!" + Style.RESET_ALL)
    input("Enter...")

def hapus_mobil_admin():
    clear()
    print(Fore.CYAN + "=== HAPUS MOBIL ===" + Style.RESET_ALL)
    plat = input("Plat yang dihapus: ").upper().strip()
    if plat in mobil_list:
        del mobil_list[plat]
        print(Fore.GREEN + "Mobil dihapus!" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Plat tidak ada!" + Style.RESET_ALL)
    input("Enter...")

def menu_admin_loop():
    while True:
        pilihan = menu_interaktif("MENU ADMIN", [
            "Lihat Daftar Mobil",
            "Tambah Mobil",
            "Update Mobil",
            "Hapus Mobil",
            "Lihat Semua Transaksi",
            "Logout"
        ])
        if pilihan == 0:
            lihat_mobil_admin()
        elif pilihan == 1:
            tambah_mobil_admin()
        elif pilihan == 2:
            update_mobil_admin()
        elif pilihan == 3:
            hapus_mobil_admin()
        elif pilihan == 4:
            lihat_transaksi()
        else:
            break
