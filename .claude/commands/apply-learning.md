# /apply-learning — Apply Approved Learning

Apply only proposals that have been explicitly approved by a human and pass the trusted policy engine.

## Required checks

1. Read the proposal from `learning/`.
2. Validate it against `learning/proposal.schema.json`.
3. Re-evaluate its gate from `policies/gates.yml`.
4. Refuse `blocked` proposals.
5. Refuse `review` proposals unless `status=approved`.
6. Never infer approval from confidence alone.
7. Write the durable memory change and an audit record.
8. Show the exact files changed.

Never modify the policy file as part of applying a learning proposal.