from __future__ import annotations

from hph_vision_core.device_profiles.models import DeviceProfile


def make_valid_device_profile() -> DeviceProfile:
    return DeviceProfile(
        id="generic-medium-phone",
        manufacturer="Generic",
        model_name="Medium phone",
        body_width_mm=72,
        body_height_mm=153,
        thickness_mm=8.5,
        screen_width_px=1170,
        screen_height_px=2532,
        pixel_density=3,
        screen_width_mm=68,
        screen_height_mm=145,
        template_family="generic-slab",
    )


def make_invalid_device_profile() -> DeviceProfile:
    return DeviceProfile(
        id="",
        manufacturer="",
        model_name="",
        body_width_mm=12,
        body_height_mm=40,
        thickness_mm=1,
        screen_width_px=-1,
        screen_height_px=0,
        pixel_density=0.1,
    )
