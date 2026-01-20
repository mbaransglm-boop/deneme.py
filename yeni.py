import streamlit as st

# Sayfa Ayarları - Sekme başlığını Instagram gibi yapalım
st.set_page_config(page_title="Instagram • Giriş Yap", page_icon="📸")

# Instagram Tasarımı İçin CSS
st.markdown("""
    <style>
    /* Arka planı beyaz yap */
    .main { background-color: white; }
    
    /* Giriş kutusunu ortala ve çerçeve ekle */
    .stTextInput>div>div>input {
        background-color: #fafafa;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
    }
    
    /* Giriş Butonu Stili */
    .stButton>button {
        width: 100%;
        background-color: #0095f6;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        height: 35px;
    }
    
    .stButton>button:hover {
        background-color: #1877f2;
        color: white;
    }

    /* Instagram Logosu Yazı Tipi Simülasyonu */
    .insta-logo {
        font-family: 'Cookie', cursive;
        font-size: 50px;
        text-align: center;
        margin-bottom: 20px;
        color: #262626;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Cookie&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# Orta Panel
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="insta-logo">Instagram</div>', unsafe_allow_html=True)
    
    # Kullanıcı Giriş Alanları
    username = st.text_input("", placeholder="Telefon numarası, kullanıcı adı veya e-posta")
    password = st.text_input("", placeholder="Şifre", type="password")
    
    if st.button("Giriş Yap"):
        if username and password:
            # ŞAKA KISMI: Buraya bir hata veya şaka mesajı ekliyoruz
            st.error("Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et.")
            st.toast("Mahvedeb47 tarafından hacklendiniz! 😉")
        else:
            st.warning("Lütfen tüm alanları doldur.")

    st.markdown("<p style='text-align: center; color: #8e8e8e; font-size: 14px;'>veya</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #385185; font-weight: bold; font-size: 14px;'>Facebook ile Giriş Yap</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00376b; font-size: 12px; margin-top: 20px;'>Şifreni mi unuttun?</p>", unsafe_allow_html=True)

# Alt Kısım
st.divider()
st.markdown("<p style='text-align: center; color: #8e8e8e;'>Hesabın yok mu? <span style='color: #0095f6; font-weight: bold;'>Kaydol</span></p>", unsafe_allow_html=True)
