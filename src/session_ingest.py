"""Normalize JSON/JSONL engineering-session exports into analysis text."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

SECRET_KEYS = {"token", "access_token", "refresh_token", "api_key", "password", "secret", "authorization"}


def sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: "[REDACTED]" if k.lower() in SECRET_KEYS else sanitize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [sanitize(v) for v in value]
    return value


def load_records(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    if path.suffix.lower() == ".jsonl":
        return [sanitize(json.loads(line)) for line in raw.splitlines() if line.strip()]
    data = sanitize(json.loads(raw))
    if isinstance(data, list):
        return [item if isinstance(item, dict) else {"content": item} for item in data]
    return [data]


def record_text(record: Any) -> str:
    if isinstance(record, dict):
        return " ".join(record_text(v) for v in record.values())
    if isinstance(record, list):
        return " ".join(record_text(v) for v in record)
    return str(record)


def ingest(paths: list[Path]) -> list[dict[str, Any]]:
    sessions = []
    for path in paths:
        records = load_records(path)
        sessions.append({"source": str(path), "records": records, "text": record_text(records)})
    return sessions
