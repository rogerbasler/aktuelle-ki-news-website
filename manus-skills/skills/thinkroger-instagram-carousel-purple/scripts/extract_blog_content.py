#!/usr/bin/env python3
"""
extract_blog_content.py
Extracts structured carousel content from a source text through an OpenAI-compatible API.
Output: JSON with 10 slides for the #ThinkRoger International Editorial Engine.

Usage:
    python extract_blog_content.py --input blog.txt --output slides.json
    python extract_blog_content.py --url https://example.com/blog-post --output slides.json
"""

import argparse
import json
import sys

try:
    from openai import OpenAI
except ImportError:
    print("openai package not found. Install with: sudo pip3 install openai")
    sys.exit(1)

SYSTEM_PROMPT = """You are an international editorial strategist for the #ThinkRoger brand.
Your task: Transform a blog article, text, or research into a fact-based, decision-relevant 10-slide Instagram Carousel in International English. The style is dark cinematic editorial.

NON-NEGOTIABLE:
- Generate exactly 10 slides.
- Slide 1 is a THESIS and MUST have a strong visual motif.
- Write in clear, concrete International English.
- Focus on evidence, context, systems thinking, and decision relevance.
- Do not invent facts, numbers, or quotes.
- No explanations outside the JSON structure.

OUTPUT FORMAT (JSON):
{
  "topic": "Short topic title",
  "slides": [
    {
      "slide_number": 1,
      "type": "THESIS",
      "headline": "A sharp, defensible claim or paradox. 5-10 words.",
      "body": null,
      "visual_note": "Mandatory strong visual motif."
    },
    {
      "slide_number": 2,
      "type": "WHY NOW",
      "headline": "The event, data point, shift, or tension that makes this timely.",
      "body": "1 short line."
    },
    {
      "slide_number": 3,
      "type": "EVIDENCE",
      "headline": "One concrete fact, number, study result, or documented example.",
      "body": "1 short line."
    },
    {
      "slide_number": 4,
      "type": "MECHANISM",
      "headline": "Explain how the system, incentive, or technology produces the outcome.",
      "body": "1 short line."
    },
    {
      "slide_number": 5,
      "type": "HIDDEN ASSUMPTION",
      "headline": "Surface what most people miss (trade-off, second-order effect).",
      "body": "1 short line."
    },
    {
      "slide_number": 6,
      "type": "COUNTERPOINT",
      "headline": "The strongest credible alternative explanation, limitation, or benefit.",
      "body": "1 short line."
    },
    {
      "slide_number": 7,
      "type": "SYSTEM VIEW",
      "headline": "Connect actors, incentives, dependencies, power, or feedback loops.",
      "body": "1 short line."
    },
    {
      "slide_number": 8,
      "type": "THINKING SHIFT",
      "headline": "The refined conclusion after weighing evidence and counterpoint.",
      "body": "1 strong insight line."
    },
    {
      "slide_number": 9,
      "type": "FRAMEWORK",
      "headline": "Three questions, tests, or actions that transfer beyond this single case.",
      "points": ["Question/Action 1", "Question/Action 2", "Question/Action 3"]
    },
    {
      "slide_number": 10,
      "type": "THINK AGAIN",
      "headline": "Invite reflection or application.",
      "body": "End with CTA and #ThinkRoger."
    }
  ],
  "caption": "Complete English caption with thesis, context, implication, sources, and exactly one hashtag: #ThinkRoger."
}

CAROUSEL STRUCTURE:
1: THESIS - A sharp, defensible claim or paradox.
2: WHY NOW - The event, data point, shift, or tension that makes this timely.
3: EVIDENCE - One concrete fact, number, study result, or documented example.
4: MECHANISM - Explain how the system, incentive, or technology produces the outcome.
5: HIDDEN ASSUMPTION - Surface what most people miss (trade-off, second-order effect).
6: COUNTERPOINT - The strongest credible alternative explanation, limitation, or benefit.
7: SYSTEM VIEW - Connect actors, incentives, dependencies, power, or feedback loops.
8: THINKING SHIFT - The refined conclusion after weighing evidence and counterpoint.
9: FRAMEWORK - Three questions, tests, or actions that transfer beyond this single case.
10: THINK AGAIN - Invite reflection or application. End with CTA and #ThinkRoger.

LANGUAGE & TONE:
- International English.
- Fact-based, analytical, precise, lightly provocative.
- Avoid hype words.
- Max 1-2 lines per slide (except Slide 9).
- Caption: Thesis, context, implication, sources (if any), #ThinkRoger.
"""

def extract_from_text(blog_text: str) -> dict:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"SOURCE MATERIAL:\n\n{blog_text}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )
    return json.loads(response.choices[0].message.content)

def extract_from_url(url: str) -> dict:
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("requests/beautifulsoup4 not found. Install with: sudo pip3 install requests beautifulsoup4")
        sys.exit(1)

    resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    article = soup.find("article") or soup.find("main") or soup.find("body")
    text = article.get_text(separator="\n", strip=True) if article else soup.get_text(separator="\n", strip=True)

    text = text[:8000]
    return extract_from_text(text)

def main():
    parser = argparse.ArgumentParser(description="Extract a #ThinkRoger carousel structure from source material")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="Path to the source text file")
    group.add_argument("--url", help="URL of the source article")
    parser.add_argument("--output", required=True, help="Output JSON file")
    args = parser.parse_args()

    print("Extracting #ThinkRoger carousel content...")

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            blog_text = f.read()
        result = extract_from_text(blog_text)
    else:
        result = extract_from_url(args.url)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Done. Slides saved to: {args.output}")
    print(f"Topic: {result.get('topic', 'N/A')}")
    print(f"Slide count: {len(result.get('slides', []))}")

if __name__ == "__main__":
    main()
