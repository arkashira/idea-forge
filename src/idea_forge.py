import argparse
import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Idea:
    idea: str
    validation_score: float
    status: str

def generate_idea(prompt: str) -> str:
    # Mocked LLM response for demonstration purposes
    return f"Idea generated from prompt: {prompt}"

def validate_idea(idea: str) -> float:
    # Simple heuristic: idea length / 100
    return len(idea) / 100

def main() -> None:
    parser = argparse.ArgumentParser(description="Idea Forge CLI")
    parser.add_argument("prompt", type=str, help="Prompt for idea generation")
    args = parser.parse_args()

    idea = generate_idea(args.prompt)
    validation_score = validate_idea(idea)

    result = Idea(idea, validation_score, "success")
    print(json.dumps(result.__dict__))

if __name__ == "__main__":
    main()
