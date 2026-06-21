import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class UserPreferences:
    interests: List[str]
    preferences: Dict[str, str]

class OnboardingWizard:
    def __init__(self):
        self.user_preferences = None

    def step1_interests(self, interests: List[str]) -> None:
        self.user_preferences = UserPreferences(interests=interests, preferences={})

    def step2_preferences(self, preferences: Dict[str, str]) -> None:
        if self.user_preferences:
            self.user_preferences.preferences = preferences
        else:
            raise ValueError("Step 1 not completed")

    def step3_first_idea(self, idea: str) -> str:
        if self.user_preferences:
            return f"First idea: {idea} for {self.user_preferences.interests[0]}"
        else:
            raise ValueError("Step 1 not completed")

    def save_preferences(self) -> None:
        if self.user_preferences:
            with open("user_preferences.json", "w") as f:
                json.dump({
                    "interests": self.user_preferences.interests,
                    "preferences": self.user_preferences.preferences
                }, f)

    def load_preferences(self) -> None:
        try:
            with open("user_preferences.json", "r") as f:
                data = json.load(f)
                self.user_preferences = UserPreferences(interests=data["interests"], preferences=data["preferences"])
        except FileNotFoundError:
            pass

    def tooltips(self) -> List[str]:
        return [
            "Welcome to IdeaForge!",
            "Explore our features to get started."
        ]
