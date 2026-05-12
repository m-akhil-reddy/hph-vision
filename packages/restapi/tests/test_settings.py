from hph_vision_api.config import Settings


def test_settings_defaults_are_local_safe() -> None:
    settings = Settings(environment="test")

    assert settings.environment == "test"
    assert settings.auth_enabled is False
    assert settings.database_url is None
