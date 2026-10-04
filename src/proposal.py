"""Proposal validation and normalization."""
from __future__ import annotations
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "learning" / "proposal.schema.json"


def validate(proposal: dict) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return [error.message for error in Draft202012Validator(schema).iter_errors(proposal)]


def require_valid(proposal: dict) -> dict:
    errors = validate(proposal)
    if errors:
        raise ValueError("Invalid learning proposal: " + "; ".join(errors))
    return proposal
