from __future__ import annotations

from hph_vision_core.device_profiles.models import DeviceProfile
from hph_vision_core.validation.numeric import (
    validate_number_range,
    validate_positive_int,
)
from hph_vision_core.validation.result import (
    ValidationResult,
    combine_validation_results,
    valid,
    validation_error,
)


def validate_device_profile(profile: DeviceProfile) -> ValidationResult:
    results = [
        validate_number_range(profile.body_width_mm, "body_width_mm", 40, 120),
        validate_number_range(profile.body_height_mm, "body_height_mm", 80, 230),
        validate_number_range(profile.thickness_mm, "thickness_mm", 3, 25),
        validate_positive_int(profile.screen_width_px, "screen_width_px"),
        validate_positive_int(profile.screen_height_px, "screen_height_px"),
        validate_number_range(profile.pixel_density, "pixel_density", 0.5, 10)
        if profile.pixel_density is not None
        else valid(),
        validate_number_range(profile.screen_width_mm, "screen_width_mm", 20, 120)
        if profile.screen_width_mm is not None
        else valid(),
        validate_number_range(profile.screen_height_mm, "screen_height_mm", 40, 230)
        if profile.screen_height_mm is not None
        else valid(),
    ]
    combined = combine_validation_results(*results)
    errors = list(combined.errors)

    if not profile.id.strip():
        errors.append(
            validation_error(
                "missing_device_id",
                "Device profile id is required.",
                "id",
            )
        )
    if not profile.manufacturer.strip():
        errors.append(
            validation_error(
                "missing_manufacturer",
                "Device manufacturer is required.",
                "manufacturer",
            )
        )
    if not profile.model_name.strip():
        errors.append(
            validation_error(
                "missing_model_name",
                "Device model name is required.",
                "model_name",
            )
        )

    return ValidationResult(errors=tuple(errors), warnings=combined.warnings)
