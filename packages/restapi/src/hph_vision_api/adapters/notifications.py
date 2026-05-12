from __future__ import annotations


class NoopNotificationAdapter:
    def clinician_review_submitted(self, submission_id: str) -> None:
        _ = submission_id
