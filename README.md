# Autonomous Legal Intelligence System

A production-oriented **Legal AI / RAG system** for structured legal case summarization, semantic precedent retrieval, and legal domain classification.

This project uses **Retrieval-Augmented Generation (RAG)**, **SentenceTransformers**, **FAISS**, and LLM-based summarization workflows to help legal researchers quickly extract key case details and retrieve similar precedents from a structured legal case dataset.

---

## Problem Statement

Legal researchers often need to review large volumes of case documents, extract key facts, identify legal issues, classify domains, and compare similar precedents. This process is time-consuming, repetitive, and difficult to scale manually.

This project demonstrates how an AI-powered legal intelligence system can support legal research by combining:

* Semantic search
* Vector-based case retrieval
* Structured legal summarization
* Domain and subdomain classification
* Citation-aware response checks
* Multi-agent style workflow design

---

## Dataset

The project uses an enriched legal case dataset containing **1,200 legal case records** with structured metadata.

Key dataset fields include:

* Case title
* Summary
* Court
* Published date
* Legal domain
* Legal subdomain
* Cleaned case text
* Token count
* Case year
* Case ID
* Jurisdiction
* Source link

---

## Key Features

* **RAG-powered legal retrieval** using FAISS and SentenceTransformers
* **Semantic precedent search** for finding similar legal cases
* **Structured legal summaries** with case title, facts, issue, rule, and disposition
* **Domain and subdomain classification** for legal case organization
* **Citation and source-link awareness** for legal research traceability
* **Guardrail checks** for empty inputs, missing context, and unsupported outputs
* **Notebook prototype** for experimentation and model testing
* Modular Python structure for future API or UI deployment

---

## Tech Stack

* Python
* Pandas
* NumPy
* SentenceTransformers
* FAISS
* Hugging Face Transformers
* LangChain
* LangGraph concepts
* CrewAI-style agent workflow concepts
* Gradio / Streamlit prototype
* Docker
* Git/GitHub

---

## System Architecture

```text
Legal Case Dataset
    ↓
Data Cleaning + Preprocessing
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Index
    ↓
Semantic Case Retrieval
    ↓
RAG Summarization Pipeline
    ↓
Validation + Citation Checks
    ↓
Structured Legal Summary + Similar Precedents
```

---

## Core Components

### Document Loader

Loads legal case records from the enriched CSV dataset and prepares fields such as title, court, domain, summary, clean text, and jurisdiction.

### Text Splitter

Splits long case text into smaller chunks for embedding, retrieval, and summarization.

### Embedding Pipeline

Uses SentenceTransformers to convert legal text into dense vector embeddings.

### FAISS Index

Stores and searches embeddings for fast semantic similarity retrieval.

### Legal RAG Pipeline

Retrieves relevant cases and generates structured legal summaries using retrieved context.

### Guardrail Layer

Applies validation checks to improve reliability, including:

* Empty query checks
* Minimum context checks
* Citation/source availability checks
* Unsupported output warnings
* Human-review recommendation for sensitive legal outputs

---

## Example Use Case

Input query:

```text
Find cases related to privacy violations and summarize the most relevant precedent.
```

Expected output:

```json
{
  "query": "privacy violations",
  "retrieved_cases": [
    {
      "title": "Martin v. Google Inc.",
      "court": "US-State",
      "domain": "Privacy / Technology",
      "similarity_score": 0.84
    }
  ],
  "structured_summary": {
    "facts": "The case involves alleged misuse of user data...",
    "issue": "Whether the defendant violated privacy obligations...",
    "rule": "The court considered statutory and common law privacy principles...",
    "disposition": "The case outcome depends on jurisdiction-specific privacy standards."
  },
  "guardrails": [
    "Legal research support only",
    "Human review recommended",
    "Source verification required"
  ]
}
```

---

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── Legal_Summarizertool_v1_draft1.ipynb
├── data/
│   └── Legal_Cases_enriched.csv
├── src/
│   ├── main.py
│   ├── config.py
│   ├── ingestion/
│   ├── retrieval/
│   ├── rag/
│   ├── guardrails/
│   └── utils/
└── docs/
    ├── architecture.md
    └── system_design.md
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/gayathripalacherla/Autonomous-Legal-Intelligence-System.git
cd Autonomous-Legal-Intelligence-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main pipeline:

```bash
python src/main.py
```

---

## Current Status

This project includes:

* Notebook prototype for experimentation
* Legal case dataset with structured metadata
* RAG and retrieval design
* FAISS-based semantic search architecture
* Structured legal summarization workflow
* Modular production-style project structure

---

## Future Enhancements

* Add FastAPI endpoint for legal query submission
* Add Streamlit interface for interactive legal search
* Add persistent FAISS index storage
* Add automated tests for retrieval and summarization
* Add GitHub Actions CI workflow
* Add evaluation metrics for retrieval quality
* Add more robust citation validation
* Expand dataset with additional legal sources

---

## Disclaimer

This project is for legal research assistance and educational purposes only. It does not provide legal advice. Outputs should be reviewed by qualified legal professionals before use in real-world legal decisions.
