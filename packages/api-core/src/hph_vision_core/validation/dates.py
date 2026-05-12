from __future__ import annotations

from datetime import datetime

from hph_vision_core.validation.result import ValidationResult, valid, validation_error


def parse_iso_datetime(value: str) -> datetime | None:
    try:
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def validate_iso_datetime(value: str | None, field: str) -> ValidationResult:
    if not value:
        return ValidationResult(
            errors=(
                validation_error("missing_datetime", f"{field} is required.", field),
            )
        )
    if parse_iso_datetime(value) is None:
        return ValidationResult(
            errors=(
                validation_error(
                    "invalid_datetime",
                    f"{field} must be an ISO 8601 datetime string.",
                    field,
                ),
            )
        )
    return valid()
