# LLM Integration Boundary

The project is intentionally split into two trust zones.

```text
Untrusted model output
        ↓
JSON proposal
        ↓
Schema validation
        ↓
Trusted policy engine
        ↓
AUTO / REVIEW / BLOCKED
        ↓
Human approval where required
        ↓
Memory + Git audit
```

## Why this matters

An LLM can suggest a learning rule, but it cannot decide what authority it has. The policy file is deterministic and external to the model.

## Adding a provider

Implement the `Extractor` protocol in `src/extractor.py`. The extractor should return proposal-shaped dictionaries only. Do not let the provider write files, execute commands, alter policy, or commit changes.

## Recommended production flow

1. Sanitize session data.
2. Send only the minimum required context to the model.
3. Request strict JSON.
4. Validate against `learning/proposal.schema.json`.
5. Recompute the gate locally from `policies/gates.yml`.
6. Require explicit approval for review-tier changes.
7. Apply through the memory store.
8. Record an audit event.
9. Commit the durable change through the normal Git workflow.

The model is therefore an **extractor**, not the security authority or deployment authority.
