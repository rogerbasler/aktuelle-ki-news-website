---
name: aigoodnews-to-instagram
description: >
  Wandelt Blog-Artikel oder Texte in fertige Instagram Carousel-Posts im AiGoodNews CI/CD um.
  Verwende diesen Skill immer wenn der Nutzer: einen Blog in einen AiGoodNews-Post umwandeln will,
  "AiGoodNews Skill", "AiGoodNews Carousel", "AiGoodNews Post", "gute News zu Instagram" sagt.
  Output: 10 AI-generierte Slide-Bilder (480×600px) im AiGoodNews Graffiti-TEDx-Design (Grün/Gold/Dunkel) + Caption + direkter Post via Instagram MCP.
  Das erste Slide (Hook) enthält immer ein AI-generiertes Bild als Hintergrund.
---

# AiGoodNews-to-Instagram Carousel

## Workflow-Übersicht

1. **Blog-Inhalt aufnehmen** - Text, URL oder Datei
2. **Kernaussagen extrahieren** - via `extract_blog_content.py` -> `slides.json`
3. **10 Slide-Bilder generieren** - via `map`-Tool parallel, AiGoodNews-Stil (Grün/Gold/Dunkel). **Slide 1 hat ein AI-generiertes Bild als Hintergrund.**
4. **Caption verfassen** - Hook + Kontext + CTA + `#AiGoodNews`
5. **Bilder hochladen** - via `manus-upload-file` -> CDN-URLs
6. **Direkt posten** - via Instagram MCP `create_instagram`

---

## Schritt 1: Blog-Inhalt aufnehmen

Akzeptiere den Blog als Text, URL oder Datei (`.txt`, `.md`, `.html`).

---

## Schritt 2: Kernaussagen extrahieren

```bash
python /home/ubuntu/skills/aigoodnews-to-instagram/scripts/extract_blog_content.py \
  --input blog.txt --output slides.json
```

Das Script liefert JSON mit Slide-Struktur (10 Slides) und Caption-Entwurf.

### Carousel-Struktur (immer 10 Slides)

| Slide | Typ | Inhalt |
|---|---|---|
| 1 | HOOK | 1 kontraintuitive These. Sticker-Badge. **Hintergrund ist ein AI-generiertes Bild passend zum Thema.** |
| 2 | WUNDE | Leser erkennt sich. Headline + 1–2 Sätze Body. |
| 3 | WARUM | Überraschende Ursache. Deep Dark Blue/Green Hintergrund. |
| 4–7 | WERT | 1 Insight pro Slide. Deko-Nummer. Teaser unten rechts. |
| 8 | AHA | Grösste Erkenntnis. Zentriert. Gold als einziger Akzent. |
| 9 | SUMMARY | Max. 3 Punkte. Checkmarks in `#00ff88`. Deep Dark Blue/Green Hintergrund. |
| 10 | CTA | **Fixe Slide - IMMER IDENTISCH** (siehe `references/brand-design.md`). |

---

## Schritt 3: Slide-Bilder generieren (via `map`-Tool)

**Standard-Methode: AI-Bildgenerierung parallel via `map`-Tool** - kein HTML, keine CSS-Slides.

Jeder Prompt beschreibt exakt eine 480×600px Slide. Alle 10 Prompts werden parallel generiert.

### Prompt-Vorlage pro Slide

