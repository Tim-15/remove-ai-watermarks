from __future__ import annotations

import os
from pathlib import Path


def unique_output_path(desired: str | Path) -> Path:
    """Return an unused output path without overwriting existing files."""
    path = Path(desired)

    if not os.path.lexists(path):
        return path

    for index in range(1, 100_000):
        candidate = path.with_name(
            f"{path.stem}_{index}{path.suffix}"
        )
        if not os.path.lexists(candidate):
            return candidate

    raise FileExistsError(
        f"No available output name for {path}"
    )
