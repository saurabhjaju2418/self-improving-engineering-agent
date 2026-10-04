# Contributing

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m src.learning_engine demo/real-world-java-api-maintenance/session.json
```

## Contribution rules

1. Never commit credentials, tokens, customer data, or raw IDE/Claude history.
2. Add tests for learning-engine or policy changes.
3. Do not weaken `policies/gates.yml` through a learned proposal.
4. Keep model/provider integrations behind `src/extractor.py`.
5. Prefer small, reviewable commits.
6. Security-sensitive behavior requires explicit human review.
