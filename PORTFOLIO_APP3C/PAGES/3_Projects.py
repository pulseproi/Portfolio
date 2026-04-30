import streamlit as st

st.set_page_config(page_title="Projects - Rena Valenzuela", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');
* { font-family: 'DM Sans', sans-serif; }
.section-label { font-size: 0.75rem; letter-spacing: 0.18em; text-transform: uppercase; color: #c8f06e; }
h2 { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; letter-spacing: -1px; }
.project-card {
    background: #18181b; border: 1px solid rgba(255,255,255,0.07);
    border-radius: 4px; padding: 1.5rem; height: 100%;
}
.project-tag { font-size: 0.65rem; letter-spacing: 0.12em; text-transform: uppercase; color: #c8f06e; background: rgba(200,240,110,0.1); padding: 0.2rem 0.5rem; }
.project-title { font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 700; margin: 0.6rem 0; color: #f0ede6; }
.project-desc { color: #888780; font-size: 0.85rem; line-height: 1.7; margin-bottom: 1rem; }
.tech-pill { display: inline-block; font-size: 0.7rem; padding: 0.2rem 0.5rem; border: 1px solid rgba(255,255,255,0.07); color: #888780; border-radius: 2px; margin: 0.2rem; }
.footer { color: #888780; font-size: 0.8rem; text-align: center; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.07); padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">⸻ What I Built</p>', unsafe_allow_html=True)
st.markdown('<h2>Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "tag": "Web App",
        "title": "Study Buddy",
        "desc": "A collaborative study platform where students can create rooms, share notes, and quiz each other in real time.",
        "stack": ["React", "Node.js", "Socket.io", "MongoDB"],
        "demo": "#",
        "github": "#",
    },
    {
        "tag": "Mobile App",
        "title": "Campus Map",
        "desc": "An interactive campus navigation app for DEBESMSCAT with indoor mapping and event announcements.",
        "stack": ["React Native", "Firebase", "Maps API"],
        "demo": "#",
        "github": "#",
    },
    {
        "tag": "Data Science",
        "title": "Grade Predictor",
        "desc": "A machine learning model that predicts student final grades based on attendance and quiz scores.",
        "stack": ["Python", "scikit-learn", "Pandas"],
        "demo": None,
        "github": "#",
    },
]

cols = st.columns(3)

for col, project in zip(cols, projects):
    with col:
        pills = "".join([f'<span class="tech-pill">{t}</span>' for t in project["stack"]])
        demo_link = f'<a href="{project["demo"]}" style="color:#c8f06e;font-size:0.75rem;text-decoration:none;margin-right:1rem;">Live Demo</a>' if project["demo"] else ""
        github_link = f'<a href="{project["github"]}" style="color:#c8f06e;font-size:0.75rem;text-decoration:none;">GitHub</a>'

        st.markdown(f"""
        <div class="project-card">
            <span class="project-tag">{project["tag"]}</span>
            <div class="project-title">{project["title"]}</div>
            <p class="project-desc">{project["desc"]}</p>
            <div style="margin-bottom:1rem;">{pills}</div>
            {demo_link}{github_link}
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer">Rena Valenzuela &copy; 2025 &nbsp;·&nbsp; CS Student · Masbate, PH</div>', unsafe_allow_html=True)