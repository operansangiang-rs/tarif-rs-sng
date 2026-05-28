import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Tarif RS SNG", layout="wide")

st.title("🏥 Sistem Informasi Tarif RS SNG")

# 1. Data Non Intensive (Ditanam langsung di script)
data_non = {
    "Kategori": ["Perawatan Umum"]*6 + ["Perawatan Khusus"]*4,
    "Kelas": ["Kelas III", "Kelas II", "Kelas I", "VIP", "DELUXE", "VVIP", "Isolasi", "Observasi", "Perinatologi", "HCU"],
    "Tarif": [250000, 350000, 550000, 700000, 850000, 1200000, 650000, 550000, 500000, 600000],
    "Deposit": [3000000, 3500000, 5000000, 7500000, 10000000, 12000000, 6500000, 5500000, 5000000, 6000000]
}
df_non = pd.DataFrame(data_non)

# 2. Data Intensive
data_int = {
    "Jenis": ["Kamar Perawatan", "Visite Dokter", "Dokter Ruangan", "Para Medis", "Monitor", "Saturasi Oksigen", "Syringe Pump (2)", "Infuse Pump (2)", "Ventilator", "Kasur Dekubitus", "Oksigen", "Udara Tekan", "Incubator", "Blue Light", "Pemasangan ETT / Intubasi", "Pemasangan Ventilator"],
    "ICU": [1000000, 250000, 80000, 85000, 320000, 250000, 580000, 640000, 1200000, 150000, 1440000, 580000, 0, 0, 510000, 620000],
    "ICU ISOLASI": [1200000, 250000, 80000, 1000000, 320000, 250000, 580000, 640000, 1200000, 150000, 1440000, 580000, 0, 0, 510000, 620000],
    "NICU": [1000000, 250000, 80000, 85000, 320000, 250000, 580000, 640000, 1200000, 0, 1440000, 580000, 320000, 310000, 510000, 620000]
}
df_int = pd.DataFrame(data_int)

# Tampilan Streamlit
menu = st.sidebar.radio("Pilih Kategori", ["Non Intensive", "Intensive"])

if menu == "Non Intensive":
    st.subheader("Data Tarif Non Intensive")
    st.dataframe(df_non, use_container_width=True)
    
    # Simulasi
    kelas_pilih = st.selectbox("Pilih Kelas", df_non['Kelas'])
    hari = st.number_input("Jumlah Hari:", min_value=1, value=1)
    tarif = df_non[df_non['Kelas'] == kelas_pilih]['Tarif'].values[0]
    st.success(f"Total: Rp {tarif * hari:,.0f}")

elif menu == "Intensive":
    st.subheader("Data Tarif Intensive")
    st.dataframe(df_int, use_container_width=True)
    
    ruang = st.selectbox("Pilih Ruang", ["ICU", "ICU ISOLASI", "NICU"])
    st.success(f"Total per hari: Rp {df_int[ruang].sum():,.0f}")
