from agents import function_tool


@function_tool
def calculate_campaign_metrics(
    impressions: int,
    clicks: int,
    conversions: int,
    cost: float,
    revenue: float,
) -> str:
    """
    Calculate important marketing campaign metrics.
    """

    ctr = (
        clicks / impressions * 100
        if impressions > 0
        else 0
    )

    conversion_rate = (
        conversions / clicks * 100
        if clicks > 0
        else 0
    )

    cost_per_conversion = (
        cost / conversions
        if conversions > 0
        else 0
    )

    roas = (
        revenue / cost
        if cost > 0
        else 0
    )

    return (
        f"CTR: {ctr:.2f}%\n"
        f"Conversion Rate: {conversion_rate:.2f}%\n"
        f"Cost Per Conversion: INR {cost_per_conversion:.2f}\n"
        f"ROAS: {roas:.2f}x"
    )