import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul web app
st.title("Visualisasi Data Produksi Beras")

# Menu Sidebar
menu = st.sidebar.selectbox("Menu", ["Latar Belakang", "Data", "Diagram"])

# Gaya untuk setiap halaman
st.markdown(
    """
    <style>
    .sidebar-content {
        background-color: #f4f4f4;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .sidebar-title {
        font-size: 20px;
    }
    .sidebar-menu-item {
        padding: 10px 0;
    }
    .sidebar-menu-item-active {
        background-color: #2e7d32;
        color: #fff;
        padding: 10px 0;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Latar Belakang
if menu == "Latar Belakang":
    st.markdown("<h1 class='sidebar-title'>Latar Belakang</h1>", unsafe_allow_html=True)
    st.write("Beras adalah komoditas pertanian penting di Indonesia dan merupakan tanaman utama yang dapat ditanam sepanjang tahun. Produktivitas padi atau beras dalam 3 tahun terakhir fluktuatif di semua provinsi di Indonesia.")
    
    st.markdown("<h2 class='sidebar-title'>Konteks</h2>", unsafe_allow_html=True)
    st.write("Data ini diambil dari Badan Pusat Statistik Indonesia (https://www.bps.go.id/) untuk menggambarkan produksi, produktivitas, dan luas lahan yang digunakan untuk budidaya padi dari tahun 2020 hingga 2022.")
    
    st.markdown("<h2 class='sidebar-title'>Penjelasan Bidang Data</h2>", unsafe_allow_html=True)
    st.write("1. **Provinsi**: Provinsi di Indonesia")
    st.write("2. **Tahun**: Tahun dari 2020 hingga 2022")
    st.write("3. **Yield.Areal(ha)**: Penggunaan lahan untuk beras")
    st.write("4. **Productivity(kw/ha)**: Produktivitas beras di setiap provinsi")
    st.write("5. **Production.(ton)**: Hasil beras di setiap provinsi")
    
# Konteks Data
if menu == "Data":   
    # Membaca data
    data = pd.read_csv("data_beras.csv") 
    st.markdown("<h1 class='sidebar-title'>Data</h1>", unsafe_allow_html=True)
    
    # Membuat selectbox untuk memfilter tahun
    tahun_terpilih = st.selectbox("Pilih Tahun", data["Year"].unique())
    
    # Filter data berdasarkan tahun terpilih
    data_terfilter = data[data["Year"] == tahun_terpilih]
    
    # Menampilkan data yang sudah difilter
    st.write(f"Data untuk tahun {tahun_terpilih}:")
    st.dataframe(data_terfilter)
    
    

    # Menyiapkan palet warna
    palette = sns.color_palette("Set3", len(data_terfilter))

    # Membuat grafik bar dengan sumbu x dan y yang dibalik
    fig, ax = plt.subplots(figsize=(14, 12))
    bars = ax.barh(data_terfilter['Provinsi'], data_terfilter['Production.(ton)'], color=palette)

    # Menambahkan label dan warna pada grafik bar
    for bar, color in zip(bars, palette):
        bar.set_color(color)
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center', color='black')

    # Mengatur label sumbu x dan y serta judul grafik
    ax.set_xlabel('Produksi (ton)')
    ax.set_ylabel('Provinsi')
    ax.set_title(f'Produksi Padi Nasional per Provinsi Tahun {tahun_terpilih }')

    # Menampilkan grafik bar
    st.subheader(f'Grafik Produksi Padi Tahun {tahun_terpilih }')
    st.pyplot(fig)
    
# Diagram
if menu == "Diagram":
    # Membaca data
    data = pd.read_csv("data_beras.csv")
    st.markdown("<h1 class='sidebar-title'>Diagram</h1>", unsafe_allow_html=True)
    total_produksi_tahun = data.groupby("Year")["Production.(ton)"].sum()
    
    # Menampilkan total produksi
    st.write("Total Produksi Beras tiap Tahun:")
    st.dataframe(total_produksi_tahun)
    
    # Membuat diagram batang dari total produksi
    plt.figure(figsize=(12, 6))
    plt.bar(total_produksi_tahun.index, total_produksi_tahun.values)
    plt.xlabel("Tahun")
    plt.ylabel("Total Produksi")
    plt.title("Diagram Batang Total Produksi Beras per Tahun")
    plt.ylim(54000000, 55000000)
    plt.xticks(total_produksi_tahun.index, rotation=45)
    st.pyplot(plt)
    
    # Menghitung rata-rata produktivitas berdasarkan tahun
    rata_rata_produktivitas = data.groupby("Year")["Productivity(kw/ha)"].mean()
    
    # Menampilkan rata-rata produktivitas
    st.write("Rata-rata Produktivitas Beras tiap Tahun:")
    st.dataframe(rata_rata_produktivitas)
    
    # Membuat diagram garis dari rata-rata produktivitas
    plt.figure(figsize=(12, 6))
    plt.plot(rata_rata_produktivitas.index, rata_rata_produktivitas.values, marker='o')
    plt.xlabel("Tahun")
    plt.ylabel("Produktivitas")
    plt.title("Diagram Garis Rata-Rata Produktivitas Beras per Tahun")
    plt.ylim(43, 47)
    plt.xticks(rata_rata_produktivitas.index, rotation=45)
    st.pyplot(plt)
    

