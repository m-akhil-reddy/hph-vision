from __future__ import annotations

import re


def normalize_device_model_name(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", value.strip().lower())
    return re.sub(r"\s+", " ", normalized).strip()
