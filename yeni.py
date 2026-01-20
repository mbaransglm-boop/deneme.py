import streamlit as st
import time

# Sayfa ayarları - Korkutucu başlık
st.set_page_config(page_title="SİSTEM HATASI - CRITICAL ERROR", layout="centered")

# Karanlık Tema ve Kırmızı Yazılar
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff0000; }
    h1 { color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚠️ DİKKAT: SİSTEME SIZILDI")
st.write("Bilinmeyen bir kaynak Midyat/Mardin üzerinden erişim sağladı.")

# 20 Saniyelik Sayaç
progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    time.sleep(0.2) # Toplam 20 saniye
    progress_bar.progress(i + 1)
    kalan_sn = 20 - int((i * 20) / 100)
    status_text.text(f"Dosyalarınız imha ediliyor... Kalan süre: {kalan_sn} saniye")

# Şaka Finali
st.error("!!! ERİŞİM TAMAMLANDI - TÜM VERİLER SİLİNDİ !!!")
time.sleep(1.5)
st.success("Sakin ol, sadece küçük bir Mahvedeb47 şakası! 😉")
st.balloons()
