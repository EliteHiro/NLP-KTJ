import streamlit as st
from embedder import Embedder
from vector_store import VectorStoreManager
from retriever import Retriever
from rag_agent import RAGAgent
from action_agent import ActionAgent
from agent_controller import AgentController

@st.cache_resource
def load_agent():
    embedder = Embedder()
    store = VectorStoreManager()
    store.load()

    retriever = Retriever(embedder, store)
    rag = RAGAgent(retriever)
    action = ActionAgent()

    return AgentController(rag, action)

agent = load_agent()

st.title("🤖 Agentic Enterprise Assistant")

query = st.chat_input("Ask a question or give an action")

if query:
    res = agent.process_query(query)
    st.write(res)
