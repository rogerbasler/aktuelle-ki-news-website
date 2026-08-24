#!/usr/bin/env python3
"""
extract_blog_content.py
Extrahiert strukturierte Carousel-Inhalte aus einem Blog-Text via OpenAI API.
Ausgabe: JSON mit Slide-Struktur für den AiGoodNews Carousel Creator.

Usage:
    python extract_blog_content.py --input blog.txt --output slides.json
    python extract_blog_content.py --url https://example.com/blog-post --output slides.json
"""

import argparse
import json
import sys
import os

try:
    from openai import OpenAI
except ImportError:
    print("openai package not found. Install with: sudo pip3 install openai")
    sys.exit(1)

SYSTEM_PROMPT = """Du bist ein Instagram-Content-Stratege für den Account @aigoodnews.
Deine Aufgabe: Extrahiere aus einem Blog-Artikel die 7–10 stärksten Kernaussagen und strukturiere sie
als Instagram Carousel-Slides im AiGoodNews-Stil.

Ausgabe-Format (JSON):
{
  "topic": "Kurzer Thementitel",
  "slides": [
    {
      "slide_number": 1,
      "type": "HOOK",
      "headline": "Kurze, kontraintuitive These (max. 8 Wörter)",
      "body": null
    },
    {
      "slide_number": 2,
      "type": "WUNDE",
      "headline": "Hauptaussage (max. 10 Wörter)",
      "body": "1–2 Sätze Kontext"
    },
    {
      "slide_number": 3,
      "type": "WARUM",
      "headline": "Überraschende Ursache (max. 10 Wörter)",
      "body": "1–2 Sätze"
    },
    {
      "slide_number": 4,
      "type": "WERT",
      "headline": "Insight-Titel",
      "body": "1–2 Sätze",
      "teaser": "Nächste Seite: ..."
    },
    ...
    {
      "slide_number": 8,
      "type": "AHA",
      "headline": "Grösste Erkenntnis",
      "body": null
    },
    {
      "slide_number": 9,
      "type": "SUMMARY",
      "headline": "Das Wichtigste",
      "points": ["Punkt 1", "Punkt 2", "Punkt 3"]
    }
  ],
  "caption": "Fertige Instagram-Caption mit Hook, Kontext, CTA und Hashtags"
}

Regeln:
- Schweizer Rechtschreibung (ä/ö/ü, kein ß)
- Ton: souverän, direkt, leicht pointiert — nie laut, kein Hype
- Keine Buzzwords ohne Substanz
- Slide 1 nie mit Frage ans Publikum öffnen
- Max. 4 Zeilen Text pro Slide (ausser Summary)
- Caption: Hook-Zeile, 2–3 Sätze Kontext, CTA, Leerzeilen, 5–8 Hashtags
"""

def extract_from_text(blog_text: str) -> dict:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Blog-Artikel:\n\n{blog_text}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )
    return json.loads(response.choices[0].message.content)

def extract_from_url(url: str) -> dict:
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("requests/beautifulsoup4 not found. Install with: sudo pip3 install requests beautifulsoup4")
        sys.exit(1)

    resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Entferne Navigation, Footer, Scripts
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    # Versuche Artikel-Content zu isolieren
    article = soup.find("article") or soup.find("main") or soup.find("body")
    text = article.get_text(separator="\n", strip=True) if article else soup.get_text(separator="\n", strip=True)

    # Kürze auf max. 8000 Zeichen
    text = text[:8000]
    return extract_from_text(text)

def main():
    parser = argparse.ArgumentParser(description="Extrahiere Carousel-Inhalte aus einem Blog")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="Pfad zur Blog-Textdatei")
    group.add_argument("--url", help="URL des Blog-Artikels")
    parser.add_argument("--output", required=True, help="Ausgabe-JSON-Datei")
    args = parser.parse_args()

    print(f"Extrahiere Carousel-Inhalte...")

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            blog_text = f.read()
        result = extract_from_text(blog_text)
    else:
        result = extract_from_url(args.url)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Fertig! Slides gespeichert in: {args.output}")
    print(f"Thema: {result.get('topic', 'N/A')}")
    print(f"Anzahl Slides: {len(result.get('slides', []))}")

if __name__ == "__main__":
    main()
