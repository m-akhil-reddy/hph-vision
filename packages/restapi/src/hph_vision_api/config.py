from __future__ import annotations

from dataclasses import dataclass, field
from os import getenv
from typing import Literal, TypeAlias, cast

Environment: TypeAlias = Literal["local", "test", "staging", "production"]


def _split_csv(value: str | None, default: list[str]) -> list[str]:
    if value is None or not value.strip():
        return default
    return [item.strip() for item in value.split(",") if item.strip()]


def _get_bool(name: str, default: bool) -> bool:
    value = getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    environment: Environment = "local"
    api_version: str = "0.1.0"
    log_level: str = "INFO"
    cors_allowed_origins: list[str] = field(default_factory=lambda: ["*"])
    trusted_hosts: list[str] = field(default_factory=lambda: ["*"])
    auth_enabled: bool = False
    database_url: str | None = None
    object_storage_bucket: str | None = None
    max_report_upload_mb: int = 10
    enable_internal_validation_endpoints: bool = True

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


def load_settings_from_env() -> Settings:
    environment = getenv("HPH_ENVIRONMENT", "local").strip().lower()
    if environment not in {"local", "test", "staging", "production"}:
        environment = "local"

    return Settings(
        environment=cast(Environment, environment),
        api_version=getenv("HPH_API_VERSION", "0.1.0"),
        log_level=getenv("HPH_LOG_LEVEL", "INFO"),
        cors_allowed_origins=_split_csv(
            getenv("HPH_CORS_ALLOWED_ORIGINS"),
            ["*"],
        ),
        trusted_hosts=_split_csv(getenv("HPH_TRUSTED_HOSTS"), ["*"]),
        auth_enabled=_get_bool("HPH_AUTH_ENABLED", False),
        database_url=getenv("HPH_DATABASE_URL"),
        object_storage_bucket=getenv("HPH_OBJECT_STORAGE_BUCKET"),
        max_report_upload_mb=int(getenv("HPH_MAX_REPORT_UPLOAD_MB", "10")),
        enable_internal_validation_endpoints=_get_bool(
            "HPH_ENABLE_INTERNAL_VALIDATION_ENDPOINTS",
            True,
        ),
    )
