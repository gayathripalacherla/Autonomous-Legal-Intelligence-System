def create_structured_summary(query: str, retrieved_cases: list) -> dict:
    """
    Create a structured legal summary from retrieved cases.
    """
    if not retrieved_cases:
        return {
            "facts": "No relevant cases retrieved.",
            "issue": "Insufficient context.",
            "rule": "Unable to determine rule without retrieved context.",
            "disposition": "Human review required."
        }

    top_case = retrieved_cases[0]

    return {
        "case_title": top_case.get("case_title", "Unknown Case"),
        "court": top_case.get("court", "Unknown Court"),
        "facts": top_case.get("summary", "Summary not available."),
        "issue": f"Legal issue related to query: {query}",
        "rule": "Rule extraction requires review of full legal text and jurisdiction-specific authority.",
        "disposition": "Use retrieved case context for research support; legal professional review recommended."
    }
