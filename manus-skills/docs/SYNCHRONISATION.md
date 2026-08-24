# Betriebsanleitung: Manus Skills synchronisieren

## Zielbild

Der Prozess ist absichtlich **einseitig**. Lokale Manus-Skills werden nach GitHub exportiert und im bestehenden Notion-Katalog referenziert. GitHub ist die versionierte technische Referenz, während Notion Suche, Kontext und Orientierung liefert.

| System | Rolle | Schreibrichtung |
|---|---|---|
| Lokale Skill-Bibliothek | Operative Quelle zum Zeitpunkt der Ausführung | Export nach GitHub |
| GitHub | Versionierte Referenz und vollständiges Archiv | Übernahme des Snapshots |
| Notion «Skill-Übersicht» | Durchsuchbarer Katalog mit Metadaten und Deep Links | Abgeleitet aus GitHub-Snapshot |

## Ablauf eines Synchronisationslaufs

1. Die aktuelle lokale Skill-Bibliothek wird vollständig in `manus-skills/skills/` kopiert.
2. Das Manifest ermittelt je Skill Name, Kurzbeschreibung, Kategorie, Dateianzahl, Speicherbedarf und SHA-256-Prüfsumme des gesamten Skill-Verzeichnisses.
3. Der Git-Diff wird geprüft. Ohne Differenz wird kein leerer Commit erzeugt.
4. Bei echten Änderungen wird der neue Snapshot nach `main` publiziert.
5. Der Notion-Katalog wird anhand des stabilen Slugs abgeglichen. Neue Skills werden angelegt, veränderte Datensätze aktualisiert und unveränderte übersprungen.
6. Die Statistik des Laufs wird dokumentiert.

## Idempotenz und Konfliktregeln

| Situation | Regel |
|---|---|
| Ein Skill existiert noch nicht in Notion | Neuen Datensatz mit Slug und GitHub-Link erstellen. |
| Prüfsumme hat sich geändert | Metadaten, Prüfsumme, GitHub-Link und Zeitstempel aktualisieren. |
| Prüfsumme ist identisch | Keinen Schreibvorgang ausführen. |
| Ein älterer, nicht von Manus verwalteter Notion-Eintrag hat denselben Anzeigenamen | Nicht verändern. Der stabile Slug entscheidet über die Zuordnung. |
| Ein lokaler Skill wurde entfernt | Im GitHub-Snapshot entfernen; Notion-Eintrag als «Archiviert» markieren, nicht löschen. |

## Sicherheits- und Qualitätskontrollen

Vor jedem Publizieren muss der laufende Prozess prüfen, ob mindestens eine `SKILL.md` im Quellverzeichnis vorhanden ist. Das Exportwerkzeug verwendet einen temporären Staging-Ordner und ersetzt den Snapshot erst nach erfolgreicher Kopie. Dies verhindert einen halbfertigen Bestand bei abgebrochener Ausführung.

Keine Zugangsdaten gehören in Skill-Snapshots oder Katalogdateien. Falls ein Skill versehentlich einen Schlüssel enthält, wird der Lauf gestoppt und der Schlüssel vor dem Commit entfernt oder rotiert. Ein Repository ist kein Safe, selbst wenn es sich gerade nett anfühlt.

## Monatliche Aufgabe

Die geplante Aufgabe wird einmal monatlich ausgeführt. Sie aktualisiert den GitHub-Snapshot und gleicht anschliessend die Notion-Datenbank ab. Ihre Ausführung soll nach dem Lauf mindestens folgende Kennzahlen zurückmelden: Anzahl lokal gefundener Skills, neu angelegte Notion-Einträge, aktualisierte Notion-Einträge, archivierte Einträge und Commit-Referenz.
