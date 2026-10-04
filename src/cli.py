"""Small local CLI for the safe learning lifecycle."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .learning_engine import detect, flatten, load_json
from .policy_engine import enforce
from .proposal import require_valid


def main() -> int:
    parser = argparse.ArgumentParser(prog="siea")
    sub = parser.add_subparsers(dest="command", required=True)
    learn = sub.add_parser("learn", help="analyze a sanitized session JSON")
    learn.add_argument("session")
    args = parser.parse_args()
    if args.command == "learn":
        session = load_json(Path(args.session))
        proposals = []
        for candidate in detect(flatten(session)):
            candidate = {
                "id": candidate["id"],
                "title": candidate["title"],
                "category": candidate["category"],
                "evidence": candidate["evidence"],
                "confidence": candidate["confidence"],
                "novelty": 0.5,
                "risk": candidate["risk"],
                "gate": "review",
                "status": "pending",
                "target": "engineering-memory",
                "proposed_change": candidate["rule"],
            }
            require_valid(candidate)
            proposals.append(enforce(candidate))
        print(json.dumps({"proposal_count": len(proposals), "proposals": proposals}, indent=2))
        return 0
    return 2
