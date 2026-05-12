from __future__ import annotations

from math import isfinite

from hph_vision_core.validation.result import (
    ValidationResult,
    valid,
    validation_error,
)


def validate_number_range(
    value: float | int | None,
    field: str,
    minimum: float,
    maximum: float,
) -> ValidationResult:
    if value is None:
        return ValidationResult(
            errors=(validation_error("missing_number", f"{field} is required.", field),)
        )

    numeric_value = float(value)
    if not isfinite(numeric_value):
        return ValidationResult(
            errors=(
                validation_error(
                    "non_finite_number",
                    f"{field} must be finite.",
                    field,
                ),
            )
        )

    if numeric_value < minimum or numeric_value > maximum:
        return ValidationResult(
            errors=(
                validation_error(
                    "number_out_of_range",
                    f"{field} must be between {minimum:g} and {maximum:g}.",
                    field,
                ),
            )
        )

    return valid()


def validate_positive_mm(value: float | int | None, field: str) -> ValidationResult:
    return validate_number_range(value, field, 0.01, 10000)


def validate_positive_int(value: int | None, field: str) -> ValidationResult:
    if value is None:
        return valid()
    if value <= 0:
        return ValidationResult(
            errors=(
                validation_error(
                    "integer_not_positive",
                    f"{field} must be a positive integer.",
                    field,
                ),
            )
        )
    return valid()


def validate_unit_interval(value: float | int | None, field: str) -> ValidationResult:
    return validate_number_range(value, field, 0, 1)
