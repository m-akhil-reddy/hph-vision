from fastapi.testclient import TestClient

from hph_vision_api.app import create_app
from hph_vision_api.config import Settings


def test_health_check() -> None:
    client = TestClient(create_app(Settings(environment="test")))

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"service": "hph-vision", "status": "ok"}


def test_version_endpoint() -> None:
    client = TestClient(create_app(Settings(environment="test")))

    response = client.get("/api/v1/version")

    assert response.status_code == 200
    assert response.json()["api_version"] == "0.1.0"
    assert response.json()["core_version"] == "0.1.0"
