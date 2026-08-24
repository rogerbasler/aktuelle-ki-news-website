---
name: black-blog-to-instagram-carousel
description: >
  Wandelt Blog-Artikel, Texte oder URLs in fertige Instagram Carousel-Posts im fragRoger Dark-Cinematic-TED-Talk-Stil um.
  Verwende diesen Skill immer wenn der Nutzer einen Blog in einen Instagram-Post oder Carousel umwandeln will,
  z. B. "repurpose diesen Blog", "mach daraus einen Carousel", "Blog zu Instagram", "Content repurposing",
  "erstelle einen Post aus diesem Artikel", "Instagram-Post aus Blog" oder "Carousel aus Blogartikel" sagt.
  Output: 10 Slide-Bilder im 4:5-Format mit bildstarken Baller-Motiven auf Slide 1-3 und Slide 9, bold-cinematischem Design, Caption und optionalem Instagram-Posting nach Review-Freigabe.
---

# Blog-to-Instagram Carousel - fragRoger Blue Cinematic Cyberpunk

## Workflow-Übersicht

1. **Blog-Inhalt aufnehmen** - Text, URL oder Datei akzeptieren.
2. **Baller-Bildstrategie festlegen** - Slide 1-3 und Slide 9 brauchen immer starke, eigenständige Bildmotive. Wenn der Nutzer Bildmaterial liefert, dieses priorisiert verwenden. Wenn kein Bild geliefert wird, passende KI-Motive erstellen, die wie Feed-Stopper funktionieren.
3. **Carousel-Struktur extrahieren** - mit `scripts/extract_blog_content.py` eine 10-Slide-Struktur erzeugen.
4. **10 Slide-Bilder generieren** - im 4:5-Format, dark, cinematic, bold, TEDx-/Kinoposter-artig und konsequent im **Black-Cyberpunk-Baller-Plakat-Modus**: echte visuelle Hook-Motive, grosse Headline-Flächen, klare Safe-Zones, starke Typografie, keine kleinteilige Textplatzierung. Die Typografie muss dominant bleiben, aber die Key-Slides dürfen nicht nur Typo-Flächen sein.
5. **Caption verfassen** - Hook, Kontext, Implikation, CTA, `#fragRoger`.
6. **Review vor Posting einholen** - finale Slides und Caption zeigen. Erst nach expliziter Freigabe posten.
7. **Bilder hochladen und posten** - CDN-URLs erstellen und via Instagram MCP veröffentlichen, wenn freigegeben.

## Schritt 1: Blog-Inhalt aufnehmen

Akzeptiere Blog-Inhalte als Text, URL oder Datei (`.txt`, `.md`, `.html`). Extrahiere die entscheidende These, den Konflikt, die Pointe und den konkreten Nutzen für Entscheider:innen.

## Schritt 2: Baller-Bildstrategie für Key-Slides

**Slide 1, Slide 2, Slide 3 und Slide 9 enthalten immer starke Bildmotive.** Das ist Pflicht, nicht Deko. Eine reine Typografiefläche ist auf diesen vier Slides nur erlaubt, wenn der Nutzer sie ausdrücklich verlangt. Standard ist: **Bild zuerst, Typografie darüber oder daneben, klare Story im Motiv.**

