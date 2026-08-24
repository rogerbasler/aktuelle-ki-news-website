---
name: lowpoly-triangles-ppt-template
description: Erstellung und Bearbeitung von Präsentationen auf Basis der FT006 LowPoly-Triangles 16:9 PowerPoint-Vorlage mit konsequenter Sketchnote-Bildwelt und blauer Akzentfarbe. Verwenden, wenn der Nutzer die DEMO PPT Vorlage, LowPoly Triangles, FT006, weisse Dreiecks-Vorlage, PresentationLoad LowPoly Template, Sketchnote-Bildwelt, blaue Akzente oder eine Präsentation in genau diesem klaren geometrisch-handgezeichneten Look wünscht.
---

# LowPoly Triangles PPT Template

## Zweck

Verwenden, um neue PowerPoint-Präsentationen im Stil der mitgelieferten Datei `FT006_LowPoly-Triangles_16x9_DE.pptx` zu erstellen oder bestehende Inhalte in diese Vorlage zu übertragen. Der Stil ist **minimalistisch, weissraumstark, geometrisch und sketchnote-basiert**, mit Low-Poly-Dreiecken als Layout-Klammer und handgezeichneten Visuals als Bildwelt. Die Vorlage eignet sich für klare Business-, Consulting-, Schulungs- und Demo-Präsentationen, wenn Seriosität wichtiger ist als grafischer Lärm. Also meistens.

## Ressourcen

| Ressource | Pfad | Zweck |
|---|---|---|
| PowerPoint-Vorlage | `templates/FT006_LowPoly-Triangles_16x9_DE.pptx` | Originale Arbeitsvorlage mit Master, Layouts, eingebetteten Fonts und Low-Poly-Grafiken |
| Analysebericht | `references/ft006_template_analysis.md` | Technische Analyse der Folien, Farben, Fonts, Medien, Platzhalter und Layouttypen |
| Kontaktübersicht | `references/ft006_contact_sheet.png` | Visuelle Übersicht aller 17 Folien der Demo-Vorlage |
| Arbeitskopie-Skript | `scripts/create_working_copy.py` | Erstellt eine neue `.pptx`-Arbeitskopie aus der gebündelten Vorlage |

Lese `references/ft006_template_analysis.md`, wenn präzise Layout-, Farb- oder Platzhalterdetails nötig sind. Öffne `references/ft006_contact_sheet.png`, wenn die Auswahl eines passenden Demo-Layouts visuell entschieden werden soll.

## Design-DNA

Halte das Design bewusst reduziert. Die Wirkung entsteht durch **grosszügigen Weissraum, starke Titel, kleine Textmengen und kantige Dreiecksakzente**. Die Vorlage nutzt ein 16:9-Format mit mehreren Master-Varianten in Farbe, Grau und Blau.

| Element | Vorgabe |
|---|---|
| Format | 16:9 Widescreen |
| Grundfläche | Weiss oder sehr helles Grau |
| Hauptakzent | Blau `#3498DB` als verbindliche Akzentfarbe für Icons, Linien, Hervorhebungen und Sketchnote-Details |
| Sekundärfarben | Schwarz `#000000`, Weiss `#FFFFFF`, Grau `#7F7F7F`, helles Grau `#E1E1E1`; Rot `#C8303F`, Grün `#9BBB59` und Gelb `#FFC000` nur sparsam für Status, Risiko oder Hervorhebungen |
| Typografie | Grosse, schmale Headline-Schrift für Titel; einfache Sans-Serif-Schrift für Fliesstext |
| Bildsprache | Handgezeichnete Sketchnote-Illustrationen, einfache Linien-Icons, Marker-Flächen, Pfeile, Rahmen und kleine Figuren mit blauem Akzent; Low-Poly-Dreiecke bleiben als geometrische Layout-Klammer erhalten |
| Textmenge | Kurze Headlines, maximal 3 bis 5 Bullet Points pro Inhaltsfolie |

Verwende die Dreiecksformen als visuelle Klammer, nicht als Tapete. Die Bildwelt muss immer wie eine **saubere Business-Sketchnote** wirken: schwarze handgezeichnete Linien, weisser Hintergrund, blaue Akzentstriche, bewusst einfache Symbolik. Das eigentliche Problem vieler Präsentationen ist nicht zu wenig Design, sondern zu wenig Priorisierung.

## Verwendbare Layouttypen

