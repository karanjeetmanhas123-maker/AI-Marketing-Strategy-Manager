import os
from datetime import datetime

from agents import function_tool


@function_tool
def save_marketing_report(
    business_name: str,
    report_content: str,
) -> str:
    """
    Save the final approved marketing strategy as a text file.
    """

    os.makedirs("outputs", exist_ok=True)

    safe_name = "".join(
        character
        for character in business_name
        if character.isalnum() or character in (" ", "-", "_")
    ).strip()

    if not safe_name:
        safe_name = "marketing_strategy"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{safe_name}_{timestamp}.txt"
    filepath = os.path.join("outputs", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(report_content)

    return f"Marketing report saved successfully to {filepath}"