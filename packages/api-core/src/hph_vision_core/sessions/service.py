from __future__ import annotations

from hph_vision_core.reliability import interpret_reliability
from hph_vision_core.sessions.models import SessionEvaluation, SessionSubmission
from hph_vision_core.sessions.recommendations import (
    RecommendationInput,
    determine_recommendation,
)
from hph_vision_core.sessions.validation import (
    REVIEW_CONSENT_TYPES,
    has_accepted_consent,
    validate_session_submission,
)
from hph_vision_core.types import DomainWarning
from hph_vision_core.validation.result import ValidationError


def validation_warning_to_domain_warning(warning: ValidationError) -> DomainWarning:
    return DomainWarning(
        code=warning.code,
        message=warning.message,
        severity="warning",
        source="validation",
    )


def aggregate_session_warnings(
    submission: SessionSubmission,
) -> tuple[DomainWarning, ...]:
    warnings: list[DomainWarning] = list(submission.warnings)
    if submission.triage_result is not None:
        warnings.extend(submission.triage_result.warnings)
    if submission.reliability is not None:
        warnings.extend(submission.reliability.warnings)
    return tuple({warning.code: warning for warning in warnings}.values())


def evaluate_session_submission(submission: SessionSubmission) -> SessionEvaluation:
    validation = validate_session_submission(submission)
    triage = submission.triage_result
    red_flags = triage.red_flags if triage is not None else ()
    urgent_red_flags = (
        triage.recommendation == "urgentCare" if triage is not None else False
    )
    reliability_interpretation = interpret_reliability(submission.reliability)
    has_results = (
        bool(submission.acuity_results) or submission.refraction_result is not None
    )
    completed = has_results and any(
        result.completed for result in submission.acuity_results
    )
    if submission.refraction_result is not None:
        completed = True
    refraction_confidence = (
        submission.refraction_result.confidence
        if submission.refraction_result is not None
        else None
    )
    all_warnings = (
        *aggregate_session_warnings(submission),
        *(
            validation_warning_to_domain_warning(warning)
            for warning in validation.warnings
        ),
    )
    has_critical_warnings = any(
        warning.severity == "critical" for warning in all_warnings
    )
    recommendation = determine_recommendation(
        RecommendationInput(
            has_red_flags=bool(red_flags),
            urgent_red_flags=urgent_red_flags,
            reliability_score=submission.reliability.score
            if submission.reliability is not None
            else None,
            refraction_confidence=refraction_confidence,
            completed=completed,
            has_critical_warnings=has_critical_warnings,
        )
    )
    can_store = validation.ok
    has_review_consent = has_accepted_consent(submission.consents, REVIEW_CONSENT_TYPES)
    can_submit_for_clinician_review = (
        can_store
        and has_review_consent
        and has_results
        and reliability_interpretation.can_interpret
        and not bool(red_flags)
        and recommendation == "clinician_review_recommended"
    )

    deduped_warnings = tuple(
        {warning.code: warning for warning in all_warnings}.values()
    )
    return SessionEvaluation(
        validation=validation,
        can_store=can_store,
        can_submit_for_clinician_review=can_submit_for_clinician_review,
        warnings=deduped_warnings,
        recommendation=recommendation,
    )
