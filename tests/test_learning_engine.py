import json
from pathlib import Path
from src.learning_engine import detect, flatten, load_json

SESSION = Path("demo/real-world-java-api-maintenance/session.json")


def test_demo_detects_negative_path_pattern():
    session = load_json(SESSION)
    proposals = detect(flatten(session))
    assert any(p["id"] == "negative-path-api-tests" for p in proposals)


def test_detector_is_deterministic():
    session = load_json(SESSION)
    text = flatten(session)
    assert detect(text) == detect(text)
