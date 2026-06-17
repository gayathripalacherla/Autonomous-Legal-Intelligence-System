def retrieve_similar_cases(query: str, cases, top_k: int = 5) -> list:
    """
    Lightweight retrieval placeholder for legal cases.

    This function returns the first top_k records as a simple baseline.
    FAISS-based retrieval can be connected through embeddings.py and faiss_index.py.
    """
    if cases is None or len(cases) == 0:
        return []

    results = []

    for _, row in cases.head(top_k).iterrows():
        results.append({
            "case_title": row.get("case_title", "Unknown Case"),
            "court": row.get("court", "Unknown Court"),
            "domain": row.get("domain", "Unknown Domain"),
            "summary": row.get("summary", ""),
            "source_link": row.get("source_link", "")
        })

    return results
