import os
from dotenv import load_dotenv

from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

# Load environment variables from .env
load_dotenv()

# Disable OpenAI tracing because we are using Groq
set_tracing_disabled(True)

# Read Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )

# Connect OpenAI Agents SDK to Groq
groq_client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

# Model used by all our agents
MODEL_NAME = "openai/gpt-oss-20b"

groq_model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=groq_client,
)