import json
import os

from agents import function_tool


MEMORY_FILE = "data/memory.json"


def _ensure_memory_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump({}, file)


@function_tool
def save_business_memory(
    business_name: str,
    product: str,
    industry: str,
    target_audience: str,
    budget: float,
    goal: str,
) -> str:
    """
    Save basic information about a business for future sessions.
    """

    _ensure_memory_file()

    data = {
        "business_name": business_name,
        "product": product,
        "industry": industry,
        "target_audience": target_audience,
        "budget": budget,
        "goal": goal,
    }

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return "Business information saved successfully."


@function_tool
def load_business_memory() -> str:
    """
    Load previously saved business information.
    """

    _ensure_memory_file()

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not data:
        return "No previous business information found."

    return json.dumps(data, indent=2)