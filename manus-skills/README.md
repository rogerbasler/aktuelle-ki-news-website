# Manus Skills Registry

Dieser Bereich sichert die lokal verfügbaren Manus-Skills als versionierbaren Snapshot. Er gehört bewusst nicht in die Website-Logik. Die Skills bleiben damit prüfbar, vergleichbar und reproduzierbar, ohne den bestehenden KI-News-Auftritt zu verheddern.

> **Quellhoheit:** Der Ordner `manus-skills/skills/` ist der technische Snapshot. GitHub hält die nachvollziehbare Versionshistorie. Notion ist der durchsuchbare Katalog für Menschen, nicht die Quelle für Dateiinhalte.

## Struktur

| Pfad | Zweck |
|---|---|
| `skills/` | Vollständige Kopie aller verfügbaren Skills inklusive `SKILL.md`, Vorlagen und Hilfsdateien. |
| `catalog/skills.json` | Maschinenlesbares Inventar mit Prüfsummen, Dateianzahl und GitHub-Links. |
| `catalog/skills.csv` | Tabellenfreundlicher Export desselben Inventars. |
| `catalog/notion-upsert.json` | Bereinigter Datensatz für den Notion-Katalog. |
| `tools/build_manifest.py` | Erzeugt die Katalogdateien reproduzierbar aus einem Skill-Verzeichnis. |
| `tools/sync_from_manus.sh` | Führt einen atomaren lokalen Snapshot aus und baut die Katalogdateien neu. |
| `docs/` | Betriebs- und Synchronisationsdokumentation. |

## Manueller Aktualisierungslauf

Der Lauf übernimmt zuerst alle aktuellen Skills und erzeugt danach Katalogdateien. Er erstellt **keinen automatischen Commit**. Das ist Absicht: Versionierung soll überprüft werden, nicht aus Versehen passieren.

```bash
cd /pfad/zum/clone/aktuelle-ki-news-website
bash manus-skills/tools/sync_from_manus.sh /home/ubuntu/skills https://github.com/rogerbasler/aktuelle-ki-news-website
git diff --stat
git status --short
```

Nach der Prüfung wird der Snapshot bewusst versioniert und publiziert:

```bash
git add manus-skills
git commit -m "chore(skills): monatlichen Snapshot aktualisieren"
git push origin main
```

## Notion-Abgleich

Der Notion-Katalog nutzt die bestehende Datenbank **«Skill-Übersicht»**. Jeder Manus-Skill erhält einen stabilen Slug, einen GitHub-Link, eine Prüfsumme und einen Zeitstempel. Bereits bestehende ältere Skill-Einträge bleiben unangetastet.

Der Abgleich ist **einseitig**: Skill-Dateien werden von Manus nach GitHub und Notion gespiegelt. Änderungen in Notion überschreiben nie die Dateien in GitHub. Das eigentliche Problem ist nicht fehlende Synchronisation, sondern konkurrierende Wahrheiten. Diese Struktur verhindert genau das.

## Monatliche Routine

Die monatliche Aufgabe aktualisiert den Snapshot, prüft die Differenz, veröffentlicht nur echte Änderungen und gleicht anschliessend den Notion-Katalog ab. Der Lauf protokolliert Anzahl, Prüfsumme und Zeitpunkt der synchronisierten Skills.
