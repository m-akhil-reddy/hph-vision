from __future__ import annotations

from hph_vision_core.fixtures.sessions import (
    FIXED_CREATED_AT,
    make_valid_session_submission,
)
from hph_vision_core.reports.builder import build_screening_report
from hph_vision_core.reports.models import ScreeningReport


def make_valid_report() -> ScreeningReport:
    return build_screening_report(
        make_valid_session_submission(),
        report_id="report-fixture",
        created_at=FIXED_CREATED_AT,
    )
