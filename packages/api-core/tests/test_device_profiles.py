from hph_vision_core.device_profiles import (
    normalize_device_model_name,
    validate_device_profile,
)
from hph_vision_core.fixtures import (
    make_invalid_device_profile,
    make_valid_device_profile,
)


def test_valid_device_profile_passes_validation() -> None:
    assert validate_device_profile(make_valid_device_profile()).ok


def test_invalid_device_profile_returns_field_errors() -> None:
    result = validate_device_profile(make_invalid_device_profile())

    assert not result.ok
    fields = {error.field for error in result.errors}
    assert "id" in fields
    assert "body_width_mm" in fields


def test_normalize_device_model_name() -> None:
    assert normalize_device_model_name("  iPhone 15-Pro!! ") == "iphone 15 pro"
