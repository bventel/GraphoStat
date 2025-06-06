import os
import streamlit as st
from PIL import Image

# --- Page Configuration ---
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

# --- Logo and Title ---
# st.write("Current directory contents:", os.listdir("images"))

logo = Image.open("images/graphostat_logo.png")  # Replace with path to your Psi logo image

col1, col2 = st.columns([1, 6])  # Slightly more space for the logo
with col1:
    st.image("images/graphostat_logo.png", width=150)  # Try 100–150
with col2:
    st.markdown('<div class="title">GraphoStat</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Structured Analysis of Ancient Greek Texts</div>', unsafe_allow_html=True)


# --- Main Description ---
st.markdown("""
<div class="description">
GraphoStat is a platform for structured analysis of ancient Greek texts.  
From grammatical patterns to stylistic profiles, it offers interpretable, reproducible reports across Biblical and classical sources — for scholars, students, pastors, and anyone exploring the Greek language.
</div>
""", unsafe_allow_html=True)

# --- CTA Button ---
st.markdown('<div class="cta">', unsafe_allow_html=True)
if st.button("Start Analysis", use_container_width=True):
    st.switch_page("1_analyze.py")
st.markdown('</div>', unsafe_allow_html=True)
