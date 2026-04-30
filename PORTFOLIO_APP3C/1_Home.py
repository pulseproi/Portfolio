import streamlit as st

st.set_page_config(page_title="Home - Rena Valenzuela", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

* { font-family: 'DM Sans', sans-serif; }

.logo { font-family: 'Playfair Display', serif; color: #c8f06e; font-size: 1.5rem; font-weight: 700; }

.home-label {
    font-size: 0.8rem; letter-spacing: 0.15em;
    text-transform: uppercase; color: #c8f06e; margin-bottom: 1rem;
}
h1 {
    font-family: 'Playfair Display', serif;
    font-size: 4rem; font-weight: 900;
    line-height: 1.0; letter-spacing: -1.5px;
}
h1 span { color: #c8f06e; display: block; }
.home-desc { color: #888780; font-size: 1rem; line-height: 1.8; max-width: 480px; }
.stButton > button {
    background-color: #c8f06e; color: #0d0d0f;
    border: none; padding: 0.75rem 1.8rem;
    font-weight: 600; border-radius: 2px;
    font-size: 0.9rem; cursor: pointer;
}
.footer { color: #888780; font-size: 0.8rem; text-align: center; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="home-label">⸻ Computer Science Student</p>', unsafe_allow_html=True)
st.markdown("""
<h1>Hello, I'm<span>Rena Valenzuela.</span></h1>
""", unsafe_allow_html=True)
st.markdown('<p class="home-desc">A passionate 3rd-year CS student building projects at the intersection of design and technology. I turn ideas into real, working things.</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 5])
with col1:
    if st.button("View My Work"):
        st.switch("projects.py")
with col2:
    if st.button("Get in Touch"):
        st.switch("contact.py")

st.markdown('<div class="footer">Rena Valenzuela &copy; 2025 &nbsp;·&nbsp; CS Student · Masbate, PH</div>', unsafe_allow_html=True)