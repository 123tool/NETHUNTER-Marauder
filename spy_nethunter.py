import os
import sys
import time
import platform
import subprocess

# =========================================================
# NETHUNTER (SPY-E)
# =========================================================
# Deskripsi: Dashboard Marauder Edition untuk Termux & Kali
# Developer: 123tool
# =========================================================

# Color Palette (Premium Cyberpunk Theme)
G = '\033[32m' # Green
R = '\033[31m' # Red
C = '\033[36m' # Cyan
Y = '\033[33m' # Yellow
W = '\033[0m'  # White
B = '\033[1m'  # Bold
M = '\033[35m' # Magenta

def clear():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    """Menampilkan branding SPY-E & 123Tool."""
    print(f"""{C}
  ███████ ██████  ██    ██      ███    ██ ███████ ████████ 
  ██      ██   ██  ██  ██       ████   ██ ██         ██    
  ███████ ██████    ████   █████ ██ ██  ██ █████      ██    
       ██ ██         ██         ██  ██ ██ ██         ██    
  ███████ ██         ██           ██   ████ ███████    ██    
  {W}-----------------------------------------------------------
  {G}[+] Mode   : Termux Marauder & NetHunter Dash
  [+] System : {platform.system()} | Arch: {platform.machine()}
  [+] Brand  : SPY-E & 123Tool (Project NAGA)
  {W}-----------------------------------------------------------
    """)

def check_root():
    """Mengecek status root perangkat."""
    if os.getuid() == 0:
        return f"{G}[PRIVILEGED / ROOTED]{W}"
    else:
        return f"{R}[UNPRIVILEGED / NON-ROOT]{W}"

def start_wifi_scan():
    """Simulasi Scanning WiFi (Marauder Mode)."""
    print(f"\n{Y}[*] Mengaktifkan WiFi Scanner (Marauder Style)...{W}")
    print(f"{C}[i] Mencari Access Point & Client di sekitar...{W}")
    time.sleep(2)
    # Menjalankan Nmap untuk scan host aktif di jaringan lokal
    try:
        # Ganti range IP sesuai kebutuhan atau gunakan subnet otomatis
        os.system("nmap -sn 192.168.1.0/24")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def run_bettercap():
    """Menjalankan Bettercap MITM Dashboard."""
    print(f"\n{G}[*] Memulai Bettercap MITM Dashboard...{W}")
    print(f"{Y}[!] Memastikan service Bettercap terpasang...{W}")
    time.sleep(1)
    os.system("bettercap -iface wlan0")

def run_wifite():
    """Menjalankan Wifite untuk Cracking WiFi."""
    print(f"\n{R}[!] Menginisialisasi Wifite (Cracking Mode)...{W}")
    print(f"{Y}[i] Catatan: Fitur ini wajib Monitor Mode & Root!{W}")
    time.sleep(1)
    # Perintah menjalankan wifite dengan mode otomatis
    os.system("sudo wifite --kill")

def install_nethunter():
    """Script installer otomatis Kali NetHunter Rootless."""
    print(f"\n{C}[*] Mempersiapkan Instalasi Kali NetHunter...{W}")
    print(f"{Y}[!] Pastikan Storage Kosong > 3GB & Internet Stabil.{W}")
    confirm = input(f"{G}[?] Lanjutkan Instalasi? (y/n): {W}")
    if confirm.lower() == 'y':
        os.system("wget -O install-nethunter-termux https://offs.ec/2Mdgk7R && chmod +x install-nethunter-termux && ./install-nethunter-termux")
    else:
        print(f"{R}[!] Instalasi dibatalkan.{W}")

def check_monitor_mode():
    """Mengecek kapabilitas Monitor Mode pada Chipset WiFi."""
    print(f"\n{Y}[*] Memeriksa Kapabilitas Chipset WiFi...{W}")
    print(f"{C}--- Interface Wireless List ---{W}")
    os.system("iw dev")
    print(f"\n{C}--- Monitor Mode Support ---{W}")
    # Perintah untuk cek apakah 'monitor' didukung oleh driver
    os.system("iw list | grep -i monitor")

def main_menu():
    """Menu Utama Interface."""
    while True:
        clear()
        banner()
        print(f" Status: {check_root()}")
        print(f"\n[{G}01{W}] WiFi Scanner (Marauder Mode)")
        print(f"[{G}02{W}] Deauth & WPA Cracking (Wifite)")
        print(f"[{G}03{W}] MITM Sniffing Dashboard (Bettercap)")
        print(f"[{G}04{W}] Install Kali NetHunter Rootless")
        print(f"[{G}05{W}] Check WiFi Monitor Mode (Hardware)")
        print(f"[{G}06{W}] Update System & Tools")
        print(f"[{R}00{W}] Exit Dashboard")
        
        try:
            choice = input(f"\n{C}SPY-NETHUNTER > {W}")
            
            if choice in ['1', '01']:
                start_wifi_scan()
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['2', '02']:
                run_wifite()
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['3', '03']:
                run_bettercap()
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['4', '04']:
                install_nethunter()
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['5', '05']:
                check_monitor_mode()
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['6', '06']:
                print(f"{G}[*] Updating system packages...{W}")
                os.system("pkg update && pkg upgrade -y")
                input(f"\n{Y}Tekan Enter untuk kembali...{W}")
            elif choice in ['0', '00']:
                print(f"{Y}[*] Mematikan Dashboard SPY-NETHUNTER. Sampai jumpa Bos Rolandino!{W}")
                break
            else:
                print(f"{R}[!] Pilihan tidak valid, silakan coba lagi.{W}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{R}[!] Program dihentikan paksa.{W}")
            break

if __name__ == "__main__":
    # Menjalankan pengecekan dependensi sederhana
    main_menu()
