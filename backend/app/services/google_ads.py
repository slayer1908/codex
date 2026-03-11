from uuid import uuid4


class GoogleAdsService:
    supported_campaign_types = [
        "Search",
        "Display",
        "Performance Max",
        "Shopping",
        "Video",
        "Demand Gen",
        "App",
        "Local",
    ]

    supported_bidding_strategies = [
        "manual CPC",
        "enhanced CPC",
        "maximize clicks",
        "maximize conversions",
        "target CPA",
        "target ROAS",
        "maximize conversion value",
        "target impression share",
    ]

    def deploy_campaign(self, payload: dict) -> dict:
        return {"external_id": f"gads-{uuid4()}", "status": "deployed", "payload": payload}
