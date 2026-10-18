import streamlit as st

st.set_page_config(page_title="CyberSafe Nigeria", page_icon="🛡️", layout="centered")
st.title("🛡️ CyberSafe Nigeria Assistant")
st.subheader("Stay Safe Online — Kare Kanka a Intanet")
st.write("Welcome! Barka da zuwa!")

language = st.selectbox("Choose language / Zaɓi harshe", ["English", "Hausa"])
topic = st.selectbox("Topic", ["Phishing", "Passwords", "2FA", "Malware", "Personal Info"])

tips = {"Phishing": "Don't click unknown links. Kada ka danna link.", "Passwords": "Use strong passwords. Yi kalmar sirri mai karfi.", "2FA": "Enable 2FA. Never share OTP.", "Malware": "Download only from trusted sources.", "Personal Info": "Don't share PIN online."}

if st.button("Show Tips"):
    st.info(tips[topic])

q = st.radio("Someone asks for your OTP?", ["Send it", "Never share it"])
if st.button("Check Answer"):
    if q == "Never share it":
        st.success("Correct! Daidai ne!")
    else:
        st.error("Wrong! Kada ka bayar da OTP!")

st.caption("CyberSafe Nigeria - Educational Project")
