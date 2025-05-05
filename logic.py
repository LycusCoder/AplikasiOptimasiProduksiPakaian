# logic.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def hitung_produksi(total_kain, jenis_kain, dataset, ukuran_fokus=None, optimasi_sisa=False, persentase=None):
    """
    Fungsi untuk menghitung produksi dengan Greedy Algorithm + variasi minimal.
    
    Args:
        total_kain: Total kain dalam meter
        jenis_kain: Jenis kain yang dipilih
        dataset: Dataset parameter kain
        ukuran_fokus: List ukuran yang difokuskan (None untuk semua ukuran)
        optimasi_sisa: True untuk optimasi sisa kain
        persentase: Dict {ukuran: nilai_persen} dari input pengguna
        
    Returns:
        Tuple: (hasil_produksi, total_keuntungan, sisa_kain, fig)
    """
    try:
        # Ambil parameter dari dataset
        data_kain = dataset[jenis_kain]
        meter_per_ukuran = data_kain["meter_per_ukuran"]
        keuntungan_per_pakaian = data_kain["keuntungan_per_pakaian"]
        harga_per_meter = data_kain["harga_per_meter"]

        # Filter ukuran jika ada fokus tertentu
        ukuran_tersedia = list(meter_per_ukuran.keys())
        if ukuran_fokus:
            ukuran_tersedia = [uk for uk in ukuran_tersedia if uk in ukuran_fokus]
            if not ukuran_tersedia:
                raise ValueError("Tidak ada ukuran yang valid untuk difokuskan")

        # Jika ada input persentase, gunakan itu
        if persentase and any(v > 0 for v in persentase.values()):
            hasil_produksi = {}
            total_keuntungan = 0
            sisa_kain = total_kain

            # Validasi jumlah persentase <= 100%
            total_persen = sum(float(persentase.get(u, 0)) for u in ukuran_tersedia)
            if total_persen > 100:
                raise ValueError("Total persentase tidak boleh melebihi 100%")

            for ukuran in ukuran_tersedia:
                try:
                    persen = float(persentase.get(ukuran, 0))
                except ValueError:
                    continue

                if persen <= 0:
                    continue

                alokasi_meter = total_kain * (persen / 100)
                jumlah_pakaian = int(alokasi_meter // meter_per_ukuran[ukuran])

                if jumlah_pakaian > 0:
                    hasil_produksi[ukuran] = jumlah_pakaian
                    total_keuntungan += jumlah_pakaian * keuntungan_per_pakaian[ukuran]
                    sisa_kain -= jumlah_pakaian * meter_per_ukuran[ukuran]

            # Buat grafik dan kembalikan hasil
            fig = buat_grafik(hasil_produksi, meter_per_ukuran, total_kain, sisa_kain)
            return hasil_produksi, total_keuntungan, sisa_kain, fig

        # Hitung rasio keuntungan bersih per meter
        rasio = {}
        for ukuran in ukuran_tersedia:
            biaya_produksi = meter_per_ukuran[ukuran] * harga_per_meter
            keuntungan_bersih = keuntungan_per_pakaian[ukuran] - biaya_produksi
            rasio[ukuran] = keuntungan_bersih / meter_per_ukuran[ukuran]

        # Urutkan ukuran berdasarkan rasio tertinggi
        urutan_produksi = sorted(rasio.items(), key=lambda x: x[1], reverse=True)

        hasil_produksi = {}
        total_keuntungan = 0
        sisa_kain = total_kain

        # Algoritma Greedy dengan optimasi sisa
        if optimasi_sisa:
            best_combination = {}
            min_sisa = total_kain
            max_keuntungan = 0

            def cari_kombinasi(index, current_kain, current_hasil, current_keuntungan):
                nonlocal best_combination, min_sisa, max_keuntungan
                if index >= len(urutan_produksi):
                    sisa = current_kain
                    if sisa < min_sisa or (sisa == min_sisa and current_keuntungan > max_keuntungan):
                        min_sisa = sisa
                        max_keuntungan = current_keuntungan
                        best_combination = current_hasil.copy()
                    return

                ukuran, _ = urutan_produksi[index]
                meter_ukuran = meter_per_ukuran[ukuran]
                max_pakaian = int(current_kain // meter_ukuran)

                for j in range(max_pakaian, -1, -1):
                    if j == 0 and not current_hasil:
                        continue  # Skip jika tidak menghasilkan apa-apa
                    new_kain = current_kain - j * meter_ukuran
                    new_hasil = current_hasil.copy()
                    if j > 0:
                        new_hasil[ukuran] = j
                    new_keuntungan = current_keuntungan + j * keuntungan_per_pakaian[ukuran]
                    cari_kombinasi(index + 1, new_kain, new_hasil, new_keuntungan)

            cari_kombinasi(0, total_kain, {}, 0)
            hasil_produksi = best_combination
            total_keuntungan = max_keuntungan
            sisa_kain = min_sisa
        else:
            # Algoritma Greedy standar
            for ukuran, _ in urutan_produksi:
                jumlah_pakaian = int(sisa_kain // meter_per_ukuran[ukuran])
                if jumlah_pakaian > 0:
                    hasil_produksi[ukuran] = jumlah_pakaian
                    total_keuntungan += jumlah_pakaian * keuntungan_per_pakaian[ukuran]
                    sisa_kain -= jumlah_pakaian * meter_per_ukuran[ukuran]
                else:
                    if sisa_kain >= meter_per_ukuran[ukuran]:
                        hasil_produksi[ukuran] = 1
                        total_keuntungan += keuntungan_per_pakaian[ukuran]
                        sisa_kain -= meter_per_ukuran[ukuran]

        # Buat grafik
        fig = buat_grafik(hasil_produksi, meter_per_ukuran, total_kain, sisa_kain)

        return hasil_produksi, total_keuntungan, sisa_kain, fig

    except Exception as e:
        raise ValueError(f"Terjadi kesalahan dalam perhitungan: {str(e)}")


def buat_grafik(hasil_produksi, meter_per_ukuran, total_kain, sisa_kain):
    """Membuat grafik visualisasi pemakaian kain"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    if hasil_produksi:
        ukuran = list(hasil_produksi.keys())
        jumlah = list(hasil_produksi.values())
        meter_pakai = [meter_per_ukuran[u] * jumlah[i] for i, u in enumerate(ukuran)]

        ax1.bar(ukuran, jumlah, color='#3498db')
        ax1.set_title('Jumlah Produksi per Ukuran')
        ax1.set_xlabel('Ukuran')
        ax1.set_ylabel('Jumlah Pakaian')

        labels = list(hasil_produksi.keys()) + ['Sisa Kain']
        sizes = meter_pakai + [sisa_kain]
        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6'][:len(labels)]
        ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax2.set_title(f'Pemakaian Kain (Total: {total_kain}m)')

    plt.tight_layout()
    return fig


def rekomendasi_kain(dataset, produk_target):
    """
    Memberikan rekomendasi jenis kain berdasarkan produk yang akan dibuat
    
    Args:
        dataset: Dataset parameter kain
        produk_target: Jenis produk yang akan dibuat (e.g. "Kemeja")
        
    Returns:
        List: Jenis kain yang direkomendasikan
    """
    rekomendasi = []
    for jenis_kain, data in dataset.items():
        if produk_target in data["rekomendasi_penggunaan"]:
            rekomendasi.append(jenis_kain)
    return rekomendasi if rekomendasi else list(dataset.keys())