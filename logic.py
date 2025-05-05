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

        hasil_produksi = {}
        total_keuntungan = 0
        sisa_kain = total_kain

        # Jika ada persentase, gunakan itu terlebih dahulu
        if persentase and any(v > 0 for v in persentase.values()):
            total_persen = sum(float(persentase.get(u, 0)) for u in ukuran_tersedia)
            if total_persen > 100:
                raise ValueError("Total persentase tidak boleh melebihi 100%")

            for ukuran in ukuran_tersedia:
                persen = float(persentase.get(ukuran, 0))
                if persen <= 0:
                    continue
                alokasi_meter = total_kain * (persen / 100)
                jumlah_pakaian = int(alokasi_meter // meter_per_ukuran[ukuran])
                if jumlah_pakaian > 0:
                    hasil_produksi[ukuran] = jumlah_pakaian
                    total_keuntungan += jumlah_pakaian * keuntungan_per_pakaian[ukuran]
                    sisa_kain -= jumlah_pakaian * meter_per_ukuran[ukuran]

            # Jika masih ada sisa kain, lanjutkan dengan greedy
            if sisa_kain > 0:
                rasio = {}
                for ukuran in ukuran_tersedia:
                    biaya = meter_per_ukuran[ukuran] * harga_per_meter
                    keuntungan_bersih = keuntungan_per_pakaian[ukuran] - biaya
                    rasio[ukuran] = keuntungan_bersih / meter_per_ukuran[ukuran]

                urutan = sorted(rasio.items(), key=lambda x: x[1], reverse=True)

                for ukuran, _ in urutan:
                    jumlah_pakaian = int(sisa_kain // meter_per_ukuran[ukuran])
                    if jumlah_pakaian > 0:
                        hasil_produksi[ukuran] = hasil_produksi.get(ukuran, 0) + jumlah_pakaian
                        total_keuntungan += jumlah_pakaian * keuntungan_per_pakaian[ukuran]
                        sisa_kain -= jumlah_pakaian * meter_per_ukuran[ukuran]

        else:
            # Jika tidak ada persentase, gunakan algoritma Greedy biasa
            rasio = {}
            for ukuran in ukuran_tersedia:
                biaya = meter_per_ukuran[ukuran] * harga_per_meter
                keuntungan_bersih = keuntungan_per_pakaian[ukuran] - biaya
                rasio[ukuran] = keuntungan_bersih / meter_per_ukuran[ukuran]

            urutan = sorted(rasio.items(), key=lambda x: x[1], reverse=True)

            for ukuran, _ in urutan:
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

        # Jika optimasi_sisa aktif, tambahkan pakaian dari ukuran termurah
        if optimasi_sisa and sisa_kain > 0:
            # Cari ukuran yang menggunakan kain paling sedikit
            ukuran_termurah = min(ukuran_tersedia, key=lambda u: meter_per_ukuran[u])
            max_tambahan = int(sisa_kain // meter_per_ukuran[ukuran_termurah])
            if max_tambahan > 0:
                hasil_produksi[ukuran_termurah] = hasil_produksi.get(ukuran_termurah, 0) + max_tambahan
                total_keuntungan += max_tambahan * keuntungan_per_pakaian[ukuran_termurah]
                sisa_kain -= max_tambahan * meter_per_ukuran[ukuran_termurah]

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