"""Append-only JSONL audit records for local runs."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]


def record(event: str, payload: dict, path: Path | None = None) -> Path:
    target = path or ROOT / "learning" / "audit.jsonl"
    target.parent.mkdir(parents=True, exist_ok=True)
    item = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **payload}
    with target.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(item, sort_keys=True) + "\n")
    return target
