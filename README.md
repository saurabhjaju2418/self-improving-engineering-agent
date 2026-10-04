<div align="center">

<img src="assets/engineering-brain.svg" alt="Self-Improving Engineering Agent" width="900" />

# 🧠 Self-Improving Engineering Agent

### A secure, Git-native learning loop for Claude Code

**Learn → Remember → Evaluate → Propose → Approve → Improve → Audit**

[![Status](https://img.shields.io/badge/status-Phase%202-7c3aed?style=for-the-badge)](https://github.com/saurabhjaju2418/self-improving-engineering-agent)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-cc785c?style=for-the-badge)](https://docs.anthropic.com/en/docs/claude-code)
[![Git Native](https://img.shields.io/badge/Git-native-181717?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![Local First](https://img.shields.io/badge/data-local--first-0b6e4f?style=for-the-badge)](#-privacy-and-data-security)

</div>

## What is this?

An open engineering-agent framework for turning useful signals from Claude Code sessions and engineering work into durable, reviewable knowledge while keeping the developer in control.

The project is **local-first by design**: your sessions, source code, memory, proposals, audit records and provider credentials stay on your machine unless you explicitly configure an external integration. The public GitHub repository contains only the framework and sanitized examples — never a user's engineering data.

```text
Claude Code / VS Code
        │
        ▼
   Local Session Data
        │
        ▼
 ┌──────────────────┐
 │  Local Learning  │
 │  • patterns      │
 │  • mistakes      │
 │  • decisions     │
 │  • preferences   │
 └────────┬─────────┘
          ▼
   Local Engineering Memory
          │
          ▼
 Improvement Proposal
          │
     ┌────┼────┐
     ▼    ▼    ▼
    AUTO REVIEW BLOCK
     │    │    │
     └────┼────┘
          ▼
   Local Audit / Optional Git
```

## 🔒 Privacy and data security

**This is a core product requirement, not an optional feature.**

When another developer clones this repository, their private engineering data must remain local by default.

### Data that stays local

- Claude Code session transcripts and artifacts
- source code and local repositories
- engineering memory
- learning proposals and approval decisions
- audit logs
- local configuration
- API keys and provider credentials
- generated embeddings/vector indexes, if enabled

### What this repository must never collect by default

- source code
- session transcripts
- prompts containing proprietary information
- customer/employee data
- credentials, tokens or secrets
- local filesystem paths from another user's machine
- telemetry or analytics

There is **no mandatory hosted backend** and no required telemetry endpoint in the core engine.

### External AI providers

An LLM provider is optional. If a user enables one, the user explicitly controls that integration and should review its data-retention and privacy terms. The core pipeline must sanitize/redact sensitive content before any optional external model call.

**Never put session data, `.env` files, tokens, API keys, credentials, proprietary source code or generated memory into the public repository.**

### Git safety

Local learning data is ignored by default. Only framework files and intentionally sanitized examples should be committed.

The repository should treat these as private by default:

```text
sessions/
learning/pending/
learning/approved/
learning/rejected/
learning/applied/
memory/private/
.local/
.env
.env.*
*.secret
*.token
*.key
```

Git history matters too: removing a secret from the latest commit does not remove it from previous commits. Rotate any credential that was ever committed. citeturn0search0

## 🚀 Quick start

### 1. Clone the framework

```bash
git clone https://github.com/saurabhjaju2418/self-improving-engineering-agent.git
cd self-improving-engineering-agent
```

### 2. Create an isolated Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the safe local demo

```bash
python -m src.learning_engine demo/real-world-java-api-maintenance/session.json
```

This uses sanitized demo data only. No network call is required.

### 5. Connect Claude Code

Copy or use the commands under `.claude/commands/` in the project where you work. Start with:

```text
/learn
/status
```

Do not point the tool at your entire home directory. Start with one repository and only the session/project artifacts you intentionally want analyzed.

### 6. Review before applying learning

```text
/review-learning
```

Only after inspecting a proposal should you use:

```text
/apply-learning
```

### 7. Run tests

```bash
pytest -q
```

## 🧪 Real-world demo

The included scenario models a Spring Boot REST API maintenance task:

1. An endpoint is implemented.
2. The developer identifies missing negative-path tests.
3. A similar correction happens again.
4. The engine detects the recurring signal.
5. It creates a structured learning proposal.
6. The policy layer evaluates the risk.
7. The developer approves the reusable rule.
8. Future engineering sessions can use the learned testing convention.

See `demo/real-world-java-api-maintenance/` and `docs/BEGINNER_GUIDE.md`.

## ✨ Core principles

| Principle | Design |
|---|---|
| **Local-first** | Private engineering data stays on the user's machine by default |
| **Git-native** | Framework changes remain reviewable in Git |
| **Human-gated** | Important improvements require explicit approval |
| **Policy-driven** | Auto, review, and blocked changes are explicit |
| **Auditable** | Durable learning events are traceable |
| **Security-first** | Secrets, permissions, production changes and security weakening are never autonomous |
| **Model-agnostic** | The learning architecture is not tied to one model vendor |
| **No mandatory telemetry** | Core functionality does not require sending usage data to us |

## 🚦 Safety model

### 🟢 Auto-apply

Low-risk knowledge maintenance such as duplicate-memory cleanup and documentation improvements.

### 🟡 Human approval

Coding standards, architecture conventions, CI/CD rules, dependency recommendations, integration rules and security recommendations.

### 🔴 Blocked

Never autonomous:

- credentials, tokens, or secrets
- permission/access changes
- production deployment
- branch protection changes
- security bypasses
- destructive operations
- weakening security controls
- arbitrary production-code self-modification

## 🗂️ Architecture

```text
.claude/                 Claude Code commands + skills
src/                     Learning and policy engine
memory/                  Durable engineering knowledge
learning/                Proposed / approved / rejected changes
policies/                Auto / review / blocked rules
scripts/                 Local utilities
sessions/                Local, ignored session-derived artifacts
.github/                 CI, security and project automation
docs/                    Beginner and architecture guides
demo/                    Sanitized reproducible examples
```

## 🧠 Learning loop

1. **Observe** — collect useful engineering signals locally.
2. **Sanitize** — remove secrets and unnecessary sensitive content.
3. **Extract** — identify patterns, decisions, mistakes and successful approaches.
4. **Evaluate** — score confidence, novelty, recurrence and risk.
5. **Detect contradictions** — identify conflicts with existing memory or policies.
6. **Propose** — generate a small, explainable improvement.
7. **Gate** — classify it as auto-apply, review, or blocked.
8. **Apply** — write only permitted changes.
9. **Audit** — record what changed and which evidence supported it.
10. **Repeat** — future sessions validate or invalidate the learned rule.

## 🛠️ Roadmap

### Phase 1 — Foundation

- [x] Repository
- [x] Animated project identity
- [x] Claude Code command structure
- [x] Memory/proposal schemas
- [x] Safety policies
- [x] Local session analyzer
- [x] Tests
- [x] Beginner demo

### Phase 2 — Self-improvement engine

- [x] Recurring-pattern detection foundation
- [x] Policy evaluation foundation
- [ ] contradiction detection
- [ ] confidence calibration
- [ ] proposal generation adapter
- [ ] approval/apply workflow persistence
- [ ] audit trail hardening
- [ ] session ingestion adapters

### Phase 3 — Engineering integrations

- GitHub
- GitLab
- merge requests / pull requests
- CI failures
- test failures
- static-analysis findings
- security findings

### Phase 4 — Engineering Brain UI

A lightweight local dashboard for learned patterns, pending improvements, confidence scores, decision history, safety events and learning velocity.

### Phase 5 — Scheduled learning

```text
Local daily sessions
       ↓
Local scheduled analysis
       ↓
Lessons + proposals
       ↓
Local policy evaluation
       ↓
Safe auto-apply / human approval
       ↓
Local engineering brief
```

## 🔐 Security philosophy

> **The agent may improve its knowledge, but it may not redefine its own authority.**

The policy layer is deliberately outside the learning loop. A learned instruction cannot grant itself permission to access secrets, deploy production code, modify security controls, or bypass human approval.

## 🤝 Contributing

Contributions are welcome, but contributors must use synthetic or sanitized examples. Never submit real customer data, proprietary source code, credentials, private session transcripts or other sensitive information.

See `SECURITY.md` and `CONTRIBUTING.md`.

## 📄 License

MIT.

---

<div align="center">

**Built for engineers who want AI that gets better without giving up control.**

</div>
