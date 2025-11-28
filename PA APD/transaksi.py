# transaksi.py
# Simpan sebagai transaksi.py
import csv
from prettytable import PrettyTable
from utils import TRANSAKSI_CSV, fmt_dt, clear
from colorama import Fore, Style

def simpan_transaksi_csv(username, plat, tgl_sewa, batas, tgl_kembali, harga, denda):
    from utils import append_transaksi_csv
    total_bayar = harga + (denda or 0)
    append_transaksi_csv(username, plat, "-", tgl_sewa, batas, tgl_kembali, harga, denda, total_bayar)

def lihat_transaksi():
    clear()
    print(Fore.CYAN + "=== RIWAYAT TRANSAKSI (transaksi_rental.csv) ===" + Style.RESET_ALL)
    try:
        with open(TRANSAKSI_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            table = PrettyTable(["Username","Plat","Mobil","Tgl Sewa","Batas","Tgl Kembali","Harga","Denda","Total","Waktu Transaksi"])
            for row in reader:
                table.add_row([
                    row.get("username",""),
                    row.get("plat",""),
                    row.get("mobil",""),
                    row.get("tgl_sewa",""),
                    row.get("batas_waktu",""),
                    row.get("tgl_kembali",""),
                    row.get("harga",""),
                    row.get("denda",""),
                    row.get("total_bayar",""),
                    row.get("waktu_transaksi","")
                ])
            print(table)
    except FileNotFoundError:
        print(Fore.YELLOW + "Belum ada transaksi." + Style.RESET_ALL)
    input("Enter...")
