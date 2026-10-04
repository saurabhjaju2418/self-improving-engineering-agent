# Session Data Boundary

Only sanitized, minimum-necessary session artifacts belong here.

## Allowed

- task descriptions
- developer corrections
- test failures
- architecture decisions
- non-sensitive outcomes

## Forbidden

- API keys and tokens
- passwords and private keys
- customer/passenger data
- email addresses when not required for the learning task
- production URLs containing credentials
- access-control details

Raw Claude/IDE history should remain local unless it has been explicitly sanitized for analysis.