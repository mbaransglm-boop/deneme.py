import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(page_title="Instagram • Giriş Yap", page_icon="📸", layout="centered")

# Instagram Arayüzü ve Jumpscare (Gelişmiş ve Kesin Çalışan Sürüm)
jumpscare_html = """
<style>
    body { 
        background-color: #ffffff; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden;
    }
    .login-container { width: 350px; padding: 40px; border: 1px solid #dbdbdb; text-align: center; background: white; }
    .logo { font-family: 'Cookie', cursive; font-size: 55px; margin-bottom: 30px; color: #262626; }
    input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #dbdbdb; background: #fafafa; border-radius: 3px; box-sizing: border-box; font-size: 12px; }
    #login-btn { width: 100%; padding: 10px; background-color: #0095f6; color: white; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; font-size: 14px; margin-top: 10px; }
    
    /* JUMPSCARE OVERLAY */
    #scare-overlay {
        display: none; position: fixed; top: 0; left: 0; 
        width: 100vw; height: 100vh; background: black; z-index: 99999;
        justify-content: center; align-items: center;
    }
    #scare-img { width: 100%; height: 100%; object-fit: cover; }
</style>

<link href="https://fonts.googleapis.com/css2?family=Cookie&display=swap" rel="stylesheet">

<div class="login-container">
    <div class="logo">Instagram</div>
    <input type="text" placeholder="Kullanıcı adı" id="u">
    <input type="password" placeholder="Şifre" id="p">
    <button id="login-btn">Giriş Yap</button>
</div>

<div id="scare-overlay">
    <!-- Daha güvenilir bir jumpscare görseli -->
    <img id="scare-img" src="https://images.squarespace-cdn.com/content/v1/51b3dc8ee4b051b96ceb10de/1383238618776-8096ID17O5V4P0P2K8X1/scary+face.jpg" onerror="this.src='https://media.giphy.com/media/3o7TKsWpY8j8oYpTJC/giphy.gif'">
</div>

<audio id="scream-sound">
    <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
</audio>

<script>
    const btn = document.getElementById('login-btn');
    const overlay = document.getElementById('scare-overlay');
    const audio = document.getElementById('scream-sound');

    btn.addEventListener('click', function() {
        audio.volume = 1.0;
        audio.play().catch(e => console.log("Ses etkileşim bekliyor"));
        
        overlay.style.display = 'flex';
        
        // Tam ekran tetikleme
        const doc = document.documentElement;
        if (doc.requestFullscreen) doc.requestFullscreen();
        else if (doc.webkitRequestFullscreen) doc.webkitRequestFullscreen();

        // Titreşim
        if (navigator.vibrate) navigator.vibrate([500, 200, 500]);
    });
</script>
"""

components.html(jumpscare_html, height=700)

