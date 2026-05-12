from hph_vision_core.validation import (
    ValidationResult,
    combine_validation_results,
    validate_number_range,
    validation_error,
    validation_warning,
)


def test_validation_result_composition() -> None:
    result = combine_validation_results(
        ValidationResult(errors=(validation_error("bad", "Bad value", "field"),)),
        ValidationResult(
            warnings=(validation_warning("warn", "Check value", "field"),)
        ),
    )

    assert not result.ok
    assert [error.code for error in result.errors] == ["bad"]
    assert [warning.code for warning in result.warnings] == ["warn"]


def test_number_range_validation() -> None:
    assert validate_number_range(0.5, "score", 0, 1).ok
    result = validate_number_range(2, "score", 0, 1)

    assert not result.ok
    assert result.errors[0].field == "score"
