# Privacy and Data Security

## Core guarantee

The framework is **local-first**. A user cloning this repository does not automatically send source code, Claude sessions, prompts, memory, proposals, audit logs, or telemetry to the project owner or any hosted service.

The public repository contains the framework, tests, documentation, and intentionally sanitized examples only.

## Data flow

```text
User repository
      |
      v
Local session artifacts
      |
      v
Local sanitizer
      |
      v
Local learning engine
      |
      +----> Local memory
      |
      +----> Local proposals
      |
      +----> Local audit log
      |
      +----> Optional external LLM
             ONLY when explicitly configured by the user
```

## Default rules

1. No mandatory telemetry.
2. No mandatory hosted backend.
3. No automatic upload of session data.
4. No automatic upload of source code.
5. No credentials stored in the repository.
6. Local learning artifacts are ignored by Git.
7. Demo data is synthetic/sanitized.
8. External provider use is opt-in and must be explicit.
9. Sensitive content should be redacted before external model calls.
10. Policy evaluation happens locally and cannot be overridden by learned content.

## What is private

Treat all of the following as private:

- source code
- prompts and session transcripts
- customer or employee information
- proprietary architecture information
- credentials and tokens
- local filesystem paths
- generated memory and embeddings
- learning proposals and approval history
- local audit logs

## External LLM providers

The project is model-agnostic. An external model adapter may be added, but it must be opt-in.

An adapter must:

- clearly identify the destination provider;
- receive only the minimum required content;
- support redaction before transmission;
- never receive credentials or secrets;
- never silently transmit whole repositories;
- document retention/privacy assumptions;
- fail closed when required privacy configuration is absent.

## Git rules

Do not commit private learning data. `.gitignore` protects common local paths, but users must still review `git status` before committing.

If a secret is committed, assume it may be compromised. Removing it from the latest commit does not remove it from Git history. Rotate it immediately and then clean the history as appropriate.

## Public demo rule

Only synthetic or sanitized data belongs under `demo/`. Never copy a real customer incident, real prompt transcript, production log, internal hostname, employee information, API token, or proprietary source code into a demo.

## Security boundary

The learning engine can propose knowledge changes. It cannot use a learned proposal to grant itself new filesystem, network, credential, deployment, or repository permissions.

**Knowledge is mutable. Authority is not self-modifiable.**
