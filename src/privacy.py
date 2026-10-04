"""Local privacy boundary for optional model integrations.

The core engine does not transmit data. This module provides conservative
redaction helpers for integrations that a user explicitly enables.
"""
from __future__ import annotations

import re
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^\s'\"]+"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]+"),
    re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----.*?-----END [A-Z ]+ PRIVATE KEY-----", re.DOTALL),
]
PRIVATE_PATHS = (".env", ".git", ".ssh", ".aws", ".kube")


def redact(text: str) -> str:
    """Redact common credential forms before optional external transmission."""
    result = text
    for pattern in SECRET_PATTERNS:
        result = pattern.sub("[REDACTED]", result)
    return result


def is_private_path(path: str | Path) -> bool:
    """Return True when a path is clearly private/sensitive by convention."""
    normalized = str(path).replace("\\", "/")
    name = Path(normalized).name
    return name == ".env" or any(part in normalized.split("/") for part in PRIVATE_PATHS)


def prepare_external_payload(text: str) -> str:
    """Conservative opt-in boundary for a model adapter."""
    return redact(text)
