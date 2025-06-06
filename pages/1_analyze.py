import streamlit as st
import os
from pathlib import Path

# --- Page config ---
st.set_page_config(page_title="Analyze | GraphoStat", layout="wide")

st.title("📁 Analyze a Greek Text")

# --- Source selection ---
source_options = ["New Testament", "Church Fathers", "Outside NT"]
selected_source = st.radio("Choose source corpus:", source_options, horizontal=True)

# --- Map source to subdirectory ---
source_dir_map = {
    "New Testament": "data/NT",
    "Church Fathers": "data/ChurchFathers",
    "Outside NT": "data/OutsideNT"
}

source_path = Path(source_dir_map[selected_source])

# --- Load available documents from the selected source ---
csv_files = sorted([f for f in source_path.glob("*.csv")])

if not csv_files:
    st.warning(f"No documents found in `{source_path}`.")
else:
    doc_display_names = [f.stem.replace("_", " ") for f in csv_files]
    selected_file = st.selectbox(f"Select a document from {selected_source}:", doc_display_names)
    
    # Store path for future use
    selected_file_path = source_path / csv_files[doc_display_names.index(selected_file)].name
    st.success(f"Selected file: `{selected_file_path.name}`")

    # Placeholder: Display head of file
    if st.checkbox("📄 Preview file contents"):
        import pandas as pd
        df = pd.read_csv(selected_file_path)
        st.dataframe(df.head(10))
