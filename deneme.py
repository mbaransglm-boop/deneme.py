import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="SİSTEM HATASI", layout="centered")

# Karanlık Tema
st.markdown("<style>.main { background-color: #000000; color: #ff0000; }</style>", unsafe_allow_html=True)

st.title("⚠️ KRİTİK HATA")
st.write("Sistem dosyaları siliniyor... Lütfen bekleyin.")

# 20 Saniyelik Sayaç
bar = st.progress(0)
for i in range(100):
    time.sleep(0.2)
    bar.progress(i + 1)

st.error("DOSYALAR SİLİNDİ! Şaka yaptım, Mahvedeb47 gururla sunar. 😉")
st.balloons()
