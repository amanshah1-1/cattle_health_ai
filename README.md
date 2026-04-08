# Cattle Health AI

![Cattle Health AI Screenshot](p_1.png)

## Description
![Cattle Health AI Screenshot](Cattle_health_AI_assistant_architecture.png)
A multi-agent AI assistant for cattle health using **LangChain RAG**, **Ollama**, and **FAISS embeddings**.  

Supports:
- Nutrition advice  
- Disease diagnosis  
- Treatment recommendations  

Provides:
- Streamlit interface for interactive chat  
- FastAPI endpoint for integration  
- Logging of all queries

  cattle_ai_assistant/
├── data.txt
├── app.py          # Streamlit app
├── agent.py        # Multi-agent / tools
├── api.py          # FastAPI endpoints
├── requirements.txt
├── README.md
└── utils.py        # helper functions (optional)

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/cattle_health_ai.git
cd cattle_health_ai
