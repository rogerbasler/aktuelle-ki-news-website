---
name: polymarket-trading-bot
description: "Aufbau, Betrieb und Haertung eines Polymarket-Trading-Agenten mit Analyse, Paper-Trading, Risiko-Kontrollen und optionalem Live-Trading. Verwenden bei: Polymarket-Marktanalyse, Aufbau einer Trading-CLI, Entwicklung autonomer Agent-Loops, Einrichtung von Gamma-API- und CLOB-Workflows, Vorbereitung von Wallet- und L2-Credentials."
---

# Polymarket Trading Bot

Verwende dieses Skill, wenn ein wiederverwendbarer Workflow fuer **Polymarket-Marktanalyse**, **Paper-Trading**, **autonome Agent-Loops** oder **optionales Live-Trading** aufgebaut werden soll. Behandle **Compliance, Credential-Sicherheit und Risk Controls** als harte Randbedingungen. Arbeite standardmaessig im **Paper-Modus** und aktiviere Live-Trading nur, wenn der Nutzer dies ausdruecklich verlangt und die lokale Konfiguration vollstaendig vorhanden ist.[1] [2] [3]

## Zielbild

Erstelle eine lokale oder serverseitige Ausfuehrungsumgebung mit drei Schichten. Die erste Schicht sammelt Daten aus der **Gamma API** und den oeffentlichen CLOB-Read-Endpunkten. Die zweite Schicht bewertet Maerkte und erzeugt strukturierte Handelsentscheidungen. Die dritte Schicht setzt die Entscheidungen nur dann um, wenn Risiko- und Betriebsregeln eingehalten werden.[1] [2]

Verwende fuer Live-Trading bevorzugt offizielle oder dokumentierte SDK-Pfade statt handgeschriebener Signierlogik. Die CLOB-Dokumentation beschreibt einen zweistufigen Authentifizierungsprozess mit **L1** zur Ableitung der API-Credentials und **L2** fuer authentifizierte Handelsanfragen. Auch bei L2-Requests muessen Orders lokal signiert werden.[2] [3]

## Arbeitsreihenfolge

Arbeite in der folgenden Reihenfolge und ueberspringe keinen Schritt, ausser der Nutzer gibt eine klare Begruendung. Halte jeden Schritt in einem Artefakt fest, etwa in einer Konfigurationsdatei, einer JSONL-Logdatei oder einem kurzen Markdown-Protokoll.

| Schritt | Zweck | Ergebnis |
| --- | --- | --- |
| 1 | Betriebs- und Compliance-Rahmen klaeren | Festlegung, ob nur Analyse, Paper-Trading oder Live-Trading gewuenscht ist |
| 2 | Marktdatenzugriff pruefen | Erfolgreiche Abfrage von Gamma-API- und CLOB-Read-Daten |
| 3 | Risk-Policy definieren | Konfiguration fuer Positionsgroessen, Tagesverlust, Exponierung und Kill-Switch |
| 4 | Paper-Execution bauen | Simulierte Orders, Positionen und PnL ohne reale Ausfuehrung |
| 5 | Agent-Loop haerten | Logging, Fehlerbehandlung, Wiederanlauf und manuelle Stop-Moeglichkeit |
| 6 | Optional Live-Trading vorbereiten | L2-Credentials, Signaturtyp, Funder-Adresse und dry-run-Checks |

## Datenquellen und Zustaendigkeiten

Nutze die APIs bewusst getrennt. Die **Gamma API** dient der Marktsuche und Metadaten-Ermittlung. Die oeffentlichen CLOB-Endpunkte dienen Preis-, Spread- und Orderbook-Abfragen. Authentifizierte CLOB-Endpunkte sind fuer Orders, Cancels und nutzerspezifische Operationen reserviert.[1] [2]

| Schicht | Quelle | Authentifizierung | Typische Aufgabe |
| --- | --- | --- | --- |
| Discovery | Gamma API | Keine | Maerkte, Events, Token-IDs, Metadaten |
| Market Read | CLOB Read | Keine | Orderbuch, Preise, Spreads, Tick Size |
| Execution | CLOB Trading | L2 + lokale Ordersignatur | Orders posten, canceln, offene Orders abfragen |

