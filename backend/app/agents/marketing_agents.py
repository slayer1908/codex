from app.agents.base import AgentContext, BaseAgent


class PlannerAgent(BaseAgent):
    name = "PlannerAgent"
    def run(self, context: AgentContext) -> dict:
        return {"plan": "Full-funnel Google Ads automation plan"}


class WebsiteIntelligenceAgent(BaseAgent):
    name = "WebsiteIntelligenceAgent"
    def run(self, context: AgentContext) -> dict:
        return {"business_type": "service", "services": ["primary offer"], "audience": ["high-intent buyers"]}


class MarketResearchAgent(BaseAgent):
    name = "MarketResearchAgent"
    def run(self, context: AgentContext) -> dict:
        return {"trends": ["category growth"], "seasonality": "moderate"}


class CompetitorAnalyzerAgent(BaseAgent):
    name = "CompetitorAnalyzerAgent"
    def run(self, context: AgentContext) -> dict:
        return {"competitors": ["competitor-a.com", "competitor-b.com"]}


class KeywordIntelligenceAgent(BaseAgent):
    name = "KeywordIntelligenceAgent"
    def run(self, context: AgentContext) -> dict:
        kws = [
            {"term": "best service near me", "match_type": "phrase", "intent": "commercial", "score": 0.89},
            {"term": "buy service online", "match_type": "exact", "intent": "transactional", "score": 0.93},
        ]
        return {"keywords": kws}


class SearchIntentAgent(BaseAgent):
    name = "SearchIntentAgent"
    def run(self, context: AgentContext) -> dict:
        return {"intent_map": {"best service near me": "commercial", "buy service online": "transactional"}}


class AdCreativeAgent(BaseAgent):
    name = "AdCreativeAgent"
    def run(self, context: AgentContext) -> dict:
        return {"ads": [{"ad_type": "Responsive Search Ads", "headline": "Grow Faster with ApexAds", "description": "AI-built campaigns that optimize every day."}]}


class LandingPageAnalyzerAgent(BaseAgent):
    name = "LandingPageAnalyzerAgent"
    def run(self, context: AgentContext) -> dict:
        return {"landing_page_feedback": ["improve CTA prominence", "add trust badges"]}


class CampaignBuilderAgent(BaseAgent):
    name = "CampaignBuilderAgent"
    def run(self, context: AgentContext) -> dict:
        return {"campaign_structure": {"types": ["Search", "Performance Max"], "ad_groups": ["Core", "Competitor"]}}


class DeploymentAgent(BaseAgent):
    name = "DeploymentAgent"
    def run(self, context: AgentContext) -> dict:
        return {"deployment": "ready"}


class AnalyticsAgent(BaseAgent):
    name = "AnalyticsAgent"
    def run(self, context: AgentContext) -> dict:
        return {"metrics": {"impressions": 1000, "clicks": 120, "conversions": 15, "spend": 240.0}}


class OptimizationAgent(BaseAgent):
    name = "OptimizationAgent"
    def run(self, context: AgentContext) -> dict:
        return {"optimizations": ["keyword pruning", "bid adjustments", "budget redistribution"]}


class BudgetAllocatorAgent(BaseAgent):
    name = "BudgetAllocatorAgent"
    def run(self, context: AgentContext) -> dict:
        return {"budget_plan": {"search": 0.5, "pmax": 0.35, "display": 0.15}}


class BiddingStrategyAgent(BaseAgent):
    name = "BiddingStrategyAgent"
    def run(self, context: AgentContext) -> dict:
        return {"bid_strategy": "target_roas" if context.target_roas else "maximize_conversions"}


class AudienceTargetingAgent(BaseAgent):
    name = "AudienceTargetingAgent"
    def run(self, context: AgentContext) -> dict:
        return {"audiences": ["custom", "in-market", "remarketing"]}


class GeoTargetingAgent(BaseAgent):
    name = "GeoTargetingAgent"
    def run(self, context: AgentContext) -> dict:
        return {"geo": {"country": context.location, "radius_targeting": "20km"}}


class SchedulingAgent(BaseAgent):
    name = "SchedulingAgent"
    def run(self, context: AgentContext) -> dict:
        return {"schedule": {"days": ["Mon", "Tue", "Wed", "Thu", "Fri"], "hours": "08:00-20:00"}}


class CreativeTestingAgent(BaseAgent):
    name = "CreativeTestingAgent"
    def run(self, context: AgentContext) -> dict:
        return {"ab_tests": ["headline_variant_A_vs_B", "cta_variant_A_vs_B"]}


class PolicyComplianceAgent(BaseAgent):
    name = "PolicyComplianceAgent"
    def run(self, context: AgentContext) -> dict:
        return {"policy_status": "compliant", "checks": ["editorial", "trademark", "restricted_content"]}


class LearningEngineAgent(BaseAgent):
    name = "LearningEngineAgent"
    def run(self, context: AgentContext) -> dict:
        return {"learning_feedback": "models updated with latest campaign performance"}
