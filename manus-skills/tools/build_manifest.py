#!/usr/bin/env python3
"""Build reproducible catalog files for a local Manus skills directory."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Finanzen", ("finance", "stock", "polymarket")),
    ("Kommunikation", ("instagram", "linkedin", "social", "heygen", "canva", "commentor")),
    ("Kreativ & Design", ("image", "slides", "presentation", "video", "music", "suno", "graffiti", "pink", "sketchnote", "visual", "carousel")),
    ("Lernen & Entwicklung", ("book", "cv", "education", "content-to-slideshow", "ebook")),
    ("Recherche & Analyse", ("analysis", "analytics", "research", "backup", "data", "news", "similarweb")),
    ("Produktivität", ("automation", "config", "persistent", "mcp", "api", "webdev", "game", "workflow", "skill-creator", "typst")),
)

FORMAT_RULES: tuple[tuple[str, str], ...] = (
    ("pdf", "PDF"),
    ("html", "HTML"),
    ("csv", "CSV"),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_tree(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(sha256_file(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def front_matter_value(content: str, key: str) -> str:
    lines = content.splitlines()
    prefix = f"{key}:"
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = line[len(prefix):].strip().strip('"')
        if value not in {">", "|", ">-", "|-"}:
            return value
        continuation: list[str] = []
        for next_line in lines[index + 1:]:
            if not next_line.strip():
                continue
            if not next_line.startswith((" ", "\t")):
                break
            continuation.append(next_line.strip())
        return " ".join(continuation)
    return ""


def one_line_description(content: str) -> str:
    description = front_matter_value(content, "description")
    if description:
        return re.sub(r"\s+", " ", description)

    for line in content.splitlines():
        candidate = line.strip()
        if candidate and not candidate.startswith(("#", "---")):
            return re.sub(r"\s+", " ", candidate)
    return "Keine Kurzbeschreibung im Skill-Header vorhanden."


def classify(slug: str) -> str:
    lowered = slug.lower()
    for category, terms in CATEGORY_RULES:
        if any(term in lowered for term in terms):
            return category
    return "Produktivität"


def output_format(slug: str) -> str:
    lowered = slug.lower()
    for term, output in FORMAT_RULES:
        if term in lowered:
            return output
    return "Markdown"


def examples(slug: str) -> str:
    readable = slug.replace("-", " ")
    return f'"{readable}", "Hilfe mit {readable}"'


def build_records(source: Path, github_base_url: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for skill_file in sorted(source.glob("*/SKILL.md")):
        skill_dir = skill_file.parent
        slug = skill_dir.name
        content = skill_file.read_text(encoding="utf-8", errors="replace")
        files = [item for item in skill_dir.rglob("*") if item.is_file()]
        records.append(
            {
                "slug": slug,
                "display_name": front_matter_value(content, "name") or slug,
                "description": one_line_description(content),
                "category": classify(slug),
                "output_format": output_format(slug),
                "trigger_examples": examples(slug),
                "source_path": f"skills/{slug}",
                "github_url": f"{github_base_url}/tree/main/manus-skills/skills/{slug}",
                "skill_file_url": f"{github_base_url}/blob/main/manus-skills/skills/{slug}/SKILL.md",
                "file_count": len(files),
                "byte_size": sum(item.stat().st_size for item in files),
                "tree_sha256": sha256_tree(skill_dir),
            }
        )
    return records


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: build_manifest.py SOURCE_SKILLS_DIR OUTPUT_CATALOG_DIR GITHUB_REPOSITORY_URL", file=sys.stderr)
        return 2

    source = Path(sys.argv[1]).expanduser().resolve()
    output = Path(sys.argv[2]).expanduser().resolve()
    github_base_url = sys.argv[3].rstrip("/")
    if not source.is_dir():
        print(f"Source directory does not exist: {source}", file=sys.stderr)
        return 2

    output.mkdir(parents=True, exist_ok=True)
    records = build_records(source, github_base_url)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload = {
        "schema_version": 1,
        "generated_at": generated_at,
        "source_directory": str(source),
        "skill_count": len(records),
        "skills": records,
    }

    (output / "skills.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (output / "skills.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0].keys()) if records else ["slug"])
        writer.writeheader()
        writer.writerows(records)
    with (output / "notion-upsert.json").open("w", encoding="utf-8") as handle:
        json.dump({"generated_at": generated_at, "skills": records}, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"Generated catalog for {len(records)} skills in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
