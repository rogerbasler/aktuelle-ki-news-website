# fragRoger Blue Cinematic Design System

## Grundprinzip

Das fragRoger Blue Carousel wirkt wie ein dunkler, pointierter TED-Talk-Moment im Instagram-Format. Es ist **bold, cinematic, kontrastreich, extrem lesbar und plakatgross**. Die Slide soll sich nicht wie ein Arbeitsblatt anfühlen, sondern wie ein Keynote-Poster mit klarer These. Die Typografie ist nicht Dekoration, sondern das Hauptmotiv. Die Farbpalette ist konsequent Blue/Black/White - kein Pink.

## Farbpalette

| Variable | HEX | Einsatz |
|---|---|---|
| `--rbr-black` | `#000000` | Standard-Hintergrund, Dark Mode first |
| `--rbr-white` | `#ffffff` | Haupttext auf dunklem Hintergrund |
| `--rbr-electric-blue` | `#00aaff` | Primärer Neon-Akzent: Zahlen, Schlüsselwörter, CTA-Highlights |
| `--rbr-deep-blue` | `#4a7fa1` | Sekundärer Akzent: Labels, Sublines, dezente Elemente |
| `--rbr-blue-secondary` | `#1a6fa8` | Tiefes Blau für Hintergrundflächen und Glows |
| `--rbr-navy` | `#0d1b3a` | Alternative Dark-Fläche, tiefes Nacht-Blau |

Electric Blue `#00aaff` maximal einmal dominant pro Slide einsetzen - für eine Zahl, ein Schlüsselwort oder den CTA. Deep Blue `#4a7fa1` wirkt als ruhiger, technischer Gegenpol. Weiss trägt die Hauptaussage. Kein Pink, kein Hot Pink, keine warmen Farbtöne.

## Typografie

**Primärschrift:** `'Avenir Next', 'Avenir', 'Barlow Condensed', sans-serif`

Avenir ist auf macOS/iOS verfügbar. Als Fallback dient **Barlow Condensed 900**. Die Schrift muss gross, komprimiert und keynote-artig wirken.

```html
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800;900&family=Barlow:wght@400;600&family=JetBrains+Mono:wght@700&display=swap');
```

```css
font-family: 'Avenir Next', 'Avenir', 'Barlow Condensed', sans-serif;
```

| Stil | Weight | Grösse bei 480×600px | Einsatz |
|---|---|---|---|
| Hero | 900 | 78-96px bei 480×600px, 115-170px bei 1080×1350px | Slide 1 und Slide 8 |
| Main | 900 | 58-76px bei 480×600px, 82-125px bei 1080×1350px | Slides 2-7 |
| CTA | 900 | 54-72px bei 480×600px, 76-110px bei 1080×1350px | Slide 10 |
| Takeaway | 800-900 | 36-52px bei 480×600px, 58-82px bei 1080×1350px | Slide 9 |
| Support | 600 | 22-30px bei 480×600px, 34-48px bei 1080×1350px | nur kurze zweite Zeile |
| Label | 700 | 10-14px bei 480×600px, 22-32px bei 1080×1350px | kleine Orientierung, nicht dekorativer Ballast |

**Regel:** Die Headline ist die Bildachse. Wenn ein Satz nicht aus zwei Metern lesbar wäre, ist er zu klein oder zu lang. Im Zweifel wird nicht kleiner gesetzt, sondern radikaler gekürzt. Kleine Schrift ist kein Designsystem, sondern Kapitulation mit Serifen.

## Bildpflicht auf Slide 1

Slide 1 enthält immer ein Bild. Das Bild ist der Pattern Interrupt. Es darf aus einem Nutzerbild, einem gelieferten Asset oder einem KI-generierten Hero-Bild bestehen.

| Situation | Vorgehen |
|---|---|
| Nutzer liefert ein Bild | Bild als Hero-Motiv verwenden, stark zuschneiden, abdunkeln, kontrastieren. |
| Nutzer liefert mehrere Bilder | Das visuell stärkste, irritierendste oder klarste Bild für Slide 1 wählen. |
| Kein Bild vorhanden | Ein KI-Hero-Bild erzeugen, das die Kernthese visuell zuspitzt. |

Das Bild muss nicht dokumentarisch nüchtern wirken. Es darf cinematic sein: dunkle Vignette, Filmgrain, Lichtkante, harte Schatten, klares Framing.

## Verbotene Designelemente

Keine Unterstriche. Keine dünnen horizontalen Trennlinien. Keine dekorativen Divider. Keine Spray-Paint-Linien als Standard. Keine Worksheet-Karten. Keine langen Textboxen. Kein überladenes Graffiti.

