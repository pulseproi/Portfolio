import streamlit as st

st.set_page_config(page_title="About - Rena Valenzuela", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
* { font-family: 'DM Sans', sans-serif; }
.section-label { font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase; color: #c8f06e; }
h2 { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; letter-spacing: -1px; }
.about-text { color: #888780; line-height: 1.9; font-size: 0.95rem; }
.about-text strong { color: #f0ede6; font-weight: 500; }
.stat-box {
    background: #18181b; border: 1px solid rgba(255,255,255,0.07);
    padding: 1.5rem; text-align: center; border-radius: 4px;
}
.stat-num { font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 900; color: #c8f06e; display: block; }
.stat-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: #888780; }
.footer { color: #888780; font-size: 0.8rem; text-align: center; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">⸻ About Me</p>', unsafe_allow_html=True)
st.markdown('<h2>Who I Am</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-text">
        <p>I'm <strong>Rena Valenzuela</strong>, a 3rd-year Computer Science student at Bicol University
        with a love for building things that live on the internet and in the real world.</p><br>
        <p>I enjoy both <strong>front-end and back-end development</strong>, and I believe the best
        digital products are built where thoughtful engineering meets great design.</p><br>
        <p>When I'm not coding, I'm studying algorithms, contributing to open-source,
        or exploring somewhere in Masbate.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        st.markdown('<div class="stat-box"><span class="stat-num">3rd</span><span class="stat-label">Year Level</span></div>', unsafe_allow_html=True)
    with r1c2:
        st.markdown('<div class="stat-box"><span class="stat-num">12+</span><span class="stat-label">Projects Done</span></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    r2c1, r2c2 = st.columns(2)
    with r2c1:
        st.markdown('<div class="stat-box"><span class="stat-num">4</span><span class="stat-label">Certifications</span></div>', unsafe_allow_html=True)
    with r2c2:
        st.markdown('<div class="stat-box"><span class="stat-num">2</span><span class="stat-label">Hackathons</span></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Rena Valenzuela &copy; 2025 &nbsp;·&nbsp; CS Student · Masbate, PH</div>', unsafe_allow_html=True)