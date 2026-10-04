# Real-World Demo: Java API Maintenance

This demo shows a realistic engineering workflow for a Spring Boot REST API where an AI coding assistant learns from repeated corrections instead of repeating the same mistake.

## Scenario

A team asks Claude Code to add a `GET /api/orders/{id}` endpoint.

### Initial attempt

The assistant creates a controller and service, but the implementation repeatedly misses one or more team expectations:

- consistent `404` handling when an order is absent
- validation/error response structure
- negative-path JUnit 5 tests
- Jackson-based DTO conventions
- OpenAPI annotations

A developer corrects the implementation during the session.

## How the self-improving agent helps

```text
Claude session
     |
     v
Corrections detected
     |
     v
Pattern extracted
     |
     v
Learning proposal
     |
     +---- low risk ----> AUTO
     |
     +---- engineering rule -> REVIEW
     |
     +---- unsafe authority/security change -> BLOCK
     |
     v
Approved knowledge
     |
     v
Future Claude sessions
```

The important point is that the system learns a **reusable engineering rule**, not a one-off code patch.

## Example learning proposal

```json
{
  "id": "api-error-tests-001",
  "type": "pattern",
  "title": "Cover negative REST paths",
  "observation": "Endpoint work repeatedly required tests for missing resources and error responses.",
  "proposed_change": "For new REST endpoints, generate success and negative-path tests by default.",
  "confidence": 0.91,
  "risk": "low",
  "action": "review"
}
```

A reviewer can approve the proposal. The rule is then stored in Git-backed engineering memory.

## Beginner walkthrough

### 1. Clone the repository

```bash
git clone https://github.com/saurabhjaju2418/self-improving-engineering-agent.git
cd self-improving-engineering-agent
```

### 2. Open the project in VS Code

```bash
code .
```

### 3. Start Claude Code

Run Claude Code from the repository root.

### 4. Establish a baseline

Ask Claude Code to implement a small REST endpoint in a sample Spring Boot project. Let it complete the task normally.

### 5. Make realistic corrections

Correct issues you would normally correct during code review—for example, ask for a `404` response and a JUnit negative-path test.

### 6. Run `/learn`

The command analyzes the session and identifies reusable lessons, patterns, and decisions.

### 7. Inspect the proposal

Run `/review-learning`.

Do not approve a proposal just because it sounds plausible. Confirm that it represents a repeated or explicit engineering preference.

### 8. Apply safe learning

Approve only appropriate proposals. Never approve a proposal that grants the agent additional access or weakens security controls.

### 9. Start another task

Ask Claude Code to create another REST endpoint.

The expected result is that the assistant now considers the learned testing and API conventions earlier in the implementation.

### 10. Check the audit trail

Use `/status` to see learning activity and pending proposals.

## What beginners should learn from this demo

1. AI output is not automatically engineering policy.
2. A correction is useful evidence, but one correction is not always a durable rule.
3. Learned knowledge should be reviewable in Git.
4. Low-risk knowledge can be automated; authority and security changes should remain human-controlled.
5. The goal is not an AI that can change itself without limits. The goal is an AI that gets better **within explicit boundaries**.

## Success criteria

The demo is successful when a later endpoint task produces the learned test/API conventions without the developer having to repeat the same instruction.
