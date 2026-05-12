from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from hph_vision_core.types import dataclass_to_dict


@dataclass(frozen=True)
class DeviceProfile:
    id: str
    manufacturer: str
    model_name: str
    body_width_mm: float
    body_height_mm: float
    thickness_mm: float
    screen_width_px: int | None = None
    screen_height_px: int | None = None
    pixel_density: float | None = None
    screen_width_mm: float | None = None
    screen_height_mm: float | None = None
    template_family: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
