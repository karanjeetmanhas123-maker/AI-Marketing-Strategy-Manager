import asyncio
import json

from openai import RateLimitError
from agents import Runner

from marketing_agents.manager import marketing_manager
from marketing_agents.market_research import market_research_agent
from marketing_agents.competitor import competitor_agent
from marketing_agents.campaign_planner import campaign_planner_agent
from marketing_agents.content_strategist import content_strategist_agent
from marketing_agents.analytics_agent import analytics_agent
from marketing_agents.optimization import optimization_agent


# ---------------------------------------------------------
# HELPER: CONVERT AGENT OUTPUT TO TEXT
# ---------------------------------------------------------

def to_json(data):
    """
    Convert Pydantic structured output or normal output
    into readable text.
    """

    if hasattr(data, "model_dump"):
        return json.dumps(
            data.model_dump(),
            indent=2,
            ensure_ascii=False,
        )

    return str(data)


# ---------------------------------------------------------
# HELPER: RUN AGENT WITH GROQ RATE LIMIT RETRY
# ---------------------------------------------------------

async def run_agent_with_retry(agent, input_text):
    """
    Run an agent and retry automatically when Groq's
    free-tier rate limit is temporarily reached.
    """

    max_retries = 5

    for attempt in range(max_retries):

        try:
            result = await Runner.run(
                agent,
                input_text,
            )

            return result

        except RateLimitError:

            if attempt == max_retries - 1:
                raise

            wait_time = 5 + (attempt * 5)

            print(
                f"Groq rate limit reached. "
                f"Waiting {wait_time} seconds before retry..."
            )

            await asyncio.sleep(wait_time)


# =========================================================
# MAIN MARKETING STRATEGY WORKFLOW
# =========================================================

async def generate_marketing_strategy(
    business_name,
    product,
    industry,
    target_audience,
    budget,
    goal,
):

    business_context = f"""
Business Name: {business_name}
Product/Service: {product}
Industry: {industry}
Target Audience: {target_audience}
Marketing Budget: INR {budget}
Marketing Goal: {goal}
"""

    # -----------------------------------------------------
    # 1. MARKET RESEARCH
    # -----------------------------------------------------

    print("Running Market Research Agent...")

    market_result = await run_agent_with_retry(
        market_research_agent,
        business_context,
    )

    market_data = market_result.final_output

    print("Market Research completed.")

    # -----------------------------------------------------
    # 2. COMPETITOR ANALYSIS
    # -----------------------------------------------------

    print("Running Competitor Analysis Agent...")

    competitor_input = f"""
Analyze competitors for the following business.

{business_context}

Keep the analysis concise and useful for campaign planning.
"""

    competitor_result = await run_agent_with_retry(
        competitor_agent,
        competitor_input,
    )

    competitor_data = competitor_result.final_output

    print("Competitor Analysis completed.")

    # -----------------------------------------------------
    # 3. CAMPAIGN PLANNER
    # -----------------------------------------------------

    print("Running Campaign Planner Agent...")

    campaign_input = f"""
Create a practical marketing campaign.

BUSINESS INFORMATION:
{business_context}

MARKET RESEARCH:
{to_json(market_data)}

COMPETITOR ANALYSIS:
{to_json(competitor_data)}

TOTAL AVAILABLE BUDGET:
INR {budget}

Create a realistic campaign.

Do not exceed the total marketing budget.

Keep the response concise.
"""

    campaign_result = await run_agent_with_retry(
        campaign_planner_agent,
        campaign_input,
    )

    campaign_data = campaign_result.final_output

    print("Campaign Planning completed.")

    # -----------------------------------------------------
    # 4. CONTENT STRATEGIST
    # -----------------------------------------------------

    print("Running Content Strategist Agent...")

    content_input = f"""
Create concise marketing content for this business.

BUSINESS:
{business_context}

CAMPAIGN PLAN:
{to_json(campaign_data)}

Create content suitable for the target audience.

Keep the response concise.
"""

    content_result = await run_agent_with_retry(
        content_strategist_agent,
        content_input,
    )

    content_data = content_result.final_output

    print("Content Strategy completed.")

    # -----------------------------------------------------
    # 5. OPTIMIZATION ADVISOR
    # -----------------------------------------------------

    print("Running Optimization Advisor Agent...")

    optimization_input = f"""
Review this proposed marketing strategy.

BUSINESS:
{business_context}

MARKET RESEARCH:
{to_json(market_data)}

COMPETITOR ANALYSIS:
{to_json(competitor_data)}

CAMPAIGN PLAN:
{to_json(campaign_data)}

CONTENT STRATEGY:
{to_json(content_data)}

Give:

STRENGTHS:
- 3 concise strengths

WEAKNESSES:
- 3 concise weaknesses

IMPROVEMENTS:
- 3 practical improvements

NEXT ACTIONS:
- 3 specific next actions

Do not invent campaign performance statistics.

Keep the response concise.
"""

    optimization_result = await run_agent_with_retry(
        optimization_agent,
        optimization_input,
    )

    optimization_data = optimization_result.final_output

    print("Optimization completed.")

    # -----------------------------------------------------
    # 6. MARKETING MANAGER
    # -----------------------------------------------------

    print("Running Marketing Manager...")

    manager_input = f"""
Prepare the final professional marketing strategy.

BUSINESS INFORMATION:
{business_context}

MARKET RESEARCH:
{to_json(market_data)}

COMPETITOR ANALYSIS:
{to_json(competitor_data)}

CAMPAIGN PLAN:
{to_json(campaign_data)}

CONTENT STRATEGY:
{to_json(content_data)}

OPTIMIZATION REVIEW:
{to_json(optimization_data)}

Create a clear final strategy with these sections:

1. Executive Summary
2. Target Audience
3. Customer Needs
4. Market Opportunities
5. Competitor Analysis
6. Brand Positioning
7. Campaign Objective
8. Marketing Channels
9. Budget Allocation
10. Content Strategy
11. KPIs
12. Optimization Recommendations
13. Next Actions

Important:

Do not invent campaign performance statistics.

Do not claim that the strategy has been approved.

The user must review and approve the strategy separately.

Keep the final report professional and reasonably concise.
"""

    final_result = await run_agent_with_retry(
        marketing_manager,
        manager_input,
    )

    final_report = final_result.final_output

    print("Final Marketing Strategy completed.")

    return {
        "market_research": to_json(market_data),
        "competitor_analysis": to_json(competitor_data),
        "campaign_plan": to_json(campaign_data),
        "content_strategy": to_json(content_data),
        "optimization": to_json(optimization_data),
        "final_report": str(final_report),
    }


