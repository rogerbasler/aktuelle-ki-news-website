# Google Search Console, Bing Webmaster Tools und Crawler-Policy

## Google Search Console: Pflichtmodul

Google Search Console liefert Daten zu Suchanfragen, Seiten, Impressionen, Klicks und Positionen, erlaubt die Übermittlung von Sitemaps und einzelnen URLs und zeigt Crawl-, Indexierungs- und Serving-Informationen über die URL-Prüfung. Nutze sie als Steuerungsinstrument, nicht als Signal für einen angeblichen Rankingbonus.

### Setup und Erstprüfung

| Reihenfolge | Schritt | Abnahme |
|---:|---|---|
| 1 | Domain Property anlegen. DNS-Verifikation bevorzugen, wenn die Organisation alle Subdomains und Protokolle abdecken soll. | Eigentumsnachweis und Owner dokumentiert. |
| 2 | XML-Sitemap einreichen. | Sitemap abrufbar; nur kanonische und indexierbare URLs. |
| 3 | Vier URL-Prüfungen durchführen: Startseite, Kernleistung, Fach-/Case-Seite, Kontakt-/Produktseite. | Crawl erlaubt, Indexierung plausibel, Canonical korrekt, keine überraschende Sperre. |
| 4 | Performance-Baseline exportieren. | Abfragen und Seiten für 90, 180 und, sofern verfügbar, 16 Monate gespeichert. |
| 5 | Indexierungs- und Verbesserungsbefunde priorisieren. | P0/P1/P2, Owner, Termin und Retest definiert. |
| 6 | Monatsrhythmus festlegen. | Neuer Inhalt, Fehlermeldungen, Sitemaps und Auswirkungen werden geprüft. |

### Für Longtail verwertbare Exporte

- Abfragen: Klicks, Impressionen, CTR, durchschnittliche Position, Land, Gerät und Zeitraum.
- Seiten: Klicks, Impressionen, CTR, durchschnittliche Position und zugeordnete Themencluster.
- Indexierung/Sitemaps: betroffene URLs, Grund, Status, letzter Abruf und Fehlerklasse.

Nenne eine Query nie automatisch ein „Keyword-Potenzial“. Prüfe zuerst Suchintention, Seite, Qualität der Antwort, Conversion-Nähe und Geschäftsrelevanz.

## Bing Webmaster Tools: Pflichtmodul

Bing empfiehlt für KI-gestützte Suche vollständige XML-Sitemaps, zutreffende `lastmod`-Werte, eine robots.txt-Referenz und die Übermittlung über Bing Webmaster Tools. Bei häufigen Änderungen kann IndexNow die Aktualisierungsmitteilung ergänzen. Sitemaps und IndexNow verbessern die Entdeckbarkeit und Aktualität, garantieren aber keine Darstellung in Bing oder Copilot.

### Setup und Erstprüfung

| Reihenfolge | Schritt | Abnahme |
|---:|---|---|
| 1 | Website hinzufügen und verifizieren. Wenn passend, bestehende Google-Search-Console-Verifikation übernehmen. | Website-Property vollständig und Owner dokumentiert. |
| 2 | XML-Sitemap einreichen und in robots.txt referenzieren. | Einreichstatus erfolgreich; letzter Abruf sichtbar; Fehler registriert oder behoben. |
| 3 | Indexierungs- und Qualitätsbefunde prüfen. | Kritische URL- oder Crawlprobleme als P0/P1/P2 erfasst. |
| 4 | IndexNow bewerten. | Entscheidung, technischer Owner, Schlüsselverwaltung und Change-Log definiert. |
| 5 | Bing-Suchdaten exportieren und gegen Google spiegeln. | Unterschiede nach Query, Seite, Land oder Zeitrahmen dokumentiert. |
| 6 | Monatlichen Review festlegen. | Sitemap, Fehler, neue/aktualisierte URLs, IndexNow und Longtail-Entwicklung geprüft. |

## Longtail-Datenprozess

| Quelle | Was entnehmen | Was damit tun |
|---|---|---|
| Search Console | Bestehende Abfragen, Zielseiten, CTR- und Impressionslücken. | Unklare Seiten verbessern, echte Content-Gaps identifizieren, Wirkung messen. |
| Bing Webmaster Tools | Bing-spezifische Abfragen, Sitemaps, Indexierungs- und Qualitätsbefunde. | Unterschiede zur Google-Nachfrage prüfen, technische Aktualität sichern. |
| CRM, Sales und Support | Kundenworte, Einwände, Kriterien, Ausschlussgründe, Fragen vor Abschluss. | Fragearchitektur und Conversion-Inhalte entwickeln. |
| Briefings und Angebote | Branchenbegriffe, Leistungsumfang, Entscheidungsphasen, Regionen. | B2B-, lokale oder transaktionale Longtails präzisieren. |

## Crawler-Policy-Template

Eine robots.txt-Regel ist kein blosses Technikdetail. Sie ist eine Geschäftsentscheidung über Sichtbarkeit, mögliche Trainingsnutzung und Rechte an Inhalten.

| Feld | Inhalt |
|---|---|
| Crawler/User-Agent | Exakte Bezeichnung gemäss offizieller Dokumentation. |
| Betreiber und Zweck | Search, Training, nutzerinitiiertes Abrufen oder anderer Zweck. |
| Betroffene Inhalte | Gesamte Domain oder begrenzter Bereich. |
| Entscheidung | Erlauben, blockieren, nur Teilbereich, offen. |
| Begründung | Sichtbarkeit, Datenschutz, Lizenz, Geschäftsmodell, Reputation. |
| Freigabe | Verantwortliche Person und Datum. |
| Retest | Datum und offizielle Quelle für Nachprüfung. |

### OpenAI: Mindestunterscheidung

| User-Agent | Zweck gemäss OpenAI | GEO-Konsequenz |
|---|---|---|
| OAI-SearchBot | Darstellung von Websites in ChatGPT-Suchfunktionen. | Bei gewünschter ChatGPT-Sichtbarkeit und freigegebener Policy gezielt zulassen. |
| GPTBot | Mögliche Nutzung von Inhalten zum Training von Grundlagenmodellen. | Separate Datenschutz- und Lizenzentscheidung; nicht mit Search verwechseln. |
| ChatGPT-User | Nutzerinitiiertes Abrufen von URLs durch ChatGPT oder Custom GPTs. | Keine automatische Crawler-/Search-Regel. |

## Monatliche Betriebsroutine

| Woche | Google | Bing | Inhalt/Governance |
|---|---|---|---|
| 1 | Neue Indexierungs- und Sitemap-Befunde. | Sitemapstatus, `last read`, Fehler, IndexNow. | Aktualisierte Seiten und reale `lastmod`-Werte. |
| 2 | Longtail-Abfragen und Seitenlücken. | Bing-Longtails und Abweichungen. | Neue FAQ-Fragen aus Sales und Support. |
| 3 | URL-Prüfung für neue oder reparierte P0/P1-Seiten. | Kritische URLs gegentesten. | Quellen, Case Studies und Profile prüfen. |
| 4 | Monatliche Baseline und Change Log. | Monatsvergleich und offene Fehler. | Prioritäten, Owner und nächste Testhypothesen festlegen. |

## Quellen

[1]: https://search.google.com/search-console/about "Google Search Console"
[2]: https://support.google.com/webmasters/answer/9008080 "Google Search Console Help: Verify site ownership"
[3]: https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search "Microsoft Bing: Sitemaps in AI-powered search"
[4]: https://developers.openai.com/api/docs/bots "OpenAI Developers: Overview of OpenAI Crawlers"
