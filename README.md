# 🧵 Aplikasi Optimasi Produksi Pakaian

**Oleh: Nourivex**

> Aplikasi desktop berbasis Tkinter untuk menghitung kombinasi produksi pakaian optimal dari ketersediaan kain, dilengkapi rekomendasi kain, persentase fokus ukuran, dan optimasi sisa kain. Dibangun menggunakan pendekatan **Greedy Algorithm**.

---

## 🚀 Fitur Utama

✅ **Input Dinamis**
- Pilih jenis produk & jenis kain dari file JSON (`jenispakaian.json`) dengan rekomendasi otomatis
- Masukkan total meter kain tersedia (default: 100m)

✅ **Fokus Ukuran & Persentase Produksi Real-Time**
- Checkbox untuk setiap ukuran (S, M, L, XL, dll.)
- Input persentase (%) untuk masing-masing ukuran
- Jika semua ukuran diceklis dan belum ada input, alokasi otomatis 25% per ukuran
- Saat checkbox diubah atau persentase diedit:
  - Persentase langsung direkalkulasi agar total tetap 100%
  - Perhitungan produksi tidak langsung dijalankan (hanya saat tombol "Hitung" diklik)
  
✅ **Optimasi Sisa Kain (Optional)**
- Setelah alokasi awal berdasarkan persentase, sistem akan:
  - Menghitung jumlah sisa kain
  - Mendistribusikan sisa kain ke ukuran termurah/terkecil (misalnya S)
  - Menambahkan pakaian tambahan jika memungkinkan

✅ **Rekomendasi Kain Otomatis**
- Berdasarkan jenis produk yang dipilih, aplikasi menyarankan jenis kain yang cocok

✅ **Visualisasi Hasil Produksi**
- Tabel hasil produksi: jumlah pakaian, penggunaan kain, keuntungan per ukuran
- Grafik batang dan pie chart interaktif:
  - Jumlah produksi per ukuran
  - Proporsi pemakaian kain dan sisa kain

✅ **Struktur Modular & Mudah Diembangkan**
- File terpisah: `main.py`, `ui.py`, `logic.py`, dan file dataset dalam format JSON
- Dataset mudah ditambah atau diedit tanpa merubah logika utama

---

## 🔧 Teknologi yang Digunakan

- **Python 3.x**
- **Tkinter** – GUI
- **Matplotlib** – Visualisasi grafik
- **JSON** – Penyimpanan data fleksibel

---

## 🛠️ Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/LycusCoder/optimasi-pakaian.git
   cd optimasi-pakaian
   ```

2. **Buat dan aktifkan virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pastikan struktur direktori seperti ini**:
   ```
   optimasi-pakaian/
   ├── data/
   │   ├── jenispakaian.json        # daftar jenis produk
   ├── docs/
   ├── logic.py                     # algoritma Greedy + optimasi sisa
   ├── ui.py                        # antarmuka Tkinter
   ├── main.py                      # entry point
   └── README.md
   ```

---

## ▶️ Cara Menjalankan

```bash
python main.py
```

### Langkah-langkah Penggunaan:
1. Jalankan aplikasi.
2. Pada tab **Input Data**:
   - Pilih jenis produk dan kain
   - Masukkan jumlah total kain (dalam meter)
   - Checklist ukuran yang ingin difokuskan
   - Atur persentase produksi per ukuran
   - (Opsional) Aktifkan opsi *Optimasi untuk Minimasi Sisa Kain*
3. Klik **"HITUNG PRODUKSI OPTIMAL"** untuk melihat hasil.
4. Tab **Hasil Optimasi** akan menampilkan:
   - Tabel jumlah produksi per ukuran
   - Total keuntungan dan sisa kain
   - Grafik batang dan pie chart visualisasi

---

## 📂 Struktur Kode

| File | Fungsi |
|------|--------|
| `main.py` | Entry point, inisialisasi aplikasi |
| `ui.py` | Antarmuka pengguna (GUI), kontrol interaksi |
| `logic.py` | Logika optimasi Greedy + redistribusi sisa kain |
| `data/jenispakaian.json` | Daftar jenis produk & Parameter kain (meter/ukuran, harga, keuntungan, rekomendasi)  |


---

## 💡 Contoh Kerja Algoritma

Misalnya:
- Total kain = 100 meter
- Persentase: XL (60%), L (30%), M (10%)
- Ukuran termurah: S (1.5m/pakaian)

Proses:
1. Alokasikan berdasarkan persentase:
   - XL: 60m → 20 pakaian
   - L: 30m → 12 pakaian
   - M: 10m → 5 pakaian
2. Sisa kain = 0m
3. Jika `optimasi_sisa=True`, sistem mencari apakah bisa tambahkan pakaian dari sisa kain (misalnya S):
   - Jika masih ada 1.5m tersisa → tambah 1 pakaian ukuran S

---

## 🧪 Validasi Input

Aplikasi melakukan validasi:
- Total kain harus lebih besar dari nol
- Total persentase tidak boleh melebihi 100%
- Minimal satu ukuran dipilih sebagai fokus produksi

---

## 🤝 Kontribusi

Silakan fork repo ini dan buat pull request! Untuk kontribusi besar, silakan buka issue terlebih dahulu.

Langkah-langkah:
1. Fork repo ini
2. Buat branch baru: `git checkout -b fitur-baru`
3. Lakukan perubahan kode
4. Commit dan push
5. Buat Pull Request

---

## 📄 Lisensi

MIT License © 2025 Nourivex

---

## ✨ Terima Kasih Telah Menggunakan Aplikasi Ini!

Jika kamu menyukai proyek ini, jangan ragu untuk memberikan feedback, kontribusi, atau bantuan pengembangan lebih lanjut.

GitHub: [LycusCoder](https://github.com/LycusCoder)  
Email: affif@nourivex.tech

---

### 🎯 Tujuan Proyek

Aplikasi ini dibuat sebagai alat bantu untuk:
- Menghitung distribusi produksi pakaian secara efisien
- Memberikan variasi produksi berdasarkan preferensi ukuran
- Memaksimalkan keuntungan dengan minimasi limbah kain

---

### 🧩 Catatan Tambahan

- Semua nilai persentase dan alokasi hanya dihitung ulang saat tombol **"HITUNG PRODUKSI OPTIMAL"** ditekan
- Redistribusi persentase real-time hanya terjadi jika checkbox berubah atau input persentase diedit, namun optimasi produksi **tidak langsung dijalankan**
- Dataset dapat diperluas untuk mendukung lebih banyak ukuran dan jenis kain
