from __future__ import annotations

from datetime import datetime

from hph_vision_core.reliability.models import ReliabilityResult
from hph_vision_core.reports.disclaimers import get_screening_disclaimer
from hph_vision_core.reports.models import ScreeningReport
from hph_vision_core.reports.warnings import dedupe_warnings
from hph_vision_core.sessions.models import SessionSubmission
from hph_vision_core.sessions.recommendations import (
    RecommendationInput,
    determine_recommendation,
)
from hph_vision_core.types import DomainWarning


def fallback_reliability() -> ReliabilityResult:
    warning = DomainWarning(
        code="reliability.missing",
        message="No reliability result was submitted; report reliability is invalid.",
        severity="critical",
        source="report",
    )
    return ReliabilityResult(score=0, level="invalid", warnings=(warning,))


def build_screening_report(
    session: SessionSubmission,
    *,
    report_id: str,
    created_at: datetime,
) -> ScreeningReport:
    reliability = session.reliability or fallback_reliability()
    triage = session.triage_result
    red_flags = triage.red_flags if triage is not None else ()
    urgent_red_flags = (
        triage.recommendation == "urgentCare" if triage is not None else False
    )
    completed = bool(session.acuity_results) or session.refraction_result is not None
    warnings = dedupe_warnings(
        (
            *session.warnings,
            *(triage.warnings if triage is not None else ()),
            *reliability.warnings,
        )
    )
    recommendation = determine_recommendation(
        RecommendationInput(
            has_red_flags=bool(red_flags),
            urgent_red_flags=urgent_red_flags,
            reliability_score=reliability.score,
            refraction_confidence=session.refraction_result.confidence
            if session.refraction_result is not None
            else None,
            completed=completed,
            has_critical_warnings=any(
                warning.severity == "critical" for warning in warnings
            ),
        )
    )

    return ScreeningReport(
        id=report_id,
        session_id=session.client_session_id,
        created_at=created_at,
        app_version=session.app_version,
        library_version=session.library_version,
        protocol_versions=session.protocol_versions,
        device_profile=session.device_profile,
        template_metadata=session.template_metadata,
        acuity_results=session.acuity_results,
        refraction_result=session.refraction_result,
        reliability=reliability,
        warnings=warnings,
        recommendation=recommendation,
        disclaimer=get_screening_disclaimer(),
    )
