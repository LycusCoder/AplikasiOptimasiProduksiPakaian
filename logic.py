import matplotlib.pyplot as plt


def hitung_penggunaan_kain(panjang_m, lebar_m, jenis_kain, dataset,
                            ukuran_fokus=None, optimasi_sisa=False, persentase=None):
    """
    Hitung produksi optimal berdasarkan luas kain (panjang x lebar)
    """
    # Ambil parameter kain
    data_kain = dataset[jenis_kain]
    meter_per_ukuran = data_kain["meter_per_ukuran"]
    keuntungan_per_pakaian = data_kain["keuntungan_per_pakaian"]

    luas_kain = panjang_m * lebar_m
    ukuran_tersedia = list(meter_per_ukuran.keys())
    if ukuran_fokus:
        ukuran_tersedia = [u for u in ukuran_tersedia if u in ukuran_fokus]
        if not ukuran_tersedia:
            raise ValueError("Tidak ada ukuran yang valid untuk difokuskan")

    hasil = {}
    total_keuntungan = 0
    sisa_kain = luas_kain

    if persentase and any(persentase.values()):
        total_persen = sum(float(persentase.get(u, 0)) for u in ukuran_tersedia)
        if total_persen > 100:
            raise ValueError("Total persentase tidak boleh melebihi 100%")
        for ukuran in ukuran_tersedia:
            p = float(persentase.get(ukuran, 0))
            if p <= 0:
                continue
            alokasi = luas_kain * (p / 100)
            jumlah = int(alokasi // meter_per_ukuran[ukuran])
            if jumlah > 0:
                hasil[ukuran] = jumlah
                total_keuntungan += jumlah * keuntungan_per_pakaian[ukuran]
                sisa_kain -= jumlah * meter_per_ukuran[ukuran]
    else:
        rasio = {u: keuntungan_per_pakaian[u] / meter_per_ukuran[u] for u in ukuran_tersedia}
        urutan = sorted(rasio.items(), key=lambda x: x[1], reverse=True)
        for ukuran, _ in urutan:
            jumlah = int(sisa_kain // meter_per_ukuran[ukuran])
            if jumlah > 0:
                hasil[ukuran] = jumlah
                total_keuntungan += jumlah * keuntungan_per_pakaian[ukuran]
                sisa_kain -= jumlah * meter_per_ukuran[ukuran]

    if optimasi_sisa and sisa_kain > 0:
        ukuran_termurah = min(ukuran_tersedia, key=lambda u: meter_per_ukuran[u])
        max_tambahan = int(sisa_kain // meter_per_ukuran[ukuran_termurah])
        if max_tambahan > 0:
            hasil[ukuran_termurah] = hasil.get(ukuran_termurah, 0) + max_tambahan
            total_keuntungan += max_tambahan * keuntungan_per_pakaian[ukuran_termurah]
            sisa_kain -= max_tambahan * meter_per_ukuran[ukuran_termurah]

    fig = buat_grafik(hasil, meter_per_ukuran, luas_kain, sisa_kain)
    return hasil, total_keuntungan, sisa_kain, fig


def buat_grafik(hasil, meter_per_ukuran, luas_total, sisa_kain):
    """Buat grafik visualisasi pemakaian kain"""
    fig, ax = plt.subplots(figsize=(8, 5))

    if not hasil:
        ax.text(0.5, 0.5, "Tidak ada produksi", ha='center', va='center')
        return fig

    ukuran = list(hasil.keys())
    pemakaian = [hasil[u] * meter_per_ukuran[u] for u in ukuran]

    bars = ax.bar(ukuran, pemakaian)
    ax.set_title("Pemakaian Kain per Ukuran (m²)")
    ax.set_xlabel("Ukuran")
    ax.set_ylabel("Luas Terpakai (m²)")

    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.2f} m²",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom'
        )

    return fig


def rekomendasi_kain(dataset, produk_target):
    """Rekomendasikan jenis kain berdasarkan produk target"""
    return [
        jenis_kain for jenis_kain, info in dataset.items()
        if produk_target in info.get("rekomendasi_penggunaan", [])
    ] or list(dataset.keys())