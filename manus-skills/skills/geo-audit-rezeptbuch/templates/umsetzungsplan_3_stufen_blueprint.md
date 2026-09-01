# Umsetzungsplan GEO in 3 Stufen

## Zweck

Erstelle aus einem öffentlichen Basischeck oder einem bestehenden GEO-Audit einen **einfachen, rollengetrennten A4-Umsetzungsplan**. Erkläre Technik und Content so, dass ein Technik-Owner und ein Fach-/Content-Owner sofort wissen, was sie tun müssen.

> **Leitthese:** Die Organisation braucht nicht mehr KI-Text. Sie braucht technisch zugängliche Seiten, echte Fachlichkeit und einen einfachen Rhythmus zur Verbesserung.

## Designsystem

| Element | Vorgabe |
|---|---|
| Papiergrund | Warmes Off-White, z. B. `#F7F5EF`. |
| Haupttext | Fast schwarz, z. B. `#111111`. |
| Technik und Daten | Tiefblau, z. B. `#1E5AA8`. |
| Risiko und Gegenposition | Magenta/Pink, z. B. `#D91F73`. |
| To-do und Freigabe | Grün, z. B. `#7BC043`. |
| Stil | Editorial Workbook, ruhig, A4-lesbar, ohne Foliendichte. |
| Sprache | Schweizer Schreibweise: ä, ö, ü direkt; ss; kein Gedankenstrich als Em Dash. |

## Pflichtstruktur: 6-10 Seiten

| Seite | Abschnitt | Ziel |
|---:|---|---|
| 1 | Cover | Domain, Zeitpunkt, Leitthese und drei Stufen. |
| 2 | Rollenübersicht | Technik-Owner, Fach-/Content-Owner und gemeinsamer Review. |
| 3 | Stufe 1: Technik aufräumen | Tabelle: Was tun, warum, fertig wenn. |
| 4 | Stufe 2: Angebot klar machen | Höchstens drei Zielseiten, Content-Bausteine und klare CTAs. |
| 5 | KI-Schreibhilfe | Input-Regeln, Start-Prompt und menschliche Qualitätsprüfung. |
| 6 | Stufe 3: Monatlich verbessern | 30-Minuten-Review, Datensignale und Kundenfragen. |
| 7 | Kurzplan | Woche 1-2, Woche 3-8, ab Monat 3. |
| 8 | Getrennte Checklisten | Technik-Checkliste und Content-Checkliste. |
| 9-10 | Optional | Quellen, technische Grenzen, zusätzliche Checklisten oder kurze Beispiele. |

## Stufe 1: Technik-Checkliste

Passe an die Befunde an. Nutze nur relevante Punkte.

- [ ] Canonical auf Startseite und wichtigen Angebotsseiten geprüft.
- [ ] robots.txt liefert HTTP 200.
- [ ] XML-Sitemap liefert HTTP 200 und enthält nur kanonische, indexierbare URLs.
- [ ] Sitemap in Google Search Console eingereicht.
- [ ] Sitemap in Bing Webmaster Tools eingereicht.
- [ ] Öffentliche technische Fehlermeldungen beseitigt.
- [ ] Crawler-Regeln gemäss freigegebener Policy umgesetzt.
- [ ] Monatlicher 15-Minuten-Check vereinbart.

## Stufe 2: Content-Bausteine

Verwende für jede priorisierte Angebotsseite die gleiche Reihenfolge:

1. Für wen ist das Angebot?
2. Welches konkrete Problem löst es?
3. Wie läuft die Zusammenarbeit ab?
4. Welches echte Beispiel, welche Erfahrung oder freigegebene Referenz belegt die Aussage?
5. Was ist der nächste Schritt?

## KI-Schreibhilfe

Verwende nur dann KI, wenn Fachwissen und freigegebene Fakten vorhanden sind. KI darf strukturieren, formulieren, kürzen und Varianten erzeugen. Sie darf keine Fakten ergänzen oder erfinden.

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

Prüfe danach: Ist jede Aussage wahr? Ist mindestens ein Beispiel konkret? Klingt der Text nach der Organisation? Ist der nächste Schritt klar?

## Stufe 3: Monatlicher Review

| Technik-Owner bringt mit | Fach-/Content-Owner bringt mit | Gemeinsam entscheiden |
|---|---|---|
| Fehler, Sitemapstatus, neue oder auffällige Seiten, relevante Suchdaten. | Neue Kundenfragen, Einwände, Angebote, Praxisbeispiele und Freigaben. | Eine bis drei Änderungen bis zum nächsten Review. |

## Content-Checkliste

Passe an die Organisation an. Nutze nur relevante Punkte.

- [ ] Für jede priorisierte Angebotsseite die fünf Kernfragen beantwortet.
- [ ] Je Angebot mindestens ein echtes Praxisbeispiel geliefert.
- [ ] Referenzen oder Kundenstimmen freigegeben.
- [ ] Fachprofil mit aktuellen, sichtbaren Fakten freigegeben.
- [ ] Häufigste Kundenfragen gesammelt.
- [ ] Für KI-Entwürfe Stichworte, Audionotiz oder Rohtext bereitgestellt.
- [ ] KI-Entwurf auf Wahrheit, Ton und CTA geprüft.
- [ ] 30-Minuten-Review mit Technik-Owner vereinbart.

## Qualitätskontrolle

1. Keine technische Aufgabe ohne objektive Abnahme.
2. Keine Content-Aufgabe ohne fachliche Verantwortung.
3. Keine KI-Aussage ohne Faktenprüfung.
4. Keine zehn ähnlichen Seiten zu Variationen derselben Frage.
5. Keine komplizierte Roadmap. Ein bis drei Änderungen pro Monat genügen.
6. PDF auf Umbrüche, Tabellenüberlauf, Links, Umlaute, ss und Em Dash prüfen.
