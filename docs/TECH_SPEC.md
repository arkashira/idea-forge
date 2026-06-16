# TECH_SPEC.md – Idea‑Forge

---

## 1. Overview

**Idea‑Forge** is an AI‑powered ideation platform that assists indie hackers, creators, and product teams in generating, refining, and validating software ideas. The system combines large‑scale language models, structured data pipelines, and a lightweight web UI to deliver a seamless ideation workflow.

The project is built on the **Axentx** autonomous AI‑workforce stack, leveraging our shared knowledge base (pgvector), data‑driven pipelines, and self‑improving loops. The goal is to ship a production‑ready product that can be integrated into the existing Axentx portfolio without duplicating any previously released modules.

---

## 2. Architecture Overview

```
┌───────────────────────┐
│  Web Front‑End (React)│
└────────────┬──────────┘
             │ REST/GraphQL
┌────────────▼──────────┐
│  API Gateway (FastAPI)│
└────────────┬──────────┘
             │ gRPC
┌────────────▼──────────┐
│  Core Service (Python)│
│  ├─ Idea Generator     │
│  ├─ Idea Validator     │
│  ├─ Knowledge Fetcher  │
│  └─ Feedback Collector │
└────────────┬──────────┘
             │
┌────────────▼──────────┐
│  LLM Inference Layer   │
│  └─ vLLM (OpenAI‑style)│
└────────────┬──────────┘
             │
┌────────────▼──────────┐
│  Data Store (Postgres) │
│  ├─ pgvector (vector DB)│
│  └─ Relational tables   │
└───────────────────────┘
```

* **Front‑End** – React + Vite, TypeScript, TailwindCSS.  
* **API Gateway** – FastAPI, async, OpenAPI spec.  
* **Core Service** – Python 3.12, async/await, dependency injection.  
* **LLM Layer** – vLLM for low‑latency inference, GPU‑accelerated.  
* **Data Store** – PostgreSQL 16 + pgvector extension for semantic search.  
* **Deployment** – Docker Compose for dev, Kubernetes (Helm) for prod.  

---

## 3. Components

| Component | Responsibility | Key Libraries |
|-----------|----------------|---------------|
| **Idea Generator** | Generates raw idea candidates from prompts. | `vllm`, `pydantic`, `asyncio` |
| **Idea Validator** | Scores ideas against validation criteria (market size, pain, feasibility). | `scikit-learn`, `pandas`, `sqlalchemy` |
| **Knowledge Fetcher** | Retrieves relevant docs from the shared BRAIN (pgvector). | `psycopg2`, `pgvector`, `langchain` |
| **Feedback Collector** | Stores user feedback, triggers self‑improvement loops. | `sqlalchemy`, `celery` |
| **Auth & Session** | OAuth2 with Google / GitHub. | `fastapi-users`, `python-jose` |
| **Metrics & Logging** | Observability. | `prometheus-client`, `loguru` |

---

## 4. Data Model

### 4.1 Relational Tables

| Table | Columns | Notes |
|-------|---------|-------|
| `users` | `id`, `email`, `name`, `created_at` | PK: `id` UUID |
| `ideas` | `id`, `user_id`, `title`, `description`, `status`, `created_at`, `updated_at` | `status`: draft/validated/archived |
| `feedback` | `id`, `idea_id`, `user_id`, `rating`, `comment`, `created_at` | |
| `validation_scores` | `idea_id`, `metric`, `value`, `timestamp` | `metric`: market_size, pain_score, feasibility |

### 4.2 Vector Store

* **Table**: `documents`  
  * `doc_id`, `content`, `vector` (pgvector)  
  * Used for semantic search during validation.

* **Index**: `ivfflat` on `vector` for fast nearest‑neighbor queries.

---

## 5. Key APIs / Interfaces

### 5.1 REST Endpoints (FastAPI)

| Method | Path | Description | Request | Response |
|--------|------|-------------|---------|----------|
| POST | `/ideas/` | Create new idea | `{ "prompt": "..." }` | `{ "idea_id": "...", "status": "draft" }` |
| GET | `/ideas/{id}` | Retrieve idea | – | `{ "id": "...", "title": "...", "description": "...", ... }` |
| POST | `/ideas/{id}/validate` | Run validation pipeline | – | `{ "scores": { ... }, "status": "validated" }` |
| POST | `/ideas/{id}/feedback` | Submit feedback | `{ "rating": 4, "comment": "..." }` | `{ "ok": true }` |
| GET | `/search?query=...` | Semantic search in knowledge base | – | `[ { "doc_id": "...", "snippet": "..."} ]` |

