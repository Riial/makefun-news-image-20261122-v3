#!/usr/bin/env python3
"""Publish the finished front page for the make.fun news-image-20261122 v3 entry.

The front page was typeset once at build time and the finished image
(entry.png, 1024x1024, typeset text plus AI illustrations) is held in this
repository. This program copies that finished image into the output
directory, so repeated runs are byte-identical and need no network access.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
    python3 main.py                          # writes /output/entry.png
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} is missing", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
