# /learn — Engineering Learning Pass

Analyze recent Claude Code work and extract only durable engineering knowledge.

## Goals

- Identify repeated patterns, mistakes, decisions, preferences, and successful approaches.
- Prefer evidence from multiple occurrences over one-off behavior.
- Never treat secrets, credentials, personal data, or production access details as learnable knowledge.
- Never change project policy directly. Create a proposal instead.

## Output

For each candidate lesson:

1. Category
2. Evidence
3. Confidence (0–1)
4. Novelty
5. Risk
6. Proposed memory path
7. Proposed content
8. Gate: `auto`, `review`, or `blocked`

Write proposals under `learning/pending/` only. Do not apply them automatically.