
# Watchlist.py
import streamlit as st
import re
from pathlib import Path


def render_markdown_with_static_images(md_text):
    """
    Render Markdown text line-by-line. When an image markdown references /static/...
    it will render the image with st.image (semi-private); otherwise it renders the
    markdown line normally.

    Supports images that appear on their own line like:
      ![alt text](/static/some.png)

    If an image path is inline inside a paragraph, it will still render the whole
    paragraph as markdown (the browser will try to fetch the URL).
    """
    if not md_text:
        return

    # Split into blocks by blank line so we don't break paragraphs too aggressively
    blocks = re.split(r'\n\s*\n', md_text)
    for block in blocks:
        # If block is a single image line, render as st.image for private static files
        img_match = re.fullmatch(r'\s*!\[([^\]]*)\]\(([^)]+)\)\s*', block.strip(), flags=re.DOTALL)
        if img_match:
            alt_text, path = img_match.groups()
            # handle leading slash paths like /static/...
            if path.startswith("/static/"):
                local_path = Path(path.lstrip("/"))
                if local_path.exists():
                    st.image(str(local_path), caption=alt_text)
                else:
                    st.warning(f"⚠️ Image not found: {local_path}")
            else:
                # external or absolute URL — render as markdown so the browser fetches it
                st.markdown(block)
        else:
            # Normal text or mixed content — render as markdown
            st.markdown(block)

st.image("static/text.png")

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
