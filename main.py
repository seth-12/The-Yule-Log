
import streamlit as st

pages = {
    "Menu": [
        st.Page("Landing.py", title ="Landing"),
        st.Page("Watchlist.py", title="Watchlist"),
        st.Page("test_page.py", title="Test")
    ],    
}

pg = st.navigation(pages, position="top")
pg.run()
