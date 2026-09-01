# Technischer GEO-Basischeck

## Zweck

Diese Referenz führt die technischen Voraussetzungen zusammen. Sie ist eine Prüfliste für Zugänglichkeit, Verstehen und Aktualität. Sie ersetzt weder einen Security-Audit noch eine vollständige technische SEO-Prüfung.

## P0: Abrufbarkeit und Indexierbarkeit

| Prüffeld | Was prüfen | Akzeptanzkriterium | Typische Massnahme |
|---|---|---|---|
| HTTPS und Antwort | Start- und strategische URLs abrufen. | Endgültige URL liefert HTTP 200 über HTTPS. | Fehlerseiten, Redirect-Ketten und Mixed Content korrigieren. |
| robots.txt | Abrufbarkeit, Syntax, Sperren für wichtige Pfade und Sitemap-Zeile. | Kritische Seiten und nötige Suchcrawler nicht versehentlich gesperrt. | Sperren begründen, Sitemap referenzieren, Test wiederholen. |
| Meta Robots | `noindex`, `nofollow`, `nosnippet`, `data-nosnippet`, `max-snippet` prüfen. | Keine unbeabsichtigte Ausschliessung strategischer Seiten. | Unbeabsichtigte Direktiven entfernen oder bewusst dokumentieren. |
| Canonical | Selbstreferenz und Ziel-URL prüfen. | Eine kanonische, indexierbare Ziel-URL pro Inhaltsvariante. | Widersprüchliche Parameter-, Sprach- oder CMS-Canonicals korrigieren. |
| Sitemap | XML-Sitemap, HTTP-Status und URL-Qualität prüfen. | Nur kanonische, indexierbare URLs; echte Aktualisierungsdaten. | Sitemap bereinigen, in Search Console und Bing einreichen. |
| Sichtbares HTML | Titel, H1, Kernangebot, Kontakt und Haupttext im HTML prüfen. | Strategische Fakten sind nicht nur in unzugänglichen Interaktionen versteckt. | Server Rendering oder zugängliche Fallbacks priorisieren. |
| Sprache und Region | `lang`, bei Mehrsprachigkeit `hreflang` und gegenseitige Referenzen prüfen. | Sprachversionen sind korrekt ausgezeichnet und erreichbar. | Sprach-/Ländervarianten konsolidieren. |

## P1: Informationsstruktur und Seitenqualität

| Prüffeld | Was prüfen | Akzeptanzkriterium |
|---|---|---|
| Titel und Beschreibung | Eindeutiger Seitentitel, präzise Meta Description. | Leistung, Zielgruppe oder Thema der Seite klar. |
| Überschriften | Eine nachvollziehbare H1-H2-H3-Struktur. | Abschnitte sind für Menschen und Systeme semantisch lesbar. |
| Interne Verlinkung | Kontextlinks zwischen Leistungs-, Case-, Fach- und Kontaktseiten. | Strategische Zielseiten sind nicht isoliert. |
| Medien | Relevante Bilder, Tabellen, PDFs und Alt-Texte. | Medien stützen die Aussage und sind nicht nur Dekoration. |
| Aktualität | Datum, Autoren, Änderungshistorie und zeitkritische Fakten. | Keine veralteten Zahlen oder vorgetäuschte Frische. |
| Conversion | Kontakt, Termin, Angebot, Kauf oder lokale Handlung. | Zielhandlung ist sichtbar, verständlich und funktionsfähig. |

## Strukturierte Daten

Strukturierte Daten müssen sichtbare Inhalte korrekt wiedergeben. Validiere mit Google Rich Results Test, Schema Validator und, falls vorhanden, Search Console. Google empfiehlt bei lokalen Unternehmensdaten: passende Eigenschaften ergänzen, Markup validieren, per URL-Prüfung testen und Sitemap einreichen.

