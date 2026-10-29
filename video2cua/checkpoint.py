"""Atomic, resumable stage outputs.

Each pipeline stage writes one JSON file into the work directory. A stage is
skipped when its file already exists, so a crashed or interrupted run resumes
from the last completed stage. Writes go to a temp file and are renamed into
place, so a stage file is either complete or absent.
"""

import json
import os
import tempfile
from pathlib import Path


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def read_json(path: Path):
    with open(path) as f:
        return json.load(f)