## Sicherheitsregeln

Speichere **Private Keys**, **API Secret** und **Passphrase** niemals in Versionskontrolle oder clientseitigem Code. Halte geheime Werte in `.env`-Dateien oder einer sicheren Secret-Verwaltung. Die offizielle Dokumentation betont explizit, dass private Schluessel nie exponiert werden duerfen und authentifizierte Requests aus einer vertrauenswuerdigen Laufzeit kommen muessen.[2]

Implementiere einen sicheren Standardzustand. Wenn Konfigurationen fehlen, schalte automatisch auf **read-only** oder **paper**. Wenn der Betriebsmodus `live` gesetzt ist, aber L2-Credentials, Signaturtyp oder Funder-Adresse fehlen, stoppe die Ausfuehrung mit einer klaren Fehlermeldung statt mit stillschweigendem Fallback.

## Mindestkonfiguration

Lege eine YAML- oder TOML-Konfiguration an, die mindestens Betriebsmodus, Polling-Intervall, Liquiditaetsfilter und Risikogrenzen enthaelt. Halte Geheimnisse in `.env`, nicht in der allgemeinen Konfigurationsdatei.

| Bereich | Pflichtfelder |
| --- | --- |
| Modus | `mode`, `poll_interval_seconds` |
| Marktfilter | `min_liquidity_usd`, `max_spread_bps`, `max_time_to_resolution_hours` |
| Risiko | `max_daily_loss_pct`, `max_position_pct`, `max_total_exposure_pct`, `edge_threshold_pct`, `confidence_threshold_pct` |
| Live-Handel | `POLYMARKET_API_KEY`, `POLYMARKET_API_SECRET`, `POLYMARKET_API_PASSPHRASE`, optional `PRIVATE_KEY`, `SIGNATURE_TYPE`, `FUNDER_ADDRESS` |
| Modellanalyse | Modellname, Basisprompt, Timeout, Max-Kandidaten pro Zyklus |

## Referenzarchitektur fuer die Implementierung

Organisiere das Projekt in klar getrennte Module. Halte Discovery, Analyse, Risiko, Execution und Logging in separaten Dateien. Wenn ein Agent-Loop verwendet wird, muss dessen Kernlogik klein bleiben und nur orchestrieren.

| Modul | Verantwortung |
| --- | --- |
| `market_data` | Maerkte laden, filtern, Token-IDs und Orderbook-Daten normieren |
| `strategy` | Edge, Confidence, Positionsgroesse und Entscheidungsrichtung ableiten |
| `risk` | Tagesverlust, Positionslimits, Blacklists, Kill-Switch und Notbremsen erzwingen |
| `paper_broker` | Simulierte Orders und PnL verwalten |
| `live_broker` | Authentifizierte CLOB-Aufrufe kapseln |
| `agent_loop` | Zeitgesteuerte Ausfuehrung, Fehlerbehandlung und State-Management |
| `logging_tools` | JSONL-Logs, Audit-Events und optionale Reports schreiben |

## Entscheidungsformat

Erzwinge fuer jede Strategie oder Modellanalyse eine strukturierte Antwort. Freitext allein ist fuer Trading-Entscheidungen unzureichend. Nutze ein JSON-Format mit festen Schluesseln, damit Risiko- und Execution-Schicht deterministisch arbeiten koennen.

> Gib fuer jeden Kandidaten genau ein JSON-Objekt mit den Feldern `decision`, `est_prob`, `edge_pct`, `confidence_pct`, `size_pct`, `max_entry_price`, `thesis`, `risks` und `time_horizon_minutes` zurueck.

Verwerfe Antworten, die nicht parsebar sind, und logge den Fehler. Fuehre in diesem Fall keinen Trade aus.

## Risk Controls

Bilde die wichtigsten Schutzmechanismen doppelt ab: einmal in der Strategie und einmal unmittelbar vor der Ausfuehrung. Das verhindert, dass ein Modellfehler allein zu einer unkontrollierten Ausfuehrung fuehrt.

