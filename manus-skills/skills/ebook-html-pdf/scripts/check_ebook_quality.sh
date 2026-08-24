#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <ebook.html> <ebook.pdf> [required_link_1 required_link_2 ...]"
  exit 1
fi

HTML_FILE="$1"
PDF_FILE="$2"
shift 2

if [ ! -f "$HTML_FILE" ]; then
  echo "HTML file not found: $HTML_FILE"
  exit 1
fi

if [ ! -f "$PDF_FILE" ]; then
  echo "PDF file not found: $PDF_FILE"
  exit 1
fi

echo "== eBook Quality Check =="
echo "HTML: $HTML_FILE"
echo "PDF:  $PDF_FILE"
echo

if command -v pdfinfo >/dev/null 2>&1; then
  echo -n "Pages: "
  pdfinfo "$PDF_FILE" | awk '/Pages/ {print $2}'
else
  echo "Pages: pdfinfo not available"
fi

echo -n "Em dash count: "
grep -o '—' "$HTML_FILE" | wc -l || true

echo -n "Sharp-s count: "
grep -o 'ß' "$HTML_FILE" | wc -l || true

echo -n "HTML table count: "
grep -oi '<table' "$HTML_FILE" | wc -l || true

echo -n "Page section count: "
grep -oi '<section class="page"' "$HTML_FILE" | wc -l || true

if [ "$#" -gt 0 ]; then
  echo
  echo "Required link checks:"
  for link in "$@"; do
    count=$(grep -oi "$link" "$HTML_FILE" | wc -l || true)
    echo "$link: $count"
  done
fi
