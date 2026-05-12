from hph_vision_core.clinician_review import (
    determine_clinician_review_eligibility,
    validate_review_status_transition,
)
from hph_vision_core.fixtures import (
    make_no_review_consent_session_submission,
    make_red_flag_session_submission,
    make_review_eligible_session_submission,
)


def test_review_eligibility_requires_review_consent() -> None:
    eligibility = determine_clinician_review_eligibility(
        make_no_review_consent_session_submission()
    )

    assert not eligibility.eligible
    assert "missing_review_consent" in eligibility.reasons


def test_review_eligible_session_passes() -> None:
    eligibility = determine_clinician_review_eligibility(
        make_review_eligible_session_submission()
    )

    assert eligibility.eligible
    assert eligibility.reasons == ()


def test_red_flag_session_not_eligible_for_async_review() -> None:
    eligibility = determine_clinician_review_eligibility(
        make_red_flag_session_submission()
    )

    assert not eligibility.eligible
    assert "red_flags_require_professional_care" in eligibility.reasons


def test_review_status_transition_validation() -> None:
    assert validate_review_status_transition("submitted", "queued").ok
    assert not validate_review_status_transition("completed", "in_review").ok
