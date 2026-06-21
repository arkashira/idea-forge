import pytest
from onboarding import OnboardingWizard, UserPreferences

def test_onboarding_wizard():
    wizard = OnboardingWizard()
    wizard.step1_interests(["tech", "innovation"])
    wizard.step2_preferences({"lang": "python", "editor": "vscode"})
    assert wizard.step3_first_idea("AI") == "First idea: AI for tech"

def test_save_and_load_preferences():
    wizard = OnboardingWizard()
    wizard.step1_interests(["tech", "innovation"])
    wizard.step2_preferences({"lang": "python", "editor": "vscode"})
    wizard.save_preferences()
    wizard.load_preferences()
    assert wizard.user_preferences.interests == ["tech", "innovation"]
    assert wizard.user_preferences.preferences == {"lang": "python", "editor": "vscode"}

def test_tooltips():
    wizard = OnboardingWizard()
    assert wizard.tooltips() == [
        "Welcome to IdeaForge!",
        "Explore our features to get started."
    ]

def test_step2_without_step1():
    wizard = OnboardingWizard()
    with pytest.raises(ValueError):
        wizard.step2_preferences({"lang": "python", "editor": "vscode"})

def test_step3_without_step1():
    wizard = OnboardingWizard()
    with pytest.raises(ValueError):
        wizard.step3_first_idea("AI")
