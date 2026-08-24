#!/usr/bin/env python3
"""Turn the exported skill catalog into one Notion create-pages request."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DATA_SOURCE_ID = "463c1e6d-2f13-46b1-9bff-689603ea7c28"


def escape_text(value: str) -> str:
    for character in ("\\", "*", "~", "`", "$", "[", "]", "<", ">", "{", "}", "|", "^"):
        value = value.replace(character, f"\\{character}")
    return value


def page_content(record: dict[str, object], sync_date: str) -> str:
    description = escape_text(str(record["description"]))
    slug = escape_text(str(record["slug"]))
    checksum = str(record["tree_sha256"])
    github_url = str(record["github_url"])
    skill_file_url = str(record["skill_file_url"])
    return "\n".join(
        [
            "## Zweck",
            description,
            "## Referenz",
            f"[Skill-Ordner auf GitHub]({github_url})",
            f"[SKILL.md auf GitHub]({skill_file_url})",
            "## Synchronisationsdaten",
            f"**Sync-ID:** `manus:{slug}`",
            f"**Prüfsumme:** `{checksum}`",
            f"**Snapshot:** {sync_date}",
            "GitHub ist die versionierte technische Referenz. Notion dient als durchsuchbarer Katalog.",
        ]
    )


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: build_notion_create_payload.py CATALOG_JSON OUTPUT_JSON", file=sys.stderr)
        return 2

    catalog_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    sync_date = datetime.now(timezone.utc).date().isoformat()
    pages = []
    for record in catalog["skills"]:
        slug = str(record["slug"])
        pages.append(
            {
                "icon": "🧩",
                "properties": {
                    "Skill-Name": f"Manus · {slug}",
                    "Beschreibung": str(record["description"]),
                    "Einsatzgebiet": "Versionierter Manus-Skill mit GitHub-Referenz und monatlichem Katalogabgleich.",
                    "Kategorie": str(record["category"]),
                    "Output-Format": str(record["output_format"]),
                    "Trigger-Beispiele": str(record["trigger_examples"]),
                    "Sync-ID": f"manus:{slug}",
                    "GitHub-Quelle": str(record["github_url"]),
                    "Prüfsumme": str(record["tree_sha256"]),
                    "date:Letzter Sync:start": sync_date,
                    "date:Letzter Sync:is_datetime": 0,
                    "Status": "Aktiv",
                },
                "content": page_content(record, sync_date),
            }
        )

    payload = {
        "parent": {"data_source_id": DATA_SOURCE_ID},
        "allow_async": True,
        "pages": pages,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(pages)} Notion pages in {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
