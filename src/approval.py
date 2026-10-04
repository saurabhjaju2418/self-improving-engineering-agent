"""Explicit proposal lifecycle and append-only audit records."""
from __future__ import annotations
from datetime import datetime, timezone
import json
from pathlib import Path


def transition(proposal: dict, decision: str) -> dict:
    gate = proposal.get("gate")
    allowed = {"approve": {"auto", "review"}, "reject": {"review", "auto"}, "block": {"blocked"}}
    if decision not in allowed or gate not in allowed[decision]:
        raise ValueError(f"Decision '{decision}' is not allowed for gate '{gate}'")
    result = dict(proposal)
    result["status"] = {"approve": "approved", "reject": "rejected", "block": "blocked"}[decision]
    return result


def audit(path: Path, event: str, proposal_id: str, details: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, "proposal_id": proposal_id, "details": details}
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
