#!/usr/bin/env python3
"""Create a working copy from the bundled FT006 LowPoly-Triangles PPTX template.

Usage:
  python create_working_copy.py /path/to/output.pptx
"""
from pathlib import Path
import shutil
import sys

SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_DIR / "templates" / "FT006_LowPoly-Triangles_16x9_DE.pptx"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python create_working_copy.py /path/to/output.pptx", file=sys.stderr)
        return 2
    output = Path(sys.argv[1]).expanduser().resolve()
    if output.suffix.lower() != ".pptx":
        print("Output path must end with .pptx", file=sys.stderr)
        return 2
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TEMPLATE, output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
