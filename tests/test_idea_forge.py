import json
from idea_forge import generate_idea, validate_idea, Idea

def test_generate_idea():
    prompt = "Test prompt"
    idea = generate_idea(prompt)
    assert idea.startswith("Idea generated from prompt: ")

def test_validate_idea():
    idea = "Test idea"
    validation_score = validate_idea(idea)
    assert 0 <= validation_score <= 1

def test_main():
    # Mock argparse
    class MockArgs:
        def __init__(self, prompt):
            self.prompt = prompt

    # Test with a prompt
    args = MockArgs("Test prompt")
    idea = generate_idea(args.prompt)
    validation_score = validate_idea(idea)
    result = Idea(idea, validation_score, "success")
    assert result.idea == idea
    assert 0 <= result.validation_score <= 1
    assert result.status == "success"

    # Test with an empty prompt
    args = MockArgs("")
    idea = generate_idea(args.prompt)
    validation_score = validate_idea(idea)
    result = Idea(idea, validation_score, "success")
    assert result.idea == idea
    assert 0 <= result.validation_score <= 1
    assert result.status == "success"
