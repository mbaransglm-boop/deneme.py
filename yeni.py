import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="Instagram • Giriş Yap", page_icon="📸", layout="centered")

# Instagram Arayüzü ve Jumpscare JS/CSS
insta_jumpscare_code = """
<style>
    body { background-color: white; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .container { width: 350px; margin: 50px auto; text-align: center; border: 1px solid #dbdbdb; padding: 20px; }
    .logo { font-family: 'Cookie', cursive; font-size: 50px; margin-bottom: 20px; }
    input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; background: #fafafa; border-radius: 3px; box-sizing: border-box; }
    button { width: 100%; padding: 10px; background-color: #0095f6; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
    
    /* Jumpscare Katmanı */
    #scare-overlay {
        display: none; position: fixed; top: 0; left: 0; 
        width: 100vw; height: 100vh; background: black; z-index: 9999;
    }
    #scare-img { width: 100%; height: 100%; object-fit: cover; }
</style>

<link href="https://fonts.googleapis.com/css2?family=Cookie&display=swap" rel="stylesheet">

<div class="container" id="login-box">
    <div class="logo">Instagram</div>
    <input type="text" placeholder="Telefon numarası, kullanıcı adı veya e-posta">
    <input type="password" placeholder="Şifre">
    <button id="login-btn">Giriş Yap</button>
</div>

<div id="scare-overlay">
    <img id="scare-img" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3N5bm9scXNyeWJ0bmZnbWJueG5ieG5ieG5ieG5ieG5ieG5ieG5ieCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKsWpY8j8oYpTJC/giphy.gif">
</div>

<audio id="scream">
    <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
</audio>

<script>
    const btn = document.getElementById('login-btn');
    const overlay = document.getElementById('scare-overlay');
    const audio = document.getElementById('scream');

    btn.addEventListener('click', function() {
        // Ses ve Görüntü Tetikleme
        audio.currentTime = 0;
        audio.play();
        overlay.style.display = 'block';
        
        // Tam ekran yapma denemesi
        if (overlay.requestFullscreen) { overlay.requestFullscreen(); }
        else if (overlay.webkitRequestFullscreen) { overlay.webkitRequestFullscreen(); }
        
        // Telefonu titret
        if (navigator.vibrate) { navigator.vibrate([500, 200, 500]); }
    });
</script>
"""

# HTML Bileşenini bas
components.html(insta_jumpscare_code, height=600)

st.markdown("<p style='text-align:center; color:#8e8e8e;'>© 2026 Instagram from Meta</p>", unsafe_allow_html=True)
