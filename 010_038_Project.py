import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="SPK Vendor Laptop - Fuzzy Tahani",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================
df = pd.read_csv("data.csv")

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("⚙️ Menu")

page = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "🏠 Dashboard",
        "📋 Data Vendor",
        "ℹ️ Rentang Nilai Fuzzy",
        "🧠 Fuzzifikasi",
        "🔍 Query Tahani",
        "🏆 Ranking",
        "📊 Visualisasi"
    ]
)

st.sidebar.divider()

# =====================================================
# QUERY INPUT
# =====================================================
st.sidebar.subheader("Input Query Fuzzy")

harga_query = st.sidebar.selectbox(
    "Harga",
    ["Murah", "Sedang", "Mahal"]
)

kualitas_query = st.sidebar.selectbox(
    "Kualitas Laptop",
    ["Rendah", "Sedang", "Tinggi"]
)

garansi_query = st.sidebar.selectbox(
    "Garansi",
    ["Pendek", "Sedang", "Lama"]
)

pelayanan_query = st.sidebar.selectbox(
    "Pelayanan Vendor",
    ["Buruk", "Cukup", "Baik"]
)

pengiriman_query = st.sidebar.selectbox(
    "Waktu Pengiriman",
    ["Cepat", "Sedang", "Lambat"]
)

rating_query = st.sidebar.selectbox(
    "Rating",
    ["Buruk", "Baik"]
)

# =====================================================
# FUNGSI KEANGGOTAAN HARGA
# =====================================================
def harga_murah(x):

    if x <= 8:
        return 1

    elif x >= 12:
        return 0

    else:
        return (12 - x) / 4


def harga_sedang(x):

    if 7 <= x <= 10:
        return (x - 7) / 3

    elif 10 < x <= 13:
        return (13 - x) / 3

    else:
        return 0


def harga_mahal(x):

    if x <= 10:
        return 0

    elif x >= 14:
        return 1

    else:
        return (x - 10) / 4

# =====================================================
# KUALITAS
# =====================================================
def kualitas_rendah(x):

    if x <= 75:
        return 1

    elif x >= 85:
        return 0

    else:
        return (85 - x) / 10


def kualitas_sedang(x):

    if 75 <= x <= 85:
        return (x - 75) / 10

    elif 85 < x <= 95:
        return (95 - x) / 10

    else:
        return 0


def kualitas_tinggi(x):

    if x <= 85:
        return 0

    elif x >= 95:
        return 1

    else:
        return (x - 85) / 10

# =====================================================
# GARANSI
# =====================================================
def garansi_pendek(x):

    if x <= 12:
        return 1

    elif x >= 24:
        return 0

    else:
        return (24 - x) / 12


def garansi_sedang(x):

    if 12 <= x <= 24:
        return (x - 12) / 12

    elif 24 < x <= 36:
        return (36 - x) / 12

    else:
        return 0


def garansi_lama(x):

    if x <= 24:
        return 0

    elif x >= 36:
        return 1

    else:
        return (x - 24) / 12

# =====================================================
# PELAYANAN
# =====================================================
def pelayanan_buruk(x):

    if x <= 75:
        return 1

    elif x >= 85:
        return 0

    else:
        return (85 - x) / 10


def pelayanan_cukup(x):

    if 75 <= x <= 85:
        return (x - 75) / 10

    elif 85 < x <= 95:
        return (95 - x) / 10

    else:
        return 0


def pelayanan_baik(x):

    if x <= 85:
        return 0

    elif x >= 95:
        return 1

    else:
        return (x - 85) / 10

# =====================================================
# PENGIRIMAN
# =====================================================
def pengiriman_cepat(x):

    if x <= 2:
        return 1

    elif x >= 5:
        return 0

    else:
        return (5 - x) / 3


def pengiriman_sedang(x):

    if 2 <= x <= 4:
        return (x - 2) / 2

    elif 4 < x <= 6:
        return (6 - x) / 2

    else:
        return 0


