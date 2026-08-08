from agents import function_tool


@function_tool
def create_research_queries(
    business: str,
    industry: str,
    target_audience: str,
) -> str:
    """
    Create useful market research queries.
    """

    queries = [
        f"{industry} market trends",
        f"{industry} customer behaviour",
        f"{industry} growth opportunities",
        f"{target_audience} buying behaviour",
        f"marketing trends for {target_audience}",
    ]

    return "\n".join(
        f"{number}. {query}"
        for number, query in enumerate(queries, start=1)
    )


@function_tool
def create_competitor_queries(
    business: str,
    industry: str,
) -> str:
    """
    Create useful competitor research queries.
    """

    queries = [
        f"{business} competitors",
        f"top companies in {industry}",
        f"{industry} competitor marketing strategies",
        f"{industry} brand positioning",
        f"{industry} competitive analysis",
    ]

    return "\n".join(
        f"{number}. {query}"
        for number, query in enumerate(queries, start=1)
    )