# data_loader.py
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import streamlit as st

@st.cache_resource
def load_data(file_path: str = "data/cattle_data.txt"):
    loader = TextLoader(file_path)
    docs = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db