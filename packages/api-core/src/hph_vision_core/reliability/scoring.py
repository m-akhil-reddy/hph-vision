from __future__ import annotations

from hph_vision_core.reliability.models import (
    ReliabilityInterpretation,
    ReliabilityLevel,
    ReliabilityResult,
)
from hph_vision_core.validation.numeric import validate_unit_interval
from hph_vision_core.validation.result import ValidationResult, validation_warning


def level_for_score(score: float) -> ReliabilityLevel:
    if score >= 0.8:
        return "high"
    if score >= 0.6:
        return "medium"
    if score >= 0.35:
        return "low"
    return "invalid"


def validate_reliability(result: ReliabilityResult) -> ValidationResult:
    score_validation = validate_unit_interval(result.score, "reliability.score")
    warnings = list(score_validation.warnings)
    if score_validation.ok and level_for_score(result.score) != result.level:
        warnings.append(
            validation_warning(
                "reliability_level_mismatch",
                "Reliability level does not match the submitted score band.",
                "reliability.level",
            )
        )
    return ValidationResult(errors=score_validation.errors, warnings=tuple(warnings))


def interpret_reliability(
    result: ReliabilityResult | None,
) -> ReliabilityInterpretation:
    if result is None:
        return ReliabilityInterpretation(
            can_interpret=False,
            should_repeat=True,
            level="invalid",
            reasons=("missing_reliability",),
        )

    reasons: list[str] = []
    if result.level == "invalid" or result.score < 0.35:
        reasons.append("invalid_reliability")
    elif result.level == "low" or result.score < 0.6:
        reasons.append("low_reliability")

    for warning in result.warnings:
        if warning.severity == "critical":
            reasons.append(warning.code)

    return ReliabilityInterpretation(
        can_interpret=result.score >= 0.35 and result.level != "invalid",
        should_repeat=result.score < 0.6 or result.level in {"low", "invalid"},
        level=result.level,
        reasons=tuple(dict.fromkeys(reasons)),
    )
