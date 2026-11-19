#!/usr/bin/env python3
"""Stub rclone: maps remote 'gdrive:path' to $FAKE_DRIVE/path. Supports lsjson, moveto."""
import json
import os
import shutil
import sys
from pathlib import Path

root = Path(os.environ["FAKE_DRIVE"])


def loc(r):
    return root / r.split(":", 1)[1].lstrip("/")


a = sys.argv[1:]
if a[0] == "lsjson":
    p = loc(a[-1])
    if not p.exists():
        sys.exit(3)
    print(json.dumps([{"Name": p.name, "Size": p.stat().st_size}]))
elif a[0] == "moveto":
    dst = loc(a[2]); dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(a[1], dst)
else:
    sys.exit(1)
