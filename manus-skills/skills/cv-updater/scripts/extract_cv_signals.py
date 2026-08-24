#!/usr/bin/env python3
"""Extract possible CV signals from a local text file.

This helper is intentionally conservative. It does not decide what belongs in a CV;
it only surfaces lines that may contain roles, talks, publications, awards, dates,
or education-related information for human review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

KEYWORDS = [
    "keynote", "speaker", "vortrag", "referat", "panel", "moderation",
    "publication", "publikation", "book", "buch", "artikel", "paper",
    "award", "auszeichnung", "ranking", "top 100", "preis",
    "phd", "promotion", "msc", "master", "bachelor", "studium",
    "founder", "gründer", "ceo", "board", "advisor", "beirat",
    "project", "projekt", "mandate", "mandat", "client", "kunde",
    "podcast", "interview", "media", "presse", "television", "tv",
]

DATE_PATTERN = re.compile(r"\b(19|20)\d{2}\b|\b\d{1,2}[./-]\d{1,2}[./-](19|20)?\d{2}\b")


def score_line(line: str) -> int:
    text = line.lower()
    score = 0
    score += sum(1 for keyword in KEYWORDS if keyword in text)
    if DATE_PATTERN.search(line):
        score += 1
    if any(char.isdigit() for char in line):
        score += 1
    return score


def extract(path: Path, min_score: int = 2) -> list[tuple[int, int, str]]:
    results: list[tuple[int, int, str]] = []
    for number, raw_line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        line = " ".join(raw_line.strip().split())
        if not line or len(line) < 20:
            continue
        score = score_line(line)
        if score >= min_score:
            results.append((number, score, line))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract possible CV update signals from a local text file.")
    parser.add_argument("file", help="Path to a UTF-8 compatible text or markdown file")
    parser.add_argument("--min-score", type=int, default=2, help="Minimum signal score, default: 2")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists() or not path.is_file():
        raise SystemExit(f"File not found: {path}")

    print("line\tscore\ttext")
    for number, score, line in extract(path, args.min_score):
        print(f"{number}\t{score}\t{line}")


if __name__ == "__main__":
    main()
