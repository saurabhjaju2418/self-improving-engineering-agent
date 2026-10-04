# Architecture

## Trust boundaries

```text
                 ENGINEERING WORK
                        │
                        ▼
                Session Sanitizer
                        │
                        ▼
                Extractor / LLM
                 (untrusted output)
                        │
                        ▼
                 JSON Schema Gate
                        │
                        ▼
              Deterministic Policy Engine
                 ┌──────┼──────┐
                 ▼      ▼      ▼
                AUTO  REVIEW  BLOCKED
                 │      │       │
                 │   Human      X
                 │  approval
                 └──────┼──────┘
                        ▼
                  Memory Store
                        │
                        ▼
                    Audit Log
                        │
                        ▼
                       Git
```

## Design rule

The learning component can improve knowledge but cannot modify the policy authority. This prevents a self-generated lesson from escalating the agent's permissions.

## Deployment modes

### Local-first

Best for developer workstations. Session processing and memory remain local; Git is the durable collaboration layer.

### Team service

Future mode: central dashboard, authentication, role-based approvals, PostgreSQL/pgvector and GitHub/GitLab integrations. The same policy boundary remains local to the service and is not controlled by the model.
