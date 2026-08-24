---
name: aibad-news-skill
description: >
  Wandelt AI-Bad-News-Artikel, Blogtexte, Notizen oder URLs in faktenorientierte Instagram-Carousel-Posts im AI-Bad-News Dark-Graffiti-Tech-Stil um. Verwende diesen Skill immer wenn der Nutzer: "AI Bad News", "aibad.news", "Bad News Carousel", "AI-Bad-News-Post", "Blog zu AI Bad News Instagram", "Palantir/CIA Carousel", "kritische KI-News als Carousel" oder "/aibad-news-skill" sagt. Output: 10 Slide-Bilder im 4:5-Format, Caption mit Schweizer Rechtschreibung, Review vor Posting, optional direkter Post via Instagram MCP mit CTA auf @fragRoger und aibad.news.
---

# AI Bad News Instagram Carousel

## Zweck

Dieser Skill erstellt aus kritischen KI-News, Blog-Artikeln oder Recherchetexten einen **faktenorientierten Instagram-Carousel** für **AI Bad News**. Die Tonalität ist nüchtern, kritisch und entscheidungsrelevant. Die Slides sollen nicht dramatisieren, sondern sichtbar machen, was Unternehmen, Entscheider:innen und interessierte Fachpersonen verstehen müssen.

Das eigentliche Problem ist nicht, dass KI schlechte Nachrichten produziert. Das eigentliche Problem ist, wenn relevante Risiken so weich verpackt werden, dass niemand mehr entscheidet. Dieser Skill verhindert genau das.

## Standard-Workflow

1. **Input aufnehmen:** Text, Datei oder URL akzeptieren. Bei URLs Inhalte extrahieren, bei Dateien Inhalt lesen.
2. **Kernaussagen extrahieren:** Fakten, Zahlen, Akteure, Zeitleiste, Implikationen und Quellen aus dem Input bestimmen.
3. **Quellenlage prüfen:** Keine neuen Fakten erfinden. Unsichere Aussagen abschwächen oder als zu prüfende Aussage markieren.
4. **10-Slide-Struktur erstellen:** Faktenorientierte Storyline ohne übermässige Dramaturgie.
5. **Slide-Bilder generieren:** 4:5 Instagram-Format im AI-Bad-News Dark-Graffiti-Tech-Stil.
6. **Caption schreiben:** Hook, Kontext, Implikation, Verweis auf aibad.news, genau ein Hashtag-Block gemäss Regeln.
7. **Review vor Posting:** Dem Nutzer Preview, ZIP und Caption zeigen. Erst nach explizitem **GO** posten.
8. **Optional posten:** Nach Freigabe Bilder hochladen und via Instagram MCP als Carousel posten.

## Output-Standard

| Element | Vorgabe |
|---|---|
| Anzahl Slides | Immer 10 Slides |
| Format | Instagram 4:5, ideal 1080×1350 oder 480×600 |
| Design | Dark Urban Graffiti Tech, kritisch, hart, faktenorientiert |
| Sprache | Deutsch oder Sprache des Inputs, Schweizer Rechtschreibung bei Deutsch |
| Posting | Immer erst Review, dann nur nach explizitem GO posten |
| CTA | @fragRoger folgen, aibad.news besuchen, Carousel speichern & teilen |

## Carousel-Struktur

| Slide | Typ | Inhalt |
|---|---|---|
| 1 | HOOK | Präziser Fakt als Titel. Keine abstrakte Frage, wenn ein harter Fakt vorhanden ist. Bei Marken/Akteuren Logos integrieren, wenn der Nutzer sie liefert. |
| 2 | FAKT | Ursprung, Gründung, Ereignis oder zentraler Auslöser. |
| 3 | FAKT | Hauptakteur oder Schlüsselverbindung erklären. |
| 4 | FAKT | Technologie, Produkt, Plattform oder Mechanismus sichtbar machen. |
| 5 | FAKT | Zahl, Vertrag, Marktgrösse, Finanzierung oder Beleg. |
| 6 | EINORDNUNG | Warum der Fakt strategisch relevant ist. |
| 7 | EUROPA/DACH | Relevanz für Europa, DACH, Unternehmen oder Regulierung. |
| 8 | ERKENNTNIS | Eine klare, nüchterne Schlussfolgerung. |
| 9 | SUMMARY | Drei präzise Punkte, keine langen Bullet-Listen. |
| 10 | CTA | Fixe AI-Bad-News-CTA-Slide gemäss unten. |

## Design-System

Verwende den Referenzstil aus `references/brand-design.md`. Wenn der Skill für Bildgenerierung genutzt wird, muss der Prompt die folgenden Konstanten enthalten:

- **Stil:** Dark Urban Graffiti Wall meets serious tech editorial typography.
- **Farben:** Schwarz `#000000`, Deep Navy `#0a192f`, Neon Green `#00ff88`, Neon Gold `#ffd700`, Weiss `#ffffff`.
- **Typografie:** Massive uppercase condensed headlines, TEDx-artige Dominanz, kurze Texte.
- **Pflichtelemente:** Top-Accent-Bar Gold-zu-Green, Slide-Counter, Ghost-Graffiti-Wort, Spray-Paint-Divider, neonfarbene Akzente.
- **Keine weichen Karten:** Keine runden Cards, keine cleanen SaaS-Layouts, keine Pastellfarben.

## Slide-Generierung

