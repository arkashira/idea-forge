```markdown
# user-stories.md

## Epic 1 – Idea Generation & Inspiration
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 1 | **As an indie hacker, I want to input a niche keyword, so that the tool suggests 5 fresh software ideas relevant to that niche.** | • Tool accepts a single keyword or short phrase.<br>• Returns exactly 5 distinct idea titles.<br>• Each idea includes a one‑sentence description.<br>• Ideas are ranked by novelty score (0‑100). | M |
| 2 | **As a creator, I want the tool to auto‑generate a 3‑sentence pitch for each idea, so that I can quickly share it on social media.** | • Pitch is no longer than 3 sentences.<br>• Pitch contains the idea title, target audience, and unique value proposition.<br>• Pitches are grammatically correct and plagiarism‑free. | S |
| 3 | **As a product founder, I want the tool to flag ideas that overlap with existing Axentx products, so that I avoid duplication.** | • System cross‑checks idea titles against the shared knowledge base.<br>• Flags any idea with >70% similarity to an existing product.<br>• Provides a brief similarity report. | M |
| 4 | **As a solo entrepreneur, I want to save my favorite ideas to a personal “Idea Vault”, so that I can revisit them later.** | • User can click “Save” on any idea.<br>• Saved ideas appear in a dedicated tab.<br>• Vault persists across sessions (local storage or backend). | S |

## Epic 2 – Idea Validation & Market Fit
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 5 | **As a startup founder, I want the tool to estimate TAM/SAM/SOM for each idea, so that I can prioritize high‑potential opportunities.** | • Tool outputs TAM, SAM, SOM in USD.<br>• Estimates are derived from publicly available market reports.<br>• Provides a confidence score (0‑1). | L |
| 6 | **As a product manager, I want to run a quick survey generator for each idea, so that I can gauge real user interest.** | • Survey contains 5 multiple‑choice questions.<br>• Survey can be shared via a unique link.<br>• Results are displayed in a simple bar chart. | M |
| 7 | **As a founder, I want the tool to simulate a landing page for each idea, so that I can run A/B tests on copy.** | • Generates two headline variants.<br>• Generates two CTA variants.<br>• Tracks click‑through rate (mocked). | L |
| 8 | **As a solo creator, I want the tool to suggest potential monetization models (subscription, freemium, one‑time), so that I can plan revenue streams.** | • Suggests 3 monetization options.<br>• Provides a brief pros/cons list for each.<br>• Options are tailored to the idea’s target market. | M |

## Epic 3 – Collaboration & Feedback Loop
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 9 | **As a team lead, I want to invite collaborators to review an idea, so that we can collectively refine it.** | • Invite link can be sent via email.<br>• Invitees can comment inline.<br>• Comments are stored and searchable. | M |
| 10 | **As a reviewer, I want to rate an idea on feasibility, uniqueness, and market fit, so that the team can prioritize.** | • Rating scale 1‑5 for each dimension.<br>• Average rating is displayed.<br>• Ratings are stored per idea. | S |
| 11 | **As a founder, I want the tool to automatically merge the highest‑rated ideas into a “Roadmap” view, so that I can plan releases.** | • Roadmap shows ideas sorted by composite score.<br>• Each idea has a status badge (Idea, Prototype, MVP).<br>• Roadmap can be exported as CSV. | L |
| 12 | **As a product strategist, I want the tool to learn from past validated ideas, so that future suggestions improve over time.** | • System tracks validation outcomes (e.g., survey response rate).<br>• Uses outcomes to adjust novelty scoring.<br>• Learning loop runs nightly. | L |

## Epic 4 – Personalization & Accessibility (Optional)
| # | User Story | Acceptance Criteria | Complexity |
|---|------------|---------------------|------------|
| 13 | **As a non‑technical founder, I want the tool to provide a “no‑code” prototype wizard, so that I can quickly build a demo.** | • Wizard guides through UI layout, data fields, and basic logic.<br>• Generates a deployable static site.<br>• No coding required. | L |
| 14 | **As a visually impaired user, I want the tool to support screen‑reader navigation, so that I can use it independently.** | • All UI elements have ARIA labels.<br>• Keyboard navigation is fully functional.<br>• Voice‑over reads all content. | M |
```
```