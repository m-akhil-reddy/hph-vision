from hph_vision_core.sessions import RecommendationInput, determine_recommendation


def test_red_flags_dominate_recommendation() -> None:
    recommendation = determine_recommendation(
        RecommendationInput(
            has_red_flags=True,
            reliability_score=0.9,
            refraction_confidence=0.9,
            completed=True,
        )
    )

    assert recommendation == "professional_exam_recommended"


def test_urgent_red_flags_dominate_recommendation() -> None:
    recommendation = determine_recommendation(
        RecommendationInput(
            has_red_flags=True,
            urgent_red_flags=True,
            reliability_score=0.9,
            completed=True,
        )
    )

    assert recommendation == "urgent_care_recommended"


def test_low_reliability_recommends_repeat() -> None:
    recommendation = determine_recommendation(
        RecommendationInput(reliability_score=0.5, completed=True)
    )

    assert recommendation == "repeat_test"
