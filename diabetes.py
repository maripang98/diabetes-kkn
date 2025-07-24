# Import library yang dibutuhkan
import streamlit as st
import pickle
import numpy as np
import os

# Menentukan path ke model
model_path = 'RF_diabetes_model.pkl'  # Pastikan path ini sesuai dengan lokasi file Anda

# Memuat model yang telah disimpan
with open(model_path, 'rb') as f:
    rf_model = pickle.load(f)  # Jangan gunakan [0] jika model bukan dalam list

# Judul dan deskripsi
st.title("Prediksi Diabetes")
st.write("Masukkan data berikut untuk memprediksi apakah seseorang berisiko diabetes.")

# Form input
kehamilan = st.number_input('Jumlah Kehamilan', min_value=0, max_value=20, step=1)
glukosa = st.number_input('Kadar Glukosa (mg/dL)', min_value=0, max_value=300, step=1)
tekanan_darah = st.number_input('Tekanan Darah (mmHg)', min_value=0, max_value=200, step=1)
bmi = st.number_input('BMI (Body Mass Index)', min_value=10.0, max_value=50.0, step=0.1, format="%.1f")
umur = st.number_input('Umur (tahun)', min_value=18, max_value=120, step=1)

# Validasi input sebelum diproses
if not all(map(np.isfinite, [kehamilan, glukosa, tekanan_darah, bmi, umur])):
    st.error("Pastikan semua nilai input valid dan tidak kosong!")
    st.stop()

# Menampilkan data yang telah dimasukkan
st.subheader("Data yang Dimasukkan")
st.write(f"Jumlah Kehamilan: {kehamilan}")
st.write(f"Kadar Glukosa: {glukosa}")
st.write(f"Tensi Darah: {tekanan_darah}")
st.write(f"BMI: {bmi}")
st.write(f"Umur: {umur}")

# Tombol prediksi
if st.button('Prediksi'):
    with st.spinner('Melakukan prediksi...'):
        # Membuat array dari input
        input_data = np.array([[kehamilan, glukosa, tekanan_darah, bmi, umur]])
        
        try:
            prediksi = rf_model.predict(input_data)

            # Menampilkan hasil
            if prediksi[0] == 1:
                st.markdown("<h2 style='color: red;'>Hasil Prediksi: Berpotensi terkena penyakit Diabetes</h2>", unsafe_allow_html=True)
                st.write("""
                **Saran Pola Hidup:**
                1. **Meningkatkan Aktivitas Fisik**: Olahraga rutin seperti berjalan cepat, bersepeda, atau berenang dapat membantu mengatur kadar gula darah.
                2. **Menerapkan Pola Makan Sehat**: Konsumsi makanan rendah gula, tinggi serat, dan kaya akan nutrisi.
                3. **Mengelola Berat Badan**: Menurunkan berat badan jika memiliki kelebihan berat badan dapat membantu menurunkan risiko diabetes.
                4. **Memantau Kadar Gula Darah**: Lakukan pemeriksaan rutin dan konsultasi dengan dokter.
                5. **Mengurangi Stres**: Meditasi atau yoga untuk relaksasi.
                """)
            else:
                st.markdown("<h2 style='color: green;'>Hasil Prediksi: Tidak berpotensi terkena penyakit Diabetes</h2>", unsafe_allow_html=True)
                st.write("""
                **Saran Pola Hidup:**
                1. **Pertahankan Pola Makan Sehat**: Makanan bergizi, rendah gula, dan kaya serat.
                2. **Rutin Berolahraga**: Jalan, lari, atau aktivitas fisik lain secara teratur.
                3. **Jaga Berat Badan Ideal**: Hindari risiko penyakit metabolik.
                4. **Pemeriksaan Rutin**: Cek kesehatan berkala.
                5. **Hindari Stres**: Kelola stres dengan baik dan tetap rileks.
                """)
        except Exception as e:
            st.error(f"Terjadi error saat melakukan prediksi: {e}")
