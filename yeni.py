import streamlit as st
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Mahvedeb47 Foto Galeri", layout="wide")

st.title("📸 Mahvedeb47 Dijital Duvarı")
st.write("Galerinden bir fotoğraf seç ve 8 kareden birine yerleştir!")

# 8 Kare için hafıza oluşturma (Session State)
if 'resimler' not in st.session_state:
    st.session_state.resimler = [None] * 8

# Görsel Izgara (Grid) Düzeni: 4 sütun, 2 satır
col_set1 = st.columns(4)
col_set2 = st.columns(4)
tum_sutunlar = col_set1 + col_set2

# 8 Kareyi ve Yükleme Butonlarını Döngüyle Oluşturma
for i in range(8):
    with tum_sutunlar[i]:
        st.markdown(f"### Bölme {i+1}")
        
        # Dosya Yükleyici (Galeriden seçmek için)
        uploaded_file = st.file_uploader(f"Foto Seç {i+1}", type=['png', 'jpg', 'jpeg'], key=f"uploader_{i}")
        
        if uploaded_file is not None:
            # Fotoğrafı belleğe al
            image = Image.open(uploaded_file)
            st.session_state.resimler[i] = image
        
        # Eğer o bölmede resim varsa göster, yoksa boş kare göster
        if st.session_state.resimler[i] is not None:
            st.image(st.session_state.resimler[i], use_container_width=True)
        else:
            st.info("Henüz foto yok")

st.divider()
st.caption("Not: Ücretsiz sürümde sayfa yenilenirse fotoğraflar sıfırlanabilir.")
