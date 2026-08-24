# Konsolen-Workflow fuer Polymarket-Agenten

## Ziel

Die Konsole dient als kontrollierte Betriebsoberflaeche fuer Discovery, Marktpruefung, Paper-Trading und optionalen Live-Betrieb. Sie soll nicht nur Befehle ausfuehren, sondern den Betriebszustand erklaeren, aktive Risiken sichtbar machen und vor gefaehrlichen Modi warnen.

## Empfohlene Befehlsgruppen

| Gruppe | Zweck | Typische Kommandos |
| --- | --- | --- |
| Discovery | Maerkte finden und filtern | `scan`, `show-market`, `orderbook` |
| Simulation | Paper-Orders und PnL | `paper-buy`, `paper-sell`, `positions`, `pnl` |
| Betrieb | Agent-Loop und Status | `autopilot`, `status`, `logs`, `killswitch` |
| Live | Vorbereitete echte Ausfuehrung | `live-buy`, `live-sell`, `cancel-order` |

## Interaktionsprinzip

Die Konsole soll jeden Schritt bestaetigbar und nachvollziehbar machen. Ein Discovery-Befehl liefert zunaechst Marktkennzahlen, Token-IDs und Spread-Daten. Erst danach darf eine Simulations- oder Live-Aktion moeglich sein. Fuer Live-Befehle muss die Konsole vor der Ausfuehrung den aktuellen Modus, das Risikolimit und die verwendete Zieladresse anzeigen.

## Autopilot-Modus

Der Autopilot arbeitet in einem festen Zyklus. In jedem Zyklus werden Kandidaten geladen, mit der Strategie bewertet, durch die Risikoschicht geprueft und anschliessend entweder simuliert oder real ausgefuehrt. Jeder Zyklus endet mit einem kompakten Audit-Eintrag. Wenn der Kill-Switch gesetzt ist, darf der Autopilot nur noch scannen und loggen.

## Sichere Defaults

Starte immer mit `paper` als Standardmodus. Wenn die Live-Konfiguration unvollstaendig ist, muessen Live-Kommandos blockiert werden. Die Konsole darf nie versuchen, fehlende Secrets zu erraten oder implizit andere Modi zu aktivieren.

## Menschliche Uebersteuerung

Die Konsole soll eine Dateiflag fuer den Kill-Switch unterstuetzen. Dadurch kann ein autonomer Loop auch ohne Prozessinteraktion gestoppt werden, etwa in einem VPS-Setup. Empfohlen ist zusaetzlich ein `status`-Befehl, der Modus, Exponierung, Tages-PnL, offene Positionen und den Zustand des Kill-Switches in einer Tabellenansicht ausgibt.
