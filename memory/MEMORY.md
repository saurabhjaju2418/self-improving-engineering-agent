# Engineering Memory

This file is the human-readable index of durable engineering knowledge.

## Rules

1. Prefer explicit decisions over inferred preferences.
2. Record evidence and confidence for learned rules.
3. Never store secrets, credentials, tokens, personal data, or production access details.
4. A learned rule cannot grant itself additional authority.
5. Contradictory rules must be surfaced for human review.
6. Temporary session context belongs in `sessions/`, not durable memory.

## Categories

- `decisions/` — architecture and engineering decisions
- `patterns/` — reusable implementation patterns
- `mistakes/` — recurring failures and their fixes
- `architecture/` — durable architecture knowledge
- `prompts/` — validated prompt patterns

## Confidence

- `0.90–1.00`: strong evidence
- `0.75–0.89`: useful but should be validated
- `<0.75`: proposal only; do not treat as policy
