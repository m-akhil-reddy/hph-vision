from __future__ import annotations

from hph_vision_api.schemas.common import ApiModel
from hph_vision_api.schemas.sessions import DeviceProfileSchema


class DeviceProfileListResponse(ApiModel):
    profiles: list[DeviceProfileSchema]


class DeviceProfileSearchResponse(ApiModel):
    profiles: list[DeviceProfileSchema]
    query: str
