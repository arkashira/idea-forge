## dataflow.md

```text
+-------------------+          +-------------------+          +-------------------+
|  External Data    |          |  Ingestion Layer  |          |  Processing/      |
|  Sources (API,    |          |  (Kafka / Kinesis)|          |  Transform Layer  |
|  Webhooks, Files) |          |  (Kafka Connect)  |          |  (Kafka Streams,  |
|  ---------------- |          |  ---------------- |          |   Flink, Spark)   |
+-------------------+          +-------------------+          +-------------------+
          |                           |                           |
          v                           v                           v
+-------------------+          +-------------------+          +-------------------+
|  Storage Tier     |          |  Query/Serving    |          |  Egress to User   |
|  (PostgreSQL,     |          |  Layer (Supabase, |          |  (REST/GraphQL,   |
|  Redis, S3)       |          |  Hasura, Supabase |          |   WebSocket)      |
+-------------------+          +-------------------+          +-------------------+
          ^                           ^                           |
          |                           |                           |
          +---------------------------+---------------------------+
```

### 1. External Data Sources
- **OpenAI / Anthropic APIs** – LLM inference for idea generation & validation.
- **GitHub REST API** – Pull repo metadata for trend analysis.
- **Product Hunt API** – Fetch trending product data for market validation.
- **Reddit / Hacker News RSS** – Capture community sentiment on emerging ideas.
- **Custom Webhooks** – User‑submitted prompts or feedback.

### 2. Ingestion Layer
| Component | Role | Auth Boundary |
|-----------|------|---------------|
| **Kafka** | Event bus for all external streams | Internal |
| **Kafka Connect** | Source connectors (GitHub, Product Hunt, RSS) | Internal |
| **HTTP Ingress** | REST endpoint for user prompts | External (JWT) |
| **Auth Service** | OAuth2 / JWT validation | External |

### 3. Processing / Transform Layer
| Component | Role | Auth Boundary |
|-----------|------|---------------|
| **Kafka Streams** | Real‑time transformation of incoming events | Internal |
| **Flink Job** | Batch enrichment (e.g., sentiment scoring) | Internal |
| **LLM Orchestrator** | Calls OpenAI/Anthropic, caches responses | Internal |
| **Validation Engine** | Cross‑checks idea against market data | Internal |

### 4. Storage Tier
| Component | Purpose | Auth Boundary |
|-----------|---------|---------------|
| **PostgreSQL** | Persist structured idea data, user profiles | Internal |
| **Redis** | Cache LLM responses & session state | Internal |
| **S3** | Store raw event logs, LLM logs, large artifacts | Internal |
| **Supabase** | Unified auth + Postgres backend for dev convenience | Internal |

### 5. Query / Serving Layer
| Component | Role | Auth Boundary |
|-----------|------|---------------|
| **Supabase Edge Functions** | API gateway for CRUD ops | External (JWT) |
| **Hasura** | GraphQL endpoint over Postgres | External (JWT) |
| **WebSocket Service** | Real‑time updates to UI | External (JWT) |
| **Rate‑Limiter** | Protect API from abuse | Internal |

### 6. Egress to User
| Component | Interface | Auth Boundary |
|-----------|-----------|---------------|
| **REST API** | `/ideas`, `/validate` | External (JWT) |
| **GraphQL API** | `/graphql` | External (JWT) |
| **WebSocket** | `/realtime` | External (JWT) |
| **CLI / SDK** | Python/Node SDK | External (API key) |

---

**Auth Flow Summary**

1. **User** authenticates via OAuth2 → receives JWT.
2. **JWT** is attached to all outbound requests to Ingestion, Query, and Egress services.
3. **Internal services** validate JWT against Auth Service; no external calls needed.
4. **External APIs** (OpenAI, GitHub, Product Hunt) use their own API keys; secrets stored in Vault and injected at runtime.

This architecture ensures a clear separation of concerns, secure auth boundaries, and a scalable pipeline from raw data to AI‑generated, market‑validated ideas.