```
Generate a single Instagram carousel slide image (480x600px, 4:5 ratio) in the AiGoodNews brand style.

DESIGN SYSTEM:
- Style: Urban Graffiti Wall meets TEDx typography - dark, bold, high-energy
- Background: Deep dark blue/green #0a192f or pure black #000000 (as specified per slide). FOR SLIDE 1 ONLY: The background must be a stunning, high-quality AI-generated photo relevant to the topic, darkened to allow text readability.
- Font: Avenir Next / Barlow Condensed 900 - massive, UPPERCASE, condensed headlines
- Brand colors: Neon Green #00ff88, Neon Gold #ffd700, White #ffffff
- Graffiti elements: Large rotated ghost-word in background (very low opacity, green/white),
  spray-paint neon glow on divider lines, neon glow on key words
- Top edge: thin gradient bar from gold (#ffd700) to green (#00ff88)
- Slide counter top-right in small monospace font (e.g. "3 / 10")
- Bottom-right: small arrow teaser in monospace (if applicable)
- NO borders, NO rounded cards, NO gradients on background (except Slide 1 photo)
- Text MUST be fully contained within the 480x600px frame — nothing cut off

SLIDE TO GENERATE:
[SLIDE DESCRIPTION]

OUTPUT: Generate exactly this one slide as a clean 480x600px image. Sharp, readable, fully inside frame.
Make it look like a premium Instagram post from a tech thought leader.
```

### Slide-Beschreibungs-Muster

**HOOK (Slide 1 - MIT BILD):**
```
SLIDE 1 - HOOK. Background: A high-quality, cinematic AI-generated photo representing '[THEMA]', heavily darkened/vignetted so white text pops clearly. Large ghost graffiti word '[THEMA]' rotated -8deg, top-right, very faint green. Top gradient bar gold-to-green. Gold spray-paint sticker badge top-left: '[THEMA-TAG]'. Main headline massive uppercase white: '[THESE ZEILE 1]' then on next line in neon gold glow: '[THESE ZEILE 2]'. Gold spray-paint divider line below. Bottom-left tiny monospace: 'AiGoodNews - [MONAT JAHR]'. Slide counter top-right: '1 / 10'.
```

**WERT-Slide (Slides 4-7):**
```
SLIDE [N] - WERT/INSIGHT. Background: [pure black / deep dark blue #0a192f alternierend].
Ghost graffiti word '[KEYWORD]' rotated -12deg, top-right, faint [green/white].
Large deco number '[N]' bottom-right, very faint green. Top gradient bar.
Monospace label: '[N] - INSIGHT'. Headline uppercase white: '[INSIGHT-TITEL]' [optional: then neon gold: '[AKZENT]'].
[Green/Gold] spray-paint divider. Body text grey: '[1-2 Sätze]'.
Bottom-right teaser: '-> [Nächste Seite Teaser]'. Counter: '[N] / 10'.
```

**AHA (Slide 8):**
```
SLIDE 8 - AHA/ERKENNTNIS. Background: pure black. Centered layout.
Ghost graffiti word 'AHA' rotated -6deg, centered background, very faint gold. Top gradient bar.
Gold spray-paint sticker badge: 'DIE ERKENNTNIS' slightly rotated.
Large centered headline in neon gold glow uppercase: '[ERKENNTNIS]'.
Gold spray-paint divider centered. Centered body text grey: '[1 Satz]'. Counter: '8 / 10'.
```

**SUMMARY (Slide 9):**
```
SLIDE 9 — SUMMARY. Background: deep dark blue #0a192f.
Ghost graffiti word 'RECAP' rotated -12deg, top-right, faint white. Top gradient bar.
Monospace label: '09 — ZUSAMMENFASSUNG'. Headline uppercase white: 'DAS WICHTIGSTE'.
Three checklist items with green checkmarks: '✓ [Punkt 1]' '✓ [Punkt 2]' '✓ [Punkt 3]'.
Counter: '9 / 10'.
```

**CTA (Slide 10 - IMMER IDENTISCH):**
```
SLIDE 10 - CTA. Background: pure black. Ghost graffiti letters 'AGN' rotated -10deg,
bottom-right, very faint green. Top gradient bar. Centered layout.
Circle logo badge top-center: green circle border with 'AGN' inside in green.
Large uppercase white: 'AIGOODNEWS'. Small monospace green: 'POSITIVE KI-NEWS FUER DIE DACH-REGION'.
Thin green horizontal divider. White text: 'DU WILLST MEHR GUTE NEWS?'
Three lines with neon gold arrows: '-> @aigoodnews auf Instagram folgen'
'-> aigoodnews.ai besuchen' '-> Carousel speichern & teilen'.
Thin green divider. Small monospace green: '#AiGoodNews #KI #ArtificialIntelligence'.
Counter: '10 / 10'.
```

