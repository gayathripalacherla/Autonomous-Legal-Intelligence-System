# Architecture

This project follows a modular Legal RAG architecture.

## Pipeline Flow

Legal Case Dataset  
→ Data Loading  
→ Text Preprocessing  
→ Embedding Generation  
→ FAISS Vector Index  
→ Semantic Retrieval  
→ Structured Legal Summarization  
→ Citation Checks  
→ Final Legal Research Output  

## Main Components

### Dataset Layer
Stores enriched legal case records including case title, court, legal domain, summary, jurisdiction, and source links.

### Retrieval Layer
Uses SentenceTransformers and FAISS to support semantic precedent retrieval.

### RAG Layer
Combines retrieved case context with summarization logic to produce structured legal summaries.

### Guardrail Layer
Validates user input, checks citation availability, and recommends human review for legal outputs.
