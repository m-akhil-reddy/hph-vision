from __future__ import annotations

from fastapi import status

from hph_vision_api.adapters.persistence import InMemoryRepository, SessionRecord
from hph_vision_api.errors import ApiError, api_error_from_validation
from hph_vision_api.schemas.sessions import SessionSubmissionRequest
from hph_vision_core import evaluate_session_submission


class SessionService:
    def __init__(self, repository: InMemoryRepository) -> None:
        self.repository = repository

    def submit_session(self, request: SessionSubmissionRequest) -> SessionRecord:
        submission = request.to_core()
        evaluation = evaluate_session_submission(submission)
        if not evaluation.validation.ok:
            raise api_error_from_validation(evaluation.validation)
        return self.repository.create_session(submission, evaluation)

    def get_session(self, session_id: str) -> SessionRecord:
        record = self.repository.get_session(session_id)
        if record is None:
            raise ApiError(
                code="not_found",
                message="Session was not found.",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return record

    def update_session_status(
        self,
        session_id: str,
        status_value: str,
    ) -> SessionRecord:
        record = self.repository.update_session_status(session_id, status_value)
        if record is None:
            raise ApiError(
                code="not_found",
                message="Session was not found.",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return record
