import streamlit as st

def render_header():
    st.markdown("""
    <div class="glass-strong" style="padding:20px">
      <h3 class="gradient-text">Intent Analysis Dashboard</h3>
      <p style="font-size:12px;color:#94a3b8">
        Groq-powered NLP Assistant
      </p>
    </div>
    """, unsafe_allow_html=True)
