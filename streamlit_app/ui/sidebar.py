import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("## 🧠 BotTrainer")
        st.caption("Groq-powered NLP Agent")

        if "show_raw" not in st.session_state:
            st.session_state.show_raw = False

        st.divider()

        st.markdown("### ⚙ Settings")
        st.toggle("👁 Show Raw Prompt", key="show_raw")

        st.divider()
        st.markdown(
            "<center><span style='color:#7C3AED'>●</span> GROQ Connected</center>",
            unsafe_allow_html=True
        )
