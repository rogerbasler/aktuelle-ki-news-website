---
name: content-to-slideshow
description: >
  Wandelt beliebige Inhalte (Blog-Artikel, Texte, URLs, Notizen, Dokumente) in fertige Präsentationen
  (Slideshows) im Urban Graffiti Tech Stil um. Verwende diesen Skill immer wenn der Nutzer:
  "mach daraus Slides", "erstelle eine Präsentation", "Blog zu Slideshow", "Content zu Slides",
  "erstelle eine Slideshow aus diesem Artikel/Text/Dokument", "repurpose als Präsentation" sagt.
  Output: Strukturierte Präsentation (HTML/Image-Slides) mit Problem-Solution-Journey Struktur,
  exportierbar als PPTX.
---

# Content-to-Slideshow - Urban Graffiti Tech

## Workflow-Übersicht

1. **Inhalt aufnehmen** - Text, URL, Datei oder Notizen
2. **Kernaussagen extrahieren** - via `extract_content.py` → `slides.json`
3. **Präsentation generieren** - via `slides`-Tool im `html` oder `image` Modus
4. **Exportieren & Bereitstellen** - via `manus-export-slides` als PPTX

---

## Schritt 1: Inhalt aufnehmen

Akzeptiere jeden Content-Typ:
- Text direkt in der Nachricht
- URL (Blog, Artikel, Webseite)
- Datei (`.txt`, `.md`, `.html`, `.pdf`)
- Stichpunkte oder Notizen

---

## Schritt 2: Kernaussagen extrahieren

```bash
python /home/ubuntu/skills/content-to-slideshow/scripts/extract_content.py \
  --input content.txt --output slides.json
```

Das Script liefert JSON mit der Slide-Struktur.

### Präsentations-Struktur (Problem-Solution-Journey)

| Slide | Typ | Inhalt |
|---|---|---|
| 1 | TITLE | Prägnanter Titel & Untertitel. |
| 2 | PAIN | "Kennst du das?" - Fokus auf Probleme und Herausforderungen der Zielgruppe. |
| 3 | LICHTBLICK | Positiver Ausblick, "Licht am Ende des Tunnels". |
| 4 | JOURNEY | 90-Tage Transformation oder 3-Phasen Plan. |
| 5 | ROADMAP | Übersicht der folgenden Kapitel/Inhalte. |
| 6+ | CONTENT | Eigentliche Inhalte (1–2 Sätze pro Slide, Key Takeaway in Bottom Bar). |
| Vorletzte | BONUS | Zusätzlicher Wert oder Tipp. |
| Letzte | CLOSING | Zusammenfassung & CTA. |

---

## Schritt 3: Präsentation generieren (via `slides`-Tool)

Nutze das `slides`-Tool, um die Präsentation zu erstellen.

**Modus-Entscheidung:**
- `html` - Standard: bearbeitbar, datenlastig, Chart.js-fähig
- `image` - Wenn der Nutzer "Nano banana", "als Bilder", "künstlerisch" oder visuell beeindruckend wünscht

**Design-Vorgaben (Urban Graffiti Tech):**

| Element | Spezifikation |
|---|---|
| Background | Deep Black `#0D0D0D` |
| Headline-Font | Montserrat 900, UPPERCASE |
| Body-Font | Inter 400/600 |
| Label-Font | JetBrains Mono 700 |
| Akzent 1 | Neon Blue `#00D4FF` |
| Akzent 2 | Neon Pink `#FF006E` |
| Akzent 3 | Lime Green `#ADFF2F` |
| Graffiti-Element | Grosses, rotiertes, low-opacity Dekowort im Hintergrund |
| Bottom Bar | Key Takeaway auf jedem Content-Slide (Pflicht) |
| Neon-Glow | Auf Headlines (`text-shadow`) |

**Slide-Dimensionen:** 1280×720px (16:9)

---

## Schritt 4: Exportieren & Bereitstellen

1. Nach der Generierung erhältst du eine URI: `manus-slides://{id}`
2. Exportiere als PPTX:
   ```bash
   manus-export-slides manus-slides://{id} ppt
   ```
3. Lade die Datei hoch:
   ```bash
   manus-upload-file <file>.pptx
   ```
4. (Optional) Canva-Import via `import-design-from-url` MCP Tool mit der CDN URL.

---

## Qualitäts-Check

- [ ] Problem-Solution-Journey Struktur eingehalten (PAIN, LICHTBLICK, JOURNEY).
- [ ] Urban Graffiti Tech Design angewendet (Dunkler Hintergrund, Neon-Akzente, Bottom Bar).
- [ ] Jeder Content-Slide hat eine Bottom Bar mit Key Takeaway.
- [ ] Schweizer Rechtschreibung (kein ß).
- [ ] Als PPTX exportiert und bereitgestellt.

---

## Referenzen

- `scripts/extract_content.py` - KI-gestützte Extraktion der Slide-Inhalte aus beliebigen Content-Quellen
