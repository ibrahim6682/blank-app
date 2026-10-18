import streamlit as st

st.set_page_config(
    page_title="CyberSafe Nigeria Assistant",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ CyberSafe Nigeria Assistant")
st.subheader("Learn to Stay Safe Online")
st.write(
    "Welcome! This application teaches you how to protect "
    "yourself, your business, and your personal information online."
)

language = st.selectbox(
    "Choose Your Language / Zaɓi Harshe",
    ["English", "Hausa"]
)

if language == "English":
    st.info(
        "Cybersecurity means protecting your devices, accounts, "
        "and personal information from online threats."
    )

    topics = {
        "Phishing Scams": [
            "Be careful with suspicious emails and messages.",
            "Do not click unknown links.",
            "Never share your password or bank OTP.",
            "Verify the sender before responding."
        ],
        "Strong Passwords": [
            "Use a long, unique password for every account.",
            "Avoid your name, birthday, or simple number sequences.",
            "Never share your password with strangers.",
            "Use a password manager if possible."
        ],
        "Two-Factor Authentication": [
            "Enable two-factor authentication (2FA) on important accounts.",
            "It adds another layer of protection.",
            "Never share verification codes with anyone.",
            "Keep your account recovery details safe."
        ],
        "Malware and Unsafe Downloads": [
            "Download applications from trusted sources.",
            "Avoid suspicious attachments.",
            "Keep your phone and applications updated.",
            "Do not install applications you do not trust."
        ],
        "Protecting Personal Information": [
            "Avoid sharing sensitive information publicly.",
            "Check privacy settings on social media.",
            "Use secure connections for sensitive activities.",
            "Be careful about what you share online."
        ]
    }

else:
    st.info(
        "Tsaron yanar gizo yana nufin kare wayarka, "
        "asusunka
