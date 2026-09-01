---
name: geo-audit-rezeptbuch
description: >
  Erstellt evidenzbasierte GEO-Analysen, technische Optimierungspläne und A4-PDF-Rezeptbücher für Firmen, KMU, B2B-Dienstleister, lokale Unternehmen, E-Commerce, Industrie, Professional Speaker und regulierte Branchen. Verwenden bei: GEO Analyse, Generative Engine Optimization, KI-Sichtbarkeit, AI Search Audit, AEO, ChatGPT-Suche optimieren, Google AI Mode, Google Search Console, Bing Webmaster Tools, IndexNow, Longtail Keywords, FAQ-Architektur, Schema Markup, robots.txt, Crawler-Policy oder GEO-Rezeptbuch. Verwenden auch bei: einfacher GEO-Plan, GEO in drei Stufen, GEO für Webmaster und Content, GEO Aufgaben verteilen, Webmaster-Checkliste oder Content-Checkliste nach GEO-Audit.
---

# GEO-Audit & Optimierungs-Rezeptbuch

## Zweck und Haltung

Erstelle eine **nachvollziehbare GEO-Analyse** und einen priorisierten Optimierungsplan. GEO verspricht keine Erwähnung in einem KI-System. Prüfe stattdessen, ob eine Website technisch zugänglich, inhaltlich verständlich, als Unternehmensentität eindeutig, fachlich belegbar, transaktionsfähig und messbar ist.

> **Arbeitsregel:** Formuliere keine Plattform-, Ranking- oder Citation-Garantien. Dokumentiere jeden Befund mit URL, technischem Test, Tool-Export, Quelle oder klar markierter Annahme.

GEO ergänzt SEO, ersetzt es nicht. Lies vor jeder Einordnung `references/geo-grundlagen.md`.

## Variante wählen

| Situation | Variante | Ergebnis |
|---|---|---|
| Öffentliche Domain liegt vor. | `Audit` | Vollständiger technischer, inhaltlicher und strategischer Audit mit Evidenz-Scorecard. |
| Keine Website oder keine prüfbare Domain liegt vor. | `Blueprint` | Informationsarchitektur, technische Anforderungen und Roadmap mit klaren Annahmen. |
| Search-Console- und/oder Bing-Exports liegen vor. | `Datenvertiefung` | Reale Abfragen, Seiten, Länder und Zeiträume ergänzen den Audit. |
| Nur Management-Prioritäten werden verlangt. | `Kurzrezept` | Scorecard, fünf Prioritäten und 30-60-90-Tage-Plan. |
| Nach einem Audit wird ein einfacher, rollengetrennter Umsetzungsplan verlangt. | `Umsetzungsplan 3 Stufen` | 6-10 A4-Seiten für Technik-Owner und Fach-/Content-Owner, inklusive Checklisten und KI-Schreibhilfe. |

Wähle `Umsetzungsplan 3 Stufen` auch bei Formulierungen wie "einfacher", "für Webmaster und Content", "wer macht was", "in drei Stufen" oder "Checkliste". Diese Variante ersetzt keinen Voll-Audit, sondern übersetzt dessen Befunde in Arbeitspakete.

## Benötigte Inputs

Frage nur nach fehlenden Angaben. Markiere nicht prüfbare Punkte als **offen**, nicht als Mangel.

| Input | Audit | Umsetzungsplan 3 Stufen | Nutzen |
|---|---:|---:|---|
| Domain | Ja, ausser Blueprint | Ja, falls technische Aufgaben enthalten sind | Öffentliche Analyse und technische Evidenz. |
| Geschäftsmodell und Kernangebote | Ja | Ja | Angebots-, Entitäts- und Conversion-Logik. |
| Zielgruppe und Region | Ja | Empfohlen | Longtail- und lokale Suchintention. |
| Search-Console-Export | Empfohlen | Optional | Reale Abfragen und Seitenperformance. |
| Bing-Export | Empfohlen | Optional | Bing-spezifische Abfragen und Sitemap-Befunde. |
| Analytics, CRM oder Vertriebssprache | Optional | Empfohlen | Echte Kundensprache und Conversion-Qualität. |
| Crawler- und Datenschutzpolicy | Empfohlen | Bei robots.txt nötig | Bewusste Entscheidung zu Sichtbarkeit und Training. |

## Gemeinsame Evidenzregeln

