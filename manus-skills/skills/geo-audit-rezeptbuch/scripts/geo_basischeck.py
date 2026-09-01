#!/usr/bin/env python3
"""Öffentlicher technischer GEO-Basischeck.

Prüft nur eine Startseite sowie öffentlich erreichbare robots.txt- und Sitemap-Hinweise.
Der Report ist eine reproduzierbare Vorprüfung, kein vollständiger Crawl, Security-Audit
oder Nachweis einer KI-Sichtbarkeit.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

USER_AGENT = "GEO-Rezeptbuch-Basischeck/1.0 (+https://www.fragroger.ai)"
TIMEOUT_SECONDS = 15
MAX_HTML_BYTES = 2_000_000


def normalise_url(value: str) -> str:
    value = value.strip()
    if not value.startswith(("http://", "https://")):
        value = f"https://{value}"
    parsed = urlparse(value)
    if not parsed.netloc:
        raise ValueError("Bitte eine gültige Domain oder URL angeben.")
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path or '/'}"


def fetch(session: requests.Session, url: str, timeout: int) -> Dict[str, Any]:
    try:
        response = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
        content = response.raw.read(MAX_HTML_BYTES + 1, decode_content=True)
        truncated = len(content) > MAX_HTML_BYTES
        if truncated:
            content = content[:MAX_HTML_BYTES]
        return {
            "requested_url": url,
            "final_url": response.url,
            "status_code": response.status_code,
            "content_type": response.headers.get("content-type", ""),
            "headers": {
                "x_robots_tag": response.headers.get("x-robots-tag", ""),
                "content_language": response.headers.get("content-language", ""),
            },
            "body": content.decode(response.encoding or "utf-8", errors="replace"),
            "truncated": truncated,
            "error": None,
        }
    except requests.RequestException as exc:
        return {
            "requested_url": url,
            "final_url": None,
            "status_code": None,
            "content_type": "",
            "headers": {},
            "body": "",
            "truncated": False,
            "error": str(exc),
        }


def content_value(node: Any) -> Optional[str]:
    if not node:
        return None
    value = node.get("content") or node.get("href")
    return value.strip() if isinstance(value, str) and value.strip() else None


def parse_json_ld(soup: BeautifulSoup) -> Dict[str, Any]:
    types: List[str] = []
    invalid_scripts = 0
    for script in soup.find_all("script", attrs={"type": re.compile(r"application/ld\+json", re.I)}):
        raw = script.string or script.get_text(strip=True)
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            invalid_scripts += 1
            continue
        items = parsed if isinstance(parsed, list) else [parsed]
        for item in items:
            if not isinstance(item, dict):
                continue
            graph = item.get("@graph", [item])
            if not isinstance(graph, list):
                graph = [graph]
            for entity in graph:
                if not isinstance(entity, dict):
                    continue
                entity_type = entity.get("@type")
                if isinstance(entity_type, list):
                    types.extend(str(entry) for entry in entity_type)
                elif entity_type:
                    types.append(str(entity_type))
    return {"types": sorted(set(types)), "invalid_jsonld_scripts": invalid_scripts}


def parse_html(page: Dict[str, Any]) -> Dict[str, Any]:
    if page["error"] or "html" not in page["content_type"].lower():
        return {"parsed": False, "reason": page["error"] or "Kein HTML-Inhalt"}

    soup = BeautifulSoup(page["body"], "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    description = content_value(soup.find("meta", attrs={"name": re.compile("^description$", re.I)}))
    robots = content_value(soup.find("meta", attrs={"name": re.compile("^robots$", re.I)}))
    canonical = content_value(soup.find("link", attrs={"rel": lambda value: value and "canonical" in value}))
    language = soup.html.get("lang") if soup.html else None
    h1s = [tag.get_text(" ", strip=True) for tag in soup.find_all("h1") if tag.get_text(strip=True)]
    h2_count = len([tag for tag in soup.find_all("h2") if tag.get_text(strip=True)])
    question_headings = [
        tag.get_text(" ", strip=True)
        for tag in soup.find_all(["h2", "h3"])
        if "?" in tag.get_text(" ", strip=True)
    ]
    links = [link.get("href") for link in soup.find_all("a", href=True)]
    parsed_domain = urlparse(page["final_url"]).netloc if page["final_url"] else ""
    internal_links = sum(
        1
        for link in links
        if link.startswith("/") or (urlparse(urljoin(page["final_url"], link)).netloc == parsed_domain)
    )
    return {
        "parsed": True,
        "html_lang": language,
        "title": title,
        "meta_description": description,
        "meta_robots": robots,
        "canonical": urljoin(page["final_url"], canonical) if canonical else None,
        "h1s": h1s,
        "h2_count": h2_count,
        "question_headings": question_headings,
        "internal_link_count_on_page": internal_links,
        "json_ld": parse_json_ld(soup),
    }


def parse_robots(text: str) -> Dict[str, Any]:
    sitemap_urls: List[str] = []
    rules: Dict[str, List[Dict[str, str]]] = {}
    current_agents: List[str] = []
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        lower_key = key.lower()
        if lower_key == "sitemap":
            sitemap_urls.append(value)
        elif lower_key == "user-agent":
            current_agents = [value]
            rules.setdefault(value.lower(), [])
        elif lower_key in {"allow", "disallow"} and current_agents:
            for agent in current_agents:
                rules.setdefault(agent.lower(), []).append({"directive": lower_key, "path": value})
    monitored_agents = ["googlebot", "bingbot", "oai-searchbot", "gptbot", "chatgpt-user"]
    return {
        "sitemap_urls": sitemap_urls,
        "declared_rules": {agent: rules.get(agent, []) for agent in monitored_agents},
        "wildcard_rules": rules.get("*", []),
        "note": "Die Regeln werden ausgewiesen, aber nicht als vollständige robots.txt-Entscheidung interpretiert. Prüfe kritische Regeln in den jeweiligen Webmaster-Tools.",
    }


def parse_sitemap(page: Dict[str, Any]) -> Dict[str, Any]:
    if page["error"]:
        return {"reachable": False, "error": page["error"]}
    text = page["body"]
    url_count = len(re.findall(r"<loc>\s*[^<]+\s*</loc>", text, flags=re.I))
    lastmod_count = len(re.findall(r"<lastmod>\s*[^<]+\s*</lastmod>", text, flags=re.I))
    return {
        "reachable": page["status_code"] == 200,
        "status_code": page["status_code"],
        "final_url": page["final_url"],
        "estimated_loc_entries": url_count,
        "estimated_lastmod_entries": lastmod_count,
        "truncated": page["truncated"],
    }


def finding(priority: str, category: str, message: str, evidence: str) -> Dict[str, str]:
    return {"priority": priority, "category": category, "message": message, "evidence": evidence}


def build_findings(page: Dict[str, Any], html: Dict[str, Any], robots: Dict[str, Any], sitemap: Dict[str, Any]) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []
    if page["status_code"] != 200:
        findings.append(finding("P0", "Abrufbarkeit", "Startseite liefert keinen HTTP-200-Status.", str(page["status_code"])))
    if page["final_url"] and not page["final_url"].startswith("https://"):
        findings.append(finding("P0", "HTTPS", "Endgültige Startseiten-URL verwendet kein HTTPS.", page["final_url"]))
    if html.get("parsed"):
        robots_meta = (html.get("meta_robots") or "").lower()
        if "noindex" in robots_meta:
            findings.append(finding("P0", "Indexierung", "Startseite enthält `noindex`.", html.get("meta_robots") or ""))
        if not html.get("canonical"):
            findings.append(finding("P1", "Canonical", "Kein Canonical-Link auf der Startseite erkannt.", page["final_url"] or ""))
        if not html.get("html_lang"):
            findings.append(finding("P1", "Sprache", "Kein `lang`-Attribut im HTML erkannt.", "<html>"))
        if not html.get("h1s"):
            findings.append(finding("P1", "Inhaltsstruktur", "Keine H1 auf der Startseite erkannt.", page["final_url"] or ""))
        if not html.get("title"):
            findings.append(finding("P1", "Metadaten", "Kein Title-Element erkannt.", page["final_url"] or ""))
        if not html.get("meta_description"):
            findings.append(finding("P2", "Metadaten", "Keine Meta Description erkannt.", page["final_url"] or ""))
        if not html.get("json_ld", {}).get("types"):
            findings.append(finding("P2", "Strukturierte Daten", "Kein parsebares JSON-LD auf der Startseite erkannt.", page["final_url"] or ""))
    if not robots.get("sitemap_urls") and not sitemap.get("reachable"):
        findings.append(finding("P1", "Sitemap", "Weder robots.txt-Sitemap-Hinweis noch erreichbare Standard-Sitemap erkannt.", "/robots.txt und /sitemap.xml"))
    if sitemap.get("reachable") and sitemap.get("estimated_loc_entries", 0) == 0:
        findings.append(finding("P2", "Sitemap", "Sitemap ist erreichbar, enthält aber keine erkannten `<loc>`-Einträge.", sitemap.get("final_url", "")))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Öffentlichen technischen GEO-Basischeck ausführen.")
    parser.add_argument("url", help="Domain oder Startseiten-URL, zum Beispiel https://beispiel.ch")
    parser.add_argument("--output", required=True, help="Pfad für die JSON-Ausgabe")
    parser.add_argument("--timeout", type=int, default=TIMEOUT_SECONDS, help="HTTP-Timeout in Sekunden")
    args = parser.parse_args()

    try:
        root_url = normalise_url(args.url)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    homepage = fetch(session, root_url, args.timeout)
    final_base = homepage["final_url"] or root_url
    parsed = urlparse(final_base)
    origin = f"{parsed.scheme}://{parsed.netloc}"

    robots_page = fetch(session, urljoin(origin, "/robots.txt"), args.timeout)
    robots = parse_robots(robots_page["body"]) if not robots_page["error"] else {"sitemap_urls": [], "declared_rules": {}, "wildcard_rules": [], "note": robots_page["error"]}

    sitemap_candidates = robots.get("sitemap_urls", []) or [urljoin(origin, "/sitemap.xml")]
    sitemap_page = fetch(session, sitemap_candidates[0], args.timeout)
    sitemap = parse_sitemap(sitemap_page)

    html = parse_html(homepage)
    report = {
        "report_type": "geo_basischeck",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Öffentliche Startseite, robots.txt und eine Sitemap. Keine vollständige Crawl-, Security-, Rankings- oder KI-Sichtbarkeitsanalyse.",
        "homepage": {key: value for key, value in homepage.items() if key != "body"},
        "html_signals": html,
        "robots_txt": {
            "url": robots_page["requested_url"],
            "status_code": robots_page["status_code"],
            "error": robots_page["error"],
            **robots,
        },
        "sitemap": sitemap,
        "findings": build_findings(homepage, html, robots, sitemap),
        "next_steps": [
            "Search Console: Property, Sitemap, URL-Prüfung und Query-Baseline prüfen.",
            "Bing Webmaster Tools: Property, Sitemapstatus, letzter Abruf und IndexNow-Entscheid prüfen.",
            "Kernleistungs-, Case- und Kontaktseiten separat bewerten.",
            "Crawler-Policy und strukturierte Daten fachlich prüfen, bevor Regeln oder Markup geändert werden.",
        ],
    }

    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print(f"Basischeck abgeschlossen: {args.output}")
    print(f"Befunde: {len(report['findings'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
