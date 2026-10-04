# Security Policy

## Scope

This project handles engineering-session signals and produces learning proposals. It is intentionally designed so learned knowledge cannot expand agent authority.

## Never store

- API keys
- OAuth tokens
- passwords
- private keys
- production credentials
- personal or customer data
- internal access details

## Safety boundary

Policy evaluation is outside the model/extraction loop. Unknown categories default to human review. Security, access-control, credential, production-deployment, destructive, and security-weakening changes are blocked.

## Reporting

For vulnerabilities, please use GitHub's private security reporting mechanism when enabled. Do not disclose secrets or exploit details in a public issue.
