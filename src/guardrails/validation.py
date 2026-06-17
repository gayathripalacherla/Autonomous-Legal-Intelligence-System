def validate_query(query: str) -> None:
    """
    Validate user query before retrieval and summarization.
    """
    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    if len(query.strip()) < 10:
        raise ValueError("Query must include enough legal context.")