def pengiriman_lambat(x):

    if x <= 4:
        return 0

    elif x >= 6:
        return 1

    else:
        return (x - 4) / 2

# =====================================================
# RATING
# =====================================================
def rating_buruk(x):

    if x <= 4.0:
        return 1

    elif x >= 5.0:
        return 0

    else:
        return (5.0 - x)


def rating_baik(x):

    if x <= 4.0:
        return 0

    elif x >= 5.0:
        return 1

    else:
        return (x - 4.0)

# =====================================================
# HITUNG FUZZIFIKASI
# =====================================================
hasil = []

for i in range(len(df)):

    vendor = df.loc[i, "Vendor"]

    harga = df.loc[i, "Harga"]
    kualitas = df.loc[i, "Kualitas"]
    garansi = df.loc[i, "Garansi"]
    pelayanan = df.loc[i, "Pelayanan"]
    pengiriman = df.loc[i, "Pengiriman"]
    rating = df.loc[i, "Rating"]

    # HARGA
    if harga_query == "Murah":
        f_harga = harga_murah(harga)

    elif harga_query == "Sedang":
        f_harga = harga_sedang(harga)

    else:
        f_harga = harga_mahal(harga)

    # KUALITAS
    if kualitas_query == "Rendah":
        f_kualitas = kualitas_rendah(kualitas)

    elif kualitas_query == "Sedang":
        f_kualitas = kualitas_sedang(kualitas)

    else:
        f_kualitas = kualitas_tinggi(kualitas)

    # GARANSI
    if garansi_query == "Pendek":
        f_garansi = garansi_pendek(garansi)

    elif garansi_query == "Sedang":
        f_garansi = garansi_sedang(garansi)

    else:
        f_garansi = garansi_lama(garansi)

    # PELAYANAN
    if pelayanan_query == "Buruk":
        f_pelayanan = pelayanan_buruk(pelayanan)

    elif pelayanan_query == "Cukup":
        f_pelayanan = pelayanan_cukup(pelayanan)

    else:
        f_pelayanan = pelayanan_baik(pelayanan)

    # PENGIRIMAN
    if pengiriman_query == "Cepat":
        f_pengiriman = pengiriman_cepat(pengiriman)

    elif pengiriman_query == "Sedang":
        f_pengiriman = pengiriman_sedang(pengiriman)

    else:
        f_pengiriman = pengiriman_lambat(pengiriman)

    # RATING
    if rating_query == "Buruk":
        f_rating = rating_buruk(rating)

    else:
        f_rating = rating_baik(rating)

    # FIRE STRENGTH
    fire_strength = min(
        f_harga,
        f_kualitas,
        f_garansi,
        f_pelayanan,
        f_pengiriman,
        f_rating
    )

    hasil.append([
        vendor,
        round(f_harga, 3),
        round(f_kualitas, 3),
        round(f_garansi, 3),
        round(f_pelayanan, 3),
        round(f_pengiriman, 3),
        round(f_rating, 3),
        round(fire_strength, 3)
    ])

# =====================================================
# DATAFRAME HASIL
# =====================================================
hasil_df = pd.DataFrame(
    hasil,
    columns=[
        "Vendor",
        "Harga",
        "Kualitas",
        "Garansi",
        "Pelayanan",
        "Pengiriman",
        "Rating",
        "Fire Strength"
    ]
)

ranking = hasil_df.sort_values(
    by="Fire Strength",
    ascending=False
).reset_index(drop=True)

ranking.index += 1

# =====================================================
# DASHBOARD
# =====================================================
if page == "🏠 Dashboard":

    st.title("🧠 Sistem Pendukung Keputusan")

    st.subheader(
        "Pemilihan Vendor Laptop Menggunakan Fuzzy Tahani"
    )

    st.write("""
    Sistem ini digunakan untuk membantu perusahaan
    memilih vendor laptop terbaik menggunakan
    metode Fuzzy Tahani berdasarkan beberapa
    kriteria.
    """)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Jumlah Vendor",
            len(df)
        )

    with c2:
        st.metric(
            "Vendor Terbaik",
            ranking.iloc[0]["Vendor"]
        )

    with c3:
        st.metric(
            "Fire Strength",
            ranking.iloc[0]["Fire Strength"]
        )

