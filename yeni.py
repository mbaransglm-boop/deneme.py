import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarlarını gizle
st.set_page_config(page_title="SİSTEM ONARIM", layout="centered")

# Başlık ve Açıklama
st.markdown("<h1 style='color:red; text-align:center;'>⚠️ DİKKAT: TRİGONOMETRİ-2.EXE ÇALIŞMAYI DURDURDU</h1>", unsafe_allow_html=True)
st.write("Cihazınızın işlemcisi aşırı ısındı. Soğutma işlemini başlatmak için aşağıdaki butona 3 kez hızlıca dokunun.")

# Jumpscare Mekanizması (HTML/JS/CSS Hepsi Bir Arada)
jumpscare_code = """
<div id="wrapper">
    <button id="scare-btn">SİSTEMİ SOĞUT VE ONAR</button>
    <div id="scare-overlay">
        <img id="scare-img" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3N5bm9scXNyeWJ0bmZnbWJueG5ieG5ieG5ieG5ieG5ieG5ieG5ieCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKsWpY8j8oYpTJC/giphy.gif">
    </div>
</div>

<audio id="scream">
    <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
</audio>

<style>
    #scare-btn {
        width: 100%; height: 300px; background-color: #ff0000; 
        color: white; font-size: 35px; font-weight: bold; 
        border: 10px double white; border-radius: 20px; cursor: pointer;
    }
    #scare-overlay {
        display: none; position: fixed; top: 0; left: 0; 
        width: 100%; height: 100%; background: black; z-index: 9999;
    }
    #scare-img { width: 100%; height: 100%; object-fit: cover; }
</style>

<script>
    const btn = document.getElementById('scare-btn');
    const overlay = document.getElementById('scare-overlay');
    const audio = document.getElementById('scream');

    btn.addEventListener('click', function() {
        // Ses çal
        audio.currentTime = 0;
        audio.play().catch(e => console.log("Ses engellendi"));
        
        // Görseli göster
        overlay.style.display = 'block';
        
        // Tam ekran yap (Mümkünse)
        if (overlay.requestFullscreen) { overlay.requestFullscreen(); }
        else if (overlay.webkitRequestFullscreen) { overlay.webkitRequestFullscreen(); }
        
        // Cihazı titret (Eğer telefondaysa)
        if (navigator.vibrate) { navigator.vibrate([500, 200, 500]); }
    });
</script>
"""

# HTML bileşenini sayfaya bas
components.html(jumpscare_code, height=600)

st.warning("Not: Sinyal hatası almamak için cihaz sesini sonuna kadar açın.")
