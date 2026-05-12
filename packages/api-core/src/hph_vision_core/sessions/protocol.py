from __future__ import annotations

from hph_vision_core.sessions.models import ProtocolVersions
from hph_vision_core.version import get_supported_protocol_versions


def get_default_protocol_versions() -> ProtocolVersions:
    supported = get_supported_protocol_versions()
    return ProtocolVersions(
        acuity=supported.acuity,
        refraction=supported.refraction,
        template=supported.template,
        report=supported.report,
    )