# =====================================================
# DATA VENDOR
# =====================================================
elif page == "📋 Data Vendor":

    st.title("📋 Data Vendor Laptop")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# =====================================================
# RENTANG NILAI FUZZY
# =====================================================
elif page == "ℹ️ Rentang Nilai Fuzzy":

    st.title("ℹ️ Rentang Nilai Fuzzy")

    st.write("""
    Halaman ini menjelaskan kategori dan
    rentang nilai fuzzy yang digunakan
    pada metode Fuzzy Tahani.
    """)

    st.subheader("💰 Harga")
    st.write("Murah ≤ 8 | Sedang 7 - 13 | Mahal ≥ 14")

    st.subheader("💻 Kualitas Laptop")
    st.write("Rendah ≤ 75 | Sedang 75 - 95 | Tinggi ≥ 95")

    st.subheader("🛡️ Garansi")
    st.write("Pendek ≤ 12 | Sedang 12 - 36 | Lama ≥ 36")

    st.subheader("🤝 Pelayanan")
    st.write("Buruk ≤ 75 | Cukup 75 - 95 | Baik ≥ 95")

    st.subheader("🚚 Pengiriman")
    st.write("Cepat ≤ 2 | Sedang 2 - 6 | Lambat ≥ 6")

    st.subheader("⭐ Rating")
    st.write("Buruk ≤ 4.0 | Baik ≥ 5.0")

# =====================================================
# FUZZIFIKASI
# =====================================================
elif page == "🧠 Fuzzifikasi":

    st.title("🧠 Proses Fuzzifikasi")

    st.dataframe(
        hasil_df,
        use_container_width=True,
        hide_index=True
    )

# =====================================================
# QUERY TAHANI
# =====================================================
elif page == "🔍 Query Tahani":

    st.title("🔍 Query Fuzzy Tahani")

    st.info(f"""
    Query yang digunakan:

    - Harga = {harga_query}
    - Kualitas = {kualitas_query}
    - Garansi = {garansi_query}
    - Pelayanan = {pelayanan_query}
    - Pengiriman = {pengiriman_query}
    - Rating = {rating_query}
    """)

    st.subheader("Hasil Query")

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=False
    )

# =====================================================
# RANKING
# =====================================================
elif page == "🏆 Ranking":

    st.title("🏆 Ranking Vendor Laptop")

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=False
    )

    best = ranking.iloc[0]

    st.success(f"""
    Vendor terbaik adalah {best['Vendor']}

    Dengan Fire Strength = {best['Fire Strength']}
    """)

# =====================================================
# VISUALISASI
# =====================================================
elif page == "📊 Visualisasi":

    st.title("📊 Visualisasi Fuzzy Tahani")

    top5 = ranking.head(5)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        top5["Vendor"],
        top5["Fire Strength"]
    )

    ax.set_title(
        "Grafik Ranking Vendor Laptop"
    )

    ax.set_xlabel("Vendor")
    ax.set_ylabel("Fire Strength")

    plt.xticks(rotation=90)

    st.pyplot(fig)

    st.subheader("Grafik Membership Function Harga")

    x = np.linspace(5, 15, 100)

    murah = [harga_murah(i) for i in x]
    sedang = [harga_sedang(i) for i in x]
    mahal = [harga_mahal(i) for i in x]

    fig2, ax2 = plt.subplots(figsize=(10,5))

    ax2.plot(x, murah, label="Murah")
    ax2.plot(x, sedang, label="Sedang")
    ax2.plot(x, mahal, label="Mahal")

    ax2.set_title("Membership Function Harga")
    ax2.legend()

    st.pyplot(fig2)
