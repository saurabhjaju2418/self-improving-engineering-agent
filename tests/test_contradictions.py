from src.contradictions import find_conflicts


def test_conflicting_java_rules_require_review():
    proposal = {"id": "p1", "proposed_change": "Use Java 21 for new services."}
    existing = [{"rule": "Services must remain on Java 8."}]
    conflicts = find_conflicts(proposal, existing)
    assert len(conflicts) == 1
    assert conflicts[0].severity == "review"


def test_identical_rule_is_not_a_conflict():
    proposal = {"id": "p1", "proposed_change": "Use Jackson annotations."}
    existing = [{"rule": "Use Jackson annotations."}]
    assert find_conflicts(proposal, existing) == []
