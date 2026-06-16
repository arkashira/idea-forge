# Roadmap – idea‑forge

> **Audience** – Product, Engineering, Design, QA, Ops  
> **Goal** – Deliver a launch‑ready MVP that validates the core value proposition, then iterate through two major release phases that expand the product’s capabilities and market reach.

---

## 1. MVP – “Idea Spark” (Launch 2026‑07‑31)

| # | Feature | Owner | Acceptance Criteria | Notes |
|---|---------|-------|---------------------|-------|
| 1 | **Idea Generation Engine** | AI‑Engineering | • Generates 3–5 unique software ideas per prompt.<br>• Uses a fine‑tuned LLM (vLLM) on the `auto` + `instr‑resp` datasets.<br>• Latency < 2 s per request. | Must be built on the existing vLLM inference stack. |
| 2 | **Idea Validation Checklist** | Product | • Checklist of 5 validation questions (market size, pain, willingness‑to‑pay, competition, technical feasibility).<br>• Auto‑filling of answers based on public data APIs. | Leverage existing data‑access layer. |
| 3 | **User Dashboard** | Front‑end | • Single‑page app (React) showing current ideas, validation status, and next steps.<br>• Responsive design. | Use existing UI component library. |
| 4 | **Auth & Onboarding** | Backend | • Email/password + OAuth (Google).<br>• Simple onboarding wizard that captures user role and interests. | Reuse company auth service. |
| 5 | **Data Persistence** | Database | • Store ideas, validation results, and user profiles in PostgreSQL.<br>• Backup strategy in place. | Align with company data schema. |
| 6 | **CI/CD Pipeline** | DevOps | • Automated tests, linting, and deployment to staging.<br>• Blue‑green deploy to production. | Use GitHub Actions + Docker. |
| 7 | **Analytics & Metrics** | Data | • Track idea generation count, validation completion rate, and user retention.<br>• Exportable CSV. | Hook into existing analytics platform. |

> **MVP‑Critical**: Items 1‑4.  
> **Non‑critical for launch**: 5‑7 (will be fully implemented but not required for first release).

---

## 2. Phase 1 – “Idea Accelerator” (2026‑10‑15)

### Theme: Deepen Validation & Community

| # | Feature | Owner | Acceptance Criteria |
|---|---------|-------|---------------------|
| 1 | **Market Research Integration** | AI‑Engineering | • Pull real‑time market data (Crunchbase, AngelList) into validation checklist.<br>• Show market size estimates. |
| 2 | **Competitive Landscape Analyzer** | Product | • Auto‑generate competitor list and SWOT summary.<br>• Highlight gaps. |
| 3 | **Community Idea Voting** | Front‑end | • Public idea feed with upvotes/downvotes.<br>• Filter by category. |
| 4 | **Idea Collaboration** | Backend | • Shared idea workspaces with comment threads.<br>• Real‑time updates via WebSocket. |
| 5 | **Export & Share** | Front‑end | • Export idea package (PDF, Markdown) with validation data.<br>• Share via link. |
| 6 | **Beta Feedback Loop** | QA | • Capture user feedback via in‑app survey.<br>• Prioritize bugs. |

> **Key Deliverable**: First community‑driven idea marketplace.

---

## 3. Phase 2 – “Idea to Product” (2027‑01‑31)

### Theme: Turn Ideas into Executable Projects

| # | Feature | Owner | Acceptance Criteria |
|---|---------|-------|---------------------|
| 1 | **Project Blueprint Generator** | AI‑Engineering | • Generates a high‑level project plan (milestones, tech stack, estimated effort). |
| 2 | **Roadmap Integration** | Product | • Sync blueprint with external tools (Jira, Trello). |
| 3 | **Prototype Builder** | Front‑end | • Low‑code UI builder for quick MVPs.<br>• Drag‑and‑drop components. |
| 4 | **Funding & Pitch Deck Generator** | AI‑Engineering | • Auto‑create pitch deck slides from idea data. |
| 5 | **Monetization Insights** | Data | • Suggest pricing models and revenue projections. |
| 6 | **Enterprise Tier** | Business | • Tiered subscription with advanced analytics, API access, and priority support. |

> **Strategic Goal**: Enable users to move from ideation to a working prototype within 4 weeks.

---

## 4. Continuous Improvement (Ongoing)

| Activity | Frequency | Owner |
|----------|-----------|-------|
| **Model Retraining** | Monthly | AI‑Engineering |
| **Feature Usage Analysis** | Weekly | Data |
| **Security Audits** | Quarterly | DevOps |
| **UX Refresh** | Bi‑annual | Design |

---

## 5. Success Metrics

| Metric | Target (MVP) | Target (Phase 1) | Target (Phase 2) |
|--------|--------------|------------------|------------------|
| Monthly Active Users | 5 k | 15 k | 40 k |
| Idea Validation Completion Rate | 70 % | 85 % | 95 % |
| Community Engagement (votes/comments) | 1 k | 5 k | 15 k |
| Revenue (subscription) | $0 | $10 k | $50 k |

---

## 6. Dependencies & Risks

| Dependency | Owner | Mitigation |
|------------|-------|------------|
| vLLM inference latency | AI‑Engineering | Optimize batch size, use GPU nodes |
| External data APIs | Product | Cache results, fallback to static data |
| Auth service uptime | DevOps | Multi‑region deployment |
| Data privacy compliance | Legal | Regular audits, GDPR/CCPA checks |

---

## 7. Release Cadence

| Release | Date | Scope |
|---------|------|-------|
| MVP | 2026‑07‑31 | Core idea generation & validation |
| v1.0 | 2026‑10‑15 | Community & advanced validation |
| v2.0 | 2027‑01‑31 | Project blueprint & prototype tools |

---

**Prepared by:**  
Senior Product & Engineering Lead – idea‑forge  
*Axentx, 2026‑06‑16*
