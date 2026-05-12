from __future__ import annotations


class HphVisionCoreError(Exception):
    """Base exception for unexpected hph-vision-core failures."""


class SerializationError(HphVisionCoreError):
    """Raised when a domain object cannot be serialized."""
