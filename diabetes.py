# Import library yang dibutuhkan
import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('RF_diabetes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Menyiapkan title dan deskripsi aplikasi
st.title("Prediksi Diabetes")
st.write("Masukkan data berikut untuk memprediksi apakah seseorang berisiko diabetes.")

# Membuat form input untuk input data
kehamilan = st.number_input('Jumlah Kehamilan', min_value=0, max_value=20, step=1)
glukosa = st.number_input('Kadar Glukosa', min_value=0, max_value=300, step=1)
tekanan_darah = st.number_input('Tekanan Darah', min_value=0, max_value=200, step=1)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, step=0.1)
umur = st.number_input('Umur', min_value=18, max_value=120, step=1)

# Menampilkan data yang telah dimasukkan oleh pengguna
st.write(f"Jumlah Kehamilan: {kehamilan}")
st.write(f"Kadar Glukosa: {glukosa}")
st.write(f"Tensi Darah: {tekanan_darah}")
st.write(f"BMI: {bmi}")
st.write(f"Umur: {umur}")

# Ketika tombol prediksi ditekan
if st.button('Prediksi'):
    with st.spinner('Melakukan prediksi...'):
        # Membuat array dengan data input
        input_data = np.array([[kehamilan, glukosa, tekanan_darah, bmi, umur]])

        # Menggunakan model untuk prediksi
        prediksi = model.predict(input_data)
    
    # Menampilkan hasil prediksi
    if prediksi == 1:
        st.markdown("<h2 style='color: red;'>Hasil Prediksi: Berpotensi terkena penyakit Diabetes</h2>", unsafe_allow_html=True)
        
        # Saran pola hidup untuk yang berpotensi diabetes
        st.write("""
        **Saran Pola Hidup:**
        1. **Meningkatkan Aktivitas Fisik**: Olahraga rutin seperti berjalan cepat, bersepeda, atau berenang dapat membantu mengatur kadar gula darah.
        2. **Menerapkan Pola Makan Sehat**: Konsumsi makanan rendah gula, tinggi serat, dan kaya akan nutrisi. Cobalah diet seimbang dengan banyak sayuran, buah-buahan, dan biji-bijian.
        3. **Mengelola Berat Badan**: Menurunkan berat badan jika Anda memiliki kelebihan berat badan dapat membantu menurunkan risiko diabetes.
        4. **Memantau Kadar Gula Darah**: Lakukan pemeriksaan rutin untuk memantau kadar gula darah dan berkonsultasi dengan dokter untuk pemantauan lebih lanjut.
        5. **Mengurangi Stres**: Praktikkan teknik relaksasi seperti meditasi atau yoga untuk mengurangi stres, yang dapat memengaruhi kadar gula darah.
        """)
    else:
        st.markdown("<h2 style='color: green;'>Hasil Prediksi: Tidak berpotensi terkena penyakit Diabetes</h2>", unsafe_allow_html=True)
        
        # Saran pola hidup untuk yang tidak berpotensi diabetes
        st.write("""
        **Saran Pola Hidup:**
        1. **Pertahankan Pola Makan Sehat**: Terus konsumsi makanan yang bergizi, rendah gula, dan kaya akan serat.
        2. **Rutin Berolahraga**: Pertahankan gaya hidup aktif dengan olahraga teratur, seperti berjalan, berlari, atau aktivitas fisik lainnya.
        3. **Jaga Berat Badan Ideal**: Pastikan untuk menjaga berat badan agar tetap sehat dan terhindar dari risiko penyakit metabolik.
        4. **Pemeriksaan Rutin**: Lakukan pemeriksaan kesehatan secara rutin untuk memastikan tetap dalam kondisi sehat dan terhindar dari penyakit lain.
        5. **Hindari Stres**: Kelola stres dengan baik dan praktikkan teknik relaksasi seperti yoga atau meditasi untuk menjaga kesehatan tubuh dan pikiran.
        """)

