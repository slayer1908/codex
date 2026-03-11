from app.agents.base import AgentContext
from app.agents.marketing_agents import (
    AdCreativeAgent,
    AnalyticsAgent,
    AudienceTargetingAgent,
    BiddingStrategyAgent,
    BudgetAllocatorAgent,
    CampaignBuilderAgent,
    CompetitorAnalyzerAgent,
    CreativeTestingAgent,
    DeploymentAgent,
    GeoTargetingAgent,
    KeywordIntelligenceAgent,
    LandingPageAnalyzerAgent,
    LearningEngineAgent,
    MarketResearchAgent,
    OptimizationAgent,
    PlannerAgent,
    PolicyComplianceAgent,
    SchedulingAgent,
    SearchIntentAgent,
    WebsiteIntelligenceAgent,
)


class AgentOrchestrator:
    def __init__(self) -> None:
        self.pipeline = [
            PlannerAgent(),
            WebsiteIntelligenceAgent(),
            MarketResearchAgent(),
            CompetitorAnalyzerAgent(),
            KeywordIntelligenceAgent(),
            SearchIntentAgent(),
            AudienceTargetingAgent(),
            GeoTargetingAgent(),
            BudgetAllocatorAgent(),
            BiddingStrategyAgent(),
            AdCreativeAgent(),
            LandingPageAnalyzerAgent(),
            CampaignBuilderAgent(),
            SchedulingAgent(),
            CreativeTestingAgent(),
            PolicyComplianceAgent(),
            DeploymentAgent(),
            AnalyticsAgent(),
            OptimizationAgent(),
            LearningEngineAgent(),
        ]

    def run(self, context: AgentContext) -> dict:
        output: dict = {"pipeline": []}
        for agent in self.pipeline:
            result = agent.run(context)
            context.memory[agent.name] = result
            output[agent.name] = result
            output["pipeline"].append(agent.name)
        return output