1. Wenn der Nutzer Bilder liefert, verwende sie priorisiert als Hero-Visuals oder visuelle Grundlage. Nutzerbilder haben Vorrang vor KI-Bildern.
2. Wenn kein Bildmaterial geliefert wird, erstelle KI-generierte Dark-Cyberpunk-Baller-Motive für Slide 1, Slide 2, Slide 3 und Slide 9.
3. Slide 1 muss den stärksten Pattern Interrupt enthalten: eine Szene, Figur, ein Konflikt, ein Paradox oder eine absurde Metapher, die sofort stoppt.
4. Slide 2 muss den Open Loop visualisieren: Ursache, Auslöser, Portal, Trigger, Dokument, Interface oder «so begann es»-Moment.
5. Slide 3 muss Story, Pain oder Konsequenz emotional und konkret machen: Menschen, Bots, Screens, Prozesse, Chaos, Erkennung, Fehlerbild.
6. Slide 9 muss Handlung sichtbar machen: Framework, Schutzschild, Gate, Checkpoint, Kontrollraum, Workflow oder Entscheidungsarchitektur.
7. Die Bildmotive sind super dark, cinematic und cyberpunk-mässig, müssen Tiefe, Schatten, starken Kontrast und Dramatik haben. Dunkel darf nicht flach oder matschig werden.

**Merksatz:** Keine ersten drei Slides ohne echtes Bildmotiv. Wenn Slide 1-3 aussehen wie Text auf einem simplen dunklen Verlauf, ist der Carousel noch nicht fertig. Das ist dann nett. Nett scrollt weg.

## Schritt 3: Carousel-Struktur extrahieren

```bash
python /home/ubuntu/skills/black-blog-to-instagram-carousel/scripts/extract_blog_content.py \
  --input blog.txt --output slides.json
```

Das Script liefert eine JSON-Struktur mit exakt 10 Slides und einem Caption-Entwurf. Falls es weniger oder mehr Slides liefert, korrigiere manuell auf exakt 10 Slides.

## Carousel-Struktur (immer 10 Slides)

| Slide | Typ | Funktion | Textregel |
|---|---|---|---|
| 1 | HOOK | Pattern Interrupt mit mutiger, kontroverser oder neugiergetriebener Aussage | 5-10 Wörter, maximal 2 Zeilen, immer mit starkem Hero-Bild |
| 2 | REHOOK | Open Loop erhöhen, Ergebnis anteasern, Antwort noch nicht liefern | 1-2 Zeilen, immer mit eigenem Bildmotiv |
| 3 | RELATABLE PAIN / STORY START | Kurze Situation oder Story eröffnen, z. B. «Die meisten denken…» | 1-2 Zeilen, immer mit eigenem Bildmotiv |
| 4 | VALUE | Erwartung brechen, erste Einsicht liefern | 1 zentrale Idee |
| 5 | VALUE | Story und Insight weiterführen | 1 zentrale Idee |
| 6 | VALUE | Konkreten Mechanismus erklären | 1 zentrale Idee |
| 7 | VALUE | Konsequenz oder Anwendung zeigen | 1 zentrale Idee |
| 8 | TURNING POINT | Aha-Moment, zentrale Perspektivenverschiebung, speicherwürdig | 1 starke Erkenntnis |
| 9 | ACTIONABLE TAKEAWAY | Klare Schritte oder Empfehlungen, sofort anwendbar | 2-3 kurze Takeaways, immer mit starkem visuellem System-/Framework-Motiv |
| 10 | CTA | Engagement Trigger, klare Handlung | Folge-, Speicher-, Teilen- oder Kontakt-CTA. Kommentar-CTA nur verwenden, wenn er strategisch begründet ist oder vom Nutzer gewünscht wird. |

## Psychologische Trigger

Nutze pro Carousel bewusst mehrere Trigger, aber ohne billigen Clickbait. Das Ziel ist Spannung mit Substanz. Die Sprache bleibt souverän, direkt und leicht dramatisch.

| Trigger | Einsatz |
|---|---|
| Neugier-Lücke | Slide 1-2 öffnen eine Lücke, die erst später geschlossen wird. |
| Pattern Interrupt | Slide 1 formuliert etwas, das irritiert oder die übliche Deutung bricht. |
| Social-Proof-Tonalität | «Viele denken…», «Die meisten übersehen…», «In Unternehmen passiert oft…». |
| FOMO | Zeige, was man verpasst, wenn man die Perspektive nicht versteht. |
| Konträre Perspektive | «Das eigentliche Problem ist nicht …, sondern …». |
| Quick Wins | Slide 9 liefert unmittelbar nutzbare Denk- oder Handlungsschritte. |