1. Lies `references/technischer-check.md` vor technischem Audit oder Schema-Empfehlungen.
2. Lies `references/plattformen-und-crawler.md` vor Aussagen zu Google, Bing, IndexNow oder Crawler-Policy.
3. Lies `references/longtail-und-faq.md` vor Longtail-, FAQ- oder KI-Antwort-Sampling.
4. Behandle Search Console und Bing Webmaster Tools als Steuerungszugänge, nie als Rankingbonus.
5. Empfehle Markup nur für sichtbare, korrekte und validierbare Fakten.
6. Trenne OAI-SearchBot, GPTBot und ChatGPT-User. Automatisiere keine pauschale Freigabe weiterer Bots.
7. Behandle `llms.txt` als optionales Experiment. Es ersetzt weder Sitemap noch Qualitätsarbeit und ist kein nachgewiesener Performance-Hebel.
8. Verwende keine dünnen Longtail-Seiten, unsichtbaren FAQs, Keyword-Stuffing oder manipulative Markups.

## Workflow: Audit, Blueprint, Datenvertiefung und Kurzrezept

1. **Kontext und Grenzen festlegen.** Kläre Angebote, Märkte, Sprachen, Zielgruppen, gewünschte Handlung und Datenlage.
2. **Technische Basis prüfen.** Führe zuerst aus:

   ```bash
   python3 /home/ubuntu/skills/geo-audit-rezeptbuch/scripts/geo_basischeck.py https://beispiel.ch --output /home/ubuntu/geo-audit/technische_befunde.json
   ```

   Prüfe HTTPS, Statuscodes, robots.txt, Sitemap, Meta Robots, Canonical, Sprachkennzeichnung, sichtbares HTML, strukturierte Daten, interne Links und technische Konsistenz. Das Script ist eine Vorprüfung, kein vollständiger Crawler oder Security-Audit.
3. **Google Search Console prüfen.** Prüfe Domain Property, Ownership, Sitemap-Status, Startseite plus drei strategische URLs, Performance-Baseline, Indexierungs- und Verbesserungsbefunde sowie monatlichen Owner. Fordere bei vorhandenen Daten Exporte für Abfragen, Seiten und Indexierung/Sitemaps an.
4. **Bing und IndexNow prüfen.** Prüfe Verifikation, Sitemap, `last read`, Verarbeitungsfehler, Indexierungsbefunde und bei häufigen Änderungen eine dokumentierte IndexNow-Entscheidung.
5. **Entität und Vertrauen prüfen.** Vergleiche sichtbare Firmen-, Personen-, Standort-, Angebots-, Referenz- und Kontaktfakten mit möglichem Markup.
6. **Longtail und Zielseiten entwickeln.** Verwende zuerst Search-Console-, Bing-, Sales-, Support- und CRM-Sprache. Cluster nach Problem, Vergleich, Lösung, Lokal, Transaktion und Vertrauen. Weise jeder wichtigen Frage genau eine Zielseite zu.
7. **Sichtbare FAQs entwickeln.** Nutze echte Fragen, Einwände und Prozessunsicherheiten. Gib direkte Antworten, Grenzen, Belege und passende nächste Schritte. `FAQPage` ist optional und kein Rich-Result- oder Citation-Versprechen.
8. **Crawler-Policy dokumentieren.** Halte Zweck, Betreiber, betroffene Inhalte, Entscheidung, Begründung, Freigabe und Retest fest.
9. **KI-Antwort-Sampling dokumentieren.** Teste 15-30 priorisierte Fragen. Speichere Datum, Engine, Modus, Locale, exakte Frage, Erwähnung, Quellen, Antwortauszug und Einschränkung. Präsentiere Beobachtungen nie als stabile Sichtbarkeitsquote.
10. **Priorisieren.** Nutze P0 für 14 Tage, P1 für 30-60 Tage und P2 als Ausbau. Berücksichtige Blockade, Wirkung, Aufwand, Abhängigkeit, Risiko, Owner und objektive Abnahme.

## Workflow: Umsetzungsplan 3 Stufen

Nutze diesen Workflow, wenn der Audit in eine einfache Umsetzungslogik übersetzt werden soll. Führe bei einer vorhandenen Domain mindestens den technischen Basischeck aus oder verwende dokumentierte Befunde eines bestehenden Audits.

### 1. Rollen generisch festlegen

Verwende diese Rollen, sofern die Organisation keine anderen Namen vorgibt:

| Rolle | Zuständigkeit |
|---|---|
| **Technik-Owner** | CMS, Hosting, Canonical, robots.txt, Sitemap, sichtbare Fehler, Search Console, Bing und technische Releases. |
| **Fach-/Content-Owner** | Angebote, fachliche Korrektheit, Praxisbeispiele, Referenzen, Freigaben, Ton und CTA. |
| **Gemeinsamer Review** | Monatliche Priorisierung einer Verbesserung anhand von Fehlern, Daten und Kundenfragen. |

