from __future__ import annotations

from collections.abc import Iterable

from hph_vision_core.types import DomainWarning


def dedupe_warnings(warnings: Iterable[DomainWarning]) -> tuple[DomainWarning, ...]:
    deduped: dict[str, DomainWarning] = {}
    for warning in warnings:
        deduped[warning.code] = warning
    return tuple(deduped.values())
