from __future__ import annotations

from pydantic import Field

from hph_vision_api.schemas.common import (
    ApiModel,
    DomainWarningSchema,
    ValidationResultSchema,
)


class SessionValidationResponse(ApiModel):
    validation: ValidationResultSchema
    recommendation: str
    can_store: bool = Field(alias="canStore")
    can_submit_for_clinician_review: bool = Field(alias="canSubmitForClinicianReview")
    warnings: list[DomainWarningSchema]
