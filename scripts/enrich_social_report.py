#!/usr/bin/env python3
"""Enrich the reduced report with CRAP fields and dashboard filter metadata."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: enrich_social_report.py REDUCED_JSON WORKFLOW_JSON OUTPUT_JSON")

    reduced_path = Path(sys.argv[1])
    workflow_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    reduced = json.loads(reduced_path.read_text(encoding="utf-8"))
    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))

    research_sources: dict[str, dict] = {}
    for field in workflow.get("fields", []):
        for source in field.get("sources", []):
            url = source.get("url")
            if url:
                research_sources[canonical_url(url)] = source

    matched = 0
    for source in reduced.get("sources", []):
        url = source.get("url")
        match = research_sources.get(canonical_url(url)) if url else None
        if not match:
            continue
        for key in ("currency", "reliability", "authority", "purpose", "trust_score"):
            if key in match:
                source[key] = match[key]
        matched += 1

    signal_meta = {
        "TS-01": {"category": "Themenmarkt", "intensity": "hoch", "sentiment": "kritisch"},
        "TS-02": {"category": "Themenmarkt", "intensity": "hoch", "sentiment": "fordernd"},
        "TS-03": {"category": "Zielgruppen-Signale", "intensity": "hoch", "sentiment": "vorsichtig und prüfend"},
        "TS-04": {"category": "Zielgruppen-Signale", "intensity": "hoch", "sentiment": "besorgt und überfordert"},
        "TS-05": {"category": "Themenmarkt", "intensity": "mittel", "sentiment": "vorsichtig positiv"},
        "TS-06": {"category": "Zielgruppen-Signale", "intensity": "hoch", "sentiment": "angespannt und frustriert"},
        "TS-07": {"category": "Zielgruppen-Signale", "intensity": "mittel", "sentiment": "skeptisch und risikosensitiv"},
        "TS-08": {"category": "Eigene Marke", "intensity": "mittel", "sentiment": "gemischt"},
    }
    for signal in reduced.get("top_signals", []):
        signal.update(signal_meta.get(signal.get("id"), {}))
        signal["evidence_grade"] = signal.get("label", "Interpretation")
        signal["observation"] = signal.get("evidence", "")
        signal["business_implication"] = signal.get("business_consequence", "")

    reduced["data_quality"] = {
        "source_count": len(reduced.get("sources", [])),
        "crap_audits_matched": matched,
        "instagram_insights": "nicht verfügbar, da kein aktives Instagram-Konto ausgewählt ist",
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(reduced, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Enriched {matched} of {len(reduced.get('sources', []))} sources")


if __name__ == "__main__":
    main()
