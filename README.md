# ⚖️ Autonomous Legal Intelligence System — Multi-Agent RAG for Structured Legal Case Summarization

## 📌 Overview
An **AI-powered multi-agent system** that performs structured legal case summarization, domain classification, and precedent retrieval.  
Combines **retrieval-augmented generation (RAG)** with **contextual memory** to help **lawyers, legal researchers, and policy analysts** quickly extract essential case details and discover relevant precedents.

---

## 🛠 Tech Stack
- **Languages:** Python  
- **AI/ML & NLP:** Hugging Face Transformers (**FLAN-T5**), SentenceTransformers, LangChain, LangGraph, FAISS  
- **Multi-Agent Framework:** CrewAI  
- **Context Management:** Model Context Protocol (MCP)  
- **UI & Deployment:** Gradio, Streamlit  
- **Cloud & Tools:** Google Colab, Git

---

## ✨ Features
- 🧠 **Multi-Agent Orchestration** — CrewAI agents handle summarization, domain classification, and recommendations  
- 📚 **RAG-Powered Retrieval** — FAISS + SentenceTransformers for semantic search & precedent retrieval  
- 📄 **Structured Summaries** — Outputs:
  - Case Title  
  - Court  
  - Date  
  - Facts  
  - Issue  
  - Rule  
  - Disposition  
- 🌐 **Interactive UI** — Accessible via Gradio & Streamlit

---

## 📂 Project Structure
autonomous-legal-intelligence/
│── app.py # Main app entry point
│── summarizer_agent.py # Agent for structured summarization
│── recommender_agent.py # Agent for precedent retrieval
│── mcp_server.py # Context management
│── requirements.txt # Dependencies
│── README.md # Project documentation

---
 ## Future Improvements
Expand retrieval sources beyond arXiv-style datasets
Add multilingual legal case summarization
Integrate with legal databases like LexisNexis or Westlaw

