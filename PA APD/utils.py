# utils.py
# Simpan sebagai utils.py
import os
import csv
import datetime
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

init(autoreset=True)

CUSTOMER_CSV = "customers.csv"
TRANSAKSI_CSV = "transaksi_rental.csv"

# data in-memory
users = {}           # username -> {"password":..., "role": "user"/"admin", "nama":..., "registered_at":...}
mobil_list = {
    "KT1234AA": {"nama": "Toyota Alphard", "harga": 1500000, "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None},
    "DA5678BB": {"nama": "BMW i8", "harga": 2500000, "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None},
    "KH8765CC": {"nama": "Mercedes Benz S-Class", "harga": 2800000, "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None},
    "KB4321DD": {"nama": "Range Rover Evoque", "harga": 2000000, "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None},
    "KU9999EE": {"nama": "Porsche Cayenne", "harga": 3000000, "status": "Tersedia", "penyewa": None, "tanggal_sewa": None, "batas_waktu": None}
}
transaksi_list = []  # in-memory cache (optional)

# constants
DENDA_MINIMUM = 300_000  # If any lateness, denda must be at least 300k as requested

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fmt_dt(dt):
    if not dt:
        return "-"
    if isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    return str(dt)

# --- customer CSV helpers ---
def load_customers_from_csv():
    """Muat customers.csv ke users dict. Jika tidak ada, buat file dan tambahkan admin default."""
    global users
    # Ensure admin exists if no CSV
    if not os.path.exists(CUSTOMER_CSV):
        with open(CUSTOMER_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username","password","nama","registered_at","role"])
            # default admin
            writer.writerow(["admin","12345678","Administrator", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "admin"])
    with open(CUSTOMER_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users[row["username"]] = {
                "password": row["password"],
                "nama": row.get("nama",""),
                "registered_at": row.get("registered_at",""),
                "role": row.get("role","user")
            }

def append_customer_to_csv(username, password, nama):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CUSTOMER_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, nama, now, "user"])
    # also update in-memory
    users[username] = {"password": password, "nama": nama, "registered_at": now, "role": "user"}

# --- transaksi CSV helpers ---
def ensure_transaksi_csv():
    if not os.path.exists(TRANSAKSI_CSV):
        with open(TRANSAKSI_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username","plat","mobil","tgl_sewa","batas_waktu","tgl_kembali","harga","denda","total_bayar","waktu_transaksi"])

def append_transaksi_csv(username, plat, mobil, tgl_sewa, batas_waktu, tgl_kembali, harga, denda, total_bayar):
    ensure_transaksi_csv()
    with open(TRANSAKSI_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            username,
            plat,
            mobil,
            fmt_dt(tgl_sewa),
            fmt_dt(batas_waktu),
            fmt_dt(tgl_kembali),
            harga,
            denda,
            total_bayar,
            fmt_dt(datetime.datetime.now())
        ])

# initialize on import
load_customers_from_csv()
ensure_transaksi_csv()
