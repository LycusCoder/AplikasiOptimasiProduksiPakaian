# 🧶 Aplikasi Optimasi Produksi Pakaian (Streamlit)

**Oleh: Nourivex**

> Aplikasi berbasis web interaktif menggunakan **Streamlit** untuk menghitung distribusi produksi pakaian optimal berdasarkan ketersediaan kain. Dilengkapi rekomendasi kain, fokus ukuran, persentase alokasi, dan optimasi sisa kain.

---

## 🚀 Fitur Utama

1. **Antarmuka Modern dengan Streamlit**

   * Desain responsif, dapat diakses via browser
   * Tab terpisah untuk *Input Data* dan *Hasil Optimasi*

2. **Input Dinamis**

   * Pilih jenis produk & jenis kain dari file JSON (`jenispakaian.json`, `kain.json`)
   * Masukkan panjang dan lebar kain (meter)
   * Hitung luas total otomatis

3. **Fokus Ukuran & Persentase Produksi**

   * Checkbox untuk setiap ukuran yang tersedia
   * Input persentase (%) untuk setiap ukuran
   * Validasi total persentase tidak melebihi 100%

4. **Optimasi Sisa Kain**

   * Opsi untuk meminimasi limbah kain
   * Sisa kain dialokasikan ke ukuran dengan kebutuhan meter terkecil

5. **Rekomendasi Kain Otomatis**

   * Berdasarkan produk target, sistem menampilkan jenis kain yang direkomendasikan

6. **Visualisasi & Laporan**

   * Tabel hasil produksi: jumlah per ukuran, penggunaan meter, keuntungan
   * Grafik batang penggunaan kain per ukuran
   * Ringkasan total keuntungan, sisa kain, dan efisiensi

7. **Modular & Mudah Diperluas**

   * Kode terpisah: `main.py`, `ui.py`, `logic.py`
   * Dataset dalam format JSON (`data/kain.json`, `data/jenispakaian.json`)
   * Tambah jenis kain atau produk tanpa mengubah logika utama

---

## 🛠️ Teknologi

* **Python 3.x**
* **Streamlit** – Framework web UI
* **Pandas** – Pengolahan DataFrame hasil
* **Matplotlib** – Pembuatan grafik
* **JSON** – Penyimpanan dataset kain dan produk

---

## 📂 Struktur Proyek

```
optimasi-pakaian/
├── data/
│   ├── kain.json             # Dataset parameter kain
│   └── jenispakaian.json     # Daftar jenis produk
├── docs/
├── logic.py                  # Logika optimasi Greedy + sisa kain
├── ui.py                     # Antarmuka Streamlit
├── main.py                   # Entry point aplikasi
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 💻 Instalasi & Jalankan

1. **Clone repository**

   ```bash
   git clone https://github.com/LycusCoder/optimasi-pakaian.git
   cd optimasi-pakaian
   ```

2. **Buat virtual environment & aktifkan**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**

   ```bash
   streamlit run main.py
   ```

5. **Akses** aplikasi di browser pada `http://localhost:8501`

---

## ▶️ Panduan Penggunaan

1. Tab **Input Data**:

   * Pilih **Jenis Produk** & **Jenis Kain**
   * Masukkan **Panjang** dan **Lebar** kain (m)
   * Pilih ukuran fokus dan atur persentase produksi
   * (Opsional) Centang **Optimasi Sisa Kain**
   * Klik **HITUNG PRODUKSI OPTIMAL**

2. Tab **Hasil Optimasi**:

   * Tabel hasil: jumlah pakaian, meter terpakai, keuntungan per ukuran
   * Grafik batang: pemakaian kain per ukuran
   * Ringkasan: Total Keuntungan, Sisa Kain, Efisiensi

---

## 🤝 Kontribusi

1. Fork repo
2. Buat branch: `git checkout -b fitur-baru`
3. Buat perubahan & commit
4. Push & buat Pull Request

---

## 📄 Lisensi

MIT © 2025 Nourivex
