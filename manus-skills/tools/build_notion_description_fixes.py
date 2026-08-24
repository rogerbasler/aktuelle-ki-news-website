#!/usr/bin/env python3
"""Create targeted Notion property updates for placeholder descriptions."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: build_notion_description_fixes.py CATALOG_JSON TASK_RESULT_JSON OUTPUT_DIR", file=sys.stderr)
        return 2

    catalog = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    task = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    output = Path(sys.argv[3])
    output.mkdir(parents=True, exist_ok=True)

    descriptions = {f"manus:{skill['slug']}": skill["description"] for skill in catalog["skills"]}
    fixes = 0
    for page in task["result"]["pages"]:
        if page["properties"].get("Beschreibung") not in {">", ">-", "|", "|-"}:
            continue
        sync_id = page["properties"]["Sync-ID"]
        payload = {
            "page_id": page["id"],
            "command": "update_properties",
            "properties": {"Beschreibung": descriptions[sync_id]},
        }
        target = output / f"{sync_id.replace(':', '_')}.json"
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        fixes += 1

    print(f"Prepared {fixes} targeted description fixes in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
