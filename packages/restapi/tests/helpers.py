from __future__ import annotations

from copy import deepcopy
from typing import Any


def valid_session_payload() -> dict[str, Any]:
    return {
        "clientSessionId": "mobile-session-test",
        "createdAt": "2026-05-12T00:00:00+00:00",
        "appVersion": "0.0.1",
        "libraryVersion": "0.0.1",
        "protocolVersions": {
            "acuity": "acuity-v0.1",
            "refraction": "refraction-v0.1",
            "template": "template-v0.1",
            "report": "report-v0.1",
        },
        "deviceProfile": {
            "id": "generic-medium-phone",
            "manufacturer": "Generic",
            "modelName": "Medium phone",
            "bodyWidthMm": 72,
            "bodyHeightMm": 153,
            "thicknessMm": 8.5,
            "screenWidthPx": 1170,
            "screenHeightPx": 2532,
            "pixelDensity": 3,
            "screenWidthMm": 68,
            "screenHeightMm": 145,
            "templateFamily": "generic-slab",
        },
        "templateMetadata": {
            "templateVersion": "template-v0.1",
            "generatedForModel": "Medium phone",
            "pageSize": "LETTER",
            "phoneBodyWidthMm": 72,
            "phoneBodyHeightMm": 153,
            "phoneThicknessMm": 8.5,
            "cardboardThicknessMm": 1.5,
            "eyeToScreenDistanceMm": 220,
        },
        "triageResult": {
            "canContinueSelfTest": True,
            "redFlags": [],
            "recommendation": "continue",
            "warnings": [],
            "unansweredQuestionIds": [],
        },
        "acuityResults": [
            {
                "eye": "right",
                "completed": True,
                "confidence": 0.86,
                "logMarEstimate": 0.1,
                "snellenEquivalent": "20/25",
                "reliabilityWarnings": [],
            }
        ],
        "refractionResult": {
            "confidence": 0.82,
            "recommendation": "clinician_review_recommended",
            "rightEye": {
                "sphere": -1.25,
                "cylinder": -0.5,
                "axis": 90,
                "sphericalEquivalent": -1.5,
            },
            "reliabilityWarnings": [],
        },
        "reliability": {"score": 0.84, "level": "high", "warnings": []},
        "warnings": [],
        "consents": [
            {
                "type": "screening",
                "accepted": True,
                "acceptedAt": "2026-05-12T00:00:00+00:00",
                "textVersion": "screening-disclaimer-v0.1",
            },
            {
                "type": "clinician_review",
                "accepted": True,
                "acceptedAt": "2026-05-12T00:00:00+00:00",
                "textVersion": "clinician-review-consent-v0.1",
            },
        ],
    }


def unsupported_protocol_payload() -> dict[str, Any]:
    payload = deepcopy(valid_session_payload())
    payload["protocolVersions"]["acuity"] = "acuity-v9"
    return payload
