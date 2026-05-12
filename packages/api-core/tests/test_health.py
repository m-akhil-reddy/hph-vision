from hph_vision_core import get_health_status


def test_get_health_status() -> None:
    assert get_health_status().to_dict() == {
        "service": "hph-vision",
        "status": "ok",
    }
