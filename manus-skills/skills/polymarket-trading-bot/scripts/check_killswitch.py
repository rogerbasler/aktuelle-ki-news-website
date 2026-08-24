#!/usr/bin/env python3
from pathlib import Path
import sys


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("./state/KILLSWITCH")
    if path.exists():
        print(f"KILLSWITCH_ACTIVE {path}")
        return 10
    print(f"KILLSWITCH_INACTIVE {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
