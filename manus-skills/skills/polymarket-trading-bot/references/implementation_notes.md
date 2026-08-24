# Implementierungsnotizen fuer Polymarket-Trading-Bots

## Offizielle Grundlagen

Die Polymarket-Quickstart-Dokumentation trennt klar zwischen oeffentlichen Marktdaten und authentifiziertem Trading. Oeffentliche Daten koennen ohne API-Key ueber die Gamma API und CLOB-Read-Endpunkte bezogen werden. Fuer das Posten von Orders werden dagegen L2-Credentials benoetigt, die ueber einen L1-Signaturprozess aus der Wallet abgeleitet werden.[1] [2]

Die Trading-Uebersicht beschreibt das CLOB als hybrid-dezentrales System mit Offchain-Matching und Onchain-Settlement auf Polygon. Daraus folgt fuer Implementierungen, dass Discovery, Signierung und Ausfuehrung logisch getrennt bleiben sollten. Die ordererzeugende Schicht muss lokal vertrauenswuerdig sein, weil die eigentliche Order signiert werden muss.[3]

## Praktische Endpunkte und Werte

| Zweck | Beispiel |
| --- | --- |
| Aktive Maerkte laden | `https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=50` |
| CLOB-Host | `https://clob.polymarket.com` |
| Chain ID | `137` fuer Polygon Mainnet |
| Token-Hinweis | `clobTokenIds[0] = YES`, `clobTokenIds[1] = NO` |

## Implementierungsprinzipien

Baue zuerst eine read-only Datenebene. Sie soll Maerkte laden, Liquiditaet und Bid/Ask aufbereiten und Kandidaten fuer Strategiepruefungen liefern. Danach wird eine Paper-Broker-Schicht erstellt, die Markt- und Simulationsdaten in einen konsistenten Bot-State ueberfuehrt. Erst wenn diese beiden Ebenen stabil sind, wird ein optionaler Live-Broker angebunden.

Verwende in der Strategieausgabe ein hartes JSON-Schema. Das reduziert Fehler in der Ausfuehrung und ermoeglicht eine deterministische Risikopruefung. Wenn ein Modell keine valide strukturierte Antwort liefert, ist die korrekte Reaktion `HOLD` statt einer heuristischen Ersatzentscheidung.

## Credential-Handling

Trenne allgemeine Konfiguration von Geheimnissen. Typische Geheimnisse sind `POLYMARKET_API_KEY`, `POLYMARKET_API_SECRET`, `POLYMARKET_API_PASSPHRASE` sowie bei direkter Signierung `PRIVATE_KEY`. Wenn Polymarket mit Proxy- oder Safe-Wallets verwendet wird, muessen `signature_type` und `funder_address` explizit in der Runtime-Konfiguration gesetzt werden.[2] [3]

## Minimaler Testpfad

Beginne mit einem manuellen Testlauf. Lade aktive Maerkte, waehle einen Markt mit ausreichender Liquiditaet, ermittle YES/NO-Token, lies Orderbuch oder Midprice und pruefe danach eine einzelne Paper-Order. Erst wenn State, Logging und PnL-Fortschreibung korrekt sind, sollte ein wiederholter Agent-Loop aktiviert werden.

## References

[1]: https://docs.polymarket.com/quickstart "Quickstart - Polymarket Documentation"
[2]: https://docs.polymarket.com/api-reference/authentication "Authentication - Polymarket Documentation"
[3]: https://docs.polymarket.com/trading/overview "Overview - Polymarket Documentation"
