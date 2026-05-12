from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from hph_vision_core.device_profiles.models import DeviceProfile
from hph_vision_core.reliability.models import ReliabilityResult
from hph_vision_core.sessions.models import (
    AcuityResult,
    ProtocolVersions,
    RefractionResult,
    TemplateMetadata,
)
from hph_vision_core.types import DomainWarning, ResultRecommendation, dataclass_to_dict


@dataclass(frozen=True)
class ScreeningReport:
    id: str
    session_id: str
    created_at: datetime
    recommendation: ResultRecommendation
    disclaimer: str
    reliability: ReliabilityResult
    warnings: tuple[DomainWarning, ...]
    acuity_results: tuple[AcuityResult, ...] = ()
    refraction_result: RefractionResult | None = None
    device_profile: DeviceProfile | None = None
    template_metadata: TemplateMetadata | None = None
    app_version: str | None = None
    library_version: str | None = None
    protocol_versions: ProtocolVersions | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