---

## Schritt 4: Caption verfassen

```
[Hook - spiegelt Slide 1, max. 125 Zeichen]

[2-3 Sätze Kontext aus dem Blog - präzise, keine Buzzwords]

[Implikation für Unternehmen / Entscheider in 1-2 Sätzen]

Mehr dazu auf aigoodnews.ai

#AiGoodNews
```

**Regeln:**
- Schweizer Rechtschreibung (kein ß)
- Kein Emoji
- Nur `#AiGoodNews` als Hashtag am Ende - kein Hashtag-Block
- Ton: souverän, präzise, leicht pointiert
- Keine EM Dashes in der Caption - nur einfache Bindestriche (-)
- Umlaute ä ö ü immer ausschreiben - NICHT ae oe ue

---

## Schritt 5: Bilder hochladen

```bash
manus-upload-file slide_01.png slide_02.png ... slide_10.png
```

Alle 10 CDN-URLs notieren.

---

## Schritt 6: Direkt posten via Instagram MCP

```bash
manus-mcp-cli tool call create_instagram --server instagram --input '{
  "type": "post",
  "caption": "[CAPTION]",
  "media": [
    {"type": "image", "media_url": "https://...slide_01.png"},
    {"type": "image", "media_url": "https://...slide_02.png"},
    ...
    {"type": "image", "media_url": "https://...slide_10.png"}
  ]
}'
```

**Standard: Direkt posten ohne Vorschau-Schritt**, ausser der Nutzer sagt explizit «zeig mir erst».

---

## Design-Regeln (IMMER einhalten)

- **Font**: Avenir Next / Barlow Condensed 900 - Headlines UPPERCASE
- **TEDx-Grössen**: hero ≥64px / main ≥44px / insight ≥36px / body 17px
- **Graffiti-Pflicht**: Rotiertes Ghost-Wort im Hintergrund + Spray-Paint-Divider + Neon-Glow auf Headlines
- **Umlaute**: Immer ä ö ü verwenden - NIEMALS ae oe ue als Ersatz
- **Keine EM Dashes**: Nur einfache Bindestriche (-) verwenden, keine langen Gedankenstriche (--)
- **Sticker-Badge** auf Hook-Slide und AHA-Slide
- **Top-Accent-Bar**: Gold-zu-Green Gradient auf jedem Slide
- **Hintergrund-Wechsel**: Black und Deep Dark Blue alternieren (Slides 1,2,4,6,8,10 = Black/Photo; 3,5,7,9 = Deep Dark Blue)
- Gold `#ffd700` nur 1× pro Slide als Neon-Akzent
- Schweizer Rechtschreibung (kein ß)
- Max. 2 Sätze Body-Text pro Slide (ausser Summary)
- Slide 10 CTA ist immer identisch
- **Slide 1 muss ein AI-generiertes Bild als Hintergrund haben**

---

## Qualitäts-Check vor dem Posten

- [ ] 10 Slides generiert, alle 480×600px, kein Text abgeschnitten
- [ ] Slide 1 hat ein passendes AI-generiertes Bild als Hintergrund
- [ ] Avenir Next / Barlow Condensed, UPPERCASE Headlines
- [ ] Graffiti-Ghost-Wort + Spray-Divider + Neon-Glow vorhanden
- [ ] Sticker auf Slide 1 und Slide 8
- [ ] Top-Accent-Bar auf allen Slides
- [ ] Slide 10 = fixe CTA (identisch)
- [ ] Caption: Hook + Kontext + Implikation + aigoodnews.ai + #AiGoodNews
- [ ] Alle CDN-URLs erreichbar
- [ ] MCP-Post abgeschickt

---

## Referenzen

- `references/brand-design.md` - Vollständiges AiGoodNews Design-System, Farben, Typografie, Graffiti-Elemente
- `scripts/extract_blog_content.py` - KI-gestützte Extraktion der Slide-Inhalte
