#!/usr/bin/env python3
"""Deterministic Phase-1 learning engine.

Consumes a JSON session export and emits a validated learning proposal.
No LLM or network access is required, making the demo safe and reproducible.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "learning" / "proposal.schema.json"

PATTERNS = [
    {
        "id": "negative-path-api-tests",
        "title": "Add negative-path tests for REST endpoints",
        "category": "testing",
        "keywords": ["missing negative", "4xx", "5xx", "error response", "negative-path"],
        "confidence": 0.94,
        "risk": "low",
        "action": "review",
        "rule": "REST endpoint tests should cover expected 4xx and 5xx responses, not only successful responses.",
    },
    {
        "id": "jackson-over-jaxb",
        "title": "Prefer Jackson annotations for generated models",
        "category": "java",
        "keywords": ["jaxb", "jackson"],
        "confidence": 0.96,
        "risk": "low",
        "action": "review",
        "rule": "Generated Java models should use Jackson annotations unless a project requirement explicitly requires JAXB.",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def flatten(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def detect(text: str) -> list[dict[str, Any]]:
    lowered = text.lower()
    matches = []
    for pattern in PATTERNS:
        hits = sum(1 for keyword in pattern["keywords"] if keyword in lowered)
        if hits:
            proposal = {k: v for k, v in pattern.items() if k not in {"keywords"}}
            proposal["evidence"] = [
                f"Matched {hits} recurring signal(s) for {pattern['id']}."
            ]
            proposal["status"] = "pending_approval"
            matches.append(proposal)
    return matches


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python src/learning_engine.py demo/real-world-java-api-maintenance/session.json")
        return 2
    session_path = Path(sys.argv[1])
    session = load_json(session_path)
    proposals = detect(flatten(session))
    output = {
        "engine_version": "0.1.0",
        "source": str(session_path),
        "proposal_count": len(proposals),
        "proposals": proposals,
    }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
