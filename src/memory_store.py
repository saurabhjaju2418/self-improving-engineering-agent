"""Git-friendly durable memory writer with explicit approval."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]


def _safe_name(value: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")


def apply_approved(proposal: dict, memory_root: Path | None = None) -> Path:
    if proposal.get("gate") == "blocked":
        raise PermissionError("Blocked learning cannot be applied")
    if proposal.get("gate") == "review" and proposal.get("status") != "approved":
        raise PermissionError("Review-tier learning requires explicit approval")
    root = memory_root or ROOT / "memory" / "patterns"
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"{_safe_name(proposal['id'])}.md"
    now = datetime.now(timezone.utc).isoformat()
    text = f"# {proposal['title']}\n\n"
    text += f"- Learned: {now}\n- Confidence: {proposal.get('confidence', 0):.2f}\n"
    text += f"- Evidence: {proposal.get('evidence', [])}\n\n"
    text += f"## Rule\n\n{proposal.get('proposed_change') or proposal.get('rule', '')}\n"
    path.write_text(text, encoding="utf-8")
    return path
