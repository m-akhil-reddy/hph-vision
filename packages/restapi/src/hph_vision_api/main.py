from __future__ import annotations

import uvicorn

from hph_vision_api.app import create_app

app = create_app()


def main() -> None:
    uvicorn.run("hph_vision_api.main:app", host="0.0.0.0", port=8000, reload=True)
