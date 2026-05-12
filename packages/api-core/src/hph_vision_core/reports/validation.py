from __future__ import annotations

from hph_vision_core.reports.disclaimers import get_screening_disclaimer
from hph_vision_core.reports.models import ScreeningReport
from hph_vision_core.validation.result import ValidationResult, valid, validation_error


def validate_screening_report(report: ScreeningReport) -> ValidationResult:
    errors = []
    if not report.id.strip():
        errors.append(
            validation_error("missing_report_id", "Report id is required.", "id")
        )
    if not report.session_id.strip():
        errors.append(
            validation_error(
                "missing_session_id",
                "Report session id is required.",
                "session_id",
            )
        )
    if report.disclaimer != get_screening_disclaimer():
        errors.append(
            validation_error(
                "missing_required_disclaimer",
                "Report disclaimer does not match the required screening disclaimer.",
                "disclaimer",
            )
        )
    return ValidationResult(errors=tuple(errors)) if errors else valid()
