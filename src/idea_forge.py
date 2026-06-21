import random
import re
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Idea:
    """A single software idea."""
    description: str
    market: str


class IdeaEngine:
    """
    Generates short software ideas based on a user prompt and stores them per user session.
    """

    # A small pool of generic idea templates. `{prompt}` will be replaced with the user prompt.
    _TEMPLATE_POOL = [
        ("A mobile app that helps {prompt} enthusiasts track their progress.", "Fitness & Hobbyists"),
        ("A SaaS dashboard for {prompt} analytics in small businesses.", "SMBs"),
        ("A browser extension that suggests {prompt} improvements while you browse.", "Productivity"),
        ("An AI‑assisted tool that automates {prompt} reporting.", "Enterprise"),
        ("A community platform for sharing {prompt} tips and tricks.", "Online Communities"),
        ("A marketplace connecting freelancers with {prompt} projects.", "Freelance Economy"),
        ("A gamified learning app focused on {prompt} skills.", "Education"),
        ("A privacy‑first service that encrypts {prompt} data.", "Security"),
        ("A low‑code builder for creating {prompt} workflows.", "Developers"),
        ("A subscription box delivering {prompt} resources monthly.", "Consumer Goods"),
    ]

    def __init__(self) -> None:
        # Session storage: user_id -> list of Idea objects
        self._session: Dict[str, List[Idea]] = {}

    def generate_ideas(self, prompt: str, user_id: str, count: int = 7) -> List[Idea]:
        """
        Generate between 5 and 10 ideas based on the prompt and store them for the user.

        Args:
            prompt: Short user prompt describing a domain or interest.
            user_id: Identifier for the user session.
            count: Desired number of ideas (clamped to 5‑10).

        Returns:
            List of generated Idea objects.

        Raises:
            ValueError: If prompt or user_id is empty/whitespace.
        """
        if not prompt or not prompt.strip():
            raise ValueError("Prompt must be a non‑empty string.")
        if not user_id or not user_id.strip():
            raise ValueError("User ID must be a non‑empty string.")

        # Clamp count to allowed range
        count = max(5, min(10, count))

        # Prepare a deterministic random seed based on prompt+user_id for reproducibility
        seed_input = f"{prompt}:{user_id}"
        seed = sum(ord(c) for c in seed_input)
        rng = random.Random(seed)

        # Choose unique templates
        chosen_templates = rng.sample(self._TEMPLATE_POOL, count)

        ideas: List[Idea] = []
        for desc_template, market in chosen_templates:
            # Simple placeholder substitution; also clean up extra whitespace
            description = desc_template.format(prompt=prompt.strip())
            description = re.sub(r"\s+", " ", description).strip()
            ideas.append(Idea(description=description, market=market))

        # Store in session (overwrite previous ideas for this user)
        self._session[user_id] = ideas
        return ideas

    def get_ideas(self, user_id: str) -> List[Idea]:
        """
        Retrieve stored ideas for a given user.

        Args:
            user_id: Identifier for the user session.

        Returns:
            List of Idea objects previously generated for the user,
            or an empty list if none exist.
        """
        return list(self._session.get(user_id, []))
