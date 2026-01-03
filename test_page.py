# test_page.py
import streamlit as st

st.set_page_config(page_title="Watchlist", page_icon="🎬")
st.title("Movie Watchlist")
movies = ["Inception", "Interstellar", "The Matrix", "Spirited Away"]
for movie in movies:
    watched = st.checkbox(f"Have you seen {movie}?")
