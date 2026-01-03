
# Watchlist.py
import streamlit as st
import re
from pathlib import Path

# st.set_page_config(page_title="Home", layout="wide")

st.markdown("""
    <style>
    /* Apply font to all elements within the main content */
    * {
        font-family: 'Noto Serif', serif !important;
    }

    /* Set background color for the entire app */
    .stApp {
        background-color: #FFFCF5;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="Watchlist", page_icon="🎬")
st.title("Home Page")
