
import streamlit as st

pages = {
    "Console": [
        st.Page("comfydir.py", title ="Comfyton Directory"),
        st.Page("yulelog.py", title="The Yule Log")
    ],    
}

pg = st.navigation(pages, position="top")
pg.run()
