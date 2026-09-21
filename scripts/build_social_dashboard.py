#!/usr/bin/env python3
"""Build the static social-listening dashboard from structured JSON data."""

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "social-listening" / "current.json"
ARCHIVE_FILE = ROOT / "archiv" / "data" / "archive-index.json"
OUTPUT_FILE = ROOT / "index.html"


def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def first(obj: dict[str, Any], *keys: str, default: Any = "") -> Any:
    for key in keys:
        value = obj.get(key)
        if value not in (None, "", [], {}):
            return value
    return default


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def slug(value: Any) -> str:
    text = str(value or "").strip().lower()
    replacements = {"ä": "ae", "ö": "oe", "ü": "ue", " ": "-", "/": "-", "_": "-"}
    for old, new in replacements.items():
        text = text.replace(old, new)
    return "".join(ch for ch in text if ch.isalnum() or ch == "-").strip("-") or "sonstige"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_sources(data: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    sources = as_list(data.get("sources"))
    normalized: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(sources, start=1):
        if not isinstance(raw, dict):
            continue
        source = dict(raw)
        source_id = str(first(source, "id", "source_id", default=f"Q{index:02d}"))
        source["id"] = source_id
        normalized.append(source)
        by_id[source_id] = source
    return normalized, by_id


def source_links(ids: Any, by_id: dict[str, dict[str, Any]]) -> str:
    links: list[str] = []
    for source_id in as_list(ids):
        source = by_id.get(str(source_id), {})
        url = first(source, "url", "link")
        label = first(source, "publisher", "title", default=source_id)
        if url:
            links.append(f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)}</a>')
        else:
            links.append(esc(source_id))
    return " · ".join(links) if links else "Keine direkte Quelle zugeordnet"


def metric_card(label: str, value: Any, detail: str, tone: str = "mint") -> str:
    return f"""
      <article class="metric-card metric-card--{esc(tone)}">
        <p class="metric-label">{esc(label)}</p>
        <strong>{esc(value)}</strong>
        <p>{esc(detail)}</p>
      </article>"""


def signal_card(signal: dict[str, Any], index: int, by_id: dict[str, dict[str, Any]]) -> str:
    category = str(first(signal, "category", "field", "kategorie", default="Themenmarkt"))
    evidence = str(first(signal, "evidence_grade", "evidence", "evidenzgrad", default="Interpretation"))
    intensity = str(first(signal, "intensity", "intensitaet", default="mittel"))
    title = first(signal, "title", "signal", "headline", default=f"Signal {index}")
    observation = first(signal, "observation", "evidence", "description", "beobachtung")
    implication = first(signal, "business_implication", "business_consequence", "implication", "geschaeftliche_implikation")
    sentiment = first(signal, "sentiment", default="neutral")
    priority = first(signal, "priority", "prioritaet", default="P2")
    sources = first(signal, "source_ids", "sources", "quellen", default=[])
    return f"""
      <article class="signal-card" data-category="{esc(slug(category))}" data-evidence="{esc(slug(evidence))}">
        <div class="signal-card__topline">
          <span class="eyebrow">#{index:02d} · {esc(category)}</span>
          <div class="badge-row">
            <span class="badge badge--evidence">{esc(evidence)}</span>
            <span class="badge badge--{esc(slug(intensity))}">{esc(intensity)}</span>
            <span class="badge badge--priority">{esc(priority)}</span>
          </div>
        </div>
        <h3>{esc(title)}</h3>
        <p class="signal-observation">{esc(observation)}</p>
        <div class="implication">
          <span>Konsequenz</span>
          <p>{esc(implication)}</p>
        </div>
        <footer>
          <span>Stimmung: {esc(sentiment)}</span>
          <span class="source-links">{source_links(sources, by_id)}</span>
        </footer>
      </article>"""


def render_actions(actions: list[Any]) -> str:
    cards: list[str] = []
    for index, raw in enumerate(actions[:3], start=1):
        action = raw if isinstance(raw, dict) else {"action": raw}
        priority = first(action, "priority", "prioritaet", default=f"P{index}")
        title = first(action, "title", "action", "massnahme", default="Massnahme")
        objective = first(action, "objective", "ziel")
        rationale = first(action, "rationale", "why_now", "reason", "begruendung")
        timing = first(action, "timing", "when", "deadline", "zeitraum", default=["sofort", "14 Tage", "Monatsende"][min(index - 1, 2)])
        deliverables = as_list(first(action, "deliverables", "umsetzung", default=[]))
        deliverable_html = "".join(f"<li>{esc(item)}</li>" for item in deliverables)
        cards.append(f"""
        <article class="action-card action-card--{index}">
          <div class="action-rank">{esc(priority)}</div>
          <div>
            <p class="eyebrow">{esc(timing)}</p>
            <h3>{esc(title)}</h3>
            <p><strong>{esc(objective)}</strong></p>
            <p>{esc(rationale)}</p>
            <ul>{deliverable_html}</ul>
          </div>
        </article>""")
    return "\n".join(cards)


