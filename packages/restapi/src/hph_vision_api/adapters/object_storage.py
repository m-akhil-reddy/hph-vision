from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ObjectStorageUrl:
    url: str
    expires_in_seconds: int
    method: str


class FakeObjectStorageAdapter:
    def create_upload_url(self, report_id: str) -> ObjectStorageUrl:
        return ObjectStorageUrl(
            url=f"memory://reports/{report_id}/upload",
            expires_in_seconds=900,
            method="PUT",
        )

    def create_download_url(self, report_id: str) -> ObjectStorageUrl:
        return ObjectStorageUrl(
            url=f"memory://reports/{report_id}/download",
            expires_in_seconds=900,
            method="GET",
        )
