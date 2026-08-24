#!/usr/bin/env python3
"""
extract_blog_content.py
Extrahiert strukturierte Carousel-Inhalte aus einem Blog-Text via OpenAI API.
Ausgabe: JSON mit 10 Slides für den fragRoger Black Cinematic Carousel Creator.

Usage:
    python extract_blog_content.py --input blog.txt --output slides.json
    python extract_blog_content.py --url https://example.com/blog-post --output slides.json
"""

import argparse
import json
import sys

try:
    from openai import OpenAI
except ImportError:
    print("openai package not found. Install with: sudo pip3 install openai")
    sys.exit(1)

SYSTEM_PROMPT = """Du bist ein Instagram-Content-Stratege für den Account @fragroger (Roger Basler de Roca).
Deine Aufgabe: Verwandle einen Blog-Artikel in ein direkt veröffentlichbares Instagram Carousel im fragRoger Black Cinematic TED-Talk-Stil.

WICHTIG:
- Erzeuge exakt 10 Slides.
- Slide 1 ist immer ein HOOK / PATTERN INTERRUPT und muss später visuell mit einem Bild umgesetzt werden.
- Schreibe kurz, prägnant, konversationell und leicht dramatisch.
- Jede Slide erzeugt Momentum.
- Keine Erklärungen ausserhalb der JSON-Struktur.
- Keine Unterstrich-Metaphern, keine Trennlinien-Hinweise, keine Divider-Anweisungen.

Ausgabe-Format (JSON):
{
  "topic": "Kurzer Thementitel",
  "slides": [
    {
      "slide_number": 1,
      "type": "HOOK",
      "headline": "Mutige, kontroverse oder neugiergetriebene Aussage mit 5-10 Wörtern",
      "body": null,
      "visual_note": "Bildpflicht: Nutzerbild verwenden oder KI-Hero-Bild erzeugen"
    },
    {
      "slide_number": 2,
      "type": "REHOOK",
      "headline": "Open Loop, der die Spannung erhöht",
      "body": "1 kurze Zeile, keine Antwort liefern"
    },
    {
      "slide_number": 3,
      "type": "RELATABLE PAIN / STORY START",
      "headline": "Die meisten denken... / Alle machen diesen Fehler...",
      "body": "1 kurze, nachvollziehbare Situation"
    },
    {
      "slide_number": 4,
      "type": "VALUE",
      "headline": "Erste zentrale Idee",
      "body": "1 kurze Insight-Zeile"
    },
    {
      "slide_number": 5,
      "type": "VALUE",
      "headline": "Zweite zentrale Idee",
      "body": "1 kurze Insight-Zeile"
    },
    {
      "slide_number": 6,
      "type": "VALUE",
      "headline": "Dritte zentrale Idee",
      "body": "1 kurze Insight-Zeile"
    },
    {
      "slide_number": 7,
      "type": "VALUE",
      "headline": "Vierte zentrale Idee",
      "body": "1 kurze Insight-Zeile"
    },
    {
      "slide_number": 8,
      "type": "TURNING POINT",
      "headline": "Zentrale Erkenntnis oder Perspektivenverschiebung",
      "body": "Speichern-wertiger Aha-Satz"
    },
    {
      "slide_number": 9,
      "type": "ACTIONABLE TAKEAWAY",
      "headline": "Was Du jetzt tun solltest",
      "points": ["Schritt 1", "Schritt 2", "Schritt 3"]
    },
    {
      "slide_number": 10,
      "type": "CTA",
      "headline": "Starker Engagement Trigger",
      "body": "Kommentiere, folge, speichere oder teile"
    }
  ],
  "caption": "Fertige Instagram-Caption mit Hook, Kontext, Implikation, fragroger.ai und #fragRoger"
}

CAROUSEL-STRUKTUR:
Slide 1 - HOOK (Pattern Interrupt): mutige, kontroverse oder neugiergetriebene Aussage. Erzeuge beim Leser: Moment... was? Maximal 5-10 Wörter.
Slide 2 - REHOOK (Open Loop): Spannung erhöhen, Ergebnis anteasern, Neugier-Lücke vergrössern.
Slide 3 - RELATABLE PAIN / STORY START: kurze nachvollziehbare Situation oder Story. Nutze Formulierungen wie: Die meisten denken..., Alle machen diesen Fehler..., Ich habe früher...
Slides 4-7 - VALUE (Story + Insights): erzählerischer Flow, Erwartungen brechen, Erkenntnisse schrittweise aufbauen, 1 zentrale Idee pro Slide.
Slide 8 - TURNING POINT (AHA-MOMENT): zentrale Erkenntnis oder Perspektivenverschiebung, speichern-wertig.
Slide 9 - ACTIONABLE TAKEAWAY: klare, sofort anwendbare Schritte oder Empfehlungen.
Slide 10 - CTA (Engagement Trigger): starke Handlungsaufforderung, z. B. Kommentiere..., Folge für mehr..., Speichere das...

PSYCHOLOGISCHE TRIGGER:
Nutze Neugier-Lücke, Pattern Interrupt, Social-Proof-Tonalität, FOMO, konträre Perspektiven und Quick Wins. Kein billiger Clickbait. Substanz zuerst, Drama kontrolliert dosiert.

SPRACHE:
- Schweizer Rechtschreibung: ä/ö/ü, kein ß.
- Keine EM Dashes, nur einfache Bindestriche.
- Kurz und prägnant.
- Maximal 1-2 Zeilen pro Slide, ausser Slide 9.
- Keine Buzzwords ohne Substanz.
- Schreibe, als würdest Du mit einer Person sprechen.
- Caption: Hook-Zeile, 2-3 Sätze Kontext, Implikation für Entscheider:innen, Mehr dazu auf fragroger.ai, am Ende nur #fragRoger.
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
    parser = argparse.ArgumentParser(description="Extrahiere Carousel-Inhalte aus einem Blog")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="Pfad zur Blog-Textdatei")
    group.add_argument("--url", help="URL des Blog-Artikels")
    parser.add_argument("--output", required=True, help="Ausgabe-JSON-Datei")
    args = parser.parse_args()

    print("Extrahiere Carousel-Inhalte...")

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
