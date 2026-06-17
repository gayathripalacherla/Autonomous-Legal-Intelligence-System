from ingestion.document_loader import load_legal_cases
from retrieval.retriever import retrieve_similar_cases
from rag.legal_rag_pipeline import generate_legal_summary
from guardrails.validation import validate_query
from utils.logger import log_step

def main():
    query = "Find cases related to privacy violations and summarize the most relevant precedent."

    validate_query(query)
    log_step("Loading legal case dataset")

    cases = load_legal_cases("data/Legal_Cases_enriched.csv")

    log_step("Retrieving similar legal cases")
    retrieved_cases = retrieve_similar_cases(query, cases)

    log_step("Generating structured legal summary")
    summary = generate_legal_summary(query, retrieved_cases)

    print(summary)

if __name__ == "__main__":
    main()
