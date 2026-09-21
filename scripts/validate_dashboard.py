#!/usr/bin/env python3
"""Validate the generated dashboard, its data and archive references."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DashboardParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.scripts: list[str] = []
        self.styles: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                raise AssertionError(f"Doppelte ID: {element_id}")
            self.ids.add(element_id)
        href = attributes.get("href")
        if tag == "a" and href:
            self.hrefs.append(href)
        if tag == "script" and attributes.get("src"):
            self.scripts.append(str(attributes["src"]))
        if tag == "link" and attributes.get("rel") == "stylesheet" and href:
            self.styles.append(href)


def main() -> None:
    data = json.loads((ROOT / "data/social-listening/current.json").read_text(encoding="utf-8"))
    archive = json.loads((ROOT / "archiv/data/archive-index.json").read_text(encoding="utf-8"))
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    assert 5 <= len(data["top_signals"]) <= 8
    assert len(data["actions"]) == 3
    assert sorted(action["priority"] for action in data["actions"]) == ["P1", "P2", "P3"]
    assert all(isinstance(source.get("trust_score"), (int, float)) for source in data["sources"])
    assert all(all(source.get(key) for key in ("currency", "reliability", "authority", "purpose")) for source in data["sources"])

    source_ids = {source["id"] for source in data["sources"]}
    used_ids = {source_id for signal in data["top_signals"] for source_id in signal["source_ids"]}
    assert used_ids <= source_ids, f"Fehlende Quellen: {sorted(used_ids - source_ids)}"

    parser = DashboardParser()
    parser.feed(html)
    assert {"inhalt", "signale", "entscheidungen", "quellen", "archiv"} <= parser.ids
    assert "/assets/social-listening.css" in parser.styles
    assert "/assets/social-listening.js" in parser.scripts
    assert sum(href.startswith("http") for href in parser.hrefs) >= len(data["sources"])

    for entry in archive.get("eintraege", []):
        target = ROOT / entry["file"]
        assert target.is_file(), f"Archivdatei fehlt: {entry['file']}"
        assert target.stat().st_size > 0, f"Archivdatei ist leer: {entry['file']}"
        data_path = entry.get("data")
        if data_path:
            assert (ROOT / data_path).is_file(), f"Archivdaten fehlen: {data_path}"

    print(
        f"Validiert: {len(data['top_signals'])} Signale, "
        f"{len(data['actions'])} Massnahmen, {len(data['sources'])} Quellen, "
        f"{len(archive.get('eintraege', []))} Archiveinträge."
    )


if __name__ == "__main__":
    main()
