#!/usr/bin/env python3
"""Archive the current social-listening dashboard before replacing its data."""

from __future__ import annotations

import json
import shutil
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CURRENT_DATA = ROOT / "data" / "social-listening" / "current.json"
CURRENT_HTML = ROOT / "index.html"
ARCHIVE_INDEX = ROOT / "archiv" / "data" / "archive-index.json"

MONTHS = {
    "januar": 1, "februar": 2, "märz": 3, "april": 4, "mai": 5, "juni": 6,
    "juli": 7, "august": 8, "september": 9, "oktober": 10, "november": 11, "dezember": 12,
}


def parse_german_date(value: str) -> date:
    parts = value.replace(".", "").split()
    if len(parts) != 3:
        raise ValueError(f"Nicht unterstütztes Datum: {value}")
    return date(int(parts[2]), MONTHS[parts[1].lower()], int(parts[0]))


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    if not CURRENT_DATA.exists() or not CURRENT_HTML.exists():
        print("Kein bestehender Social-Listening-Stand zum Archivieren.")
        return

    report = load_json(CURRENT_DATA)
    report_date = parse_german_date(str(report["generated_at"]))
    iso_year, iso_week, _ = report_date.isocalendar()
    archive_dir = ROOT / "archiv" / "social-listening" / str(iso_year)
    stem = f"kw{iso_week:02d}-{report_date.isoformat()}"
    html_target = archive_dir / f"{stem}.html"
    json_target = archive_dir / f"{stem}.json"
    archive_dir.mkdir(parents=True, exist_ok=True)

    if not html_target.exists():
        shutil.copy2(CURRENT_HTML, html_target)
    if not json_target.exists():
        shutil.copy2(CURRENT_DATA, json_target)

    archive = load_json(ARCHIVE_INDEX) if ARCHIVE_INDEX.exists() else {"version": 2, "eintraege": []}
    entries = archive.setdefault("eintraege", [])
    relative_html = html_target.relative_to(ROOT).as_posix()
    relative_json = json_target.relative_to(ROOT).as_posix()
    if not any(item.get("file") == relative_html for item in entries if isinstance(item, dict)):
        entries.insert(0, {
            "type": "Social Listening",
            "kw": f"{iso_week:02d}",
            "jahr": str(iso_year),
            "datum": report_date.isoformat(),
            "title": report.get("headline", f"Social Listening KW {iso_week:02d}/{iso_year}"),
            "file": relative_html,
            "data": relative_json,
        })
    archive["version"] = 2
    archive["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    ARCHIVE_INDEX.write_text(json.dumps(archive, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Archiviert: {relative_html} und {relative_json}")


if __name__ == "__main__":
    main()
