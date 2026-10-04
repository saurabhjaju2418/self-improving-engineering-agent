# Beginner Guide

This guide explains the project from zero. You do not need to understand agent architecture before starting.

## 1. What is this project?

The Self-Improving Engineering Agent helps an AI coding assistant learn reusable engineering knowledge from real development sessions.

It does **not** give the AI unlimited self-modification powers.

Think of it as:

```text
Your coding session
      ↓
What went wrong / what worked
      ↓
Learning proposal
      ↓
Safety + confidence checks
      ↓
Human approval when needed
      ↓
Version-controlled engineering memory
      ↓
Better future sessions
```

## 2. Prerequisites

Install:

- Git
- VS Code
- Claude Code
- Python 3.11+ for the Phase 1 scripts

You do not need a database or cloud account for the initial local-first workflow.

## 3. Get the project

```bash
git clone https://github.com/saurabhjaju2418/self-improving-engineering-agent.git
cd self-improving-engineering-agent
```

## 4. Understand the folders

| Folder | Purpose |
|---|---|
| `.claude/` | Claude Code commands and agent instructions |
| `memory/` | Durable engineering knowledge |
| `learning/` | Proposed and processed improvements |
| `policies/` | Safety and approval rules |
| `demo/` | Hands-on real-world scenario |
| `docs/` | Documentation |

## 5. Your first learning cycle

Start Claude Code from the repository root.

### Step A — Work normally

Ask Claude Code to perform a small engineering task.

Example:

> Add a Spring Boot REST endpoint for retrieving an order by ID. Include controller, service, DTO, OpenAPI documentation and JUnit 5 tests.

### Step B — Correct the assistant

If the implementation misses a convention, correct it as you normally would.

Examples:

> Use Jackson annotations for the DTO.

> Add a test for the order-not-found case.

> Return the project's standard error response.

### Step C — Learn

Run:

```text
/learn
```

The learning process should ask: Is this correction a one-time change, an explicit project rule, or a repeated pattern?

### Step D — Review

Run:

```text
/review-learning
```

Inspect each proposal.

Look for:

- evidence
- confidence
- scope
- risk
- proposed change

### Step E — Apply

Only approved, policy-compliant proposals should become durable memory.

Never approve a proposal that:

- exposes credentials
- changes access permissions
- disables security controls
- bypasses tests or review
- enables autonomous production deployment

### Step F — Check status

Run:

```text
/status
```

This should show pending and processed learning activity.

## 6. Try the included demo

Go to:

```text
/demo/real-world-java-api-maintenance/
```

Follow that scenario end-to-end. It demonstrates how a repeated correction becomes a reusable engineering rule.

## 7. How to decide whether something should be learned

Use this simple rule:

| Evidence | Recommended action |
|---|---|
| One accidental correction | Do not permanently learn it yet |
| Explicit project instruction | Review and store as a rule |
| Repeated correction | Strong learning candidate |
| Security/access change | Block or require explicit human control |
| Production deployment change | Never auto-apply |

## 8. Troubleshooting

### `/learn` does nothing

Confirm Claude Code was started from the repository root and that the `.claude/commands/` files are present.

### A proposal looks wrong

Reject it. Learning is not mandatory.

### A rule conflicts with an existing rule

Do not silently overwrite the existing rule. Treat the conflict as a review item.

### You want to remove learned knowledge

Delete or edit the corresponding Git-tracked memory entry and commit the change like any other engineering change.

## 9. Recommended workflow for teams

```text
Feature work
   ↓
Claude Code
   ↓
Human review / corrections
   ↓
/learn
   ↓
/review-learning
   ↓
Approved proposal
   ↓
Git commit / PR
   ↓
Future sessions use the knowledge
```

## 10. Golden rule

**The agent can become more knowledgeable, but it must not become more powerful merely because it learned something.**
