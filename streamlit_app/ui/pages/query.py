import streamlit as st
from groq_client import call_groq
from ui.chat_message import chat_message

def render_query():
    st.markdown("## 💬 Chat with NLP Agent")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_query = st.text_input("Ask your enterprise assistant")

    if st.button("Send") and user_query:
        result, raw = call_groq(
            user_query,
            show_raw=st.session_state.show_raw
        )

        st.session_state.chat_history.append({
            "role": "user",
            "text": user_query
        })

        st.session_state.chat_history.append({
            "role": "bot",
            "text": result["answer"],
            "intent": result["intent"],
            "confidence": result["confidence"],
            "entities": result["entities"],
            "raw": raw
        })

    for msg in st.session_state.chat_history:
        chat_message(
            role=msg["role"],
            text=msg["text"],
            intent=msg.get("intent"),
            confidence=msg.get("confidence"),
            entities=msg.get("entities"),
            raw=msg.get("raw"),
        )
