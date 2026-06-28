```markdown
# partner-targets.md

## Partner Integration Roadmap – Idea‑Forge

| # | Partner | API / SDK | Free‑Tier Limits | Integration Effort | Value‑Add (User Job) | Revenue Model | Priority |
|---|---------|-----------|------------------|--------------------|----------------------|---------------|----------|
| 1 | **Product Hunt API** | Public REST endpoints for listings, tags, and votes | 10 k requests/month, 1 k listings | **S** | *Validate idea traction*: auto‑fetch trending categories & user feedback to surface high‑potential niches. | Affiliate (click‑through) | **A** |
| 2 | **Crunchbase API** | Company & funding data | 10 k requests/month, 1 k companies | **M** | *Market sizing*: pull TAM/SAM/SOM, competitor funding, and team size to quantify opportunity. | Revenue‑share (lead‑based) | **A** |
| 3 | **Google Trends API (via pytrends)** | Keyword interest over time | 1 k queries/day | **S** | *Demand validation*: surface rising search terms for idea refinement. | None (free) | **B** |
| 4 | **Typeform API** | Form creation & response retrieval | 1 k responses/month | **S** | *User validation*: embed quick polls to gauge pain points and willingness‑to‑pay. | Affiliate (form‑hosting fee) | **A** |
| 5 | **Stripe API** | Payment processing & subscriptions | Unlimited (free tier) | **M** | *Monetization*: enable in‑app purchases of premium idea packs or consulting. | Transaction fee (2.9%+30¢) | **C** |
| 6 | **Zapier Platform** | Connectors to 3 k+ apps | Unlimited (free tier) | **L** | *Automation*: let users trigger idea‑forge outputs into their own workflows (e.g., Trello, Notion). | Subscription (Zapier) | **B** |
| 7 | **OpenAI API** | GPT‑4 / embeddings | 20 k tokens/month | **M** | *Core AI engine*: generate ideas, summaries, and market analysis. | Usage‑based (per token) | **A** |
| 8 | **Slack API** | Bot & message posting | 1 k messages/day | **S** | *Collaboration*: share ideas in real‑time with team channels. | None (free) | **C** |

### Integration Effort Notes
- **S (Small)**: RESTful endpoints, minimal auth, 1–2 days of work.
- **M (Medium)**: Requires OAuth flows or SDK integration, ~1 week.
- **L (Large)**: Complex event streams or multi‑step workflows, ~2–3 weeks.

### Revenue‑Share / Affiliate Opportunities
- **Product Hunt**: 5% click‑through commission on traffic driven to listings.
- **Crunchbase**: 10% of leads that convert to paid Idea‑Forge accounts.
- **Typeform**: 15% of paid form plans used via our integration.
- **Zapier**: 20% of subscription revenue for each user who activates our Zap.

### Roadmap Timeline (Quarterly)
| Quarter | Focus | Deliverables |
|---------|-------|--------------|
| Q1 2027 | Core AI + OpenAI, Product Hunt, Google Trends | Idea generation + trend validation |
| Q2 2027 | Crunchbase, Typeform, Stripe | Market sizing + user validation + payment |
| Q3 2027 | Slack, Zapier | Collaboration + workflow automation |
| Q4 2027 | Polish, analytics, revenue‑share optimization | Scale & partner revenue optimization |

--- 

**Next Steps**  
1. Prioritize signing data‑sharing agreements with Product Hunt & Crunchbase.  
2. Build a modular integration layer to plug APIs with minimal friction.  
3. Launch a beta with Product Hunt & Google Trends to validate the revenue‑share model.  
4. Iterate on user feedback and expand to remaining partners.