
import streamlit as st

pages = {
    "Console": [
        st.Page("comfydir.py", title ="Comfyton Directory"),
        st.Page("Watchlist.py", title="Watchlist"),
        st.Page("test_page.py", title="Test")
    ],    
}

pg = st.navigation(pages, position="top")
pg.run()
