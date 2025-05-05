# Aplikasi Optimasi Produksi Pakaian

**Oleh: Nourivex**

> Aplikasi desktop berbasis Tkinter untuk menghitung kombinasi produksi pakaian optimal dari ketersediaan kain, dilengkapi rekomendasi kain, persentase fokus ukuran, dan visualisasi real-time.

---

## 🚀 Fitur Utama

* **Input Dinamis**

  * Pilih jenis produk dari `jenispakaian.json`.
  * Pilih jenis kain dari `data/jenispakaian.json` berdasarkan rekomendasi otomatis.
  * Masukkan total meter kain yang tersedia.

* **Fokus Ukuran & Persentase**

  * Checklist ukuran (S, M, L, XL, ...) dan masukkan persentase (%) porsi produksi per ukuran.
  * Alokasi awal berdasarkan persentase, sisanya dioptimasi greedy.

* **Optimasi Sisa Kain (Optional)**

  * Mode minimasi sisa kain untuk memaksimalkan pemakaian bahan.

* **Rekomendasi Kain Otomatis**

  * Berdasarkan product target, tampilkan list kain yang paling cocok.

* **Visualisasi Real-Time**

  * Tabel hasil produksi lengkap (jumlah, meter terpakai, keuntungan).
  * Grafik batang dan pie chart pemakaian kain & sisa.

* **Ekspor & Extendable**

  * Mudah diperluas dataset kain dan produk via JSON.
  * Struktur kode modular: `ui.py`, `logic.py`, `data.py`, `jenispakaian.json`.

---

## 🛠️ Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/LycusCoder/optimasi-pakaian.git
   cd optimasi-pakaian
   ```

2. **Buat virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```

3. **Struktur Direktori**

   ```text
   optimasi-pakaian/
   ├── data/
   │   ├── jenispakaian.json        # daftar produk
   │   └── dataset_kain.json        # parameter kain
   ├── logic.py                     # core algoritma optimasi
   ├── ui.py                        # antarmuka Tkinter
   ├── main.py                      # entry-point aplikasi
   └── README.md
   ```

---

## ▶️ Cara Menjalankan

```bash
python main.py
```

1. Jalankan `main.py`.
2. Pada tab **Input Data**:

   * Pilih produk & kain.
   * Masukkan total meter kain.
   * Centang ukuran dan atur persentase produksi.
   * (Opsional) Aktifkan `Minimasi Sisa Kain`.
3. Klik **Hitung Produksi**.
4. Pindah ke tab **Hasil** untuk melihat tabel dan grafik.

---

## 📂 Struktur Kode

* `main.py`
  Entry-point, instansiasi `OptimasiApp`.

* `ui.py`
  Seluruh definisi antarmuka pengguna (Tkinter + Matplotlib).

* `logic.py`
  Algoritma Greedy + optimasi sisa kain + pembuatan grafik.

* `data/jenispakaian.json`
  Daftar jenis produk yang tersedia.

* `data/dataset_kain.json`
  Parameter kain: meter per ukuran, harga per meter, keuntungan, rekomendasi.

---

## 🤝 Kontribusi

1. Fork repo ini
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Tambah fitur X'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

---

## 📝 Lisensi

MIT License © 2025 Nourivex

---

Terima kasih telah menggunakan aplikasi ini!

✨ **Nourivex** ✨
