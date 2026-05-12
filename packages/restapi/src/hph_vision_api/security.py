from __future__ import annotations

from hph_vision_api.adapters.auth import Actor


def can_access_resource(_actor: Actor, _resource_owner_id: str | None = None) -> bool:
    return True