### 5.2 gRPC Service (Core)

* `GenerateIdea(prompt: string) -> IdeaResponse`
* `ValidateIdea(idea_id: string) -> ValidationResponse`
* `CollectFeedback(feedback: Feedback) -> Ack`

---

## 6. Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Frontend** | React, TypeScript, Vite, TailwindCSS | Rapid UI prototyping, low bundle size |
| **API** | FastAPI (Python 3.12) | Async, auto‑docs, dependency injection |
| **LLM** | vLLM (vllm-project/vllm) | Production‑grade inference, GPU scaling |
| **Data** | PostgreSQL 16 + pgvector | Relational + vector search |
| **Background Jobs** | Celery + Redis | Feedback processing, retraining triggers |
| **Auth** | fastapi-users + OAuth2 | Secure, standard |
| **Observability** | Prometheus, Grafana, Loguru | Metrics, logs |
| **Containerization** | Docker, Docker Compose | Development consistency |
| **Orchestration** | Kubernetes + Helm | Production scaling |
| **CI/CD** | GitHub Actions | Automated tests, lint, build |

---

## 7. Dependencies

| Category | Package | Version |
|----------|---------|---------|
| **Python** | `fastapi` | `^0.111.0` |
| | `uvicorn` | `^0.30.0` |
| | `pydantic` | `^2.7.0` |
| | `vllm` | `^0.5.0` |
| | `psycopg2-binary` | `^2.9.9` |
| | `pgvector` | `^0.3.0` |
| | `langchain` | `^0.2.0` |
| | `scikit-learn` | `^1.5.0` |
| | `pandas` | `^2.2.0` |
| | `celery` | `^5.4.0` |
| | `redis` | `^5.0.0` |
| | `fastapi-users` | `^12.0.0` |
| | `python-jose` | `^3.3.0` |
| | `prometheus-client` | `^0.20.0` |
| | `loguru` | `^0.7.2` |
| **Node** | `react` | `^18.3.0` |
| | `typescript` | `^5.4.0` |
| | `vite` | `^5.0.0` |
| | `tailwindcss` | `^3.4.0` |

All dependencies are pinned to the latest stable releases at the time of writing.

---

## 8. Deployment

### 8.1 Development

```bash
docker compose up --build
```

* **Ports**  
  * API: `8000`  
  * Frontend: `5173`  
  * Postgres: `5432`  
  * Redis: `6379`

### 8.2 Production

1. **Helm Chart** – `charts/idea-forge`  
   * Deploy to Kubernetes cluster with GPU nodes for vLLM.  
   * Secrets stored in Vault (or K8s secrets).  
2. **Autoscaling** –  
   * Horizontal Pod Autoscaler on API and Core services.  
   * vLLM pods scale based on GPU queue length.  
3. **CI/CD** – GitHub Actions push to Docker registry, Helm upgrade.  
4. **Observability** – Prometheus scrape, Grafana dashboards, Loki for logs.

---

## 9. Security & Compliance

* OAuth2 with Google/GitHub for authentication.  
* HTTPS enforced via Ingress.  
* Rate limiting on API endpoints (`slowapi`).  
* GDPR‑friendly data handling: user data can be deleted via `/users/me`.  
* All secrets managed via Vault; no hard‑coded credentials.

---

## 10. Future Enhancements

| Feature | Priority | Notes |
|---------|----------|-------|
| **Multimodal Idea Generation** | Medium | Integrate image prompts via Stable Diffusion. |
| **Auto‑Retraining** | High | Feedback loop triggers fine‑tuning of vLLM. |
| **Marketplace Integration** | Low | Export validated ideas to external marketplaces. |
| **Collaboration Mode** | Medium | Real‑time co‑editing of ideas. |

---

## 11. Acceptance Criteria

1. **Idea Generation** – API returns a coherent idea within 2 s on average.  
2. **Validation** – Scores are stored and retrievable; status changes to `validated`.  
3. **Feedback** – User feedback persists; triggers a retraining job after 1000 entries.  
4. **Observability** – Metrics exposed at `/metrics`; logs shipped to Loki.  
5. **Security** – All endpoints require authentication; rate limits applied.  
6. **Deployment** – Helm chart installs successfully on a test cluster; pods are healthy.  

---

*Prepared by: Senior Product/Engineering Lead – Axentx*
