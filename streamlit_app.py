import streamlit as st
st.set_page_config(page_title="CyberSafe Nigeria", page_icon="🛡️", layout="centered")
st.title("🛡️ CyberSafe Nigeria Assistant")
st.subheader("Stay Safe Online — Kare Kanka a Intanet")
st.write("Welcome! Barka da zuwa!")
language = st.selectbox("Choose language", ["English", "Hausa"])
topic = st.selectbox("Topic", ["Phishing", "Passwords", "2FA", "Malware", "Personal Info"])
tips = {"Phishing": "Don't click unknown links.", "Passwords": "Use strong passwords.", "2FA": "Enable 2FA. Never share OTP.", "Malware": "Only trusted sources.", "Personal Info": "Don't share PIN."}
if st.button("Show Tips"):
    st.info(tips[topic])
q = st.radio("OTP?", ["Send it", "Never share it"])
if st.button("Check Answer"):
    if q == "Never share it":
        st.success("Correct!")
    else:
        st.error("Wrong!")
st.caption("CyberSafe Nigeria")
