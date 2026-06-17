def check_source_links(retrieved_cases: list) -> dict:
    """
    Check whether retrieved cases include source links for traceability.
    """
    if not retrieved_cases:
        return {
            "has_sources": False,
            "message": "No retrieved cases available for citation verification."
        }

    source_count = sum(
        1 for case in retrieved_cases if case.get("source_link")
    )

    return {
        "has_sources": source_count > 0,
        "source_count": source_count,
        "message": "Human verification of legal sources is recommended."
    }
