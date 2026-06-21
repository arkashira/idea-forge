# Idea Forge

A minimal Python library that turns a short founder prompt into a list of fresh software ideas.
Each idea includes a one‑sentence description and a suggested target market, and the ideas are
kept in an in‑memory session for later retrieval.

## Features

- Generate 5‑10 ideas instantly (well under the 3‑second requirement).
- Deterministic output for the same `(prompt, user_id)` pair.
- Simple in‑memory session storage (`user_id` → list of ideas).

## Installation
