import streamlit as st
import datetime

# Sayfa Ayarları
st.set_page_config(page_title="Mahvedeb47 YKS Takip", layout="wide")

# Başlık
st.title("🚀 Mahvedeb47 YKS Çalışma Paneli")
st.write("Hedefine odaklan, disiplini bırakma!")

# Yan Menü (Sidebar)
st.sidebar.header("Menü")
sayfa = st.sidebar.selectbox("Gitmek istediğin yer:", ["Ana Sayfa", "Ders Notlarım", "Kripto Köşesi"])

# --- ANA SAYFA ---
if sayfa == "Ana Sayfa":
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⏳ Sınava Ne Kadar Kaldı?")
        # YKS Tarihini buraya giriyoruz (Örnek: 20 Haziran 2026)
        yks_tarihi = datetime.date(2026, 6, 20)
        bugun = datetime.date.today()
        kalan = yks_tarihi - bugun
        st.metric(label="Kalan Gün", value=f"{kalan.days} Gün")
        
    with col2:
        st.subheader("📝 Günün Hedefi")
        hedef = st.text_input("Bugün neyi bitireceksin?", "Trigonometri 2. fasikül bitecek.")
        if st.button("Kaydet"):
            st.success("Hedef başarıyla güncellendi!")

# --- DERS NOTLARI ---
elif sayfa == "Ders Notlarım":
    st.subheader("📚 Ders Notları Deposu")
    ders = st.selectbox("Ders Seç:", ["Matematik", "Kimya", "Fizik"])
    
    if ders == "Matematik":
        st.markdown("- **Trigonometri:** Sin(120) = Sin(60) olduğunu unutma!")
        st.markdown("- **Logaritma:** $log(a) - log(b) = log(a/b)$")
    elif ders == "Kimya":
        st.markdown("- **Organik:** Benzen halkası aromatik bir bileşiktir.")
        st.markdown("- **Ketonlar:** İndirgenirse sekonder alkol oluşur.")

# --- KRİPTO KÖŞESİ ---
elif sayfa == "Kripto Köşesi":
    st.subheader("💰 Mola ve Yatırım Takibi")
    st.write("GTX 1650'leri satıp BNB'ye geçme planını unutma!")
    st.info("BNB Airdrop takvimi için Binance Launchpad'i kontrol et.")
