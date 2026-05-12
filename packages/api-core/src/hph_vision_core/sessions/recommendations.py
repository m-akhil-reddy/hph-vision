from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from hph_vision_core.types import ResultRecommendation, dataclass_to_dict
from hph_vision_core.version import RECOMMENDATION_POLICY_VERSION


@dataclass(frozen=True)
class RecommendationInput:
    has_red_flags: bool = False
    urgent_red_flags: bool = False
    reliability_score: float | None = None
    refraction_confidence: float | None = None
    completed: bool = False
    has_critical_warnings: bool = False

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


def determine_recommendation(input: RecommendationInput) -> ResultRecommendation:
    if input.urgent_red_flags:
        return "urgent_care_recommended"
    if input.has_red_flags:
        return "professional_exam_recommended"

    reliability_score = input.reliability_score
    if reliability_score is None:
        return "repeat_test"
    if reliability_score < 0.35 or input.has_critical_warnings:
        return "invalid_result"
    if not input.completed:
        return "repeat_test"
    if reliability_score < 0.6:
        return "repeat_test"
    if input.refraction_confidence is not None and input.refraction_confidence < 0.5:
        return "clinician_review_recommended"

    return "clinician_review_recommended"


def get_recommendation_policy_version() -> str:
    return RECOMMENDATION_POLICY_VERSION
