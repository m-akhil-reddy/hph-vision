from __future__ import annotations

from hph_vision_core.clinician_review.models import ClinicianReviewEligibility
from hph_vision_core.sessions.models import SessionSubmission
from hph_vision_core.sessions.service import evaluate_session_submission
from hph_vision_core.sessions.validation import (
    REVIEW_CONSENT_TYPES,
    has_accepted_consent,
)
from hph_vision_core.validation.result import ValidationResult


def determine_clinician_review_eligibility(
    session: SessionSubmission,
) -> ClinicianReviewEligibility:
    evaluation = evaluate_session_submission(session)
    reasons: list[str] = []

    if not evaluation.validation.ok:
        reasons.append("invalid_session")
    if not has_accepted_consent(session.consents, REVIEW_CONSENT_TYPES):
        reasons.append("missing_review_consent")
    if not session.acuity_results and session.refraction_result is None:
        reasons.append("insufficient_test_data")
    if session.triage_result is not None and session.triage_result.red_flags:
        reasons.append("red_flags_require_professional_care")
    if session.reliability is None:
        reasons.append("missing_reliability")
    elif session.reliability.score < 0.35 or session.reliability.level == "invalid":
        reasons.append("invalid_reliability")
    elif session.reliability.score < 0.6 or session.reliability.level == "low":
        reasons.append("low_reliability")
    if evaluation.recommendation == "urgent_care_recommended":
        reasons.append("urgent_care_recommended")

    deduped_reasons = tuple(dict.fromkeys(reasons))
    return ClinicianReviewEligibility(
        eligible=not deduped_reasons,
        reasons=deduped_reasons,
        validation=evaluation.validation,
    )


def empty_eligibility() -> ClinicianReviewEligibility:
    return ClinicianReviewEligibility(
        eligible=False,
        reasons=("not_evaluated",),
        validation=ValidationResult(),
    )