# ---------------------------------------------------------
# FUNCTION USED BY GRADIO FOR STRATEGY
# ---------------------------------------------------------

def run_strategy(
    business_name,
    product,
    industry,
    target_audience,
    budget,
    goal,
):

    return asyncio.run(
        generate_marketing_strategy(
            business_name,
            product,
            industry,
            target_audience,
            budget,
            goal,
        )
    )


# =========================================================
# CAMPAIGN PERFORMANCE ANALYTICS WORKFLOW
# =========================================================

async def analyze_campaign_performance(
    impressions,
    clicks,
    conversions,
    cost,
    revenue,
):
    """
    Run the Analytics Agent using campaign performance
    information entered by the user.
    """

    analytics_input = f"""
Analyze the following marketing campaign performance.

Impressions: {int(impressions)}
Clicks: {int(clicks)}
Conversions: {int(conversions)}
Advertising Cost: INR {cost}
Revenue: INR {revenue}

You must use the calculate_campaign_metrics tool.

Calculate and discuss:

- CTR
- Conversion Rate
- Cost Per Conversion
- ROAS

After calculating the metrics, explain whether the
campaign is performing effectively.

Then provide practical marketing recommendations.

Do not invent any additional campaign statistics.

Use this format:

CAMPAIGN METRICS:

PERFORMANCE ANALYSIS:

RECOMMENDATIONS:
"""

    print("Running Marketing Analytics Agent...")

    result = await run_agent_with_retry(
        analytics_agent,
        analytics_input,
    )

    print("Marketing Analytics completed.")

    return str(result.final_output)


# ---------------------------------------------------------
# FUNCTION USED BY GRADIO FOR ANALYTICS
# ---------------------------------------------------------

def run_analytics(
    impressions,
    clicks,
    conversions,
    cost,
    revenue,
):

    return asyncio.run(
        analyze_campaign_performance(
            impressions,
            clicks,
            conversions,
            cost,
            revenue,
        )
    )