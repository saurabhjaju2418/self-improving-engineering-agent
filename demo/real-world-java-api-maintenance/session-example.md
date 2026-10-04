# Simulated Session Example

This is a safe, deterministic example for demonstrating the learning concept without requiring access to a real enterprise repository.

## Session 1 — Developer request

```text
Developer: Add GET /api/orders/{id}. Follow our standard REST conventions and add tests.
```

## Assistant implementation

The assistant produces a happy-path test but misses the missing-order case.

## Developer correction

```text
Developer: We always test the not-found path. Add a 404 test and use the standard error response.
```

## Session 1 learning evidence

```yaml
observation: Missing-order test was added after developer correction.
confidence: 0.70
status: candidate
```

A single correction is not automatically promoted to a permanent rule.

## Session 2 — Similar request

A second endpoint is created and again initially lacks a negative-path test.

The developer makes the same correction.

The agent now has stronger evidence:

```yaml
observation: Negative REST paths were corrected in two independent endpoint tasks.
confidence: 0.91
risk: low
proposed_rule: Generate success and negative-path tests for new REST endpoints by default.
action: review
```

## Human decision

The developer reviews the evidence and approves the rule.

The system stores the approved rule in Git-backed memory.

## Session 3 — Improvement

For a new endpoint, the assistant proactively proposes:

- happy-path test
- not-found test
- invalid-input test where applicable
- standard error response assertion

The developer still reviews the resulting code.

## Why this is self-improvement

The model did not rewrite its own underlying model weights. It improved its **project-specific engineering context** using evidence from prior work, with an explicit approval boundary.
