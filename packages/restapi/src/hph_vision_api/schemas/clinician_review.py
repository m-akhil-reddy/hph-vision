from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from hph_vision_api.schemas.common import ApiModel

ReviewStatusLiteral = Literal[
    "submitted",
    "queued",
    "in_review",
    "needs_more_information",
    "completed",
    "cancelled",
    "rejected",
    "expired",
]


class ClinicianReviewCreateRequest(ApiModel):
    session_id: str = Field(alias="sessionId")


class ClinicianReviewSubmissionResponse(ApiModel):
    id: str
    session_id: str = Field(alias="sessionId")
    status: ReviewStatusLiteral
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    reasons: list[str] = Field(default_factory=list)


class ClinicianReviewStatusResponse(ApiModel):
    id: str
    status: ReviewStatusLiteral
    updated_at: datetime = Field(alias="updatedAt")
