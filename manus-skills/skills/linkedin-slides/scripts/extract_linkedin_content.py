#!/usr/bin/env python3
"""
extract_linkedin_content.py
Extracts and structures content for a 10-slide LinkedIn presentation.
Outputs slides.json with the full slide structure.

Usage:
    python extract_linkedin_content.py --input content.txt --output slides.json --topic "AI Leadership"
"""

import argparse
import json
import os
import sys
from openai import OpenAI

SYSTEM_PROMPT = """You are a LinkedIn content strategist for Roger Basler de Roca — MSc Digital Business,
PhD Candidate, Top-100-Speaker, Digital Entrepreneur and AI thought leader in the DACH region.

Your task: Transform any input content into a structured 10-slide LinkedIn presentation
that follows the Hook-Problem-Solution-Facts-CTA narrative arc.

SLIDE STRUCTURE (exactly 10 slides):
1. TITLE    - Attention-grabbing title that sparks curiosity. Bold claim or provocative question.
              Fields: title (max 8 words), subtitle (max 12 words), badge_text (2-3 words, e.g. "AI REALITY CHECK")
2. HOOK     - One counter-intuitive or surprising statement that stops the scroll.
              Fields: headline (max 10 words), subline (max 15 words), hook_label (e.g. "THE UNCOMFORTABLE TRUTH")
3. PROBLEM  - The real pain point the audience faces. Make them feel seen.
              Fields: headline, body (2 sentences max), pain_points (list of 3 short items)
4. INSIGHT  - Surprising root cause or reframe. "What nobody tells you..."
              Fields: headline, body (2 sentences max), insight_label (e.g. "THE REAL ISSUE")
5. SOLUTION - The core solution or approach. Clear and actionable.
              Fields: headline, body (2 sentences max), steps (list of 3 short action items)
6. FACT_1   - Compelling statistic or data point #1 with context.
              Fields: stat (number + unit), stat_label, context (1 sentence), source
7. FACT_2   - Compelling statistic or data point #2 with context.
              Fields: stat (number + unit), stat_label, context (1 sentence), source
8. EXAMPLE  - Concrete real-world example or case study.
              Fields: headline, body (2 sentences max), example_label (e.g. "REAL WORLD"), result (1 sentence)
9. SUMMARY  - 3 key takeaways. Crisp and memorable.
              Fields: headline (e.g. "THE 3 THINGS THAT MATTER"), takeaways (list of exactly 3 items)
10. CTA     - Call to action. Always Roger's brand. FIXED STRUCTURE.
              Fields: cta_headline (e.g. "WANT MORE?"), cta_body (1 sentence), cta_items (list of 3 action items)

RULES:
- All text UPPERCASE-ready (short, punchy, no filler words)
- Schweizer Rechtschreibung (kein ß, immer ä ö ü)
- No hashtags, no emoji
- Facts must be real, credible, and cited with source
- CTA slide always references Roger Basler de Roca and ki-power.me
- Language: match the input language (German or English)

Return ONLY valid JSON with this exact structure:
{
  "topic": "...",
  "language": "de" or "en",
  "slides": [
    {"slide": 1, "type": "TITLE", ...fields},
    {"slide": 2, "type": "HOOK", ...fields},
    ...
  ]
}"""


def extract_content(input_text: str, topic: str = "") -> dict:
    client = OpenAI()
    user_msg = f"TOPIC: {topic}\n\nCONTENT:\n{input_text}" if topic else f"CONTENT:\n{input_text}"
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )
    return json.loads(response.choices[0].message.content)


def main():
    parser = argparse.ArgumentParser(description="Extract LinkedIn slide content from any input")
    parser.add_argument("--input", required=True, help="Input file path (.txt, .md) or '-' for stdin")
    parser.add_argument("--output", default="slides.json", help="Output JSON file path")
    parser.add_argument("--topic", default="", help="Optional topic override")
    args = parser.parse_args()

    if args.input == "-":
        input_text = sys.stdin.read()
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            input_text = f.read()

    print(f"Extracting slide content for: {args.topic or 'auto-detected topic'}...")
    result = extract_content(input_text, args.topic)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(result.get('slides', []))} slides to {args.output}")
    print(f"Language: {result.get('language', 'unknown')}")
    print(f"Topic: {result.get('topic', 'unknown')}")
    return result


if __name__ == "__main__":
    main()
