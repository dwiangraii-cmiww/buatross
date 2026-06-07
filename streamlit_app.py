import streamlit as st
import pandas as pd

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="Kalkulator Kimia Digital",
    page_icon="🧪",
    layout="wide"
)

# ============================================
# DATABASE KIMIA LENGKAP
# ============================================
@st.cache_data
def get_chemicals_db():
    return {
        # Garam & Senyawa Ionik
        "NaCl - Natrium Klorida": 58.44,
        "KCl - Kalium Klorida": 74.55,
        "CaCl2 - Kalsium Klorida": 110.98,
        "MgCl2 - Magnesium Klorida": 95.21,
        "NH4Cl - Amonium Klorida": 53.49,
        "Na2SO4 - Natrium Sulfat": 142.04,
        "K2SO4 - Kalium Sulfat": 174.26,
        "MgSO4 - Magnesium Sulfat": 120.37,
        "CuSO4 - Tembaga Sulfat": 159.61,
        
        # Senyawa Natrium
        "NaOH - Natrium Hidroksida": 40.00,
        "Na2CO3 - Natrium Karbonat": 105.99,
        "NaHCO3 - Natrium Bikarbonat": 84.01,
        "NaNO3 - Natrium Nitrat": 85.00,
        
        # Senyawa Kalium
        "KOH - Kalium Hidroksida": 56.11,
        "KNO3 - Kalium Nitrat": 101.10,
        "KMnO4 - Kalium Permanganat": 158.03,
        
        # Asam
        "HCl - Asam Klorida": 36.46,
        "H2SO4 - Asam Sulfat": 98.08,
        "HNO3 - Asam Nitrat": 63.01,
        "H3PO4 - Asam Fosfat": 97.99,
        "CH3COOH - Asam Asetat": 60.05,
        
        # Basa
        "NH4OH - Amonium Hidroksida": 35.05,
        "Ca(OH)2 - Kalsium Hidroksida": 74.09,
        
        # Senyawa Organik
        "C6H12O6 - Glukosa": 180.16,
        "C12H22O11 - Sukrosa": 342.30,
        "C2H5OH - Etanol": 46.07,
        "CH3OH - Metanol": 32.04,
        "CO(NH2)2 - Urea": 60.06,
        
        # Logam
        "FeSO4 - Besi(II) Sulfat": 151.91,
        "AgNO3 - Perak Nitrat": 169.87,
        "ZnO - Seng Oksida": 81.38,
        "MgO - Magnesium Oksida": 40.30,
        "CaO - Kalsium Oksida": 56.08,
    }

@st.cache_data
def get_periodic_table():
    return pd.DataFrame([
        {"No": 1, "S": "H", "Nama": "Hidrogen", "M": 1.008, "K": "Non-logam"},
        {"No": 2, "S": "He", "Nama": "Helium", "M": 4.003, "K": "Gas Mulia"},
        {"No": 3, "S": "Li", "Nama": "Litium", "M": 6.941, "K": "Logam Alkali"},
        {"No": 4, "S": "Be", "Nama": "Berilium", "M": 9.012, "K": "Logam Alkali Tanah"},
        {"No": 5, "S": "B", "Nama": "Boron", "M": 10.81, "K": "Metalloid"},
        {"No": 6, "S": "C", "Nama": "Karbon", "M": 12.011, "K": "Non-logam"},
        {"No": 7, "S": "N", "Nama": "Nitrogen", "M": 14.007, "K": "Non-logam"},
        {"No": 8, "S": "O", "Nama": "Oksigen", "M": 15.999, "K": "Non-logam"},
        {"No": 9, "S": "F", "Nama": "Fluor", "M": 18.998, "K": "Halogen"},
        {"No": 10, "S": "Ne", "Nama": "Neon", "M": 20.180, "K": "Gas Mulia"},
        {"No": 11, "S": "Na", "Nama": "Natrium", "M": 22.990, "K": "Logam Alkali"},
        {"No": 12, "S": "Mg", "Nama": "Magnesium", "M": 24.305, "K": "Logam Alkali Tanah"},
        {"No": 13, "S": "Al", "Nama": "Aluminium", "M": 26.982, "K": "Logam Post-Transisi"},
        {"No": 14, "S": "Si", "Nama": "Silikon", "M": 28.086, "K": "Metalloid"},
        {"No": 15, "S": "P", "Nama": "Fosfor", "M": 30.974, "K": "Non-logam"},
        {"No": 16, "S": "S", "Nama": "Belerang", "M": 32.065, "K": "Non-logam"},
        {"No": 17, "S": "Cl", "Nama": "Klorin", "M": 35.453, "K": "Halogen"},
        {"No": 18, "S": "Ar", "Nama": "Argon", "M": 39.948, "K": "Gas Mulia"},
        {"No": 19, "S": "K", "Nama": "Kalium", "M": 39.098, "K": "Logam Alkali"},
        {"No": 20, "S": "Ca", "Nama": "Kalsium", "M": 40.078, "K": "Logam Alkali Tanah"},
        {"No": 26, "S": "Fe", "Nama": "Besi", "M": 55.845, "K": "Logam Transisi"},
        {"No": 29, "S": "Cu", "Nama": "Tembaga", "M": 63.546, "K": "Logam Transisi"},
        {"No": 30, "S": "Zn", "Nama": "Seng", "M": 65.38, "K": "Logam Transisi"},
        {"No": 47, "S": "Ag", "Nama": "Perak", "M": 107.868, "K": "Logam Transisi"},
        {"No": 79, "S": "Au", "Nama": "Emas", "M": 196.967, "K": "Logam Transisi"},
    ])

# ============================================
# LOAD DATA
# ============================================
chemicals = get_chemicals_db()
df_periodik = get_periodic_table()

