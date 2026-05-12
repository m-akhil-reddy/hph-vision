from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from hph_vision_core.types import dataclass_to_dict


@dataclass(frozen=True)
class HealthStatus:
    service: str = "hph-vision"
    status: str = "ok"

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