## Schreibstil für Slides

Schreibe kurz, prägnant und konversationell. Jede Zeile muss Momentum erzeugen. Keine Füllwörter. Keine langen Erklärungen. Keine Fachbegriffs-Dusche, nur klare Einsicht. Schreibe, als würdest Du mit einer Person sprechen.

**Output-Format für die Slide-Texte:**

```text
Slide 1 - HOOK
[5-10 Wörter, maximal 2 Zeilen]

Slide 2 - REHOOK
[1-2 Zeilen, Open Loop]

Slide 3 - RELATABLE PAIN / STORY START
[1-2 Zeilen, nachvollziehbare Situation]

Slide 4 - VALUE
[1 zentrale Idee]

Slide 5 - VALUE
[1 zentrale Idee]

Slide 6 - VALUE
[1 zentrale Idee]

Slide 7 - VALUE
[1 zentrale Idee]

Slide 8 - TURNING POINT
[Speichern-wertiger Aha-Moment]

Slide 9 - ACTIONABLE TAKEAWAY
[2-3 kurze, sofort anwendbare Schritte]

Slide 10 - CTA
[Engagement Trigger]
```

Keine zusätzlichen Erklärungen in der Slide-Struktur ausgeben, wenn der Nutzer explizit «direkt veröffentlichbar» oder «keine Erklärungen» verlangt.

## Schritt 4: Slide-Bilder generieren

**Standard-Methode:** 10 einzelne 4:5-Slide-Bilder erzeugen. Verwende standardmässig **1080×1350px** oder höher im gleichen 4:5-Seitenverhältnis. Das Design ist nicht weichgespülter Pastell-Content, sondern bold, super dark, cinematic, cyberpunk-mässig, TED Talk Poster mit verbindlichem Baller-Bildstandard für Slide 1-3 und Slide 9.

### Black-Cyberpunk-Baller-Plakat-Modus: Bildmotiv, Typografie und Wirkung

Jede Slide muss wie ein Keynote-Poster funktionieren, nicht wie eine Folie mit nettem Hintergrund. Auf Slide 1-3 und Slide 9 ist das Bildmotiv der erste Scroll-Stopp, die Headline ist der zweite Schlag. Wenn das Bild interessant ist, aber der Text klein, brav oder irgendwo oben links verloren wirkt, ist die Slide nicht fertig. Wenn der Text stark ist, aber das Bild nur dekorativer dunkler Nebel ist, ist die Slide ebenfalls nicht fertig.

**Verbindliche Layout-Regeln:**