Der alte Look mit Linien unter Headlines wird nicht mehr verwendet. Spannung entsteht über **Skalierung, Kontrast, Bildtiefe, Leerraum, Licht und Typografie**, nicht über Separatoren.

## Erlaubte Designelemente

| Element | Einsatz |
|---|---|
| Cinematic Vignette | Dunkle Bildränder, Fokus auf Headline oder Motiv. |
| Filmgrain | Sehr subtil, für Tiefe und Haptik. |
| Ghost-Word | Grosses, sehr transparentes Hintergrundwort, maximal ein Wort. |
| Dramatischer Crop | Besonders auf Slide 1, um Spannung zu erzeugen. |
| Massive Typografie | Hauptinstrument des Designs. |
| Einzelakzent in Electric Blue #00aaff | Für eine Zahl, ein Schlüsselwort oder CTA. Maximal einmal pro Slide. |
| Deep Blue Glow #4a7fa1 | Dezent, technisch, kühl, für Labels und Sublines. |

## Layout-Prinzipien

Jede Slide hat eine zentrale Idee. Die Komposition darf asymmetrisch sein. Nutze negative Fläche bewusst. Text nie an den Rand quetschen. Keine Slide braucht eine Erklärung, wenn die Headline stark genug ist. Body-Text ist Ausnahme, nicht Standard.

### Plakat-Modus

Der neue Standard ist **Plakat-Modus**. Das bedeutet: Headline zuerst, Bild danach. Die Hauptaussage muss auch als Thumbnail lesbar bleiben und darf nicht als kleine Textinsel auf einem schönen Hintergrund verschwinden.

| Layout-Zone | Einsatz | Wirkung |
|---|---|---|
| Oben dominant | Hook, Pain, Value-Slides | Sofortige Lesbarkeit beim Scrollen |
| Zentrum dominant | Rehook, Turning Point | Keynote-Moment, maximale Wucht |
| Unten dominant | Takeaway oder CTA | Bühne für Bildmotiv im oberen Bereich |

Verwende pro Slide bewusst gesetzte Zeilenumbrüche mit maximal 3-5 Wörtern pro Zeile. Die Headline soll rund 35-55% der sichtbaren Komposition tragen. Auf Slide 1 und Slide 8 darf sie noch dominanter sein. Ein einzelnes Electric-Blue-Wort (#00aaff) kann die Blickführung setzen. Blue ist ein Skalpell, kein Konfettikanonchen. Kein Pink.

## Struktur der 10 Slides

| Slide | Typ | Design-Fokus |
|---|---|---|
| 1 | HOOK | Bildpflicht, Pattern Interrupt, 5-10 Wörter, maximal plakatgross |
| 2 | REHOOK | Open Loop, mehr Spannung, keine Auflösung, zentral oder oben dominant |
| 3 | RELATABLE PAIN / STORY START | Wiedererkennung, kurze Story, persönlicher Einstieg, grosse Typo statt Erklärung |
| 4-7 | VALUE | Story + Insight, eine Idee pro Slide, kurze Zeilen und starke Fläche |
| 8 | TURNING POINT | Aha-Moment, speicherwürdige Perspektive, zweitgrösster Typografie-Moment nach Slide 1 |
| 9 | ACTIONABLE TAKEAWAY | 2-3 klare Schritte, sofort anwendbar, jeder Schritt gross lesbar |
| 10 | CTA | Direkter Engagement Trigger, nicht klein, nicht höflich, klarer Call |

## CTA-Slide

Slide 10 ist nicht mehr zwingend immer identisch. Sie muss zum Inhalt passen und eine klare Handlung auslösen. Gute CTA-Varianten:

```text
Kommentiere «CHECKLISTE» und ich sende sie Dir.
```

```text
Folge @fragroger für klare KI-Denkanstösse.
```

```text
Speichere das, bevor es im Feed verschwindet.
```

Der CTA soll spezifisch, kurz und direkt sein. Keine Hashtag-Wand. Kein generisches «Like und teile» ohne Grund.

## Qualitätsstandard

Ein gutes fragRoger Black Cinematic Carousel fühlt sich an wie eine kurze Keynote: starke These, kontrollierte Spannung, klare Einsicht, konkrete Handlung. Wenn eine Slide aussieht wie ein PDF-Auszug, ist sie falsch. Wenn sie im Kontaktbogen nicht sofort lesbar ist, ist die Schrift zu klein. Ein bisschen frech darf sie sein. Albern nicht. Wir sind nicht im Kinderprogramm, auch wenn der Algorithmus manchmal so tut.
