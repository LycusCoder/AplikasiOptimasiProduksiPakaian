import os
import json
import streamlit as st
import pandas as pd
from logic import hitung_penggunaan_kain, rekomendasi_kain

# Load dataset kain dari JSON
kain_path = os.path.join(os.path.dirname(__file__), 'data', 'kain.json')
with open(kain_path, 'r', encoding='utf-8') as f:
    DATASET = json.load(f)

# Load daftar produk
jenispakaian_path = os.path.join(os.path.dirname(__file__), 'data', 'jenispakaian.json')
try:
    with open(jenispakaian_path, 'r', encoding='utf-8') as f:
        DAFTAR_PRODUK = json.load(f)
except Exception:
    DAFTAR_PRODUK = [
        "Kemeja", "Celana panjang", "Seragam", "Dress",
        "Blus", "Jas", "Legging", "Gaun", "Jeans"
    ]

DEFAULT_KAIN = list(DATASET.keys())[0]

st.set_page_config(page_title="Optimasi Produksi Pakaian", layout="wide")
st.title("🧶 Aplikasi Optimasi Produksi Pakaian")
st.markdown("Aplikasi untuk menghitung produksi optimal berdasarkan ukuran kain (Panjang × Lebar)")

def run():
    tab_input, tab_hasil = st.tabs(["📊 Input Data", "📈 Hasil Optimasi"])

    with tab_input:
        with st.form(key="form_input"):
            col1, col2 = st.columns(2)

            with col1:
                produk_target = st.selectbox("Jenis Produk:", options=DAFTAR_PRODUK)
                jenis_kain = st.selectbox(
                    "Jenis Kain:",
                    options=list(DATASET.keys()),
                    index=list(DATASET.keys()).index(DEFAULT_KAIN)
                )
                st.subheader("Ukuran Kain (meter)")
                panjang = st.number_input("Panjang Kain (meter):", value=10.0, step=0.5)
                lebar = st.number_input("Lebar Kain (meter):", value=1.5, step=0.1)
                luas_total = panjang * lebar
                st.info(f"Luas Total Kain: **{luas_total:.2f} m²**")

            with col2:
                rekom_kain = rekomendasi_kain(DATASET, produk_target)
                st.markdown(f"**Rekomendasi Kain:** {', '.join(rekom_kain)}")
                if jenis_kain not in rekom_kain:
                    st.warning(f"{jenis_kain} tidak direkomendasikan untuk {produk_target}")

            # Fokus ukuran
            ukuran_tersedia = list(DATASET[jenis_kain]["meter_per_ukuran"].keys())
            st.subheader("Fokus Ukuran Produksi")
            cols = st.columns(len(ukuran_tersedia))
            ukuran_fokus = []
            for i, ukuran in enumerate(ukuran_tersedia):
                if cols[i].checkbox(ukuran.upper(), value=True):
                    ukuran_fokus.append(ukuran)

            # Persentase produksi
            st.subheader("Persentase Produksi (%)")
            cols_persen = st.columns(len(ukuran_tersedia))
            persentase = {}
            for i, ukuran in enumerate(ukuran_tersedia):
                if ukuran in ukuran_fokus:
                    persentase[ukuran] = cols_persen[i].number_input(
                        ukuran.upper(),
                        min_value=0.0,
                        max_value=100.0,
                        value=25.0,
                        key=f"persen_{ukuran}"
                    )

            total_persen = sum(persentase.values()) if ukuran_fokus else 0
            st.write(f"**Total Persentase Saat Ini**: {total_persen:.1f}%")

            if total_persen > 100:
                st.error("⚠️ Total persentase melebihi 100%. Harap sesuaikan.")

            optimasi_sisa = st.checkbox("Optimasi untuk Minimasi Sisa Kain")
            submit = st.form_submit_button("HITUNG PRODUKSI OPTIMAL")

    with tab_hasil:
        if submit:
            if total_persen > 100:
                st.error("Total persentase tidak boleh melebihi 100%")
            elif not ukuran_fokus:
                st.warning("Silakan pilih setidaknya satu ukuran.")
            else:
                try:
                    hasil, keuntungan_total, sisa_kain, fig = hitung_penggunaan_kain(
                        panjang,
                        lebar,
                        jenis_kain,
                        DATASET,
                        ukuran_fokus,
                        optimasi_sisa,
                        persentase
                    )
                    # Siapkan DataFrame hasil
                    rows = []
                    for ukuran, jumlah in hasil.items():
                        meter = DATASET[jenis_kain]["meter_per_ukuran"][ukuran]
                        keuntungan = DATASET[jenis_kain]["keuntungan_per_pakaian"][ukuran]
                        rows.append({
                            "Ukuran": ukuran.upper(),
                            "Jumlah": jumlah,
                            "Meter/Pakaian": f"{meter:.2f} m²",
                            "Total Meter": f"{meter * jumlah:.2f} m²",
                            "Keuntungan/Pakaian": f"Rp{int(keuntungan):,}".replace(",", "."),
                            "Total Keuntungan": f"Rp{int(keuntungan * jumlah):,}".replace(",", ".")
                        })
                    df = pd.DataFrame(rows)
                    st.dataframe(df, use_container_width=True)
                    st.pyplot(fig)

                    efisiensi = (luas_total - sisa_kain) / luas_total * 100 if luas_total > 0 else 0
                    st.success(
                        f"📈 **Total Keuntungan**: Rp{int(keuntungan_total):,}  \n"
                        f"🧵 **Sisa Kain**: {sisa_kain:.2f} m²  \n"
                        f"🔍 **Efisiensi**: {efisiensi:.1f}%"
                    )
                except Exception as e:
                    st.error(f"🚨 Kesalahan: {str(e)}")