def render_competitors(items: list[Any]) -> str:
    rows: list[str] = []
    for raw in items:
        item = raw if isinstance(raw, dict) else {"competitor": raw}
        rows.append(f"""
          <tr>
            <th scope="row">{esc(first(item, 'competitor', 'actor', 'name', 'wettbewerber'))}</th>
            <td>{esc(first(item, 'current_message', 'current_positioning', 'visible_positioning', 'visible_offer', 'message', 'positioning', 'aktuelle_botschaft'))}</td>
            <td>{esc(first(item, 'resonance', 'market_relevance', 'visible_offer', 'resonanz', default='Nicht belastbar quantifiziert'))}</td>
            <td>{esc(first(item, 'gap', 'gap_or_risk', 'boundary', 'luecke'))}</td>
            <td>{esc(first(item, 'differentiation', 'our_differentiation', 'our_position', 'unsere_differenzierung', default='Prüfbare Arbeitsresultate statt allgemeiner KI-Versprechen.'))}</td>
          </tr>""")
    if not rows:
        rows.append('<tr><td colspan="5">Keine belastbaren Wettbewerbsdaten in dieser Ausgabe.</td></tr>')
    return "\n".join(rows)


def render_verbatims(items: list[Any], by_id: dict[str, dict[str, Any]]) -> str:
    cards: list[str] = []
    for raw in items[:6]:
        item = raw if isinstance(raw, dict) else {"quote": raw}
        cards.append(f"""
        <figure class="quote-card">
          <blockquote>«{esc(first(item, 'quote', 'zitat'))}»</blockquote>
          <figcaption>
            <span>{esc(first(item, 'context', 'kontext'))}</span>
            <span>{source_links(first(item, 'source_id', 'source_ids', 'quelle'), by_id)}</span>
          </figcaption>
        </figure>""")
    if not cards:
        cards.append('<p class="empty-state">Keine wortgetreu verifizierbaren Originalstimmen in dieser Ausgabe.</p>')
    return "\n".join(cards)


def render_sources(sources: list[dict[str, Any]]) -> str:
    rows: list[str] = []
    for source in sources:
        score = first(source, "trust_score", "score", default="")
        try:
            score_value = max(0.0, min(20.0, float(score)))
            score_label = f"{score_value:g}/20"
            score_width = score_value * 5
        except (TypeError, ValueError):
            score_label = esc(score)
            score_width = 0
        url = first(source, "url", "link")
        title = first(source, "title", default="Quelle")
        publisher = first(source, "publisher", "source", default="")
        link = f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(title)}</a>' if url else esc(title)
        rows.append(f"""
          <tr>
            <td><strong>{esc(publisher)}</strong><br>{link}</td>
            <td>{esc(first(source, 'date', 'datum'))}</td>
            <td>{esc(first(source, 'type', 'typ'))}</td>
            <td>{esc(first(source, 'currency', default='Geprüft'))}</td>
            <td>{esc(first(source, 'reliability', default='Geprüft'))}</td>
            <td>{esc(first(source, 'authority', default='Geprüft'))}</td>
            <td>{esc(first(source, 'purpose', default='Geprüft'))}</td>
            <td><div class="score"><span style="width:{score_width:.0f}%"></span></div><small>{score_label}</small></td>
          </tr>""")
    return "\n".join(rows)


def render_archive(archive_data: dict[str, Any]) -> str:
    entries = as_list(archive_data.get("eintraege") or archive_data.get("analysen"))
    cards: list[str] = []
    for raw in entries[:12]:
        item = raw if isinstance(raw, dict) else {}
        path = first(item, "file", "path")
        title = first(item, "title", default=f"KW {first(item, 'kw')} / {first(item, 'jahr')}")
        item_type = first(item, "type", default="Wochenanalyse")
        date = first(item, "datum", "date")
        href = "/" + str(path).lstrip("/") if path else "#"
        cards.append(f"""
        <a class="archive-card" href="{esc(href)}">
          <span>{esc(item_type)}</span>
          <strong>{esc(title)}</strong>
          <small>{esc(date)}</small>
        </a>""")
    if not cards:
        cards.append('<p class="empty-state">Das Archiv wird ab der nächsten Ausgabe gefüllt.</p>')
    return "\n".join(cards)


