# app.py
import streamlit as st
from model import get_agent_chain
from utils import log_query

st.set_page_config(page_title="🐄 Cattle Health AI Assistant", layout="centered")

st.title("🐄 Cattle Health AI Assistant")

# Agent selection
agent_name = st.selectbox("Choose Agent", ["Nutrition", "Diagnosis", "Treatment"])
qa_chain = get_agent_chain(agent_name)

# User query input
query = st.text_input("Ask something about cattle")

if query:
    result = qa_chain.invoke({"question": query})
    answer = result["answer"]
    st.write("🤖 Answer:")
    st.write(answer)
    
    # Log queries
    log_query(agent_name, query, answer)