Weise nie stillschweigend alle Aufgaben einer einzigen Person zu. Jede Aufgabe braucht Owner, minimalen Input und Abnahme.

### 2. Stufe 1: Technik aufräumen

Priorisiere Canonical, robots.txt, XML-Sitemap, sichtbare technische Fehler, Google Search Console und Bing Webmaster Tools. Formuliere für jede Aufgabe nur: **Was tun? Warum? Fertig, wenn?**. Halte Crawler-Freigaben als Fach- und Policy-Entscheid fest.

### 3. Stufe 2: Angebot klar machen

Wähle höchstens drei priorisierte Angebotsseiten. Der Fach-/Content-Owner liefert für jede Seite:

1. Für wen ist das Angebot?
2. Welches konkrete Problem löst es?
3. Wie läuft die Zusammenarbeit ab?
4. Welches echte Beispiel, welche Erfahrung oder freigegebene Stimme belegt die Aussage?
5. Was ist der nächste Schritt?

Der Technik-Owner setzt Struktur, Medien, CTA, interne Links und die technisch saubere Publikation um.

### 4. Verantwortungsvolle KI-Schreibhilfe

Erlaube KI für erste Entwürfe, Gliederungen, Varianten, Kürzungen, FAQ-Entwürfe und Zusammenfassungen. Der Fach-/Content-Owner liefert Stichworte, Audionotizen, echte Beispiele, freigegebene Fakten, Grenzen und CTA. KI strukturiert und formuliert, erfindet aber nichts.

> **Qualitätsregel:** Schlechter Input erzeugt generischen Text. Gute Fachlichkeit entsteht aus konkreten Situationen, echten Erfahrungen, einer klaren Haltung und anschliessender menschlicher Prüfung.

Verwende diesen anpassbaren Start-Prompt:

```text
Du bist eine sachliche Website-Redaktion. Schreibe eine Seite über [ANGEBOT] für [ZIELGRUPPE].
Die Person hat dieses Problem: [PROBLEM].
So arbeitet die Organisation oder Fachperson: [ABLAUF / METHODE].
Dieses echte, freigegebene Beispiel darf verwendet werden: [BEISPIEL].
Diese Haltung oder Grenze ist wichtig: [HALTUNG / TABU].
Verwende nur diese bestätigten Fakten: [FAKTEN].
Erfinde keine Zahlen, Ergebnisse, Kundenstimmen, Referenzen, Preise oder rechtlich relevanten Aussagen.
Baue die Seite so auf: Für wen, wobei hilft es, wie läuft es ab, warum diese Lösung, nächster Schritt.
Schliesse mit diesem CTA: [CTA].
```

Lass den Fach-/Content-Owner jeden Entwurf gegen vier Fragen prüfen: Ist jede Aussage wahr? Ist mindestens ein Beispiel konkret? Klingt der Text nach der Organisation? Ist der nächste Schritt klar?

### 5. Stufe 3: Monatlich verbessern

Führe einen 30-Minuten-Review ein. Der Technik-Owner bringt Fehler, Sitemap-Status, relevante Seiten- und Suchdaten. Der Fach-/Content-Owner bringt neue Kundenfragen, Einwände, Angebote und Beispiele. Entscheidet gemeinsam nur eine bis drei konkrete Änderungen bis zum nächsten Review.

### 6. Abschlusschecklisten

Beende jeden Umsetzungsplan mit zwei getrennten Checklisten. Erstelle sie auf Basis von `templates/umsetzungsplan_3_stufen_blueprint.md`.

- **Technik-Checkliste:** Canonical, robots.txt, XML-Sitemap, Search Console, Bing, sichtbare Fehler, freigegebene Crawler-Regeln und Monatscheck.
- **Content-Checkliste:** Angebotsfragen, echte Praxisbeispiele, Referenzfreigaben, aktuelles Fachprofil, Kundenfragen, KI-Input, KI-Review und gemeinsamer Review-Termin.

## Ausgabeformate

### Voll-Audit

Lies vor der Gestaltung `templates/rezeptbuch_blueprint.md` und verwende `templates/scorecard.csv`. Erstelle zuerst ein vollständiges Markdown-Blueprint, dann editierbares HTML und rendere ein A4-PDF.

