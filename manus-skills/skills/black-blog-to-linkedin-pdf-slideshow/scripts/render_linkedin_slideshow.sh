#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  printf 'Verwendung: %s <input.html> <output-ordner>\n' "$0" >&2
  exit 64
fi

input_html="$1"
output_dir="$2"
pdf_path="$output_dir/linkedin_slideshow.pdf"
preview_dir="$output_dir/preview"
check_path="$output_dir/layout_pruefung.md"

if [[ ! -f "$input_html" ]]; then
  printf 'HTML-Datei nicht gefunden: %s\n' "$input_html" >&2
  exit 66
fi

if ! command -v weasyprint >/dev/null 2>&1; then
  printf 'WeasyPrint ist nicht installiert oder nicht im Pfad.\n' >&2
  exit 69
fi

if ! command -v pdftoppm >/dev/null 2>&1; then
  printf 'pdftoppm ist nicht installiert oder nicht im Pfad.\n' >&2
  exit 69
fi

mkdir -p "$output_dir" "$preview_dir"
weasyprint "$input_html" "$pdf_path"
pdftoppm -png -r 144 "$pdf_path" "$preview_dir/page" >/dev/null

page_count="$(pdfinfo "$pdf_path" | awk '/^Pages:/ {print $2}')"
sharp_s_count="$(grep -o "$(printf '\303\237')" "$input_html" | wc -l || true)"
em_dash_count="$(grep -o "$(printf '\342\200\224')" "$input_html" | wc -l || true)"

cat > "$check_path" <<EOF
# Layout-Prüfung

| Prüfung | Ergebnis | Nächste Aktion |
|---|---:|---|
| Gerenderte PDF-Seiten | ${page_count:-unbekannt} | Visuell Seite 1, 3, 6, 8 und 10 prüfen. |
| PNG-Vorschauen | $(find "$preview_dir" -maxdepth 1 -name 'page-*.png' | wc -l) | Lesbarkeit, Ränder und Überlagerungen prüfen. |
| Scharfes-S-Zeichen in HTML | $sharp_s_count | Für Schweizer Texte muss der Wert 0 sein. |
| Em-Dash-Zeichen in HTML | $em_dash_count | Für deutsche Roger-Texte muss der Wert 0 sein. |

## Manuelle Abnahme

- [ ] Hauptaussage jeder Seite ist ohne Zoom lesbar.
- [ ] Keine abgeschnittenen Elemente oder Textüberlagerungen.
- [ ] Quellenhinweise sind vorhanden und lesbar.
- [ ] Bildmotive stärken die Aussage statt sie nur zu dekorieren.
- [ ] Der LinkedIn-Post-Entwurf ist inhaltlich eigenständig und belegt.
EOF

printf 'PDF erzeugt: %s\n' "$pdf_path"
printf 'Vorschauen erzeugt: %s\n' "$preview_dir"
printf 'Prüfdatei erzeugt: %s\n' "$check_path"
