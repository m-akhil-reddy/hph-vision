from __future__ import annotations

from hph_vision_api.schemas.common import ApiModel


class HealthResponse(ApiModel):
    service: str
    status: str


class ReadinessResponse(ApiModel):
    service: str
    status: str
    dependencies: dict[str, str]


class VersionResponse(ApiModel):
    service: str
    api_version: str
    core_version: str
    supported_protocol_versions: dict[str, str]
