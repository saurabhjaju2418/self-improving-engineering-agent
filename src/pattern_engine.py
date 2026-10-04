"""Cross-session recurrence and contradiction analysis."""
from __future__ import annotations
from collections import Counter
from typing import Iterable


def recurring(signals: Iterable[str], minimum: int = 2) -> list[dict]:
    counts = Counter(s.lower().strip() for s in signals if s.strip())
    return [{"signal": signal, "occurrences": count} for signal, count in counts.items() if count >= minimum]


def contradictions(existing_rules: Iterable[str], proposed_rules: Iterable[str]) -> list[dict]:
    pairs = []
    for proposal in proposed_rules:
        p = proposal.lower()
        for rule in existing_rules:
            r = rule.lower()
            if ("jaxb" in p and "jackson" in r) or ("jackson" in p and "jaxb" in r):
                pairs.append({"proposal": proposal, "existing": rule, "reason": "Potentially conflicting serialization convention; human review required."})
    return pairs
