import streamlit as st

def chat_message(role, text, intent=None, confidence=None, entities=None, raw=None):
    cls = "user" if role == "user" else "bot"

    html = f"<div class='chat {cls}'>{text}"

    if intent:
        html += f"<br>🎯 <span class='pill'>{intent}</span>"

    if confidence is not None:
        html += f"<br>⚡ Confidence: {confidence*100:.1f}%"

    if entities:
        html += "<br>🏷 "
        for k, v in entities.items():
            html += f"<span class='pill'>{k}: {v}</span> "

    if raw:
        html += f"<br><pre style='font-size:11px;opacity:0.7'>{raw}</pre>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