- Haupttext mindestens **45-70% der sichtbaren Slide-Fläche** einnehmen lassen. Die Headline ist das Hauptmotiv, nicht Dekoration.
- Slide 1, Slide 8 und starke Turning-Point-Slides besonders gross setzen: Die Headline darf **60-85% der Bildbreite** dominieren, solange sie vollständig lesbar bleibt.
- Bei 1080×1350px als Richtwert: Hero-Headline **150-210px**, Main-Headline **125-190px**, CTA **105-160px**, Label maximal **22-32px**. Wenn viele Zeilen nötig sind, Text zuerst kürzen statt Schrift klein machen.
- Textblöcke nicht schüchtern in die Ecke setzen. Verwende klare Zonen: **oben dominant**, **zentriert dominant** oder **unten dominant**. Die Aussage soll wie auf einer TEDx-Keynote-Bühne stehen.
- Maximal **1 bis 4 Wörter pro Zeile**, harte Umbrüche bewusst setzen. Lieber fünf starke Kurzzeilen als eine lange Satzwurst, die aussieht wie ein Amtsformular mit Neonlicht.
- Mindestens **80px Innenabstand** zu allen Rändern. Kein Text darf optisch gequetscht wirken.
- **Keine negativen Zeilenabstände.** Kinoposter-Typografie darf eng wirken, aber Zeilen dürfen nicht kollidieren. Lesbarkeit schlägt Drama.
- Ein Schlüsselwort pro Slide darf in leuchtendem Neon Electric Blue (#00aaff) stehen. Der Rest bleibt weiss, hellgrau oder sehr hell auf super dark Hintergrund. Kein Pink.
- Dunkle Hintergründe brauchen trotzdem Kontrast: Tiefe Schatten, grelle Lichtkanten, Vignette, Cutouts oder grosse helle Typo-Zonen einsetzen.
- Keine langen Sätze als Bildtext. Wenn eine Aussage nicht plakatfähig ist, zuerst kürzen, dann gestalten.
- **Baller-Regel für Slide 1-3 und Slide 9:** Jede dieser Slides braucht ein konkretes Motiv mit Subjekt, Szene, Konflikt und visueller Metapher.
- **Keine generischen Tech-Hintergründe** auf Key-Slides. Abstrakte Neonlinien, zufällige Partikel oder leere Dark-Gradient-Flächen zählen nicht als Bildmotiv.

**Merksatz:** Erst Bildidee, dann Typografie, dann Dekoration. Der Algorithmus scrollt schnell. Kleine Schrift ist höflich, aber leider unsichtbar. Dunkelheit ohne Konflikt ist Deko. Deko konvertiert selten.

### Prompt-Vorlage pro Slide

```text
Generate a single Instagram carousel slide image (4:5 ratio, minimum 480x600px) in the fragRoger dark cinematic cyberpunk TED Talk style.

DESIGN SYSTEM:
- Style: bold cinematic TED Talk poster meets subtle urban cyberpunk graffiti texture.
- Background: super dark, pure black #000000 or deep navy #0d1b3a, with cinematic depth, vignette, grain, dramatic contrast and neon light edges.
- Typography: Avenir Next / Barlow Condensed 900, ultra-large uppercase headlines, very few words, bold cinematic TEDx keynote poster composition. The headline must dominate the slide and occupy roughly 45-70% of the visible canvas; on hero slides it may occupy up to 85% of the width if still fully readable. Use clean positive line spacing, never overlapping text.
- Brand colors: Electric Blue #00aaff, Deep Blue #4a7fa1, White #ffffff.
- Slide 1, Slide 2, Slide 3 and Slide 9 MUST include strong cinematic image motifs, not just text on dark abstract backgrounds. Use user-provided images if available; otherwise generate suitable AI image motifs.
- Primary accent color is Electric Blue #00aaff. Deep Blue #4a7fa1 is the secondary accent. Hot Pink is NOT used in this design system.
- NO underline dividers, NO thin separator lines, NO decorative horizontal rules.
- Do NOT use spray-paint divider lines. Use scale, contrast, image depth, shadows, neon light, framing and composition instead.
- Keep subtle graffiti only as texture or ghost-word, never as clutter.
- Use one dominant visual idea per slide. For Slide 1-3 and Slide 9, the visual idea must be concrete and story-driven: a subject, a scene, a conflict, and a clear metaphor.
- Text MUST be fully contained within the frame and instantly readable on mobile. Use very large type, intentional line breaks, strong contrast, and a minimum safe margin of 80px on a 1080x1350 canvas.
- Max 1-2 headline blocks per slide. Use 1-4 words per line where possible. Slide 9 may contain 2-3 very short takeaways, but each takeaway must still be large, bold and poster-like, not body text. If the slide becomes crowded, simplify the wording before reducing font size.
- Slide counter may be small and unobtrusive. Labels must stay secondary; the main headline must be the visual hero.

SLIDE TO GENERATE:
[SLIDE DESCRIPTION]

OUTPUT: Generate exactly one premium Instagram carousel slide. It should feel like a cinematic cyberpunk keynote poster, not a worksheet. The typography must be oversized, bold, dramatic, and intentionally placed.
```

### Slide 1 - HOOK

```text
SLIDE 1 - HOOK / PATTERN INTERRUPT.
Must include the strongest image motif of the carousel. Use the provided image if available; otherwise generate a super dark cinematic cyberpunk hero image with a concrete subject, strong scene and visual conflict.
The image should feel like a feed-stopping movie poster: a person, bot, object, crisis, absurd metaphor or dramatic situation that visualises the core hook. Avoid generic tech backgrounds.
Dark overlay, dramatic crop, high contrast, subtle vignette, neon light edges. Massive uppercase headline with 5-10 words. The headline must be huge, poster-like, and dominate the image without hiding the subject.
No underline. No divider. No explanatory body text.
The reader should think: «Moment… was?»
```

### Slide 2 - REHOOK

```text
SLIDE 2 - REHOOK / OPEN LOOP.
Increase tension without giving away the answer. Tease the result. Make the next slide feel necessary.
Must include a concrete image motif that visualises the trigger or origin of the story: portal, switch, document, interface, exposed field, spark, message, hidden instruction, before/after moment.
Use oversized bold typography, super dark cinematic cyberpunk darkness, one strong visual metaphor. The text block should feel like a stage headline: large, assertive, and deliberately placed.
No underline. No divider. Max 1-2 lines.
```

### Slide 3 - RELATABLE PAIN / STORY START

```text
SLIDE 3 - RELATABLE PAIN / STORY START.
Start with a short, recognisable situation: «Die meisten denken…», «Alle machen diesen Fehler…», «Ich habe früher…».
Must include a concrete story image: a human, bot, team, screen, broken process, awkward moment, failed automation, exposed dashboard or visible consequence.
Make it feel personal, direct and slightly uncomfortable.
No underline. No divider. Max 1-2 lines.
```

### Slides 4-7 - VALUE

```text
SLIDE [N] - VALUE / STORY + INSIGHT.
Continue the story in a clear flow. Break expectations, build insight step by step.
One central idea only. Short, concrete, useful.
Use bold cinematic cyberpunk composition, very large type, subtle texture, strong contrast. The type must carry the slide even without the background image.
No underline. No divider. Max 1-2 lines.
```

### Slide 8 - TURNING POINT

```text
SLIDE 8 - TURNING POINT / AHA-MOMENT.
Reveal the central insight or perspective shift. This is the speichern-wertige moment.
Make it feel like a true realisation, not a summary.
Use the most dramatic typographic composition after Slide 1.
No underline. No divider. Max 1-2 lines.
```

### Slide 9 - ACTIONABLE TAKEAWAY

```text
SLIDE 9 - ACTIONABLE TAKEAWAY.
Give clear, immediately applicable steps or recommendations.
Must include a strong system or framework image motif: security gate, workflow board, control room, shield, checkpoint, decision architecture, risk map, cockpit, data stream, or human approval moment.
Use 2-3 short takeaways, not paragraphs.
Each takeaway must be large enough to read instantly on mobile. Use bold hierarchy and spacing instead of tiny boxes. If generated callout text becomes too dense, reduce wording and keep only the strongest action phrases.
No underline. No divider.
```

### Slide 10 - CTA

```text
SLIDE 10 - CTA / ENGAGEMENT TRIGGER.
Use a strong action prompt. Default CTA logic:
- «Folge @fragroger auf Instagram»
- «Speichere & teile das Carousel»
- «Melde Dich für [themenspezifischen Nutzen]»
Use a comment CTA only when the user explicitly asks for it or when the comment keyword directly supports a clear lead magnet. Do not invent generic keywords such as «SOUVERÄN» without strategic reason.
CTA must be direct, conversational and specific.
No underline. No divider.
```

## Schritt 5: Caption verfassen

```text
[Hook - spiegelt Slide 1, max. 125 Zeichen]

[2-3 Sätze Kontext aus dem Blog - präzise, keine Buzzwords]

[Implikation für Unternehmen / Entscheider:innen in 1-2 Sätzen]

Mehr dazu auf https://www.fragroger.social

#fragRoger
```

**Regeln (NICHT VERHANDELBAR):**

- **UMLAUTE PFLICHT:** ä ö ü Ä Ö Ü IMMER direkt ausschreiben. `ae`, `oe`, `ue`, `Ae`, `Oe`, `Ue` als Ersatz sind VERBOTEN. Gilt für Caption, Slide-Texte, Labels und alle anderen Textfelder ohne Ausnahme.
- Schweizer Rechtschreibung: kein ß, stattdessen ss.
- Keine EM Dashes, nur einfache Bindestriche.
- Kein Emoji.
- Nur `#fragRoger` als Hashtag am Ende, kein Hashtag-Block.
- Ton: souverän, präzise, leicht pointiert.
- Standard-Link in der Caption: `https://www.fragroger.social`, sofern der Nutzer keine andere Ziel-URL nennt.
- Keine erfundenen Kommentar-Keywords. Kommentar-CTA nur mit thematischer Begründung oder nach Nutzerwunsch.
- Vor dem Posten: Caption auf ae/oe/ue prüfen und ggf. korrigieren.

## Schritt 6: Review und Posting

Vor dem Posting immer die finalen Slides und die Caption zur Review zeigen. Erst nach expliziter Freigabe posten. Wenn der Nutzer bereits ausdrücklich «direkt posten» verlangt, trotzdem kurz die Freigabe bestätigen lassen, sobald finale Medien und Caption bereit sind.

```bash
manus-upload-file slide_01.png slide_02.png ... slide_10.png
```

Nach Freigabe via Instagram MCP posten:

```bash
manus-mcp-cli tool call create_instagram --server instagram --input '{
  "type": "post",
  "caption": "[CAPTION]",
  "media": [
    {"type": "image", "media_url": "https://...slide_01.png"},
    {"type": "image", "media_url": "https://...slide_02.png"},
    {"type": "image", "media_url": "https://...slide_10.png"}
  ]
}'
```

## Design-Regeln (immer einhalten)

- Slide 1, Slide 2, Slide 3 und Slide 9 immer mit starkem Bildmotiv. Nutzerbild vor KI-Bild.
- Slide 1-3 müssen den Feed stoppen: Szene, Subjekt, Konflikt, visuelle Metapher. Keine reinen Typo-Slides auf den ersten drei Slides.
- Slide 9 muss Handlung sichtbar machen: Framework, Schutzschild, Gate, Checkpoint, Kontrollraum oder Entscheidungsarchitektur.
- Bold cinematic cyberpunk TED-Talk-Design, keine Worksheet-Optik.
- Keine Unterstriche, keine Trennlinien, keine horizontalen Divider.
- Keine Spray-Paint-Divider als Standard-Stilelement.
- Graffiti nur subtil: Textur, Ghost-Word, Körnung, Wandgefühl.
- Schrift dominiert. Wenige Wörter, grosse Wirkung. **Plakat-Modus ist Standard.** Jede Hauptaussage muss gross, laut und bewusst platziert sein.
- Headlines UPPERCASE, Avenir Next / Barlow Condensed 900. Die Headline ist mindestens 45-70% der sichtbaren Komposition, Hero-Slides dürfen bis 85% dominieren, wenn die Lesbarkeit intakt bleibt.
- Typografie muss **bold cinematic, cyberpunk-artig und kinoplakatfähig** sein: grossflächig, kontrastreich, sauber gesetzt, nicht gedrängt. Keine negativen Zeilenabstände, keine überlappenden Zeilen.
- Dark first: Schwarz oder Deep Navy, starke Kontraste, Vignette, Filmgrain, Neon-Lichtkanten.
- Electric Blue `#00aaff` als primärer Neon-Akzent einsetzen. Maximal ein Schlüsselwort oder eine Zahl pro Slide.
- Deep Blue `#4a7fa1` als sekundärer, ruhigerer Akzent für Labels und Sublines.
- Kein Pink. Kein Hot Pink. Keine Farbe ausserhalb der Blue/Black/White-Palette.
- Maximal 1-2 Textblöcke pro Slide, ausser Slide 9. Pro Zeile möglichst 1-4 Wörter. Keine langen Satzwürste, die aussehen wie ein Amtsformular mit Neonlicht.
- Wenn eine AI-generierte Key-Slide zwar schön aussieht, aber wenig Motivkraft hat, neu generieren oder als Referenz nutzen und mit klarerem Motiv prompten. «Schön» reicht nicht. Es muss ballern.
- Slide 10 muss als starker Engagement Trigger funktionieren: fragRoger-Emblem, KI-Literacy-Subline, CTA mit klarer Handlung. Standard: '@fragroger auf Instagram folgen', 'Carousel speichern & teilen' und themenspezifischer Kontakt-CTA.
- **UMLAUTE:** ä ö ü Ä Ö Ü immer direkt ausschreiben. ae/oe/ue als Ersatz sind verboten.
- Wenn der Nutzer eigene Bilder oder Logos liefert, diese priorisiert verwenden: Hero-Visual auf Slide 1, Marken-/Firmenlogo auf dem inhaltlich passenden Slide, optional erneut auf Slide 10. Nutzerbilder haben immer Vorrang vor KI-generierten Bildern.

## Qualitäts-Check vor Review

- [ ] Exakt 10 Slides erstellt.
- [ ] Alle Slides im 4:5-Format.
- [ ] Slide 1 enthält ein starkes Hero-Bild mit klarem Pattern Interrupt.
- [ ] Slide 2 enthält ein eigenes Bildmotiv, das den Open Loop oder Auslöser visualisiert.
- [ ] Slide 3 enthält ein eigenes Bildmotiv, das Story, Pain oder Konsequenz konkret macht.
- [ ] Slide 9 enthält ein starkes visuelles System-/Framework-Motiv für die Takeaways.
- [ ] Keine Key-Slide 1-3 oder 9 ist nur Text auf abstraktem Hintergrund.
- [ ] Keine Unterstriche, keine Trennlinien, keine horizontalen Divider.
- [ ] Jede Slide hat maximal 1 zentrale Aussage.
- [ ] Haupttext ist plakatgross gesetzt, bold-cinematisch und wirkt auch im Thumbnail lesbar.
- [ ] Die Kontaktübersicht zeigt sofort: erster Eindruck = Bildwucht, zweiter Eindruck = klare These. Wenn nicht, Key-Slides überarbeiten.
- [ ] Zeilenabstände sind positiv und sauber. Keine Kollisionen, keine gedrängte Negativ-Typografie.
- [ ] Textplatzierung ist bewusst: oben dominant, zentriert dominant oder unten dominant, nicht zufällig klein in einer Ecke.
- [ ] Struktur folgt Hook, Rehook, Pain/Story, Value 4-7, Turning Point, Takeaway, CTA.
- [ ] Caption nutzt Schweizer Rechtschreibung, enthält standardmässig `https://www.fragroger.social` und endet nur mit `#fragRoger`.
- [ ] **UMLAUT-CHECK:** Caption und alle Slide-Texte auf ae/oe/ue durchsuchen und durch ä/ö/ü ersetzen.
- [ ] Review vor Posting eingeholt.

## Referenzen

- `references/brand-design.md` - fragRoger Dark Cinematic Cyberpunk Design-System.
- `scripts/extract_blog_content.py` - KI-gestützte Extraktion der 10-Slide-Struktur.
