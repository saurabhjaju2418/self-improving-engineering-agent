#!/usr/bin/env python3
"""Deterministic, schema-validating learning proposal engine."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from .policy_engine import enforce
from .proposal import require_valid

PATTERNS = [
    {
        "id": "negative-path-api-tests",
        "title": "Add negative-path tests for REST endpoints",
        "category": "low-risk-test-generation-hint",
        "keywords": ["missing negative", "4xx", "5xx", "error response", "negative-path"],
        "confidence": 0.94,
        "risk": "low",
        "rule": "REST endpoint tests should cover expected 4xx and 5xx responses, not only successful responses.",
    },
    {
        "id": "jackson-over-jaxb",
        "title": "Prefer Jackson annotations for generated models",
        "category": "coding-standard",
        "keywords": ["jaxb", "jackson"],
        "confidence": 0.96,
        "risk": "low",
        "rule": "Generated Java models should use Jackson annotations unless a project requirement explicitly requires JAXB.",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def detect(text: str) -> list[dict[str, Any]]:
    lowered = text.lower()
    results = []
    for pattern in PATTERNS:
        hits = sum(1 for keyword in pattern["keywords"] if keyword in lowered)
        if not hits:
            continue
        proposal = {
            "id": pattern["id"],
            "title": pattern["title"],
            "category": pattern["category"],
            "evidence": [f"Matched {hits} recurring signal(s) for {pattern['id']}.", "Observed in sanitized engineering session input."],
            "confidence": pattern["confidence"],
            "novelty": 0.5,
            "risk": pattern["risk"],
            "gate": "review",
            "status": "pending",
            "target": "engineering-memory",
            "proposed_change": pattern["rule"],
        }
        require_valid(proposal)
        results.append(enforce(proposal))
    return results


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python src/learning_engine.py demo/real-world-java-api-maintenance/session.json")
        return 2
    session_path = Path(sys.argv[1])
    session = load_json(session_path)
    proposals = detect(flatten(session))
    print(json.dumps({"engine_version": "0.2.0", "source": str(session_path), "proposal_count": len(proposals), "proposals": proposals}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
