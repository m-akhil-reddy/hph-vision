from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from hph_vision_core.types import dataclass_to_dict

ValidationSeverity = Literal["error", "warning"]


@dataclass(frozen=True)
class ValidationError:
    code: str
    message: str
    field: str | None = None
    severity: ValidationSeverity = "error"

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple[ValidationError, ...] = ()
    warnings: tuple[ValidationError, ...] = ()

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)

    def with_error(
        self,
        code: str,
        message: str,
        field: str | None = None,
    ) -> ValidationResult:
        return ValidationResult(
            errors=(*self.errors, validation_error(code, message, field)),
            warnings=self.warnings,
        )

    def with_warning(
        self,
        code: str,
        message: str,
        field: str | None = None,
    ) -> ValidationResult:
        return ValidationResult(
            errors=self.errors,
            warnings=(*self.warnings, validation_warning(code, message, field)),
        )


def validation_error(
    code: str,
    message: str,
    field: str | None = None,
) -> ValidationError:
    return ValidationError(code=code, message=message, field=field, severity="error")


def validation_warning(
    code: str,
    message: str,
    field: str | None = None,
) -> ValidationError:
    return ValidationError(code=code, message=message, field=field, severity="warning")


def valid(*warnings: ValidationError) -> ValidationResult:
    return ValidationResult(warnings=warnings)


def invalid(
    *errors: ValidationError,
    warnings: tuple[ValidationError, ...] = (),
) -> ValidationResult:
    return ValidationResult(errors=errors, warnings=warnings)


def combine_validation_results(*results: ValidationResult) -> ValidationResult:
    errors: list[ValidationError] = []
    warnings: list[ValidationError] = []
    for result in results:
        errors.extend(result.errors)
        warnings.extend(result.warnings)
    return ValidationResult(errors=tuple(errors), warnings=tuple(warnings))
