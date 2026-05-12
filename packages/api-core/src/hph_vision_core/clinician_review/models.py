from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, TypeAlias

from hph_vision_core.types import dataclass_to_dict
from hph_vision_core.validation.result import ValidationResult

ReviewStatus: TypeAlias = Literal[
    "submitted",
    "queued",
    "in_review",
    "needs_more_information",
    "completed",
    "cancelled",
    "rejected",
    "expired",
]


@dataclass(frozen=True)
class ClinicianReviewEligibility:
    eligible: bool
    reasons: tuple[str, ...]
    validation: ValidationResult

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
