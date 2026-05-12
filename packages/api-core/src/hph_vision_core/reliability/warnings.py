from __future__ import annotations

from hph_vision_core.types import DomainWarning


def missing_reliability_warning() -> DomainWarning:
    return DomainWarning(
        code="reliability.missing",
        message="No reliability result was submitted with the session.",
        severity="warning",
        source="reliability",
    )
