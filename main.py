#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261125.

Copies the stored news-summary image (entry.png, in the same
directory as this file) to the output directory as entry.png.

Deterministic: the copy is byte-for-byte, with no timestamps,
no network and no randomness, so repeated runs produce identical
output. The image itself was rendered by build_image.py in this
same repo; this program only copies it.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing source image: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    # copyfile is byte-for-byte with no metadata copied, so the
    # output is identical on every run.
    shutil.copyfile(source, dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
