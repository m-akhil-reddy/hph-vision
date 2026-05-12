from __future__ import annotations

from hph_vision_core.clinician_review.models import ReviewStatus
from hph_vision_core.validation.result import ValidationResult, valid, validation_error

ALLOWED_REVIEW_STATUS_TRANSITIONS: dict[ReviewStatus, tuple[ReviewStatus, ...]] = {
    "submitted": ("queued", "cancelled", "rejected", "expired"),
    "queued": ("in_review", "cancelled", "rejected", "expired"),
    "in_review": ("needs_more_information", "completed", "cancelled", "rejected"),
    "needs_more_information": ("in_review", "cancelled", "expired"),
    "completed": (),
    "cancelled": (),
    "rejected": (),
    "expired": (),
}


def validate_review_status_transition(
    current: ReviewStatus,
    next_status: ReviewStatus,
) -> ValidationResult:
    if next_status in ALLOWED_REVIEW_STATUS_TRANSITIONS[current]:
        return valid()
    return ValidationResult(
        errors=(
            validation_error(
                "invalid_review_status_transition",
                (
                    f"Cannot transition clinician review from {current!r} "
                    f"to {next_status!r}."
                ),
                "status",
            ),
        )
    )
