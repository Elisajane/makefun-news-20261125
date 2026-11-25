#!/usr/bin/env python3
"""Hand over the entry image that ships with this repository.

The repository holds the finished picture as entry.png. This program
does nothing but copy that file, byte for byte, to the output folder
the harness expects, so the delivered image is always exactly the one
in the repository. It uses only the standard library, touches no
network, and writes the same bytes on every run.

The output folder comes from MAKEFUN_OUTPUT_DIR when that variable is
set to a non-empty value, and defaults to /output otherwise.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def bundled_image():
    """Return the path of the image shipped beside this program."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def output_folder():
    """Return the folder the copy goes to, from the environment or default."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if wanted.strip():
        return Path(wanted)
    return Path(DEFAULT_OUTPUT_DIR)


def main():
    source = bundled_image()
    if not source.is_file():
        print("missing bundled image:", source, file=sys.stderr)
        return 1
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / IMAGE_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        print("copy size mismatch:", target, file=sys.stderr)
        return 2
    print("wrote", target, target.stat().st_size, "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
