"""Conservative contradiction checks for proposed engineering rules."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Conflict:
    proposal_id: str
    reason: str
    severity: str = "review"


def find_conflicts(proposal: dict, existing_rules: list[dict]) -> list[Conflict]:
    """Detect explicit rule conflicts using normalized terms.

    This intentionally errs toward review. It is not an LLM judge and never
    auto-resolves contradictory engineering policy.
    """
    proposed = str(proposal.get("proposed_change", "")).lower()
    conflicts: list[Conflict] = []
    for rule in existing_rules:
        current = str(rule.get("rule", rule.get("proposed_change", ""))).lower()
        if not current or current == proposed:
            continue
        pairs = (("jackson", "jaxb"), ("junit 5", "junit 4"), ("java 21", "java 8"))
        for left, right in pairs:
            if left in proposed and right in current or right in proposed and left in current:
                conflicts.append(Conflict(str(proposal.get("id", "unknown")), f"Potential conflict between {left} and {right}"))
                break
    return conflicts
