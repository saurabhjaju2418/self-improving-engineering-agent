# Phase 1 Implementation

## Goal

Turn engineering-session evidence into safe, reviewable learning proposals.

## Quick start

Requirements: Python 3.10+ and a clone of this repository.

```bash
python3 src/learning_engine.py demo/real-world-java-api-maintenance/session.json
```

The command is deterministic and does not call an external model or network.

## Output

The engine emits JSON proposals containing:

- `id` — stable rule identifier
- `category` — engineering domain
- `confidence` — evidence confidence
- `risk` — change risk
- `action` — suggested gate (`review` in the demo)
- `rule` — durable engineering rule
- `evidence` — why the rule was proposed
- `status` — starts as `pending_approval`

## Safe lifecycle

1. Collect session evidence.
2. Detect recurring signals.
3. Generate a proposal.
4. Validate the proposal against the schema.
5. Apply policy gates.
6. Human approves review-tier proposals.
7. Only then persist durable memory.
8. Record the change in Git/audit history.

## Important limitation

Phase 1 is deliberately deterministic. It demonstrates the safety and data flow before an LLM is introduced. The next implementation step is to replace keyword detection with an LLM-backed extractor while preserving the same schema and policy boundary.
