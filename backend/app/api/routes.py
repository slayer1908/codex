from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.base import AgentContext
from app.core.database import get_db
from app.models.entities import Ad, Campaign, Keyword, PerformanceMetric
from app.schemas.campaign import (
    AdResponse,
    AnalyticsResponse,
    CampaignBuildResponse,
    CampaignRequest,
    DeploymentResponse,
    KeywordResponse,
)
from app.services.google_ads import GoogleAdsService
from app.services.orchestrator import AgentOrchestrator

router = APIRouter()
orchestrator = AgentOrchestrator()
gads = GoogleAdsService()


@router.post("/analyze-website")
def analyze_website(request: CampaignRequest):
    context = AgentContext(
        website_url=str(request.website_url),
        location=request.location,
        monthly_budget=request.monthly_budget,
        target_cpa=request.target_cpa,
        target_roas=request.target_roas,
        memory={},
    )
    return orchestrator.run(context)


@router.post("/generate-keywords", response_model=list[KeywordResponse])
def generate_keywords(request: CampaignRequest):
    context = AgentContext(str(request.website_url), request.location, request.monthly_budget, request.target_cpa, request.target_roas, {})
    output = orchestrator.run(context)
    return output["KeywordIntelligenceAgent"]["keywords"]


@router.post("/generate-ads", response_model=list[AdResponse])
def generate_ads(request: CampaignRequest):
    context = AgentContext(str(request.website_url), request.location, request.monthly_budget, request.target_cpa, request.target_roas, {})
    output = orchestrator.run(context)
    return output["AdCreativeAgent"]["ads"]


@router.post("/build-campaign", response_model=CampaignBuildResponse)
def build_campaign(request: CampaignRequest):
    context = AgentContext(str(request.website_url), request.location, request.monthly_budget, request.target_cpa, request.target_roas, {})
    output = orchestrator.run(context)
    return CampaignBuildResponse(
        campaign_name=f"ApexAds | {request.location} | {request.website_url.host}",
        channels=gads.supported_campaign_types,
        bidding_strategy=output["BiddingStrategyAgent"]["bid_strategy"],
        structure=output["CampaignBuilderAgent"]["campaign_structure"],
    )


@router.post("/deploy-campaign", response_model=DeploymentResponse)
def deploy_campaign(request: CampaignRequest, db: Session = Depends(get_db)):
    campaign = Campaign(
        website_url=str(request.website_url),
        campaign_name=f"ApexAds Deployment | {request.website_url.host}",
        budget=request.monthly_budget,
        currency=request.currency,
    )
    db.add(campaign)
    db.commit()
    db.refresh(campaign)
    external = gads.deploy_campaign({"campaign_id": campaign.id, "website": campaign.website_url})
    campaign.status = external["status"]
    db.commit()
    return DeploymentResponse(campaign_id=campaign.id, external_id=external["external_id"], status=external["status"])


@router.get("/get-analytics", response_model=list[AnalyticsResponse])
def get_analytics(db: Session = Depends(get_db)):
    rows = db.query(PerformanceMetric).all()
    return [
        AnalyticsResponse(
            campaign_id=row.campaign_id,
            impressions=row.impressions,
            clicks=row.clicks,
            conversions=row.conversions,
            spend=row.spend,
            ctr=row.ctr,
            conversion_rate=row.conversion_rate,
        )
        for row in rows
    ]


@router.post("/run-optimization")
def run_optimization(request: CampaignRequest):
    context = AgentContext(str(request.website_url), request.location, request.monthly_budget, request.target_cpa, request.target_roas, {})
    output = orchestrator.run(context)
    return {"optimization": output["OptimizationAgent"], "learning": output["LearningEngineAgent"]}