Erstelle bei Bildgenerierung möglichst zuerst **Slide 1 als Stilreferenz**. Nutze diese danach als Referenz für die restlichen Slides, damit der Carousel nicht aussieht wie zehn verschiedene Agenturen mit demselben WLAN-Passwort.

### Standard-Prompt-Baustein

```text
Create one Instagram carousel slide in exact 4:5 ratio for AI Bad News. Visual style: dark urban graffiti tech, black/deep navy background, neon green #00ff88 and neon gold #ffd700 accents, massive uppercase condensed typography, serious factual editorial mood. Add a thin top accent bar from neon gold to neon green, slide counter top-right, faint rotated ghost graffiti word, spray-paint divider, sharp readable text fully inside frame. No rounded cards, no borders, no clutter, no invented claims.
```

### Titel-Slide mit Logos

Wenn der Nutzer Logos liefert, nutze sie als Referenzbilder. Logos dürfen visuell integriert werden, aber nicht verfälscht, parodiert oder mit erfundenen Wortmarken ersetzt werden. Der Titel muss den zentralen Fakt tragen.

Beispiel für Palantir/CIA:

```text
Main headline: PALANTIR / UND DIE CIA / VERBINDUNG.
Subtitle: Frühe Finanzierung über In-Q-Tel, die strategische VC-Einheit der CIA.
Include the supplied Palantir logo and CIA seal as recognisable visual references.
```

## Fixe CTA-Slide

Slide 10 muss standardmässig diesen Inhalt verwenden:

```text
AI BAD NEWS
WARUM WIR BEI KI WACHSAM BLEIBEN MÜSSEN

DU WILLST MEHR BAD NEWS?
-> @fragRoger auf Instagram folgen
-> aibad.news besuchen
-> Carousel speichern & teilen

#AiBadNews #KI #ArtificialIntelligence
```

CTA-Regeln:

- Nie `AiGoodNews` erwähnen.
- Nie `@aibad.news` als Instagram-Folgehinweis verwenden, ausser der Nutzer verlangt es explizit.
- Standard-Instagram-Account ist **@fragRoger**.
- Standard-Website ist **aibad.news**.
- Die CTA-Slide bleibt dunkel, minimal und markenkonform.

## Caption-Regeln

Die Caption besteht aus vier Abschnitten:

1. **Hook:** 1 Satz, direkt aus Slide 1 abgeleitet.
2. **Kontext:** 2 bis 3 Sätze mit den wichtigsten Fakten.
3. **Implikation:** 1 bis 2 Sätze für Unternehmen, Entscheider:innen oder Öffentlichkeit.
4. **Verweis und Hashtag:** `Mehr dazu auf aibad.news` und Hashtag-Block.

Standardabschluss:

```text
Mehr dazu auf aibad.news

#AiBadNews
```

Bei deutschen Texten gelten immer:

- Schweizer Rechtschreibung, kein `ß`.
- Umlaute ä ö ü ausschreiben, nicht ae oe ue.
- Keine EM-Dashes. Verwende kurze Bindestriche oder klare Satzpunkte.
- Keine Emoji.
- Ton: souverän, präzise, leicht pointiert, aber nicht verschwörerisch.

## Faktentreue und Sourcing

AI Bad News lebt nicht von Alarmismus, sondern von belastbarer Einordnung. Deshalb:

- Verwende nur Fakten aus dem Input oder aus explizit recherchierten Quellen.
- Wenn Zahlen im Input stehen, übernimm sie nur, wenn die Quelle plausibel ist, oder formuliere: «Der Artikel nennt ...».
- Bei umstrittenen Aussagen keine absolute Sprache verwenden.
- Bei Marken, Behörden oder Personen sachlich bleiben.
- Keine erfundenen Logos, Claims, Verträge, Datensätze oder Jahreszahlen ergänzen.

## Review- und Posting-Regel

Vor jedem Posting muss der Nutzer eine Review erhalten:

- Kontaktbogen/Preview aller 10 Slides.
- ZIP mit allen Einzelbildern.
- Caption als Textdatei.
- Hinweis: «Wenn es passt, antworte mit GO.»

Erst nach explizitem **GO** dürfen Bilder hochgeladen und via Instagram MCP gepostet werden.

## Typische Trigger und Verhalten

| Nutzer sagt | Verhalten |
|---|---|
| `/aibad-news-skill` | Diesen Skill verwenden. |
| `mach daraus AI Bad News Instagram` | 10-Slide-Carousel erstellen. |
| `Fokus auf Palantir/CIA` | Faktenstruktur auf Palantir, CIA, In-Q-Tel ausrichten. |
| `nur Fakten` | Dramaturgische Slides wie «blinde Stelle» vermeiden. |
| `Logo einbauen` | Gelieferte Logos als Bildreferenzen nutzen. |
| `posten` | Erst Review zeigen, dann nach GO posten. |

## Qualitätscheck vor Review

- [ ] 10 Slides vorhanden.
- [ ] Format 4:5.
- [ ] Slide 1 enthält den zentralen Fakt als klare Headline.
- [ ] Bei gelieferten Logos sind sie sichtbar und erkennbar integriert.
- [ ] Keine AiGoodNews-Verweise vorhanden.
- [ ] Slide 10 nennt @fragRoger und aibad.news.
- [ ] Caption nennt aibad.news und #AiBadNews.
- [ ] Keine erfundenen Fakten.
- [ ] Schweizer Rechtschreibung eingehalten.
- [ ] Review vor Posting erstellt.