def main() -> None:
    data = load_json(DATA_FILE)
    archive_data = load_json(ARCHIVE_FILE) if ARCHIVE_FILE.exists() else {}
    sources, sources_by_id = normalize_sources(data)
    signals = [item for item in as_list(data.get("top_signals")) if isinstance(item, dict)]
    actions = as_list(data.get("actions"))
    competitors = as_list(data.get("competitor_radar"))
    verbatims = as_list(data.get("verbatims"))
    limitations = [str(item) for item in as_list(data.get("limitations"))]

    fact_count = sum(1 for item in signals if str(first(item, "evidence_grade", "evidence")).lower() == "fakt")
    interpretation_count = sum(1 for item in signals if str(first(item, "evidence_grade", "evidence")).lower() == "interpretation")
    high_count = sum(1 for item in signals if str(first(item, "intensity", "intensitaet")).lower() == "hoch")
    categories = []
    for signal in signals:
        category = str(first(signal, "category", "field", "kategorie", default="Themenmarkt"))
        if category not in categories:
            categories.append(category)

    headline = first(data, "headline", default="KI wird zur Führungsfrage")
    summary = first(data, "executive_summary", "summary")
    generated = first(data, "generated_at", "stand", default="19. September 2026")
    period = first(data, "primary_period", "period", "zeitraum", default="12. bis 19. September 2026")
    methodology = first(data, "methodology", "method", default="Öffentliche Quellen, CRAP-Prüfung, Trennung von Fakt, Interpretation und Hypothese.")
    brand_data = first(data, "brand", default={})
    brand = first(brand_data, "name", default="Roger Basler de Roca") if isinstance(brand_data, dict) else brand_data
    audience_data = first(data, "audience", "zielgruppe", default={})
    audience = first(audience_data, "primary", default="Schweizer und DACH-KMU") if isinstance(audience_data, dict) else audience_data
    methodology_data = first(data, "methodology", "method", default={})
    if isinstance(methodology_data, dict):
        methodology = first(methodology_data, "scope", default="Öffentliche Quellen, CRAP-Prüfung, Trennung von Fakt, Interpretation und Hypothese.")
    else:
        methodology = methodology_data

    category_buttons = ['<button class="filter-chip is-active" data-filter="all">Alle Signale</button>']
    category_buttons.extend(
        f'<button class="filter-chip" data-filter="{esc(slug(category))}">{esc(category)}</button>' for category in categories
    )
    signal_html = "\n".join(signal_card(signal, i, sources_by_id) for i, signal in enumerate(signals, start=1))
    limitation_html = "".join(f"<li>{esc(item)}</li>" for item in limitations)

    document = f"""<!doctype html>
<html lang="de-CH">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#081713">
  <meta name="description" content="Wöchentliches Social-Listening-Dashboard für KI, Unternehmen und Bildung im Schweizer und DACH-Markt.">
  <meta property="og:title" content="Social Listening Intelligence | {esc(generated)}">
  <meta property="og:description" content="{esc(headline)}">
  <meta property="og:type" content="website">
  <title>Social Listening Intelligence | {esc(generated)}</title>
  <link rel="stylesheet" href="/assets/social-listening.css">
  <script src="/assets/social-listening.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#inhalt">Zum Inhalt</a>
  <header class="site-header">
    <div class="shell header-bar">
      <a class="brand" href="/" aria-label="Dashboard Startseite">
        <span class="brand-mark">RB</span>
        <span><strong>Social Listening</strong><small>Decision Intelligence</small></span>
      </a>
      <nav aria-label="Hauptnavigation">
        <a href="#signale">Signale</a>
        <a href="#entscheidungen">Entscheidungen</a>
        <a href="#quellen">Evidenz</a>
        <a href="#archiv">Archiv</a>
      </nav>
    </div>
  </header>

  <main id="inhalt">
    <section class="hero shell">
      <div class="hero-copy">
        <p class="kicker">Wochenradar · {esc(period)}</p>
        <h1>{esc(headline)}</h1>
        <p class="hero-summary">{esc(summary)}</p>
        <div class="hero-meta">
          <span>Stand {esc(generated)}</span>
          <span>{esc(brand)}</span>
          <span>{esc(audience)}</span>
        </div>
      </div>
      <aside class="method-card">
        <p class="eyebrow">Methodik</p>
        <p>{esc(methodology)}</p>
        <div class="method-legend">
          <span><i class="dot dot--fact"></i>Fakt</span>
          <span><i class="dot dot--interpretation"></i>Interpretation</span>
          <span><i class="dot dot--hypothesis"></i>Hypothese</span>
        </div>
      </aside>
    </section>

    <section class="metrics shell" aria-label="Kennzahlen">
      {metric_card('Entscheidende Signale', len(signals), 'gefiltert nach Relevanz', 'mint')}
      {metric_card('Direkte Quellen', len(sources), 'mit CRAP-Prüfung', 'blue')}
      {metric_card('Fakten', fact_count, f'{interpretation_count} Interpretationen ergänzt', 'violet')}
      {metric_card('Hohe Intensität', high_count, 'fordert zeitnahe Reaktion', 'coral')}
    </section>

    <section class="section shell" id="signale">
      <div class="section-heading">
        <div>
          <p class="kicker">01 · Signalmatrix</p>
          <h2>Was sich bewegt und warum es zählt</h2>
        </div>
        <p>Relevanz statt Reichweite. Ein Like ist nett. Ein ungelöstes Geschäftsproblem zahlt Rechnungen.</p>
      </div>
      <div class="filters" role="group" aria-label="Signale filtern">
        {''.join(category_buttons)}
        <span class="filter-divider" aria-hidden="true"></span>
        <button class="filter-chip" data-evidence-filter="fakt">Nur Fakten</button>
        <button class="filter-chip" data-evidence-filter="interpretation">Interpretationen</button>
        <button class="filter-chip" data-evidence-filter="hypothese">Hypothesen</button>
      </div>
      <p class="filter-status" aria-live="polite"></p>
      <div class="signal-grid">
        {signal_html or '<p class="empty-state">Keine belastbaren Signale in dieser Ausgabe.</p>'}
      </div>
    </section>

    <section class="decision-band" id="entscheidungen">
      <div class="shell">
        <div class="section-heading section-heading--inverse">
          <div>
            <p class="kicker">02 · Entscheidungen</p>
            <h2>Von Beobachtung zu Handlung</h2>
          </div>
          <p>Drei Prioritäten. Denn eine Liste mit zwölf «Quick Wins» ist bloss Prokrastination im Business-Hemd.</p>
        </div>
        <div class="action-grid">
          {render_actions(actions)}
        </div>
      </div>
    </section>

    <section class="section shell" id="wettbewerb">
      <div class="section-heading">
        <div>
          <p class="kicker">03 · Wettbewerbsradar</p>
          <h2>Positionen, Resonanz und Lücken</h2>
        </div>
        <p>Öffentliche Signale zeigen Positionierung, nicht automatisch Markterfolg. Der entscheidende Unterschied liegt in dieser Nüchternheit.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Wettbewerbsfeld</th><th>Botschaft</th><th>Resonanz</th><th>Lücke</th><th>Unsere Gegenposition</th></tr></thead>
          <tbody>{render_competitors(competitors)}</tbody>
        </table>
      </div>
    </section>

    <section class="section shell" id="stimmen">
      <div class="section-heading">
        <div>
          <p class="kicker">04 · Originalstimmen</p>
          <h2>Was die Zielgruppe tatsächlich sagt</h2>
        </div>
        <p>Nur wortgetreu belegte Aussagen. Keine erfundenen Personas mit erstaunlich passender Meinung.</p>
      </div>
      <div class="quote-grid">{render_verbatims(verbatims, sources_by_id)}</div>
    </section>

    <section class="section shell" id="quellen">
      <div class="section-heading">
        <div>
          <p class="kicker">05 · Quellen-Audit</p>
          <h2>Evidenz vor Behauptung</h2>
        </div>
        <p>Currency, Reliability, Authority und Purpose werden separat betrachtet. Eine Primärquelle ist authentisch, aber nicht automatisch neutral.</p>
      </div>
      <div class="table-wrap table-wrap--sources">
        <table>
          <thead><tr><th>Quelle</th><th>Datum</th><th>Typ</th><th>C</th><th>R</th><th>A</th><th>P</th><th>Score</th></tr></thead>
          <tbody>{render_sources(sources)}</tbody>
        </table>
      </div>
      <details class="limitations">
        <summary>Datenlücken und Grenzen</summary>
        <ul>{limitation_html or '<li>Keine zusätzlichen Einschränkungen dokumentiert.</li>'}</ul>
      </details>
    </section>

    <section class="archive-section" id="archiv">
      <div class="shell">
        <div class="section-heading">
          <div>
            <p class="kicker">06 · Archiv</p>
            <h2>Frühere Datenstände</h2>
          </div>
          <p>Jede Aktualisierung ersetzt die Startseite. Der vorherige Stand bleibt als datierter Snapshot erhalten.</p>
        </div>
        <div class="archive-grid">{render_archive(archive_data)}</div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="shell footer-grid">
      <div><strong>Social Listening Intelligence</strong><p>Öffentliche Signale für bessere Entscheidungen.</p></div>
      <div><span>Kuratiert für</span><a href="https://ki-power.me/" target="_blank" rel="noopener noreferrer">Roger Basler de Roca</a></div>
      <div><span>Aktualisierung</span><strong>Montag, 04:00 Uhr</strong></div>
    </div>
  </footer>
</body>
</html>
"""
    clean_document = "\n".join(line.rstrip() for line in document.splitlines()) + "\n"
    OUTPUT_FILE.write_text(clean_document, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE} with {len(signals)} signals and {len(sources)} sources")


if __name__ == "__main__":
    main()
