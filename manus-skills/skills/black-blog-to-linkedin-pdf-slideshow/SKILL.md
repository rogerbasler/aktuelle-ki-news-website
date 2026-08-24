---
name: black-blog-to-linkedin-pdf-slideshow
description: >
  Wandelt Blog-Artikel, Fachtexte, URLs, Notizen oder Dokumente in professionelle LinkedIn-PDF-Slideshows
  im fragRoger Black Editorial Stil um. Unterstützt sowohl HTML/WeasyPrint-Rendering als auch direkte
  Bilderzeugung jeder Slide via GPT Image 2 (gpt-image-2). Verwende diesen Skill immer wenn der Nutzer sagt:
  „Blog zu LinkedIn“, „LinkedIn PDF“, „LinkedIn Slideshow“, „LinkedIn Carousel als PDF“, „mit GPT Image2 erstellen“,
  „mit Image2 erstellen“, „Folien mit GPT Image“ oder Inhalte als visuelle LinkedIn-Präsentation aufbereiten will.
  Output: 10 Slide-Bilder im 4:5-Format (GPT Image 2 oder HTML/PDF), gebündeltes PDF, Blueprint und LinkedIn-Post-Entwurf.
---

# Blog-to-LinkedIn PDF Slideshow

## Zweck

Erstelle aus einem Inhalt eine **argumentativ belastbare, visuell starke LinkedIn-Slideshow als mehrseitiges PDF**. Die Slideshow soll im Feed stoppen, beim Durchblättern Orientierung schaffen und bei Entscheider:innen eine konkrete Frage, Konsequenz oder Handlungslogik auslösen.

Der Standard ist **Black Editorial**: tiefschwarze Flächen (#050505), kontrollierte Cyan-Akzente (#00A6FF), grosse präzise Typografie, starke Kontraste und reduzierte visuelle Metaphern.

## Produktionsmodi

| Modus | Wann nutzen | Vorgehen |
|---|---|---|
| **GPT Image 2 (Standard bei Nutzeranforderung)** | Wenn der Nutzer „mit GPT Image2“, „mit Image2“, „vollständige Bild-Slides“ verlangt | Jede Slide wird einzeln via `generate_image` (Model `gpt-image-2`, 4:5) mit embedded Text oder dediziertem Motiv generiert und danach zu einer PDF kombiniert. |
| **HTML / WeasyPrint** | Wenn editierbare Typografie, pixelgenaue Tabellen oder HTML-Quellcode gewünscht sind | HTML-Vorlage mit WeasyPrint zu PDF rendern und PNG-Vorschauen erzeugen. |

## Standard-Output (GPT Image 2 Modus)

1. `slides/slide_01.png` bis `slide_10.png` (generiert mit `gpt-image-2`, 4:5 Aspect Ratio).
2. `linkedin_slideshow.pdf` (Zusammenfassung der 10 Bildseiten als druckfertiges LinkedIn-Dokument).
3. `content_blueprint.md` (Storyline, Seitentexte, Prompts, Quellen, LinkedIn-Post-Entwurf).
4. `layout_pruefung.md` (Qualitätsprüfung der 10 Slides).

## 10-Seiten-Struktur (Black Editorial)

| Seite | Funktion | Typografie / Inhalt |
|---:|---|---|
| 1 | **Hook** | Grosser, provokanter Headline-Text mit Stopp-Effekt, z. B. `GOOGLE TRAINIERT KI MIT DATEN EINER INSOLVENTEN AIRLINE`. |
| 2 | **Rehook & Fakten** | Zahlen und Fakten zum Deal (Kaufpreis 10 Mio. USD, 100 Mio. E-Mails, 500 Mio. Chats). |
| 3 | **Konsequenz** | Die eigentliche Brisanz: Wert liegt in den Beziehungsnetzen und Prozessmustern. |
| 4 | **Reframing** | Vorab-Bereinigung vs. Rekonstruktionsrisiko durch Kontext und Relationen. |
| 5 | **Mechanismus** | Anonymisierung vs. Pseudonymisierung (Art. 4 Nr. 5 vs. Erw. 26 DSGVO). |
| 6 | **Evidenz / Governance** | DSK-Beschluss vom 11.09.2024: Verkauf von Kundendaten als isoliertes Asset regelmässig einwilligungspflichtig. |
| 7 | **Verantwortung** | Rolle des Insolvenzverwalters (Art. 4 Nr. 7 DSGVO) und struktureller Interessenkonflikt. |
| 8 | **Framework** | Vierfach-Test für Daten-Asset-Deals (Rechtsgrundlage, Zweckbindung, Anonymisierung, Audit). |
| 9 | **Handlung** | 3 Handlungsschritte für VR und Geschäftsleitung (Inventory, Stresstest, Transaction Controls). |
| 10 | **Abschluss & CTA** | Schlussfolgerung, Speicher-Impuls und Absender Roger Basler de Roca. |

## Prompt-Framework für GPT Image 2 Slides

Verwende für jede Slide einen präzisen englischen Prompt mit deutschem Textinhalt im Black Editorial Design:

```text
Create a premium vertical 4:5 slide image in a Black Editorial corporate design for LinkedIn.
Background: deep pitch black #050505, minimal dark charcoal surface #101417.
Typography to render on the slide:
- Top label: "[TOP METADATA IN UPPERCASE]"
- Headline: "[BOLD DOMINANT HEADLINE IN GERMAN]"
- Key text / bullet points: "[CONCISE GERMAN TEXT]"
- Footer: "[FOOTER / PAGE NUMBER]"
Visual element: [specific visual metaphor with subtle electric cyan #00A6FF glow and steel blue #547188 accents].
Style: clean high-contrast editorial Swiss graphic design, bold readable typography, generous negative space, no clutter, photorealistic materials where applicable, no watermarks, professional corporate keynote standard.
```

## PDF-Erstellung aus GPT Image 2 Slides

Nach der Generierung aller 10 PNGs werden diese mit Python / `img2pdf` oder `pdf2image` zu `linkedin_slideshow.pdf` verbunden.
