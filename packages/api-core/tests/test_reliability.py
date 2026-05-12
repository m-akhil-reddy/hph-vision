from hph_vision_core.reliability import (
    ReliabilityResult,
    interpret_reliability,
    validate_reliability,
)


def test_validate_reliability_score_range() -> None:
    result = validate_reliability(ReliabilityResult(score=1.2, level="high"))

    assert not result.ok
    assert result.errors[0].field == "reliability.score"


def test_interpret_low_reliability_recommends_repeat() -> None:
    interpretation = interpret_reliability(ReliabilityResult(score=0.4, level="low"))

    assert interpretation.can_interpret
    assert interpretation.should_repeat
    assert "low_reliability" in interpretation.reasons
