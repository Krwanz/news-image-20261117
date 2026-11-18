#!/usr/bin/env python3
"""news-image-20261117 entry: write the poster to /output/entry.png.

The poster (entry.png beside this file) sums up Tuesday 17 November
2026's world news in one image. This program just copies it to the
output directory, so both grader runs write the same bytes.

Runs with no network, standard library only. Outside the grader's
container MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    with open(dst, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a whole PNG")
    if size > 1048576:
        raise SystemExit("entry.png is over the 1 MiB cap")
    print("wrote {} ({} bytes)".format(dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
