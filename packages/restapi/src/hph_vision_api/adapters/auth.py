from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ActorRole = Literal[
    "anonymous_user",
    "patient_user",
    "clinician_user",
    "admin_user",
    "internal_service",
]


@dataclass(frozen=True)
class Actor:
    id: str
    role: ActorRole
    authenticated: bool = False


def anonymous_actor() -> Actor:
    return Actor(id="anonymous", role="anonymous_user", authenticated=False)
