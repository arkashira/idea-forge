import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class MarketSummary:
    market_size_estimate: int
    competitive_density: int

class IdeaForge:
    def __init__(self, knowledge_base: Dict):
        self.knowledge_base = knowledge_base

    def get_market_summary(self, idea: str) -> MarketSummary:
        if idea not in self.knowledge_base:
            raise ValueError(f"Idea '{idea}' not found in knowledge base")

        data = self.knowledge_base[idea]
        market_size_estimate = data.get("market_size_estimate", 0)
        competitive_density = data.get("competitive_density", 0)

        return MarketSummary(market_size_estimate, competitive_density)

    def get_ideas(self) -> Dict:
        return self.knowledge_base
