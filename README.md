# 🛍️ Smart Retail Visitor Prediction System

## UAS Teknologi Big Data

### Identitas Mahasiswa

* Nama : Dina Muzaina Aqillah
* NIM : 230104040221
* Kelas : TI23A
* Mata Kuliah : Teknologi Big Data
* Dosen Pengampu : Muhayat, M.IT

---

## 📌 Deskripsi Project

Smart Retail Visitor Prediction System merupakan sistem analisis pengunjung pusat perbelanjaan yang dibangun menggunakan teknologi Big Data. Sistem ini melakukan simulasi data pengunjung pada beberapa zona pusat perbelanjaan, kemudian melakukan proses agregasi menggunakan PySpark, menyimpan hasil ke format Parquet, melakukan prediksi menggunakan Machine Learning Linear Regression, dan menampilkan hasil analisis melalui dashboard Streamlit.

Pipeline yang digunakan:

Visitor Tracking → Spark Aggregation → Parquet Storage → Machine Learning Prediction → Streamlit Dashboard

---

## 🎯 Tujuan Project

1. Mengimplementasikan Big Data Pipeline menggunakan PySpark.
2. Melakukan transformasi data pengunjung pusat perbelanjaan.
3. Menyimpan hasil pengolahan dalam format Parquet.
4. Menerapkan Machine Learning menggunakan Linear Regression.
5. Menampilkan visualisasi data menggunakan Streamlit dan Plotly.

---

## 🛠️ Teknologi yang Digunakan

* Python
* Apache Spark (PySpark)
* Parquet
* Scikit-Learn
* Streamlit
* Plotly
* Pandas

---

## 📂 Struktur Project

```text
uas-tbg-230104040221/
│
├── main_uts_230104040221.py
├── dashboard_230104040221.py
├── README.md
│
└── output/
    ├── visitor_total/
    ├── visitor_time/
    └── ml_visitor/
```

---

## 📊 Dataset

### Field Data

* timestamp
* zone
* visitor_count

### Zona Pengunjung

* FoodCourt
* FashionArea
* Cinema

### Karakteristik Data

* Durasi data: 180 menit
* Jumlah pengunjung acak: 10 – 500 orang

---

## ⚙️ Tahapan Pengolahan Data

### 1. Data Generation

Data pengunjung dihasilkan secara acak untuk tiga zona pusat perbelanjaan selama 180 menit.

### 2. Spark Transformation

Dilakukan beberapa proses analisis:

* Total pengunjung tiap zona
* Tren pengunjung setiap 15 menit
* Dataset Machine Learning berdasarkan jam

### 3. Parquet Storage

Hasil transformasi disimpan dalam format Parquet pada folder:

* output/visitor_total
* output/visitor_time
* output/ml_visitor

### 4. Machine Learning

Model yang digunakan:

* Linear Regression

Target prediksi:

* visitor_count berdasarkan hour

### 5. Dashboard Visualization

Dashboard dibuat menggunakan Streamlit dan Plotly dengan fitur:

* Dropdown filter zona
* KPI total pengunjung
* Grafik tren pengunjung
* Grafik prediksi pengunjung
* Informasi jam sibuk pengunjung

---

## ▶️ Cara Menjalankan Program

### Menjalankan Pipeline Big Data

```bash
python3 main_uts_230104040221.py
```

### Menjalankan Dashboard

```bash
streamlit run dashboard_230104040221.py
```

---

## 📈 Hasil Analisis

Berdasarkan hasil simulasi data dan proses Machine Learning, sistem mampu mengidentifikasi tren jumlah pengunjung pada setiap zona pusat perbelanjaan. Informasi jam sibuk dapat digunakan sebagai dasar pengambilan keputusan untuk pengelolaan sumber daya, penjadwalan staf, serta peningkatan pelayanan pada waktu dengan tingkat kunjungan tinggi.

---

## ✅ Checklist Implementasi

* PySpark berhasil dijalankan
* Transformasi data berhasil
* Penyimpanan Parquet berhasil
* Dashboard Streamlit berjalan
* Grafik Plotly tampil
* Prediksi Linear Regression berjalan
* Filter zona berfungsi dengan baik

---

## 📸 Dokumentasi

Tambahkan screenshot berikut pada repository:

1. Screenshot terminal saat proses Parquet berhasil dibuat.
2. Screenshot folder output Parquet.
3. Screenshot dashboard Streamlit.
4. Screenshot grafik prediksi pengunjung.

---

## 👨‍💻 Author

Dina Muzaina Aqillah
NIM 230104040221
Program Studi Teknologi Informasi
