from __future__ import annotations

from hph_vision_core.sessions.models import ProtocolVersions
from hph_vision_core.validation.result import ValidationResult, valid, validation_error
from hph_vision_core.version import get_supported_protocol_versions


def validate_protocol_versions(versions: ProtocolVersions) -> ValidationResult:
    supported = get_supported_protocol_versions()
    errors = []
    comparisons = (
        ("acuity", versions.acuity, supported.acuity),
        ("refraction", versions.refraction, supported.refraction),
        ("template", versions.template, supported.template),
        ("report", versions.report, supported.report),
    )

    for field, submitted, expected in comparisons:
        if submitted is None:
            errors.append(
                validation_error(
                    "missing_protocol_version",
                    f"{field} protocol version is required.",
                    f"protocol_versions.{field}",
                )
            )
            continue
        if submitted != expected:
            errors.append(
                validation_error(
                    "unsupported_protocol_version",
                    (
                        f"Unsupported {field} protocol version {submitted!r}; "
                        f"expected {expected!r}."
                    ),
                    f"protocol_versions.{field}",
                )
            )

    return ValidationResult(errors=tuple(errors)) if errors else valid()
