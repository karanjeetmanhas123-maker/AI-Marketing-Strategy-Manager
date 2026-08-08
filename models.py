from pydantic import BaseModel


# Output from Market Research Agent
class MarketResearchResult(BaseModel):
    target_audience: str
    customer_needs: list[str]
    market_trends: list[str]
    opportunities: list[str]


# Output from Competitor Analysis Agent
class CompetitorResult(BaseModel):
    competitors: list[str]
    competitor_strengths: list[str]
    competitor_weaknesses: list[str]
    market_opportunities: list[str]
    recommended_positioning: str


# Output from Campaign Planner Agent
class CampaignPlan(BaseModel):
    objective: str
    channels: list[str]
    campaign_ideas: list[str]
    budget_allocation: dict[str, float]
    kpis: list[str]


# Output from Content Strategist Agent
class ContentPlan(BaseModel):
    social_media_posts: list[str]
    ad_copy: list[str]
    email_ideas: list[str]
    hashtags: list[str]
    reel_ideas: list[str]


# Output from Analytics Agent
class AnalyticsResult(BaseModel):
    best_channel: str
    average_ctr: float
    total_conversions: int
    total_revenue: float
    recommendations: list[str]


# Output from Optimization Agent
class OptimizationResult(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    improvements: list[str]
    next_actions: list[str]