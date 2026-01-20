import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="DİKKAT: SİSTEM HATASI", layout="centered")

# CSS ile arka planı siyah ve yazıları ürkütücü yapalım
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff0000; }
    .stButton>button { 
        width: 100%; 
        height: 100px; 
        font-size: 25px; 
        background-color: #ff0000; 
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚠️ KRİTİK SİSTEM HATASI")
st.write("Cihazınızda ciddi bir güvenlik açığı tespit edildi. Lütfen aşağıdan onarımı başlatın.")

# Şaka Mekanizması
if st.button("SİSTEMİ ŞİMDİ ONAR (ÖNEMLİ)"):
    # 1. Korkunç Görsel
    # Not: Buraya istediğin korkunç bir görselin direkt linkini koyabilirsin.
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3N5bm9scXNyeWJ0bmZnbWJueG5ieG5ieG5ieG5ieG5ieG5ieG5ieCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKsWpY8j8oYpTJC/giphy.gif", use_container_width=True)
    
    # 2. Ses Efekti (HTML ile otomatik çalma)
    # Sesin çalması için tarayıcının butona basıldığında ses izni vermesini sağlar.
    audio_html = """
        <audio autoplay>
            <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
    
    st.error("GÜVENLİK İHLALİ! MAHVEDEB47 TARAFINDAN HACKLENDİNİZ!")

st.divider()
st.caption("Not: Sesin çıkması için telefonunuzun sesinin açık olduğundan emin olun.")
