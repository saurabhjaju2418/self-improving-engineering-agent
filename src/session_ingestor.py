"""Local-only ingestion of explicitly selected session artifacts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .privacy import is_private_path


def load_json_session(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if is_private_path(p):
        raise ValueError(f"Refusing to ingest sensitive path: {p}")
    if not p.is_file():
        raise FileNotFoundError(p)
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Session artifact must contain a JSON object")
    return data


def collect_text(session: dict[str, Any]) -> str:
    """Flatten explicitly supplied session fields; never scans the filesystem."""
    def flatten(value: Any) -> str:
        if isinstance(value, dict):
            return " ".join(flatten(v) for v in value.values())
        if isinstance(value, list):
            return " ".join(flatten(v) for v in value)
        return str(value)

    return flatten(session)
