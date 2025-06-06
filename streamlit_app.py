import streamlit as st

st.set_page_config(
    page_title="GraphoStat",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
# 🧠 GraphoStat

#### Statistical Profiles of Greek Texts — From Scripture to Classical Thought

Welcome to **GraphoStat**, a platform for analyzing Greek texts using standardized grammatical metrics. Whether you're exploring Paul's letters or the writings of Plutarch, GraphoStat helps you extract meaningful patterns from parsing codes — all without needing programming skills.

---
""")

st.success("📈 Explore standard metrics like mean, frequency, PCA, and more.")

if st.button("Start Analysis"):
    st.switch_page("pages/1_📁_Analyze.py")  # Streamlit multipage switch
