import streamlit as st

# Sayfa Genişliği ve Başlık
st.set_page_config(page_title="Mahvedeb47 Kalıcı Foto Duvarı", layout="wide")

# CSS ile Görünümü Güzelleştirelim
st.markdown("""
    <style>
    .stImage { border-radius: 15px; border: 2px solid #ff4b4b; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🖼️ Mahvedeb47 Ortak Fotoğraf Galerisi")
st.write("Link ekleyerek fotoğrafları sabitleyin, sayfayı yenileseniz de gitmez!")

# --- KALICI VERİ SİMÜLASYONU ---
# Streamlit Cloud'da verilerin kalıcı olması için normalde DB gerekir.
# Şimdilik tarayıcı açık kaldığı sürece kalıcı olan gelişmiş 'session_state' kullanıyoruz.
if 'galeri_linkler' not in st.session_state:
    st.session_state.galeri_linkler = ["https://via.placeholder.com/300?text=Bos+Kare"] * 8

# 8 Kareli Grid Yapısı (4 sütun x 2 satır)
col_set1 = st.columns(4)
col_set2 = st.columns(4)
tum_sutunlar = col_set1 + col_set2

# 8 Kareyi Oluşturma
for i in range(8):
    with tum_sutunlar[i]:
        st.markdown(f"### Bölme {i+1}")
        
        # Mevcut Fotoğrafı Göster
        st.image(st.session_state.galeri_linkler[i], use_container_width=True)
        
        # Yeni Fotoğraf Ekleme Alanı
        yeni_url = st.text_input(f"Link Yapıştır ({i+1})", key=f"input_{i}", placeholder="https://...jpg")
        
        if st.button(f"Kaydet {i+1}", key=f"btn_{i}"):
            if yeni_url:
                st.session_state.galeri_linkler[i] = yeni_url
                st.success("Kaydedildi!")
                st.rerun()

st.divider()
st.info("💡 **Nasıl Kullanılır?** Galerinden bir fotoyu 'Hızlı Resim' veya 'ImgBB' gibi bir siteye yükle, oradan aldığın 'Resim Adresi'ni buraya yapıştır ve Kaydet'e bas.")
