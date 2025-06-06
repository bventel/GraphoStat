import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="GraphoStat",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    .title { 
        font-size: 3rem; 
        font-weight: 700; 
        font-family: Georgia, serif;
        margin-bottom: 0.25rem;
    }
    .tagline {
        font-size: 1.3rem;
        font-style: italic;
        color: #444;
        margin-bottom: 2rem;
    }
    .description {
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 700px;
        margin: auto;
        text-align: justify;
    }
    .cta {
        margin-top: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title + Tagline ---
st.markdown('<div class="title">GraphoStat</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Statistical Profiles of Greek Texts — From Scripture to Classical Thought</div>', unsafe_allow_html=True)

# --- Description Text ---
st.markdown("""
<div class="description">
Welcome to <strong>GraphoStat</strong>, a platform for analyzing Greek texts using standardized grammatical metrics. Whether you're exploring Paul’s letters or the writings of Plutarch, GraphoStat helps you extract meaningful patterns from parsing codes — all without needing programming skills.

Our system offers consistent, reproducible reports based on morphologically tagged Greek texts — including metrics like frequency, mean parsing vectors, PCA embeddings, and syntactic clustering. Built for scholars, theologians, and digital humanists alike.
</div>
""", unsafe_allow_html=True)

# --- CTA Button ---
st.markdown('<div class="cta">', unsafe_allow_html=True)
if st.button("🚀 Start Analysis"):
    st.switch_page("pages/1_📁_Analyze.py")
st.markdown('</div>', unsafe_allow_html=True)
