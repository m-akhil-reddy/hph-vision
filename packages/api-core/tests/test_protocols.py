from hph_vision_core.sessions import ProtocolVersions, get_default_protocol_versions
from hph_vision_core.validation.protocols import validate_protocol_versions


def test_default_protocol_versions_are_supported() -> None:
    assert validate_protocol_versions(get_default_protocol_versions()).ok


def test_unsupported_protocol_version_is_error() -> None:
    result = validate_protocol_versions(
        ProtocolVersions(
            acuity="acuity-v9",
            refraction="refraction-v0.1",
            template="template-v0.1",
            report="report-v0.1",
        )
    )

    assert not result.ok
    assert result.errors[0].code == "unsupported_protocol_version"
