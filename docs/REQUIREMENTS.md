# REQUIREMENTS.md

## Project: idea‑forge  
**Repository:** `arkashira/idea-forge`  
**Owner:** Axentx  
**Purpose:** An AI‑powered ideation platform that assists indie hackers and creators in generating, refining, and validating software product ideas.

---

## 1. Functional Requirements

| ID | Description | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR‑1** | **Idea Generation** | Must | • User can input a seed keyword or phrase.<br>• System returns ≥ 5 unique, high‑level software idea concepts within 2 s.<br>• Each idea includes a short title, description, and estimated market size. |
| **FR‑2** | **Idea Refinement** | Must | • User selects an idea and can request deeper details (features, target personas, pain points).<br>• System expands the idea into a 1‑page PRD outline within 3 s. |
| **FR‑3** | **Market Validation** | Must | • System queries public data sources (e.g., Crunchbase, Product Hunt, Reddit) to fetch metrics: active users, funding, competitor count.<br>• Validation score (0‑100) displayed; threshold ≥ 70 considered “validated”. |
| **FR‑4** | **Idea Ranking** | Should | • User can rank ideas by custom criteria (e.g., feasibility, revenue potential).<br>• System re‑orders list accordingly. |
| **FR‑5** | **Export & Collaboration** | Should | • Export PRD outline to Markdown, PDF, or CSV.<br>• Shareable link with read‑only view. |
| **FR‑6** | **User Authentication** | Must | • OAuth2 via GitHub or Google.<br>• Session timeout after 30 min inactivity. |
| **FR‑7** | **API Access** | Should | • RESTful endpoint `/ideas` for programmatic generation.<br>• Rate limit: 60 req/min per user. |
| **FR‑8** | **Admin Dashboard** | Should | • View usage analytics, user growth, and validation success rate. |
| **FR‑9** | **Data Privacy** | Must | • User data stored encrypted at rest (AES‑256).<br>• GDPR & CCPA compliance. |
| **FR‑10** | **Logging & Monitoring** | Must | • Log all requests with user ID, timestamp, latency.<br>• Alert on > 5 s latency or > 1 % error rate. |

---

## 2. Non‑Functional Requirements

| Category | Requirement | Target |
|----------|-------------|--------|
| **Performance** | Average response time for FR‑1 & FR‑2 ≤ 2 s (95th percentile). | 2 s |
| **Scalability** | Handle 10 k concurrent users without degradation. | 10 k |
| **Reliability** | 99.9 % uptime SLA. | 99.9 % |
| **Security** | OWASP Top‑10 mitigations, OWASP ASVS Level 2. | ASVS 2 |
| **Compliance** | GDPR, CCPA, ISO 27001 (baseline). | ISO 27001 |
| **Maintainability** | Code coverage ≥ 85 % for core modules. | 85 % |
| **Extensibility** | Plug‑in architecture for new data sources (e.g., Kaggle, StackOverflow). | Yes |
| **Usability** | Mobile‑first responsive UI; WCAG 2.1 AA compliance. | AA |

---

## 3. Constraints

1. **Data Sources** – Only publicly available APIs (Crunchbase API v3, Product Hunt API, Reddit API) may be used; no paid data feeds.
2. **AI Model** – Must use an open‑source LLM (e.g., `vllm` or `sglang`) hosted on internal GPU clusters; no external cloud inference.
3. **Budget** – Total dev cost ≤ $120 k for MVP; infrastructure cost ≤ $5 k/month.
4. **Timeline** – MVP release in 12 weeks from project kickoff.
5. **Legal** – All user‑generated content owned by the user; platform retains non‑exclusive license for analytics.

---

## 4. Assumptions

- Users have a stable internet connection and a modern browser (Chrome/Edge/Firefox).
- External APIs remain available and do not change endpoints during the project.
- The LLM inference engine can be scaled horizontally with minimal code changes.
- GDPR/CCPA compliance can be achieved with the chosen hosting provider (AWS GovCloud or EU‑centric region).

---

## 5. Deliverables

1. **Backend** – REST API, AI inference layer, data ingestion pipelines.  
2. **Frontend** – React SPA with responsive design.  
3. **Documentation** – API spec (OpenAPI), developer guide, user manual.  
4. **CI/CD** – Automated tests, linting, Docker images, Kubernetes deployment manifests.  
5. **Monitoring** – Prometheus + Grafana dashboards, alert rules.  

---

## 6. Acceptance Criteria Summary

- All functional requirements pass automated tests and manual QA.  
- Performance benchmarks met under simulated load.  
- Security audit shows no critical vulnerabilities.  
- Compliance documentation signed off by legal.  
- MVP demo delivered to stakeholders within 12 weeks.

---