# Session State
if 'result_prep' not in st.session_state:
    st.session_state.result_prep = None
if 'result_dil' not in st.session_state:
    st.session_state.result_dil = None
if 'result_dil_air' not in st.session_state:
    st.session_state.result_dil_air = None
if 'nama_zat_fix' not in st.session_state:
    st.session_state.nama_zat_fix = None

# ============================================
# TAMPILAN UTAMA
# ============================================
st.title("Kalkulator Kimia Digital")
st.markdown("---")

# PILIH TAB
tab1, tab2, tab3 = st.tabs(["Pembuatan Larutan", "Pengenceran", "Tabel Periodik"])

# ==================== TAB 1: PEMBUATAN LARUTAN ====================
with tab1:
    st.header("Pembuatan Larutan")
    st.info("Rumus: m = M x V x Mr")
    
    # Referensi
    with st.expander("Referensi Rumus"):
        st.markdown("""
        **Rumus:** m = M x V x Mr
        
        - m = massa (gram)
        - M = molaritas (mol/L)
        - V = volume (L)
        - Mr = massa molar (g/mol)
        
        **Sumber:**
        - Petrucci, et al. (2017). General Chemistry. Pearson.
        - Hill, et al. (2012). Chemistry: The Central Science. Prentice Hall.
        """)
    
    # Mode pilihan
    mode = st.radio("Pilih Mode:", ["Pilih dari Database", "Input Manual"], horizontal=True)
    
    col1, col2 = st.columns(2)
    
    if mode == "Pilih dari Database":
        with col1:
            selected_chem = st.selectbox("Pilih Zat:", list(chemicals.keys()))
            mr_val = chemicals[selected_chem]
        with col2:
            st.write("**Mr:**", mr_val, "g/mol")
            st.session_state.nama_zat_fix = selected_chem.split(" - ")[0]
    else:
        with col1:
            nama_zat = st.text_input("Nama Zat:", placeholder="Contoh: Garam")
            mr_val = st.number_input("Mr (g/mol):", min_value=0.01, value=58.44, step=0.01)
        with col2:
            st.session_state.nama_zat_fix = nama_zat if nama_zat else "Zat"
    
    # Input Volume & Konsentrasi
    col_v, col_c = st.columns(2)
    with col_v:
        vol_ml = st.number_input("Volume (mL):", min_value=1.0, value=100.0)
    with col_c:
        conc_m = st.number_input("Konsentrasi (M):", min_value=0.0001, value=0.1, format="%.4f")
    
    # Hitung
    if st.button("Hitung Massa", type="primary", use_container_width=True):
        vol_l = vol_ml / 1000
        massa = conc_m * vol_l * mr_val
        st.session_state.result_prep = massa
    
    # Hasil
    if st.session_state.result_prep:
        st.success(f"**Massa yang ditimbang: {st.session_state.result_prep:.4f} gram**")
        st.caption(f"Untuk membuat larutan {st.session_state.nama_zat_fix}")

# ==================== TAB 2: PENGENCERAN ====================
with tab2:
    st.header("Pengenceran Larutan (C1 x V1 = C2 x V2)")
    st.info("Rumus pengenceran")
    
    with st.expander("Referensi Rumus"):
        st.markdown("""
        **Rumus:** C1 x V1 = C2 x V2
        
        - C1 = Konsentrasi stok (M)
        - V1 = Volume stok yang diambil (mL)
        - C2 = Konsentrasi target (M)
        - V2 = Volume target (mL)
        
        **Sumber:**
        - Petrucci, et al. (2017). General Chemistry. Pearson.
        - Hill, et al. (2012). Chemistry: The Central Science. Prentice Hall.
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        c1 = st.number_input("Konsentrasi Stok (M):", min_value=0.01, value=1.0, format="%.2f")
    with col2:
        c2 = st.number_input("Konsentrasi Target (M):", min_value=0.0001, value=0.1, format="%.4f")
    
    v2 = st.number_input("Volume Target (mL):", min_value=1.0, value=100.0, step=10.0)
    
    if st.button("Hitung Volume", type="primary", use_container_width=True):
        if c1 <= c2:
            st.error("Konsentrasi stok harus lebih besar dari target!")
        else:
            v1 = (c2 * v2) / c1
            air_tambah = v2 - v1
            st.session_state.result_dil = v1
            st.session_state.result_dil_air = air_tambah
    
    if st.session_state.result_dil:
        st.success(f"Ambil Volume Stok (V1): {st.session_state.result_dil:.2f} mL")
        st.info(f"Tambahkan air: {st.session_state.result_dil_air:.2f} mL")

# ==================== TAB 3: TABEL PERIODIK ====================
with tab3:
    st.header("Tabel Periodik Unsur")
    
    # Legend
    st.markdown("""
    **Legenda Warna:**
    - Merah: Logam Alkali
    - Kuning: Logam Alkali Tanah
    - Hijau: Non-logam
    - Biru: Logam Transisi
    - Ungu: Gas Mulia
    - Orange: Halogen
    - Abu-abu: Metalloid
    """)
    
    # Pencarian
    search = st.text_input("Cari Unsur:", placeholder="Contoh: Besi, Fe, atau 26")
    
    if search:
        filtered = df_periodik[
            df_periodik['Nama'].str.contains(search, case=False) | 
            df_periodik['S'].str.contains(search, case=False) |
            df_periodik['No'].astype(str).str.contains(search)
        ]
    else:
        filtered = df_periodik
    
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.caption(f"Menampilkan {len(filtered)} unsur dari {len(df_periodik)} total")

# Footer
st.markdown("---")
st.caption("Kalkulator Kimia Digital v1.0 | Referensi: Petrucci & Hill")