Die Demo-Datei enthält 17 sichtbare Folien und 35 Layouts. Für neue Präsentationen sind vor allem folgende Muster relevant:

| Layouttyp | Demo-Folien | Verwendung |
|---|---:|---|
| Cover, farbig | 1, 3 | Starker Einstieg, Programm, Keynote, Workshop-Titel |
| Cover, grau | 6, 8 | Seriöser Einstieg, Executive-Version, ruhige Variante |
| Cover, blau | 11, 13 | Technologie-, Daten- oder KI-Themen mit kühlerer Wirkung |
| Eine Textbox | 2, 7, 12 | These, zentrale Erklärung, kompakte Argumentation |
| Zwei Textboxen | 4, 9, 14 | Vergleich, Vorher-Nachher, Problem-Lösung, zwei Perspektiven |
| Promo-/Beispielfolien | 5, 10, 15 | Nicht als inhaltliches Kernlayout verwenden, ausser bewusst als Kachel-/Ressourcenübersicht adaptiert |
| Font-/Copyrightfolien | 16, 17 | Nicht in Kundendecks übernehmen, ausser rechtliche Hinweise sind ausdrücklich erforderlich |

## Workflow für neue Präsentationen

1. **Arbeitskopie erzeugen.** Kopiere nie direkt in der gebündelten Vorlage herum. Nutze bei Bedarf:

   ```bash
   python /home/ubuntu/skills/lowpoly-triangles-ppt-template/scripts/create_working_copy.py /home/ubuntu/output/neue_praesentation.pptx
   ```

2. **Inhalte zuerst verdichten.** Erstelle vor dem Layouten eine klare Storyline. Jede Folie braucht eine Entscheidung: informieren, kontrastieren, beweisen, aktivieren oder abschliessen.

3. **Passende Layoutmuster wählen.** Nutze Cover für Einstieg und Kapitelwechsel, Ein-Textbox-Folien für Kernthesen, Zwei-Textbox-Folien für Gegensätze oder Entscheidungslogik.

4. **Demo-Texte konsequent ersetzen.** Entferne Placeholder wie `TEXT 1 BOX`, `TEXT 2 BOXES`, `Enter your subheadline here`, `Enter your footer text here`, Foliennummer-Dummies, Beispiel-Logos und Demo-Verweise.

5. **Branding bewusst setzen.** Ersetze das Demo-Logo nur, wenn der Nutzer ein eigenes Logo oder eine neutrale Version wünscht. Bei externer Nutzung Copyright- und Lizenzhinweise der Quelle beachten.

6. **Foliendesign kontrollieren.** Prüfe am Ende: keine überfüllten Folien, keine uneinheitlichen Bullet-Ebenen, keine zufälligen Farbmischungen, keine abgeschnittenen Dreiecke durch falsches Skalieren.

## Empfohlene Story-Strukturen

Für Business-Präsentationen diese robuste Struktur bevorzugen:

| Abschnitt | Funktion | Typische Layouts |
|---|---|---|
| Titel | Thema und Relevanz setzen | Cover |
| Problem | Spannung und Entscheidungsbedarf zeigen | Eine Textbox oder zwei Textboxen |
| Einordnung | Kontext, Markt, Daten oder Ursache erklären | Eine Textbox |
| Lösung | Ansatz, Modell oder Vorgehen darstellen | Zwei Textboxen |
| Beleg | Beispiel, Datenpunkt, Case oder Mini-Framework | Eine Textbox, optional Kachelansicht |
| Umsetzung | Schritte, Rollen, Zeitplan oder 90-Tage-Logik | Zwei Textboxen |
| Abschluss | Entscheidung, Call-to-Action, nächste Schritte | Cover oder reduzierte Textfolie |

Wenn die Präsentation für Roger erstellt wird, eine **prägnante These**, eine **systemische Einordnung**, eine **konkrete Implikation** und eine **entscheidungsrelevante Schlussfolgerung** pro Abschnitt bevorzugen. Schweizer Schreibweise verwenden.

## Textregeln

Schreibe kurz, klar und mit hoher Informationsdichte. Keine Buzzword-Parade. Die Vorlage verträgt keine Bleiwüsten, und sie hat recht damit.

| Element | Empfehlung |
|---|---|
| Titel | 3 bis 7 Wörter, stark und konkret |
| Untertitel | 1 präzisierender Satz, maximal 14 Wörter |
| Bullet Points | 3 bis 5 Punkte, je maximal 1 Zeile wenn möglich |
| Zwei-Spalten-Folien | Links Problem oder Ausgangslage, rechts Konsequenz oder Lösung |
| Fusszeile | Nur nutzen, wenn Datum, Anlass oder Quellenhinweis relevant ist |

