import streamlit as st
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.pages.query import render_query

# Load CSS
for css in ["base", "header", "sidebar", "chat"]:
    with open(f"assets/{css}.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_sidebar()
render_header()
render_query()
