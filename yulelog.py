import streamlit as st
import re
from pathlib import Path
from config import render_markdown_with_static_images as render_images
from config import config as cfg

# cfg()

class World:
    def __init__(self, temperature):
        self.temperature = temperature

if "world" not in st.session_state:
    st.session_state.world = World(90)
world = st.session_state.world

st.title("Temperature Tracker")
temp_display = st.empty()
temp_display.write(f"Current Temp: {world.temperature}")

if st.button("Increase Temp"):
    world.temperature += 1
    temp_display.write(f"Current Temp: {world.temperature}")