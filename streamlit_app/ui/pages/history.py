import streamlit as st

def render_history():
    st.markdown("## 🕒 Conversation History")

    if "chat_history" not in st.session_state or not st.session_state.chat_history:
        st.info("No conversations yet.")
        return

    for i, msg in enumerate(st.session_state.chat_history):
        role = "User" if msg["role"] == "user" else "Agent"
        st.markdown(f"""
        <div class="glass" style="padding:12px; margin-bottom:10px">
          <b>{role}:</b><br>
          {msg["text"]}
        </div>
        """, unsafe_allow_html=True)
