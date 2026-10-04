"""Policy evaluation is intentionally outside the learning loop."""
from __future__ import annotations
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_policy(path: Path | None = None) -> dict:
    policy_path = path or ROOT / "policies" / "gates.yml"
    return yaml.safe_load(policy_path.read_text(encoding="utf-8"))


def gate_for(category: str, policy: dict | None = None) -> str:
    policy = policy or load_policy()
    if category in policy.get("blocked", []):
        return "blocked"
    if category in policy.get("auto", []):
        return "auto"
    if category in policy.get("review", []):
        return "review"
    return policy.get("default_gate", "review")


def enforce(proposal: dict, policy: dict | None = None) -> dict:
    """Return a copy whose gate is determined only by trusted policy."""
    result = dict(proposal)
    result["gate"] = gate_for(result.get("category", ""), policy)
    if result["gate"] == "blocked":
        result["status"] = "blocked"
    elif result.get("status") not in {"approved", "applied"}:
        result["status"] = "pending" if result["gate"] == "review" else "pending"
    return result
