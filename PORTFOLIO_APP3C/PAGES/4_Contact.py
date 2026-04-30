import streamlit as st

st.set_page_config(page_title="Contact - Rena Valenzuela", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
* { font-family: 'DM Sans', sans-serif; }
.section-label { font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase; color: #c8f06e; }
h2 { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; letter-spacing: -1px; }
.contact-info p { color: #888780; line-height: 1.8; font-size: 0.95rem; }
.contact-detail { display: flex; align-items: center; gap: 0.8rem; color: #888780; font-size: 0.9rem; margin-bottom: 0.8rem; }
.stTextInput > div > input, .stTextArea > div > textarea {
    background: #18181b !important; border: 1px solid rgba(255,255,255,0.07) !important;
    color: #f0ede6 !important; border-radius: 2px !important;
}
.stButton > button {
    background-color: #c8f06e; color: #0d0d0f;
    border: none; padding: 0.75rem 1.8rem;
    font-weight: 600; border-radius: 2px; font-size: 0.9rem;
}
.footer { color: #888780; font-size: 0.8rem; text-align: center; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">⸻ Say Hello</p>', unsafe_allow_html=True)
st.markdown('<h2>Contact Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("""
    <div class="contact-info">
        <p>I'm open to internships, freelance projects, or just a good conversation about tech. Drop me a message!</p>
        <br>
        <div class="contact-detail">📧 &nbsp; rena.valenzuela@email.com</div>
        <div class="contact-detail">💼 &nbsp; linkedin.com/in/renavalenzuela</div>
        <div class="contact-detail">🐙 &nbsp; github.com/renavalenzuela</div>
        <div class="contact-detail">📍 &nbsp; Masbate, Philippines</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    name = st.text_input("Name", placeholder="Your name")
    email = st.text_input("Email", placeholder="your@email.com")
    message = st.text_area("Message", placeholder="What's on your mind?", height=130)

    if st.button("Send Message"):
        if name and email and message:
            st.success(f"Message sent! Thanks, {name}. I'll get back to you soon.")
        else:
            st.warning("Please fill in all fields before sending.")

st.markdown('<div class="footer">Rena Valenzuela &copy; 2025 &nbsp;·&nbsp; CS Student · Masbate, PH</div>', unsafe_allow_html=True)