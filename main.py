#!/usr/bin/env python3
"""news-image-20261118 — "Sum up 18 November's world news in one image".

The artwork is image.png beside this file: a newspaper front page for
Wednesday 18 November 2026, drawn as a flat-illustration SVG (news.svg)
and rendered to PNG. This program copies the PNG, byte for byte, to
entry.png in the output directory, so both grader runs produce exactly
the same file. Standard library only; no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "image.png"
OUTPUT_NAME = "entry.png"


def output_dir() -> Path:
    # In the grader the output directory is /output; MAKEFUN_OUTPUT_DIR
    # stands in for it on a developer machine.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, target)
    # The entry is graded on the exact bytes written, and the program is
    # run twice: verify the copy landed whole so a short write can never
    # slip through as a corrupt image.
    if target.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("entry.png does not match image.png after copying")


if __name__ == "__main__":
    main()