| Kontrolltyp | Regel |
| --- | --- |
| Tagesverlust | Stoppe alle neuen Trades, wenn realisierte plus unrealisierte PnL unter dem Grenzwert liegt |
| Positionsgroesse | Begrenze pro Markt die Exponierung auf einen kleinen Prozentsatz des Kontostands |
| Gesamt-Exponierung | Halte die Summe aller offenen Positionen unter einer Obergrenze |
| Kandidatenfilter | Handle nur Maerkte mit ausreichender Liquiditaet und akzeptablem Spread |
| Kill-Switch | Pruefe vor jedem Zyklus eine Dateiflag oder einen externen Override |
| Cooldown | Vermeide Mehrfachausfuehrungen auf demselben Markt innerhalb kurzer Intervalle |

## Standard-Workflow fuer neue Aufgaben

Beginne mit einem **Readiness Check**. Lade einige aktive Maerkte, extrahiere `clobTokenIds`, pruefe Preise oder Orderbuch und schreibe ein kurzes Verifikationsprotokoll. Implementiere danach zunaechst **Paper-Trading** mit synthetischer Positionsfuehrung. Aktiviere den Agent-Loop erst, wenn manuelle Einzeltests erfolgreich sind. Erst danach darf ein Live-Broker angebunden werden.[1] [2]

Wenn der Nutzer nach einem autonomen Bot fragt, formuliere den Ablauf explizit als `scan -> analyze -> enforce risk -> execute -> log -> sleep`. Halte Zustandsdaten in Dateien oder einer kleinen lokalen Datenbank, damit Neustarts nachvollziehbar bleiben.

## Betriebsregeln fuer autonome Ausfuehrung

Setze die Schleife so auf, dass sie bei Fehlern nicht abstuerzt, sondern den Fehler mit Zeitstempel loggt, eine Backoff-Pause einlegt und erst dann fortsetzt. Schreibe fuer jede Entscheidung einen Audit-Eintrag mit Marktreferenz, Preiseingang, Entscheidungsgrundlage, Risikopruefung und tatsaechlicher Aktion. Falls ein Kill-Switch aktiv ist, fuehre nur Logging aus und keine Order-Funktionen.

## Live-Trading-Checkliste

Vor jedem Wechsel von `paper` auf `live` muessen folgende Punkte erfuellt sein.

| Pruefung | Erwartung |
| --- | --- |
| Credentials | L2-Credentials vorhanden und plausibel |
| Wallet-Modell | `signature_type` und `funder_address` korrekt fuer EOA oder Proxy/Safe |
| Funds | Ausreichend USDC.e; bei EOA auch POL fuer Gas |
| Dry Run | Marktdaten, Tick Size und Orderparameter erfolgreich verifiziert |
| Limits | Risk-Policy aktiv und getestet |
| Stop-Mechanismus | Kill-Switch oder manueller Override funktionsfaehig |

## Wann zusaetzliche Ressourcen lesen

Lies `references/implementation_notes.md`, wenn konkrete Endpunkte, Umgebungsvariablen oder Modulnamen benoetigt werden. Lies `references/console_workflow.md`, wenn eine interaktive CLI oder REPL aufgebaut oder erweitert werden soll. Verwende `templates/env.example` als Ausgangspunkt fuer lokale Konfigurationen. Nutze `scripts/check_killswitch.py` oder aequivalente Helfer fuer deterministische Betriebspruefungen, statt die gleiche Logik wiederholt neu zu schreiben.

## Ausfuehrungshinweise

Schreibe Nutzerantworten und technische Dokumentation in klaren Abschnitten mit kurzer Begruendung fuer Designentscheidungen. Wenn Live-Trading angefragt wird, dokumentiere deutlich, welche Teile wirklich implementiert sind, welche Credentials lokal benoetigt werden und welche Schritte der Nutzer selbst validieren muss. Mache keine Aussagen, die geografische oder regulatorische Beschraenkungen relativieren.

## References

[1]: https://docs.polymarket.com/quickstart "Quickstart - Polymarket Documentation"
[2]: https://docs.polymarket.com/api-reference/authentication "Authentication - Polymarket Documentation"
[3]: https://docs.polymarket.com/trading/overview "Overview - Polymarket Documentation"
