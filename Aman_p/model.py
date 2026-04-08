# model.py
from langchain_community.llms import Ollama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from data_loader import load_data

# Initialize database and LLM
db = load_data()
llm = Ollama(model="llama3")  # Ollama local

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Multi-agent prompt templates (simplified)
agent_prompts = {
    "Nutrition": "You are a cattle nutrition expert. Answer concisely.",
    "Diagnosis": "You are a cattle disease diagnosis expert. Answer carefully.",
    "Treatment": "You are a cattle treatment expert. Provide safe recommendations."
}

# Function to get RAG chain per agent
def get_agent_chain(agent_name: str):
    prompt = agent_prompts.get(agent_name, "")
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=db.as_retriever(),
        memory=memory
    )