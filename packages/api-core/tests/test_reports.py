from hph_vision_core.fixtures import FIXED_CREATED_AT, make_valid_session_submission
from hph_vision_core.reports import (
    SCREENING_DISCLAIMER,
    build_screening_report,
    validate_screening_report,
)


def test_build_screening_report_includes_required_disclaimer() -> None:
    report = build_screening_report(
        make_valid_session_submission(),
        report_id="report-test",
        created_at=FIXED_CREATED_AT,
    )

    assert report.disclaimer == SCREENING_DISCLAIMER
    assert report.recommendation == "clinician_review_recommended"
    assert validate_screening_report(report).ok
    assert report.to_dict()["created_at"].startswith("2026-05-12")
