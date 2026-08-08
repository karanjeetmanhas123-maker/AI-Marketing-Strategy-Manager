from agents import Agent

from config import groq_model


optimization_agent = Agent(
    name="Optimization Advisor Agent",

    instructions="""
    You are a senior marketing optimization advisor.

    Review the provided marketing strategy.

    Identify the most important strengths, weaknesses,
    improvements and next actions.

    Keep the response concise.

    You MUST return all four sections:

    STRENGTHS:
    - Give 3 strengths.

    WEAKNESSES:
    - Give 3 weaknesses.

    IMPROVEMENTS:
    - Give 3 practical improvements.

    NEXT ACTIONS:
    - Give 3 specific next actions.

    Do not return JSON.
    Do not invent campaign performance statistics.
    """,

    model=groq_model,
)