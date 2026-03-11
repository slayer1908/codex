from dataclasses import dataclass
from typing import Any


@dataclass
class AgentContext:
    website_url: str
    location: str
    monthly_budget: float
    target_cpa: float | None
    target_roas: float | None
    memory: dict[str, Any]


class BaseAgent:
    name = "BaseAgent"

    def run(self, context: AgentContext) -> dict[str, Any]:
        raise NotImplementedError
