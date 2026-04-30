import streamlit as st

st.set_page_config(page_title="Skills - Rena Valenzuela", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
* { font-family: 'DM Sans', sans-serif; }
.section-label { font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase; color: #c8f06e; }
h2 { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; letter-spacing: -1px; }
.skill-cat-title { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: #8fd4a8; font-weight: 500; margin-bottom: 0.5rem; }
.footer { color: #888780; font-size: 0.8rem; text-align: center; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">⸻ What I Know</p>', unsafe_allow_html=True)
st.markdown('<h2>My Skills</h2>', unsafe_allow_html=True)

skills = {
    "Frontend": [
        ("HTML & CSS", 90),
        ("JavaScript", 80),
        ("React", 70),
    ],
    "Backend": [
        ("Python", 85),
        ("Node.js", 65),
        ("MySQL", 75),
    ],
    "Tools": [
        ("Git & GitHub", 80),
        ("Figma", 60),
        ("Linux / CLI", 70),
    ],
}

cols = st.columns(3)

for col, (category, items) in zip(cols, skills.items()):
    with col:
        st.markdown(f'<p class="skill-cat-title">{category}</p>', unsafe_allow_html=True)
        for skill, pct in items:
            st.markdown(f"**{skill}** — {pct}%")
            st.progress(pct / 100)
            st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="footer">Rena Valenzuela &copy; 2026 &nbsp;·&nbsp; CS Student · Masbate, PH</div>', unsafe_allow_html=True)