| Typ | Sinnvoll bei | Mindestinhalt | Nicht tun |
|---|---|---|---|
| `Organization` | Firmen, Verbände, Schulen, NGOs. | Name, URL, Logo, Kontakt sofern sichtbar. | Erfundene Auszeichnungen oder Profile verknüpfen. |
| `LocalBusiness` | Lokale Filiale oder örtliches Unternehmen. | Name, Adresse, Telefonnummer, Öffnungszeiten, URL. | Falsche Filialen oder unzutreffende Einzugsgebiete. |
| `Service` | Konkrete Dienstleistungen. | Sichtbare Leistungsbeschreibung und Anbieterbezug. | Allgemeine Phrasen als scheinbare Leistungen modellieren. |
| `Product`/`Offer` | Reale Produkte mit sichtbaren Daten. | Name, Bild, Preis/Verfügbarkeit nur wenn zutreffend. | Fantasiepreise, Verfügbarkeit oder Reviews. |
| `Person`/`ProfilePage` | Fachpersonen, Sprecher, Führungskräfte. | Name, Rolle, fachlich belegbare Informationen. | Kompetenz ohne Quelle behaupten. |
| `Article` | Fachartikel, Cases, Guides. | Headline, Autor, Bild und echtes Änderungsdatum. | `dateModified` bei jeder technischen Speicherung ändern. |
| `FAQPage` | Sichtbare FAQ-Fragen mit einer Antwort. | Vollständige sichtbare Fragen und Antworten. | Google-Rich-Result- oder Citation-Wirkung versprechen. |
| `QAPage` | Echte Nutzerfragen mit mehreren Beiträgen. | Frage, Antworten, Urheber. | Normale Unternehmens-FAQ damit auszeichnen. |

## Sitemap und Aktualität

Google und Bing können Sitemaps zur URL-Entdeckung nutzen. Bing betont für KI-gestützte Suche besonders vollständige XML-Sitemaps, echte `lastmod`-Werte, die Referenzierung in robots.txt, die Übermittlung in Bing Webmaster Tools und, bei häufigen Änderungen, IndexNow.

| Entscheidung | Empfehlung |
|---|---|
| Kleine statische Website | XML-Sitemap, robots.txt-Referenz, Einreichung in Google und Bing; manueller Retest bei wichtigen Änderungen. |
| CMS mit regulären Änderungen | Automatische Sitemap, korrekte Canonicals, echte `lastmod`-Werte, monatliche Fehlerkontrolle. |
| Shop, News, Marktplatz oder Verzeichnis | XML-Sitemap und IndexNow bewerten; Schlüssel, CMS-Integration, Fehler- und Change-Log definieren. |
| Mehrsprachige Website | Separate klare URL-Struktur, `hreflang`, konsistente Canonicals, Sitemap-Qualität je Sprachversion. |

`changefreq` und `priority` sind keine glaubwürdigen Steuerhebel. Verwende ein `lastmod` nur dann, wenn sich der Inhalt der URL substanziell verändert hat.

## Crawler-Policy

Führe eine Crawler-Entscheidungstabelle. Bei jeder Regel müssen Zweck, Betreiber, Quelle, Inhaltstyp, Risiko, Policy-Owner und Retest-Datum sichtbar sein.

| Crawler-Gruppe | Grundsatz |
|---|---|
| Googlebot und Bingbot | Nicht aus Versehen blockieren, wenn Google- oder Bing-Sichtbarkeit gewünscht ist. |
| OAI-SearchBot | Bei gewünschter Darstellung in ChatGPT-Suche und nach Policy-Freigabe gezielt beurteilen. |
| GPTBot | Getrennt von OAI-SearchBot betrachten, weil es mögliche Trainingsnutzung betrifft. |
| ChatGPT-User | Nicht als automatischen Suchcrawler behandeln; nutzerinitiiert und nicht zur Steuerung von Search-Opt-outs bestimmt. |
| Weitere KI-Bots | Nicht nach Namen oder Gerüchten automatisieren. Offizielle Dokumentation und Unternehmerrichtlinie prüfen. |

## Quellen

[1]: https://developers.google.com/search/docs/appearance/structured-data/local-business "Google Search Central: LocalBusiness structured data"
[2]: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap "Google Search Central: Build and submit a sitemap"
[3]: https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search "Microsoft Bing: Sitemaps in AI-powered search"
[4]: https://developers.openai.com/api/docs/bots "OpenAI Developers: Crawlers und robots.txt"
