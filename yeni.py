import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="SİSTEM GÜVENLİK UYARISI", layout="centered")

# CSS ve JavaScript Entegrasyonu (Tam Ekran ve Ani Ses İçin)
st.markdown("""
    <style>
    /* Arka planı siyah ve profesyonel yapalım */
    .main { background-color: #111; color: white; text-align: center; }
    .stButton>button { 
        width: 100%; height: 150px; font-size: 30px; 
        background-color: #d32f2f; color: white; border-radius: 10px;
        font-weight: bold; border: 5px solid white;
    }
    #jumpscare-overlay {
        display: none;
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: black;
        z-index: 9999;
        justify-content: center;
        align-items: center;
    }
    #jumpscare-img { width: 100%; height: 100%; object-fit: cover; }
    </style>

    <div id="jumpscare-overlay">
        <img id="jumpscare-img" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3N5bm9scXNyeWJ0bmZnbWJueG5ieG5ieG5ieG5ieG5ieG5ieG5ieCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKsWpY8j8oYpTJC/giphy.gif">
    </div>

    <audio id="scream-audio" preload="auto">
        <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
    </audio>

    <script>
    function triggerJumpscare() {
        // Ses çal
        var audio = document.getElementById('scream-audio');
        audio.volume = 1.0;
        audio.play();

        // Görseli göster ve tam ekran yap
        var overlay = document.getElementById('jumpscare-overlay');
        overlay.style.display = 'flex';
        
        if (overlay.requestFullscreen) {
            overlay.requestFullscreen();
        } else if (overlay.webkitRequestFullscreen) {
            overlay.webkitRequestFullscreen();
        }
    }
    </script>
    """, unsafe_allow_html=True)

# Kullanıcıyı kandıracak arayüz
st.write("### ⚠️ CİHAZINIZA VİRÜS BULAŞTI!")
st.write("Midyat/Mardin konumundan şüpheli bir IP adresi tüm dosyalarınıza erişiyor.")
st.write("Dosyalarınızın silinmesini engellemek için hemen aşağıdaki butona basın.")

# Streamlit butonu yerine HTML butonu kullanarak JS tetikliyoruz
st.components.v1.html("""
    <button onclick="parent.triggerJumpscare()" style="
        width: 100%; height: 200px; background-color: #ff0000; 
        color: white; font-size: 40px; font-weight: bold; 
        border: none; border-radius: 20px; cursor: pointer;
    ">
        VİRÜSÜ TEMİZLE VE SİSTEMİ KURTAR
    </button>
""", height=250)

st.warning("Not: İşlemin başarılı olması için cihaz sesinin %100 açık olduğundan emin olun.")