| Datei | Pflichtinhalt |
|---|---|
| `geo_rezeptbuch.pdf` | A4-Entscheidungs- und Umsetzungsdokument. |
| `geo_rezeptbuch.html` | Editierbare HTML-Quelle mit eingebettetem CSS. |
| `content_blueprint.md` | Befunde, Annahmen, Massnahmen, Quellen und Seitenlogik. |
| `geo_scorecard.csv` | Bewertungs- und Evidenzdaten. |
| `technische_befunde.json` | Ergebnis des Basischecks, falls eine Domain vorliegt. |
| `layout_pruefung.md` | Visuelle und technische Endkontrolle. |

### Umsetzungsplan 3 Stufen

Lies vor der Gestaltung `templates/umsetzungsplan_3_stufen_blueprint.md`. Erstelle ein 6-10-seitiges A4-Arbeitsdokument. Nutze keine Scorecard, wenn sie nicht für die Entscheidung nötig ist.

| Datei | Pflichtinhalt |
|---|---|
| `geo_3_stufen.pdf` | Rollengetrennter A4-Umsetzungsplan. |
| `geo_3_stufen.html` | Editierbare HTML-Quelle mit eingebettetem CSS. |
| `webmaster_checkliste.md` | Technische Aufgaben mit Abnahmen. |
| `content_checkliste.md` | Fach-/Content-Aufgaben inklusive KI-Review. |
| `ki_schreibhilfe.md` | Start-Prompt, Input-Regeln und Qualitätsprüfung. |
| `layout_pruefung.md` | Visuelle und technische Endkontrolle. |

Nutze helles Editorial-Workbook-Design: schwarzer Text für Thesen, Blau für Technik und Daten, Pink für Risiken und Gegenpositionen, Grün für priorisierte To-dos. Verwende für Deutsch Schweizer Schreibweise: ä, ö, ü direkt; ss statt ß; kein Gedankenstrich als Em Dash.

## Qualitätsregeln

- Zitiere offizielle Plattformdokumentation und Primärquellen bei Tatsachenbehauptungen.
- Markiere Annahmen klar. Verwechsle fehlende Daten nicht mit fehlender Qualität.
- Prüfe PDF auf Seitenzahl, Links, Quellen, Tabellenüberlauf, Umbrüche, Umlaute, ss-Schreibweise und Em Dash.
- Verwechsle KI-unterstütztes Schreiben nie mit ungeprüfter Veröffentlichung.
- Verbiete erfundene Zahlen, Ergebnisse, Testimonials, Referenzen, Preise, Verfügbarkeiten und rechtlich relevante Aussagen.
- Halte die einfache Variante einfach: maximal drei Angebotsseiten, ein 30-Minuten-Review und eine bis drei Änderungen pro Monat.

## Referenzen und Ressourcen

| Ressource | Wann laden oder verwenden |
|---|---|
| `references/geo-grundlagen.md` | Immer, vor Begriffsklärung und strategischer Einordnung. |
| `references/technischer-check.md` | Technischer Audit, Schema, robots.txt, Sitemap und IndexNow. |
| `references/plattformen-und-crawler.md` | Google Search Console, Bing Webmaster Tools und Crawler-Policy. |
| `references/longtail-und-faq.md` | Longtail-Cluster, Zielseiten, sichtbare FAQs und Query-Sampling. |
| `scripts/geo_basischeck.py` | Öffentliche technische Basisprüfung. |
| `templates/rezeptbuch_blueprint.md` | Voll-Audit als A4-Rezeptbuch. |
| `templates/scorecard.csv` | Scorecard und Evidenzregister für Voll-Audit. |
| `templates/umsetzungsplan_3_stufen_blueprint.md` | Rollengetrennter, einfacher Umsetzungsplan. |

## Trigger-Beispiele

- "Analysiere unsere Website für ChatGPT, Google AI Mode und Bing Copilot und liefere ein PDF."
- "Mach einen GEO-Audit für unser Schweizer KMU."
- "Erstelle aus diesem Search-Console-Export Longtail-Seiten und einen GEO-Fahrplan."
- "Prüfe unsere Bing Webmaster Tools, Sitemap und IndexNow-Strategie."
- "Baue eine FAQ-Architektur, aber ohne SEO-Märchen."
- "Wir brauchen ein GEO-Rezeptbuch für unseren B2B-Vertrieb."
- "Mach uns einen einfachen GEO-Plan für Webmaster und Content."
- "Teile die GEO-Aufgaben in drei Stufen auf."
- "Erstelle nach dem Audit eine Webmaster- und Content-Checkliste."
