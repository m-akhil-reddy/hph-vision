from __future__ import annotations

from typing import TYPE_CHECKING

from hph_vision_core.validation.dates import parse_iso_datetime, validate_iso_datetime
from hph_vision_core.validation.numeric import (
    validate_number_range,
    validate_positive_int,
    validate_positive_mm,
    validate_unit_interval,
)
from hph_vision_core.validation.result import (
    ValidationError,
    ValidationResult,
    combine_validation_results,
    invalid,
    valid,
    validation_error,
    validation_warning,
)

if TYPE_CHECKING:
    from hph_vision_core.sessions.models import ProtocolVersions


def validate_protocol_versions(versions: ProtocolVersions) -> ValidationResult:
    from hph_vision_core.validation.protocols import (
        validate_protocol_versions as _validate_protocol_versions,
    )

    return _validate_protocol_versions(versions)


__all__ = [
    "ValidationError",
    "ValidationResult",
    "combine_validation_results",
    "invalid",
    "parse_iso_datetime",
    "valid",
    "validate_iso_datetime",
    "validate_number_range",
    "validate_positive_int",
    "validate_positive_mm",
    "validate_protocol_versions",
    "validate_unit_interval",
    "validation_error",
    "validation_warning",
]
