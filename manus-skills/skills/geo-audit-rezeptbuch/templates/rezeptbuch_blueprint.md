# Blueprint: GEO-Audit & Optimierungs-Rezeptbuch

## Verwendungszweck

Nutze diesen Blueprint, um nach einem GEO-Audit ein editierbares HTML und ein A4-PDF zu erstellen. Beginne mit belastbaren Befunden und der Scorecard. Layout ist ein Instrument für Entscheidungen, keine Ausrede für dünne Analyse.

## Designsystem

| Element | Vorgabe |
|---|---|
| Papiergrund | Warmes Off-White, z. B. `#F7F5EF`. |
| Haupttext | Fast schwarz, z. B. `#111111`. |
| Technik und Daten | Tiefblau, z. B. `#1E5AA8`. |
| Risiko und Gegenposition | Magenta/Pink, z. B. `#D91F73`. |
| To-do und Freigabe | Grün, z. B. `#7BC043`. |
| Stil | Editorial Workbook, ruhig und A4-lesbar. Keine Foliendichte. |
| Wiederkehrendes Rezept | Wirkung, Befund, Zutaten, Zubereitung, Prüfpunkt, Owner, Risiko, Messung. |
| Sprache | Schweizer Schreibweise: ä, ö, ü; verwende ss; kein Gedankenstrich als Em Dash. |

## Dokumentstruktur

| Seite | Abschnitt | Ziel |
|---:|---|---|
| 1 | Cover | Firmenname, Domain, Analysezeitpunkt, Titel und kurze GEO-These. |
| 2 | So wird das Rezeptbuch genutzt | Bewertungslegende, Quellenlogik, Analysegrenzen. |
| 3 | GEO Reality Check | GEO, SEO und AEO sauber einordnen. Keine Garantieversprechen. |
| 4 | Scorecard | Sieben Reifedimensionen, Gesamtbild und zentrale Evidenzlücken. |
| 5 | Zutatenliste und Entscheidungsgrenzen | Fehlende Daten, Zugänge, Crawler-Policy und Freigaben. |
| 6 | Mise en place: technische P0-Checks | Abrufbarkeit, Indexierbarkeit, Sitemap, Canonical und Robots. |
| 7-8 | Google Search Console Control Room | Verifikation, Sitemap, URL-Prüfung, Baseline und Betriebsrhythmus. |
| 9-10 | Bing Webmaster & IndexNow Control Room | Verifikation, Sitemapstatus, Frische, Fehlerlog und Entscheidung. |
| 11 | Entity & Schema Map | Firma, Angebote, Personen, Standorte und strukturierte Daten. |
| 12-13 | Longtail-Speisekarte | Fragencluster, Zielseiten, Suchintention, Content Gaps und Priorität. |
| 14 | FAQ-Architektur | Sichtbare Fragen, Antwortregeln, Markup-Grenzen. |
| 15-17 | Top-Rezepte | Je Seite eine priorisierte P0/P1-Massnahme im Rezeptformat. |
| 18 | KI-Antwort-Sampling | Datierte Beobachtungen nach Engine und Frage. |
| 19 | 30-60-90-Tage-Plan | Owner, Abhängigkeiten, Aufwand und Abnahme. |
| 20 | Governance & nächster Schritt | Monatsrhythmus, Change Log, erster verbindlicher Schritt. |
| 21 | Quellen und technische Notizen | Offizielle Quellen, Tools, Testdatum und Annahmen. |

## Rezeptseite

```markdown
# Rezept [Nummer]: [Massnahme]

**Wirkung:** [Welche Sichtbarkeits-, Vertrauens- oder Conversionlücke wird geschlossen?]

**Befund:** [URL/Test/Tool-Export/Quelle oder markierte Annahme]

| Zutaten | Zubereitung | Prüfpunkt |
|---|---|---|
| [Daten, Personen, Systeme, Freigaben] | 1. ... 2. ... 3. ... | [Objektive Abnahme] |

| Priorität | Owner | Aufwand | Risiko | Messung |
|---|---|---|---|---|
| P0/P1/P2 | [Rolle] | S/M/L | [Risiko] | [Baseline und Indikator] |
```

## Scorecard-Karten

Jede Scorecard-Karte enthält eine Punktzahl von 0 bis 4, einen Satz zur Lage und ein verlinktes oder klar beschriebenes Evidenzstück. Eine Zahl ohne Ursache gehört ins Schaufenster, nicht in ein Management-Dokument.

| Bewertung | Bedeutung |
|---:|---|
| 0 | Blockiert, nicht vorhanden oder nicht prüfbar. |
| 1 | Schwach, widersprüchlich oder mit hohem Risiko. |
| 2 | Grundsätzlich vorhanden, aber lückenhaft oder ungemessen. |
| 3 | Solide und operativ kontrolliert. |
| 4 | Klar, aktuell, belegt und mit messbarer Governance. |

## Endkontrolle

1. HTML in A4-PDF rendern.
2. Cover, Scorecard, dichteste Rezeptseite, Longtail-Matrix und Schlussseite visuell prüfen.
3. Seitenzahl, Quellenlinks, Tabellenüberlauf, Umbrüche und Darstellung der Umlaute prüfen.
4. Doppelt-s-Schreibweise und Gedankenstriche als Em Dash prüfen. Beides darf nicht vorkommen.
5. PDF, HTML, Blueprint, CSV-Scorecard, technischer Befund und Layoutprüfung gemeinsam ausliefern.