Geeignete Formulierungslogik:

> Das eigentliche Problem ist nicht ..., sondern ...

> Was oft unterschätzt wird: ...

> Der entscheidende Unterschied liegt in ...

> Die Konsequenz daraus ist: ...

## Umgang mit Bildern, Charts und Diagrammen

Nutze keine generische Stockfoto-Bildwelt. Wenn ein Bild oder Key Visual nötig ist, muss es als **Sketchnote** gedacht und umgesetzt werden: handgezeichnete Linien, reduzierte Figuren, Pfeile, Sprechblasen, kleine Frameworks, Mini-Szenen und blaue Akzente. Der visuelle Stil soll menschlich, erklärend und leicht roh wirken, aber nicht kindlich. Entscheidend ist Verständlichkeit, nicht Doodle-Dekoration.

| Visual-Typ | Vorgabe |
|---|---|
| Key Visual | Eine zentrale Sketchnote-Szene mit schwarzer Linienzeichnung, weissem Hintergrund und blauem Fokus-Element |
| Icons | Handgezeichnete Line-Icons, maximal zweifarbig: Schwarz plus Blau `#3498DB` |
| Diagramme | Schlicht, flach, mit blauen Akzenten und optional handgezeichneten Pfeilen oder Rahmen |
| Personen | Einfache Sketchnote-Figuren, keine realistischen Fotos, keine überzeichnete Comic-Ästhetik |
| Hintergründe | Weiss oder sehr helles Grau, keine Foto-Texturen, keine schweren Verläufe |

Für Datenfolien einfache Diagramme bevorzugen: Balken, Linien, Wasserfall, 2x2-Matrix oder Prozesslogik. Keine 3D-Effekte ergänzen, ausser sie sind bereits sauber in der Vorlage angelegt. Wenn Diagramme erstellt werden, Blau als primäre Akzentfarbe verwenden und Beschriftungen auf das Minimum reduzieren. Der Chart soll die Aussage tragen, nicht die Folie in Excel cosplayen lassen.

### Sketchnote-Promptmuster

Wenn ein Visual generiert oder beschrieben wird, dieses Muster verwenden und fachlich anpassen:

> Minimalistische Business-Sketchnote auf weissem Hintergrund, schwarze handgezeichnete Linien, klare geometrische Komposition passend zu einer LowPoly-Triangle-PowerPoint-Vorlage, blaue Akzentfarbe `#3498DB` für Fokuslinien und Hervorhebungen, einfache Symbole, Pfeile, Rahmen, kleine abstrahierte Figuren, viel Weissraum, professionell, präzise, erklärend, keine Stockfoto-Optik, keine realistischen Personen, keine Comic-Übertreibung.

## Qualitätscheck vor Auslieferung

Vor der Auslieferung prüfen:

| Prüffrage | Erwartung |
|---|---|
| Ist jede Demo-Beschriftung entfernt? | Ja |
| Passt jede Folie zu einem klaren Layouttyp? | Ja |
| Sind Titel und Bullet Points kurz genug? | Ja |
| Sind Dreiecksakzente konsistent und nicht zufällig platziert? | Ja |
| Ist die Bildwelt konsequent als Sketchnote umgesetzt? | Ja |
| Wird Blau `#3498DB` als primäre Akzentfarbe verwendet? | Ja |
| Sind generische Stockfotos und beliebige Clipart-Elemente vermieden? | Ja |
| Sind Farben aus der Vorlage übernommen und zugunsten von Blau kontrolliert reduziert? | Ja |
| Sind Promo-, Font- und Copyrightfolien entfernt oder bewusst genutzt? | Ja |
| Liegt das Ergebnis als `.pptx` vor? | Ja, wenn Präsentation erstellt wurde |

## Rechtlicher Hinweis zur Vorlage

Die Vorlage enthält Hinweise auf PresentationLoad und erlaubt laut Demo-Folie die Nutzung für persönliche, edukative und geschäftliche Präsentationen. Nicht als eigenes Template weiterverkaufen oder als originär eigenes Werk ausgeben. Bei Kundendecks und öffentlicher Verteilung die Herkunft und Lizenzhinweise respektieren. Kreativität ist gut. Lizenzhygiene ist besser.
