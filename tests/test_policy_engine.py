from src.policy_engine import gate_for, enforce


def test_unknown_category_defaults_to_review():
    assert gate_for("unknown-category") == "review"


def test_secrets_are_blocked():
    assert gate_for("secrets") == "blocked"
    result = enforce({"category": "secrets", "status": "pending"})
    assert result["gate"] == "blocked"
    assert result["status"] == "blocked"


def test_low_risk_auto_category_is_not_reviewed():
    assert gate_for("prompt-improvement") == "auto"
