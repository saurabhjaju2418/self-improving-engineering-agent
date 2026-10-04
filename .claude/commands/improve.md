# /improve — Generate Improvement Proposals

Review `learning/pending/` and engineering memory for high-confidence opportunities.

## Rules

- Propose small, reversible changes.
- Do not modify production source code.
- Do not modify security controls, permissions, credentials, deployment access, or branch protection.
- Detect contradictions before proposing a new rule.
- Every proposal must cite its evidence and explain expected benefit.

Classify every proposal:

- `auto`: low-risk knowledge maintenance
- `review`: engineering behavior or policy change requiring approval
- `blocked`: unsafe or privileged change

Only write proposal files. Never apply changes from this command.