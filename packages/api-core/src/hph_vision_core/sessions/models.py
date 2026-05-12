from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal, TypeAlias

if TYPE_CHECKING:
    from hph_vision_core.validation.result import ValidationResult

from hph_vision_core.device_profiles.models import DeviceProfile
from hph_vision_core.reliability.models import ReliabilityResult
from hph_vision_core.types import (
    DomainWarning,
    Eye,
    ResultRecommendation,
    dataclass_to_dict,
)

TriageRecommendation: TypeAlias = Literal[
    "continue",
    "seekProfessionalCare",
    "urgentCare",
]


@dataclass(frozen=True)
class ProtocolVersions:
    acuity: str | None = None
    refraction: str | None = None
    template: str | None = None
    report: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class ConsentRecord:
    type: str
    accepted: bool
    accepted_at: datetime | None
    text_version: str

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class TemplateMetadata:
    template_version: str
    generated_for_model: str
    page_size: str
    phone_body_width_mm: float
    phone_body_height_mm: float
    phone_thickness_mm: float
    cardboard_thickness_mm: float
    eye_to_screen_distance_mm: float

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class TriageResult:
    can_continue_self_test: bool
    red_flags: tuple[str, ...] = ()
    recommendation: TriageRecommendation = "continue"
    warnings: tuple[DomainWarning, ...] = ()
    unanswered_question_ids: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class AcuityResult:
    eye: Eye
    completed: bool
    confidence: float
    log_mar_estimate: float | None = None
    snellen_equivalent: str | None = None
    reliability_warnings: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class EyeRefractionEstimate:
    sphere: float | None = None
    cylinder: float | None = None
    axis: int | None = None
    spherical_equivalent: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class RefractionResult:
    confidence: float
    recommendation: ResultRecommendation
    right_eye: EyeRefractionEstimate | None = None
    left_eye: EyeRefractionEstimate | None = None
    binocular: EyeRefractionEstimate | None = None
    reliability_warnings: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class PatientContext:
    age_range: str | None = None
    current_glasses: bool | None = None
    previous_prescription: bool | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class EnvironmentContext:
    ambient_light_lux: float | None = None
    screen_brightness: float | None = None
    distance_confidence: float | None = None
    tilt_confidence: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class SessionSubmission:
    client_session_id: str
    created_at: datetime
    protocol_versions: ProtocolVersions
    consents: tuple[ConsentRecord, ...]
    app_version: str | None = None
    library_version: str | None = None
    device_profile: DeviceProfile | None = None
    template_metadata: TemplateMetadata | None = None
    triage_result: TriageResult | None = None
    acuity_results: tuple[AcuityResult, ...] = ()
    refraction_result: RefractionResult | None = None
    reliability: ReliabilityResult | None = None
    warnings: tuple[DomainWarning, ...] = ()
    patient_context: PatientContext | None = None
    environment: EnvironmentContext | None = None

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


@dataclass(frozen=True)
class SessionEvaluation:
    validation: ValidationResult
    can_store: bool
    can_submit_for_clinician_review: bool
    warnings: tuple[DomainWarning, ...]
    recommendation: ResultRecommendation

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)
