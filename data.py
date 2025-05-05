# data.py
# Dataset parameter kain: {jenis_kain: {meter_per_ukuran, harga_per_meter, keuntungan_per_pakaian, elastisitas, rekomendasi_penggunaan}}

DATASET_KAIN = {
    "Katun": {
        "meter_per_ukuran": {"S": 1.5, "M": 2.0, "L": 2.5, "XL": 3.0},
        "harga_per_meter": 20000,
        "keuntungan_per_pakaian": {"S": 45000, "M": 55000, "L": 65000, "XL": 75000},
        "elastisitas": "Rendah",
        "rekomendasi_penggunaan": ["Kemeja", "Baju santai", "Celana panjang"]
    },
    "Polyester": {
        "meter_per_ukuran": {"S": 1.2, "M": 1.8, "L": 2.2, "XL": 2.8},
        "harga_per_meter": 15000,
        "keuntungan_per_pakaian": {"S": 35000, "M": 45000, "L": 55000, "XL": 65000},
        "elastisitas": "Sedang",
        "rekomendasi_penggunaan": ["Seragam", "Jas", "Pakaian formal"]
    },
    "Rayon": {
        "meter_per_ukuran": {"S": 1.4, "M": 1.9, "L": 2.4, "XL": 2.9},
        "harga_per_meter": 18000,
        "keuntungan_per_pakaian": {"S": 40000, "M": 50000, "L": 60000, "XL": 70000},
        "elastisitas": "Rendah",
        "rekomendasi_penggunaan": ["Dress", "Blus", "Atasan santai"]
    },
    "Wool": {
        "meter_per_ukuran": {"S": 1.6, "M": 2.1, "L": 2.6, "XL": 3.1},
        "harga_per_meter": 32000,
        "keuntungan_per_pakaian": {"S": 55000, "M": 65000, "L": 75000, "XL": 85000},
        "elastisitas": "Rendah",
        "rekomendasi_penggunaan": ["Jas", "Jaket tebal", "Celana formal musim dingin"]
    },
    "Spandex": {
        "meter_per_ukuran": {"S": 1.0, "M": 1.4, "L": 1.8, "XL": 2.2},
        "harga_per_meter": 23000,
        "keuntungan_per_pakaian": {"S": 50000, "M": 60000, "L": 70000, "XL": 80000},
        "elastisitas": "Tinggi",
        "rekomendasi_penggunaan": ["Legging", "Baju olahraga", "Swimsuit"]
    },
    "Linen": {
        "meter_per_ukuran": {"S": 1.7, "M": 2.2, "L": 2.7, "XL": 3.2},
        "harga_per_meter": 25000,
        "keuntungan_per_pakaian": {"S": 60000, "M": 70000, "L": 80000, "XL": 90000},
        "elastisitas": "Rendah",
        "rekomendasi_penggunaan": ["Gaun", "Setelan ringan", "Kemeja premium"]
    },
    "Denim": {
        "meter_per_ukuran": {"S": 1.8, "M": 2.3, "L": 2.8, "XL": 3.3},
        "harga_per_meter": 38000,
        "keuntungan_per_pakaian": {"S": 65000, "M": 75000, "L": 85000, "XL": 95000},
        "elastisitas": "Rendah hingga Sedang",
        "rekomendasi_penggunaan": ["Jeans", "Rok denim", "Jaket jeans"]
    }
}