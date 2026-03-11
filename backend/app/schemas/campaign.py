from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class CampaignRequest(BaseModel):
    website_url: HttpUrl
    location: str
    monthly_budget: float = Field(gt=0)
    target_cpa: float | None = None
    target_roas: float | None = None
    currency: str = "USD"


class KeywordResponse(BaseModel):
    term: str
    match_type: str
    intent: str
    score: float


class AdResponse(BaseModel):
    ad_type: str
    headline: str
    description: str
    assets: dict[str, Any] = {}


class CampaignBuildResponse(BaseModel):
    campaign_name: str
    channels: list[str]
    bidding_strategy: str
    structure: dict[str, Any]


class DeploymentResponse(BaseModel):
    campaign_id: int
    external_id: str
    status: str


class AnalyticsResponse(BaseModel):
    campaign_id: int
    impressions: int
    clicks: int
    conversions: int
    spend: float
    ctr: float
    conversion_rate: float
