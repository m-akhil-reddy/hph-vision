from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from hph_vision_api.adapters.object_storage import FakeObjectStorageAdapter
from hph_vision_api.adapters.persistence import InMemoryRepository
from hph_vision_api.config import Settings, load_settings_from_env
from hph_vision_api.errors import configure_exception_handlers
from hph_vision_api.logging import configure_logging
from hph_vision_api.middleware import RequestIdMiddleware, SecurityHeadersMiddleware
from hph_vision_api.routers import (
    clinician_review_router,
    device_profiles_router,
    health_router,
    reports_router,
    sessions_router,
    validation_router,
    version_router,
)
from hph_vision_api.version import API_VERSION


def configure_middleware(app: FastAPI, settings: Settings) -> None:
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(RequestIdMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if settings.trusted_hosts != ["*"]:
        app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.trusted_hosts)


def include_routers(app: FastAPI, settings: Settings) -> None:
    app.include_router(health_router)
    app.include_router(version_router)
    app.include_router(sessions_router)
    app.include_router(reports_router)
    app.include_router(clinician_review_router)
    app.include_router(device_profiles_router)
    if settings.enable_internal_validation_endpoints:
        app.include_router(validation_router)


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or load_settings_from_env()
    configure_logging(resolved_settings)
    app = FastAPI(
        title="HPH Vision API",
        version=resolved_settings.api_version or API_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.state.settings = resolved_settings
    app.state.repository = InMemoryRepository()
    app.state.object_storage = FakeObjectStorageAdapter()
    configure_middleware(app, resolved_settings)
    configure_exception_handlers(app)
    include_routers(app, resolved_settings)
    return app
