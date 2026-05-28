import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Tarif RS SNG", layout="wide")

st.title("🏥 Sistem Informasi Tarif RS SNG")

# Load Data (Pastikan file csv ada di folder yang sama)
try:
    df_non = pd.read_csv('tarif_non_intensive.csv')
    df_int = pd.read_csv('tarif_intensive.csv')
except FileNotFoundError:
    st.error("File data tidak ditemukan. Pastikan file .csv sudah ada di folder!")
    st.stop()

# Sidebar Menu
menu = st.sidebar.radio("Pilih Kategori Perawatan", ["Non Intensive", "Intensive"])

if menu == "Non Intensive":
    st.header("Perawatan Non Intensive")
    st.dataframe(df_non, use_container_width=True)
    
    # Input Simulasi
    st.subheader("Simulasi Biaya")
    col1, col2 = st.columns(2)
    with col1:
        kelas_pilih = st.selectbox("Pilih Kelas:", df_non['Kelas'])
    with col2:
        hari = st.number_input("Jumlah Hari Inap:", min_value=1, value=1)
    
    tarif = df_non[df_non['Kelas'] == kelas_pilih]['Tarif'].values[0]
    deposit = df_non[df_non['Kelas'] == kelas_pilih]['Deposit'].values[0]
    total = tarif * hari
    
    st.info(f"Tarif per hari: Rp {tarif:,.0f}")
    st.success(f"Total Biaya Kamar ({hari} hari): Rp {total:,.0f}")
    st.warning(f"Deposit yang diperlukan: Rp {deposit:,.0f}")

elif menu == "Intensive":
    st.header("Perawatan Intensive")
    st.dataframe(df_int, use_container_width=True)
    
    st.subheader("Simulasi Total per Hari")
    ruang = st.selectbox("Pilih Ruang:", ["ICU", "ICU ISOLASI", "NICU"])
    
    # Menghitung total semua item untuk ruang yang dipilih
    total_harian = df_int[ruang].sum()
    
    st.success(f"Total Estimasi Biaya per Hari di {ruang}: Rp {total_harian:,.0f}")
