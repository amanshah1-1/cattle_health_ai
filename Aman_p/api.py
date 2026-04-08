# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import get_agent_chain
from utils import log_query

app = FastAPI()

class Query(BaseModel):
    agent: str
    question: str

@app.post("/ask")
def ask_cattle(query: Query):
    chain = get_agent_chain(query.agent)
    result = chain.invoke({"question": query.question})
    answer = result["answer"]
    log_query(query.agent, query.question, answer)
    return {"answer": answer}