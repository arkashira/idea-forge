import pytest
from idea_forge import IdeaForge, MarketSummary

@pytest.fixture
def knowledge_base():
    return {
        "idea1": {"market_size_estimate": 100, "competitive_density": 5},
        "idea2": {"market_size_estimate": 200, "competitive_density": 8},
    }

def test_get_market_summary(knowledge_base):
    idea_forge = IdeaForge(knowledge_base)
    market_summary = idea_forge.get_market_summary("idea1")
    assert market_summary.market_size_estimate == 100
    assert market_summary.competitive_density == 5

def test_get_market_summary_not_found(knowledge_base):
    idea_forge = IdeaForge(knowledge_base)
    with pytest.raises(ValueError):
        idea_forge.get_market_summary("nonexistent_idea")

def test_get_ideas(knowledge_base):
    idea_forge = IdeaForge(knowledge_base)
    ideas = idea_forge.get_ideas()
    assert len(ideas) == 2
    assert "idea1" in ideas
    assert "idea2" in ideas
