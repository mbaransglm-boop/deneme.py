import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(page_title="Instagram • Giriş Yap", page_icon="📸", layout="centered")

# Instagram Arayüzü ve Jumpscare Mekanizması (HTML/JS/CSS)
# Not: Görsel olarak senin istediğin o korkunç yüzü ve yüksek sesli çığlığı entegre ettim.
jumpscare_html = """
<style>
    body { 
        background-color: #ffffff; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }
    .login-container {
        width: 350px;
        padding: 40px;
        border: 1px solid #dbdbdb;
        text-align: center;
        background: white;
    }
    .logo {
        font-family: 'Cookie', cursive;
        font-size: 55px;
        margin-bottom: 30px;
        color: #262626;
    }
    input {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #dbdbdb;
        background: #fafafa;
        border-radius: 3px;
        box-sizing: border-box;
        font-size: 12px;
    }
    #login-btn {
        width: 100%;
        padding: 10px;
        background-color: #0095f6;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        font-size: 14px;
        margin-top: 10px;
    }
    #login-btn:active {
        background-color: #1877f2;
    }
    .divider {
        margin: 20px 0;
        color: #8e8e8e;
        font-size: 13px;
        display: flex;
        align-items: center;
    }
    .divider::before, .divider::after {
        content: "";
        flex: 1;
        border-bottom: 1px solid #dbdbdb;
        margin: 0 10px;
    }
    .fb-login {
        color: #385185;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        margin-top: 15px;
        display: block;
        text-decoration: none;
    }
    .forgot {
        color: #00376b;
        font-size: 12px;
        margin-top: 20px;
        display: block;
        text-decoration: none;
    }

    /* JUMPSCARE OVERLAY */
    #scare-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: black;
        z-index: 99999;
        justify-content: center;
        align-items: center;
    }
    #scare-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
</style>

<!-- Font for Instagram Logo -->
<link href="https://fonts.googleapis.com/css2?family=Cookie&display=swap" rel="stylesheet">

<div class="login-container" id="main-box">
    <div class="logo">Instagram</div>
    <form onsubmit="return false;">
        <input type="text" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
        <input type="password" placeholder="Şifre" required>
        <button id="login-btn">Giriş Yap</button>
    </form>
    <div class="divider">VEYA</div>
    <a class="fb-login">Facebook ile Giriş Yap</a>
    <a class="forgot">Şifreni mi unuttun?</a>
</div>

<div id="scare-overlay">
    <!-- Buradaki URL senin istediğin o korkunç görselin linkidir -->
    <img id="scare-img" src="https://files.catbox.moe/p7uof4.jpg">
</div>

<audio id="scream-sound">
    <source src="https://www.soundboard.com/handler/DownLoadTrack.ashx?cliptitle=Scream&filename=22/227575-f71694f4-5f4b-4433-8b7c-3f5f3e7e8b8a.mp3" type="audio/mp3">
</audio>

<script>
    const loginBtn = document.getElementById('login-btn');
    const overlay = document.getElementById('scare-overlay');
    const scream = document.getElementById('scream-sound');

    loginBtn.addEventListener('click', function() {
        // Sesi en sona çek ve çal
        scream.volume = 1.0;
        scream.play().catch(e => console.log("Ses engellendi, etkileşim gerekiyor."));

        // Görseli göster
        overlay.style.display = 'flex';

        // Tam ekran yap (Fullscreen API)
        const elem = document.documentElement;
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen();
        }

        // Cihazı titret (Sadece mobil cihazlarda çalışır)
        if (navigator.vibrate) {
            navigator.vibrate([500, 100, 500, 100, 500]);
        }
    });
</script>
"""

# HTML bileşenini geniş ekrana bas
components.html(jumpscare_html, height=700)

st.markdown("<div style='text-align:center; margin-top:20px; color:#8e8e8e;'>Meta'dan Instagram</div>", unsafe_allow_html=True)

