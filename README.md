# ApexAds Autonomous AI Marketing OS

ApexAds is a multi-agent autonomous marketing platform that analyzes a business website and automatically creates, deploys, and optimizes Google Ads campaigns.

## Core capabilities
- Website intelligence and business/audience profiling
- Market + competitor research
- Keyword strategy and search intent mapping
- Ad creative generation
- Campaign structure building and deployment
- Continuous analytics, optimization, and ML feedback loops

## Agent pipeline
User Input → Website Analysis → Market Research → Keyword Intelligence → Campaign Strategy → Ad Creation → Campaign Construction → Campaign Deployment → Performance Monitoring → Optimization Loop → Machine Learning Feedback

## Agents implemented
1. PlannerAgent
2. WebsiteIntelligenceAgent
3. MarketResearchAgent
4. CompetitorAnalyzerAgent
5. KeywordIntelligenceAgent
6. SearchIntentAgent
7. AdCreativeAgent
8. LandingPageAnalyzerAgent
9. CampaignBuilderAgent
10. DeploymentAgent
11. AnalyticsAgent
12. OptimizationAgent
13. BudgetAllocatorAgent
14. BiddingStrategyAgent
15. AudienceTargetingAgent
16. GeoTargetingAgent
17. SchedulingAgent
18. CreativeTestingAgent
19. PolicyComplianceAgent
20. LearningEngineAgent

## API endpoints
- `POST /analyze-website`
- `POST /generate-keywords`
- `POST /generate-ads`
- `POST /build-campaign`
- `POST /deploy-campaign`
- `GET /get-analytics`
- `POST /run-optimization`

## Run with Docker
```bash
docker compose up --build
```

Backend: http://localhost:8000/docs
Frontend: http://localhost:3000

## Stack
- Backend: Python, FastAPI, SQLAlchemy
- AI: OpenAI API integrations (extensible)
- ML: PyTorch predictive + reinforcement loop skeleton
- Data: PostgreSQL + Pinecone vector index
- Queue: Redis + Celery
- Frontend: Next.js + React + Tailwind-ready scaffolding
- Infra: Docker, Kubernetes, AWS Terraform stub

## Notes
This repository includes production-oriented scaffolding with explicit extension points for deeper Google Ads API integration, OpenAI tool-calling flows, and robust ML training pipelines.
