# 📡 SPY-NETHUNTER (Marauder)
### [ Advanced Wireless & Network Audit Toolkit ]

![Version](https://img.shields.io/badge/Version-1.5.0--Stable-red.svg)
![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Linux%20|%20Root-blue.svg)

**SPY-NETHUNTER** adalah toolkit otomatisasi yang menggabungkan kekuatan Kali NetHunter ke dalam Termux. Didesain untuk meniru fitur **ESP32 Marauder** (WiFi Scanning, Deauth, Beacon Spam) hanya menggunakan perangkat Android Anda.

---

## ⚡ Fitur Utama (The Marauder Clone)
- **WiFi Scanner**: Mencari Access Point & Client di sekitar secara real-time.
- **Deauth Attack**: Memutuskan koneksi perangkat dari WiFi (Wajib Monitor Mode).
- **Beacon Spam**: Membuat ratusan SSID WiFi palsu untuk membingungkan target.
- **MITM Dashboard**: Sniffing trafik data di jaringan lokal menggunakan Bettercap.
- **One-Click Install**: Setup Kali NetHunter Rootless secara otomatis.

---

## 🛠️ Persyaratan (Requirements)
1. **Android**: Minimal versi 7.0.
2. **Termux**: Versi terbaru dari F-Droid (Bukan Play Store).
3. **Storage**: Minimal 3GB-5GB ruang kosong (Untuk Image Kali).
4. **Monitor Mode**: Disarankan HP sudah **Root** dengan chipset Snapdragon (via Nexmon) untuk fitur Deauth.

---

## 📥 Instalasi Cepat

### 📱 Langkah 1: Setup Kali NetHunter di Termux
Jalankan perintah ini di Termux Anda:
```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install wget -y
wget -O install-nethunter-termux [https://offs.ec/2Mdgk7R](https://offs.ec/2Mdgk7R)
chmod +x install-nethunter-termux
./install-nethunter-termux
```
### 👹 Clone SPY-NETHUNTER
```bash
git clone [https://github.com/username-kamu/SPY-NETHUNTER.git](https://github.com/username-kamu/SPY-NETHUNTER.git)
cd SPY-NETHUNTER
pip install requests
python spy_nethunter.py
```
### 📖 Panduan Penggunaan
​Jalankan nethunter di Termux untuk masuk ke lingkungan Kali.
​Jalankan menu spy_nethunter.py untuk memilih mode serangan:
​Mode 1: Scanning jaringan (Marauder Style).
​Mode 2: Menjalankan Wifite untuk cracking password.
​Mode 3: Menjalankan Bettercap untuk memantau data (Sniffing).
​⚠️ Disclaimer
​Alat ini dibuat hanya untuk tujuan pendidikan, audit keamanan, dan riset forensik digital. Penggunaan alat ini untuk mengakses jaringan tanpa izin adalah tindakan ilegal. Rolandino & 123Tool tidak bertanggung jawab atas segala penyalahgunaan.
