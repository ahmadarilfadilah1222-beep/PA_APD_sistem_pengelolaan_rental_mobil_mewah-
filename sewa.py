# sewa.py
# Simpan sebagai sewa.py
import datetime
from utils import mobil_list, append_transaksi_csv, clear, DENDA_MINIMUM
from colorama import Fore, Style

def sewa_mobil(username):
    clear()
    print(Fore.CYAN + "=== SEWA MOBIL ===" + Style.RESET_ALL)
    for plat, d in mobil_list.items():
        print(f"{plat} - {d['nama']} - Rp{d['harga']} - {d['status']}")
    plat = input("\nMasukkan plat yang ingin disewa: ").upper().strip()
    if plat not in mobil_list:
        print(Fore.RED + "Plat tidak ditemukan!" + Style.RESET_ALL)
        input("Enter...")
        return
    mobil = mobil_list[plat]
    if mobil["status"] != "Tersedia":
        print(Fore.YELLOW + "Mobil tidak tersedia!" + Style.RESET_ALL)
        input("Enter...")
        return
    hari = input("Sewa berapa hari? ").strip()
    if not hari.isdigit() or int(hari) <= 0:
        print(Fore.RED + "Durasi harus angka positif!" + Style.RESET_ALL)
        input("Enter...")
        return
    hari = int(hari)
    tgl_sewa = datetime.datetime.now()
    batas = tgl_sewa + datetime.timedelta(days=hari)
    mobil["status"] = f"Disewa {username}"
    mobil["penyewa"] = username
    mobil["tanggal_sewa"] = tgl_sewa
    mobil["batas_waktu"] = batas
    total_bayar = mobil["harga"] * hari
    # simpan transaksi awal (waktu transaksi = sekarang) - tgl_kembali masih "-"
    append_transaksi_csv(username, plat, mobil["nama"], tgl_sewa, batas, None, mobil["harga"], 0, total_bayar)
    print(Fore.GREEN + "\nMobil berhasil disewa!" + Style.RESET_ALL)
    print(f"Tanggal sewa : {tgl_sewa}")
    print(f"Batas kembali : {batas}")
    print(f"Total bayar   : Rp{total_bayar}")
    input("Enter...")

def kembalikan_mobil(username):
    clear()
    print(Fore.CYAN + "=== PENGEMBALIAN MOBIL ===" + Style.RESET_ALL)
    ditemukan = False
    for plat, mobil in mobil_list.items():
        if mobil.get("penyewa") == username:
            ditemukan = True
            tgl_sewa = mobil.get("tanggal_sewa")
            batas = mobil.get("batas_waktu")
            tgl_kembali = datetime.datetime.now()
            harga = mobil["harga"]
            # hitung denda: jika terlambat, denda minimal DENDA_MINIMUM
            denda = 0
            if batas and tgl_kembali > batas:
                # user minta denda minimal 300k (tetap), kita terapkan denda flat 300k
                denda = DENDA_MINIMUM
            total_bayar = harga * max(1, ( (batas - tgl_sewa).days if tgl_sewa and batas else 1 ))  # fallback
            # update mobil
            mobil["status"] = "Tersedia"
            mobil["penyewa"] = None
            mobil["tanggal_sewa"] = None
            mobil["batas_waktu"] = None
            # simpan transaksi lengkap ke CSV
            append_transaksi_csv(username, plat, mobil["nama"], tgl_sewa, batas, tgl_kembali, harga, denda, total_bayar + denda)
            print(Fore.GREEN + "Mobil berhasil dikembalikan!" + Style.RESET_ALL)
            print(f"Tanggal kembali: {tgl_kembali}")
            if denda > 0:
                print(Fore.RED + f"Denda keterlambatan: Rp{denda}" + Style.RESET_ALL)
            else:
                print("Tidak ada denda.")
    if not ditemukan:
        print(Fore.YELLOW + "Anda tidak memiliki mobil yang sedang disewa." + Style.RESET_ALL)
    input("Enter...")