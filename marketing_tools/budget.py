from agents import function_tool


@function_tool
def check_budget(
    total_budget: float,
    instagram_budget: float,
    google_ads_budget: float,
    influencer_budget: float,
    content_budget: float,
    email_budget: float,
) -> str:
    """
    Check whether a proposed marketing budget allocation
    exceeds the total available marketing budget.
    """

    allocated = (
        instagram_budget
        + google_ads_budget
        + influencer_budget
        + content_budget
        + email_budget
    )

    remaining = total_budget - allocated

    if allocated > total_budget:
        return (
            f"Budget exceeded. Total budget is INR {total_budget:.2f}. "
            f"Proposed spending is INR {allocated:.2f}. "
            f"Reduce spending by INR {abs(remaining):.2f}."
        )

    return (
        f"Budget is valid. Total budget is INR {total_budget:.2f}. "
        f"Allocated amount is INR {allocated:.2f}. "
        f"Remaining budget is INR {remaining:.2f}."
    )