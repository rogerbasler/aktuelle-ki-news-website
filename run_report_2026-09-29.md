# Run-Report: KI Power Update

**Ausführung:** 29. September 2026  
**Zielseite:** https://rogerbasler.github.io/aktuelle-ki-news/  
**Repository:** `rogerbasler/aktuelle-ki-news-website`

## Ergebnisübersicht

Die Ausgabe wurde auf **exakt 15 sichtbare, duplikatfreie Meldungen** begrenzt und im verlangten Verhältnis 5 + 4 + 3 + 2 + 1 kategorisiert. Alle sichtbaren Überschriften sind deutsch formuliert. Die Seite trägt den Titel **KI Power Update**, führt im Header den Hinweis **powered by www.ki-power.me** und enthält in der Fusszeile die verlangte Formulierung.

| Prüfkriterium | Ergebnis |
|---|---|
| Kandidatenrecherche | 45 Originalartikel aus t3n, heise, Handelsblatt und TechCrunch dokumentiert |
| Finale Auswahl | 15 Meldungen, keine inhaltlichen Duplikate |
| Verteilung | 5 KI News der Woche, 4 Tools & Startups, 3 Regulierung & Ethik, 2 Stimmen & Perspektiven, 1 Business & Society |
| Sichtbare Titel | vollständig auf Deutsch |
| Quellen-URLs | direkte Originalartikel-URLs, keine Übersichtsseiten |
| Linkprüfung | alle 15 URLs zweimal geprüft, siehe `auswahl_und_linkpruefung_2026-09-29.md` |
| Datum | 29. September 2026 |
| Geschützte Dateien | `style.css` und `ki-update-podcast-episode-1.wav` unverändert |

## Podcast-Skript

Das neue Skript liegt in `podcast_skript_2026-09-29.md` vor. Es beginnt ohne Begrüssung mit der Frage: "Was bedeuten die neuen Sicherheitsvorfälle bei OpenAI für Unternehmen, die KI-Agenten bereits heute mit echten Aufgaben betrauen?" Das Skript ist in drei geeignete Chunks gegliedert, umfasst 502 Wörter und hat bei angenommener Basisgeschwindigkeit von 2,5 Wörtern pro Sekunde und Tempo 1.4 eine rechnerische Zielzeit von **143,4 Sekunden**.

## HeyGen-Audio: transparenter Status

Die verpflichtende HeyGen-Erzeugung wurde **nicht durchgeführt**. Daher wurde auch keine Stimme ausgewählt und es gibt **keine erfundene Voice-ID**.

| Anforderung | Status | Dokumentierte Ursache |
|---|---|---|
| HeyGen API | nicht zugänglich | Die vorhandene HeyGen-API-Anbindung wurde aktiviert, stellte aber in der Ausführungsumgebung keinen API-Schlüssel bereit. |
| Voice Library | nicht zugänglich | Die HeyGen-Stimmenbibliothek leitete auf eine Anmeldeseite weiter. Ohne authentifizierten Zugriff können Sprache, Geschlecht und Stil nicht belastbar gefiltert, mindestens drei Kandidatinnen nicht angehört und keine öffentliche Voice-ID verifiziert werden. |
| Stimme "Lea inside sitting" ersetzen | nicht ausgeführt | Kein autorisierter Zugriff auf die Voice Library. |
| Audio-Chunks mit HeyGen erstellen | nicht ausgeführt | Kein verifizierbarer HeyGen-Zugang. |
| Geschwindigkeit 1.4 | nicht auf Audiodatei angewendet | Keine neue, autorisiert erzeugte Audiodatei vorhanden. |
| MP3 aktualisieren | nicht ausgeführt | Gemäss Vorgabe wurde kein nicht autorisierter Voice-Fallback verwendet. Die bestehende Audio-Datei blieb unverändert. |

> Die Ursachen sind eine Zugriffs- und Autorisierungseinschränkung, nicht ein Qualitätsurteil über vorhandene Stimmen. Eine Auswahl ohne hörbare Vorschau oder verifizierte Voice-ID wäre geraten, und Raten ist bei Audio-Publishing ungefähr so sinnvoll wie Governance per Glückskeks.

## Linkprüfung

Die Linkprüfung ist separat in `auswahl_und_linkpruefung_2026-09-29.md` dokumentiert. Jede finale URL wurde erst technisch mit Weiterleitungsauflösung und danach inhaltsbasiert geprüft. Die fünf t3n-URLs antworteten auf den automatisierten HTTP-Abruf mit `406`, waren jedoch in der zweiten Prüfung auf exakt derselben Original-URL mit Titel und Artikelinhalt erreichbar. Alle 15 Quellen verweisen damit auf funktionierende Originalartikel.

## Veröffentlichung und Verifikation

Die Veröffentlichung erfolgte am 29. September 2026 **ausschliesslich über die GitHub-Git-API**. Dabei wurden Blob-, Tree-, Commit- und Ref-Endpunkte verwendet, nicht `git push`.

| Prüfschritt | Ergebnis |
|---|---|
| Commit | `0e7b06ee4981886a23ca8692178a48d1a50ea638` |
| Commit-Nachricht | `Update KI News - 29. September 2026` |
| Main-Referenz | zeigt auf denselben Commit |
| GitHub-Pages-Build | Status `built`, erstellt 29.09.2026 um 13:15:23 UTC, abgeschlossen um 13:16:40 UTC |
| Rohdatei via GitHub Contents API | Titel, Datum, Header, Fusszeile und 15 News-Karten geprüft |
| Kanonische Pages-Domain | https://news.fragroger.ai/ live mit der aktualisierten Seite und 15 Meldungen geprüft |

### Abweichung der vom Auftrag genannten URL

Die GitHub-Pages-API meldet für dieses Repository als kanonische Domain **https://news.fragroger.ai/**. Diese Domain zeigt nach dem erfolgreichen Build die neue Seite.

Die im Auftrag genannte Adresse `https://rogerbasler.github.io/aktuelle-ki-news/` zeigte bei zwei Abrufen nach dem Build weiterhin eine ältere, inhaltlich andere Seite vom 26. September 2026. Diese Ausgabe entspricht weder dem aktuellen Main-Branch noch der GitHub-Pages-Konfiguration des ausgewählten Repositorys. Der direkte Pages-Build und die kanonische Domain sind verifiziert; die Abweichung der Projekt-URL liegt ausserhalb der in diesem Repository konfigurierten Pages-Quelle und wurde deshalb nicht mit einer unautorisierten Änderung an einem anderen Repository übergangen.
