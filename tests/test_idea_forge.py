import pytest
from idea_forge import IdeaEngine, Idea


@pytest.fixture
def engine():
    return IdeaEngine()


def test_generate_ideas_happy_path(engine):
    prompt = "budget travel"
    user_id = "user123"
    ideas = engine.generate_ideas(prompt, user_id, count=6)

    # Must return exactly the requested (clamped) number of ideas
    assert len(ideas) == 6

    # Each idea must be an Idea instance with non‑empty fields
    for idea in ideas:
        assert isinstance(idea, Idea)
        assert isinstance(idea.description, str) and idea.description
        assert isinstance(idea.market, str) and idea.market

    # Ensure the prompt appears in each description (case‑insensitive)
    for idea in ideas:
        assert "budget travel" in idea.description.lower()


def test_ideas_are_stored_in_session(engine):
    prompt = "remote team building"
    user_id = "alice"
    generated = engine.generate_ideas(prompt, user_id, count=5)
    stored = engine.get_ideas(user_id)

    # Stored list should be equal (order preserved)
    assert stored == generated

    # Retrieving for unknown user yields empty list
    assert engine.get_ideas("unknown_user") == []


def test_generate_ideas_clamps_count(engine):
    prompt = "AI art"
    user_id = "bob"

    # Request too few
    few = engine.generate_ideas(prompt, user_id, count=2)
    assert len(few) == 5  # clamped up

    # Request too many
    many = engine.generate_ideas(prompt, user_id, count=20)
    assert len(many) == 10  # clamped down


def test_generate_ideas_empty_prompt_raises(engine):
    with pytest.raises(ValueError) as exc:
        engine.generate_ideas("", "userX")
    assert "Prompt must be a non‑empty string" in str(exc.value)


def test_generate_ideas_empty_user_id_raises(engine):
    with pytest.raises(ValueError) as exc:
        engine.generate_ideas("some prompt", "   ")
    assert "User ID must be a non‑empty string" in str(exc.value)


def test_generate_ideas_is_deterministic_for_same_input(engine):
    prompt = "personal finance"
    user_id = "charlie"

    first = engine.generate_ideas(prompt, user_id, count=7)
    second = engine.generate_ideas(prompt, user_id, count=7)

    # Because we overwrite the session each call, the returned lists should be identical
    assert first == second
