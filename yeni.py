import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(page_title="Instagram", page_icon="📸", layout="centered")

# Instagram Gerçekçi Tasarım (CSS)
st.markdown("""
    <style>
    /* Arka planı bembeyaz yap */
    .main { background-color: #ffffff !important; }
    
    /* Giriş kutuları tasarımı */
    .stTextInput>div>div>input {
        background-color: #fafafa;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        color: #262626;
        height: 38px;
        font-size: 12px;
    }
    
    /* Mavi Giriş Butonu */
    .stButton>button {
        width: 100%;
        background-color: #0095f6;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        height: 32px;
        margin-top: 10px;
    }
    
    .stButton>button:hover {
        background-color: #1877f2;
        color: white;
    }

    /* Logo fontu */
    @import url('https://fonts.googleapis.com/css2?family=Cookie&display=swap');
    .insta-header {
        font-family: 'Cookie', cursive;
        font-size: 60px;
        text-align: center;
        color: #262626;
        margin-bottom: 30px;
    }
    
    /* Alt kısımdaki gri yazılar */
    .footer-text {
        color: #8e8e8e;
        font-size: 14px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Ekranı ortalamak için boş sütunlar kullanıyoruz
left_co, cent_co, last_co = st.columns([1, 4, 1])

with cent_co:
    # Instagram Logosu
    st.markdown('<div class="insta-header">Instagram</div>', unsafe_allow_html=True)
    
    # Kullanıcı adı ve Şifre alanları
    user_input = st.text_input("", placeholder="Telefon numarası, kullanıcı adı veya e-posta")
    pass_input = st.text_input("", placeholder="Şifre", type="password")
    
    if st.button("Giriş Yap"):
        if user_input and pass_input:
            # Gerçekçi hata mesajı
            st.error("Üzgünüz, şifren yanlıştı. Lütfen şifreni dikkatlice kontrol et.")
            
            # Şaka patlaması: Yazılanları gösteriyoruz
            st.markdown(f"""
            <div style="border:1px dashed red; padding:10px; margin-top:20px; text-align:center;">
                <p style="color:black;"><b>Mahvedeb47 Yakaladı! 😉</b></p>
                <p style="color:blue;">Yazılan Kullanıcı: {user_input}</p>
                <p style="color:blue;">Yazılan Şifre: {pass_input}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Lütfen bilgileri eksiksiz girin.")

    # Diğer elemanlar
    st.markdown("<br><p class='footer-text'>veya</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#385185; font-weight:600; font-size:14px; cursor:pointer;'>Facebook ile Giriş Yap</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00376b; font-size:12px; margin-top:15px;'>Şifreni mi unuttun?</p>", unsafe_allow_html=True)

    # Kaydol kısmı
    st.markdown("<br><div style='border:1px solid #dbdbdb; padding:20px; text-align:center;'>"
                "<span class='footer-text'>Hesabın yok mu? </span>"
                "<span style='color:#0095f6; font-weight:600;'>Kaydol</span>"
                "</div>", unsafe_allow_html=True)
