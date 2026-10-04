"""Phase 2 orchestration: ingest -> recurrence -> proposal -> policy -> audit.

Provider-neutral: an LLM may later supply candidate signals, but the trusted
policy and validation layers remain deterministic.
"""
from __future__ import annotations
import json
from pathlib import Path
from .learning_engine import detect
from .session_ingest import ingest
from .pattern_engine import recurring, contradictions


def analyze(paths: list[Path], existing_rules: list[str] | None = None) -> dict:
    sessions = ingest(paths)
    texts = [s["text"] for s in sessions]
    candidates = []
    for text in texts:
        candidates.extend(detect(text))
    signals = [p["id"] for p in candidates]
    recurrence = recurring(signals, minimum=2)
    proposals = []
    seen = set()
    for proposal in candidates:
        if proposal["id"] in seen:
            continue
        seen.add(proposal["id"])
        matches = next((r for r in recurrence if r["signal"] == proposal["id"]), None)
        proposal["recurrence"] = matches["occurrences"] if matches else 1
        if proposal["recurrence"] >= 2:
            proposal["confidence"] = min(1.0, proposal["confidence"] + 0.02)
        proposals.append(proposal)
    conflicts = contradictions(existing_rules or [], [p["proposed_change"] for p in proposals])
    if conflicts:
        for proposal in proposals:
            if any(c["proposal"] == proposal["proposed_change"] for c in conflicts):
                proposal["gate"] = "review"
                proposal["status"] = "pending"
    return {"engine_version": "0.3.0", "sessions": len(sessions), "recurring_signals": recurrence, "contradictions": conflicts, "proposals": proposals}


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(prog="siea-phase2")
    parser.add_argument("sessions", nargs="+", type=Path)
    parser.add_argument("--existing-rule", action="append", default=[])
    args = parser.parse_args()
    print(json.dumps(analyze(args.sessions, args.existing_rule), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
