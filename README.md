# Social Listening Intelligence Dashboard

Öffentliches, wöchentlich aktualisiertes Social-Listening-Dashboard für **Roger Basler de Roca** mit Fokus auf Schweizer und DACH-KMU.

## Zweck

Das Dashboard verdichtet öffentliche Markt-, Marken-, Wettbewerbs- und Zielgruppensignale zu konkreten Entscheidungen. Es trennt konsequent zwischen **Fakt**, **Interpretation** und **Hypothese**. Quellen werden nach Currency, Reliability, Authority und Purpose geprüft.

## Beobachtungsfelder

1. **Eigene Marke:** Roger Basler de Roca, #fragRoger, ThinkRoger und ki-power.me
2. **Themenmarkt:** KI im Unternehmen, AI Agents, KI-Regulierung, KI und Arbeitsmarkt, Educational Consulting
3. **Wettbewerb:** öffentlich sichtbare deutschsprachige KI-Berater:innen, Speaker und Weiterbildungsanbieter
4. **Zielgruppen-Signale:** Schweizer und DACH-KMU, Geschäftsleitungen sowie Marketing-, HR- und Innovationsverantwortliche

## Aktualisierung und Archiv

Die Startseite `index.html` bleibt das einzige aktuelle Dashboard. Vor jeder wöchentlichen Aktualisierung wird der bisherige Stand als datierter HTML-Snapshot unter `archiv/social-listening/JJJJ/` gesichert. Frühere KI-News- und Tool-Ausgaben bleiben ebenfalls im Archiv erhalten.

Der aktuelle strukturierte Datenstand liegt in `data/social-listening/current.json`. Der vollständige Quellenbericht steht in [`RESEARCH.md`](./RESEARCH.md).

## Reproduzierbarer Build

```bash
python3 scripts/archive_current_dashboard.py
python3 scripts/build_social_dashboard.py
```

Vor dem Ersetzen der aktuellen Daten archiviert `scripts/archive_current_dashboard.py` das bestehende HTML und JSON. Die Datenanreicherung für den CRAP-Audit erfolgt mit `scripts/enrich_social_report.py`. Alle Skripte verwenden nur die Python-Standardbibliothek.

## Datenhinweis

Interne Instagram-Insights werden nur verwendet, wenn im verbundenen Instagram-Connector ein aktives Konto ausgewählt ist. Ohne Kontoauswahl nutzt das Dashboard ausschliesslich öffentlich sichtbare Informationen und weist die Datenlücke explizit aus.

## Veröffentlichung

Das Repository wird über GitHub Pages mit der Custom Domain [news.fragroger.ai](http://news.fragroger.ai/) veröffentlicht.
