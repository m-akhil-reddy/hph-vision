from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from hph_vision_core.types import dataclass_to_dict

__version__ = "0.1.0"  # semantic-release
CORE_PACKAGE_NAME = "hph-vision-core"
RECOMMENDATION_POLICY_VERSION = "recommendation-policy-v0.1"
SCREENING_CONSENT_TEXT_VERSION = "screening-disclaimer-v0.1"
REVIEW_CONSENT_TEXT_VERSION = "clinician-review-consent-v0.1"

SUPPORTED_ACUITY_PROTOCOL_VERSION = "acuity-v0.1"
SUPPORTED_REFRACTION_PROTOCOL_VERSION = "refraction-v0.1"
SUPPORTED_TEMPLATE_PROTOCOL_VERSION = "template-v0.1"
SUPPORTED_REPORT_SCHEMA_VERSION = "report-v0.1"


@dataclass(frozen=True)
class SupportedProtocolVersions:
    acuity: str = SUPPORTED_ACUITY_PROTOCOL_VERSION
    refraction: str = SUPPORTED_REFRACTION_PROTOCOL_VERSION
    template: str = SUPPORTED_TEMPLATE_PROTOCOL_VERSION
    report: str = SUPPORTED_REPORT_SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return dataclass_to_dict(self)


def get_core_version() -> str:
    return __version__


def get_supported_protocol_versions() -> SupportedProtocolVersions:
    return SupportedProtocolVersions()
