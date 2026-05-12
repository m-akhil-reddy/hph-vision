from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, TypeAlias

from hph_vision_core.types import DomainWarning, dataclass_to_dict

ReliabilityLevel: TypeAlias = Literal["high", "medium", "low", "invalid"]


@dataclass(frozen=True)
class ReliabilityResult:
    score: float
    level: ReliabilityLevel
    warnings: tuple[DomainWarning, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class ReliabilityInterpretation:
    can_interpret: bool
    should_repeat: bool
    level: ReliabilityLevel
    reasons: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
