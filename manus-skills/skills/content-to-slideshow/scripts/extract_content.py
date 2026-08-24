#!/usr/bin/env python3
"""
extract_content.py
Extrahiert strukturierte Slideshow-Inhalte aus einem Blog-Text via OpenAI API.
Ausgabe: JSON mit Slide-Struktur für den fragRoger Slideshow Creator.

Usage:
    python extract_content.py --input blog.txt --output slides.json
    python extract_content.py --url https://example.com/blog-post --output slides.json
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

SYSTEM_PROMPT = """Du bist ein Präsentations-Stratege für Roger Basler de Roca.
Deine Aufgabe: Extrahiere aus einem Blog-Artikel die stärksten Kernaussagen und strukturiere sie
als Präsentations-Slides im fragRoger Urban Graffiti Tech Stil.

Die Präsentation muss folgende Struktur haben:
1. Title Slide
2. Pain (Problem/Herausforderung)
3. Lichtblick (Lösung/Hoffnung)
4. Journey (90-Tage Transformation oder 3-Phasen Plan)
5. Roadmap (Übersicht der folgenden Kapitel)
6. Content Chapters (Die eigentlichen Inhalte aus dem Blog, 3-5 Slides)
7. Bonus (Zusätzlicher Wert)
8. Closing (Zusammenfassung & CTA)

Ausgabe-Format (JSON):
{
  "topic": "Kurzer Thementitel",
  "slides": [
    {
      "slide_number": 1,
      "type": "TITLE",
      "headline": "Prägnanter Titel",
      "subline": "Untertitel oder Tagline"
    },
    {
      "slide_number": 2,
      "type": "PAIN",
      "headline": "Kennst du das?",
      "points": ["Problem 1", "Problem 2", "Problem 3"]
    },
    {
      "slide_number": 3,
      "type": "LICHTBLICK",
      "headline": "Der Ausweg",
      "body": "Kurze Beschreibung der Lösung"
    },
    {
      "slide_number": 4,
      "type": "JOURNEY",
      "headline": "Die Transformation",
      "phases": ["Phase 1", "Phase 2", "Phase 3"]
    },
    {
      "slide_number": 5,
      "type": "ROADMAP",
      "headline": "Was dich erwartet",
      "chapters": ["Kapitel 1", "Kapitel 2", "Kapitel 3"]
    },
    {
      "slide_number": 6,
      "type": "CONTENT",
      "headline": "Inhaltstitel",
      "body": "1-2 Sätze",
      "takeaway": "Key Takeaway für die Bottom Bar"
    },
    ...
    {
      "slide_number": 10,
      "type": "CLOSING",
      "headline": "Zusammenfassung",
      "points": ["Punkt 1", "Punkt 2", "Punkt 3"]
    }
  ]
}

Regeln:
- Schweizer Rechtschreibung (ä/ö/ü, kein ß)
- Ton: souverän, direkt, leicht pointiert - nie laut, kein Hype
- Keine Buzzwords ohne Substanz
- Max. 2 Sätze Body-Text pro Slide (ausser Listen)
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

    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    article = soup.find("article") or soup.find("main") or soup.find("body")
    text = article.get_text(separator="\n", strip=True) if article else soup.get_text(separator="\n", strip=True)

    text = text[:8000]
    return extract_from_text(text)

def main():
    parser = argparse.ArgumentParser(description="Extrahiere Slideshow-Inhalte aus einem Blog")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="Pfad zur Blog-Textdatei")
    group.add_argument("--url", help="URL des Blog-Artikels")
    parser.add_argument("--output", required=True, help="Ausgabe-JSON-Datei")
    args = parser.parse_args()

    print(f"Extrahiere Slideshow-Inhalte...")

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
