from __future__ import annotations

from hph_vision_core.health.models import HealthStatus


def get_health_status() -> HealthStatus:
    return HealthStatus()
