from hph_vision_core.fixtures import (
    make_low_reliability_session_submission,
    make_no_review_consent_session_submission,
    make_red_flag_session_submission,
    make_unsupported_protocol_session_submission,
    make_valid_session_submission,
)
from hph_vision_core.sessions import (
    evaluate_session_submission,
    validate_session_submission,
)


def test_valid_session_can_store_and_submit_for_review() -> None:
    evaluation = evaluate_session_submission(make_valid_session_submission())

    assert evaluation.validation.ok
    assert evaluation.can_store
    assert evaluation.can_submit_for_clinician_review
    assert evaluation.recommendation == "clinician_review_recommended"


def test_red_flag_session_is_flagged_and_not_review_eligible() -> None:
    evaluation = evaluate_session_submission(make_red_flag_session_submission())

    assert evaluation.validation.ok
    assert evaluation.can_store
    assert not evaluation.can_submit_for_clinician_review
    assert evaluation.recommendation == "professional_exam_recommended"


def test_unsupported_protocol_session_is_not_storable() -> None:
    result = validate_session_submission(make_unsupported_protocol_session_submission())

    assert not result.ok
    assert result.errors[0].code == "unsupported_protocol_version"


def test_low_reliability_blocks_review_submission() -> None:
    evaluation = evaluate_session_submission(make_low_reliability_session_submission())

    assert evaluation.validation.ok
    assert not evaluation.can_submit_for_clinician_review
    assert evaluation.recommendation == "repeat_test"


def test_missing_review_consent_blocks_review_not_storage() -> None:
    evaluation = evaluate_session_submission(
        make_no_review_consent_session_submission()
    )

    assert evaluation.validation.ok
    assert evaluation.can_store
    assert not evaluation.can_submit_for_clinician_review
