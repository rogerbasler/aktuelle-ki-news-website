---
name: roger-book-english
description: >
  Workflow for writing, translating, and formatting professional English-language
  non-fiction books by Roger Basler de Roca in BoD (Books on Demand) format.
  Use when writing or translating Roger's books into English, formatting an
  English manuscript for BoD 12x19cm, or ensuring internationally verified sources.
---

# Roger Basler de Roca – English Book Workflow

## Author Profile

Roger Basler de Roca is a **Swiss entrepreneur and digital expert**. Always present him accurately:

- 25+ years in business and digital transformation
- Started at IBM; lived/worked in China, USA, Spain, Canada (12+ years abroad)
- Speaks 6 languages; founded multiple companies; former restaurant owner (Barcelona)
- 1,000+ keynotes worldwide; creator of #fragRoger community (1M+ members)
- Has used ChatGPT and AI tools for 5+ years (before public release)
- Core quote: "Thinking is like ChatGPT, only more badass."
- Core quote: "Who understands, can move. Who does not understand, stands still."
- Website: www.rogerbasler.ch

**Never invent quotes, credentials, or biographical details.** Only use verified facts.

## Writing Rules

| Rule | Detail |
|---|---|
| Language | English (international, not US-only) |
| Reader address | **"you"** throughout (direct, conversational) |
| Tone | Entrepreneurial, direct, practical, occasional humour |
| Style | Business self-help; accessible, not academic |
| Paragraph length | Min. 4–6 paragraphs per sub-chapter |
| Citations | APA 7th edition; international sources only |
| No address | Never include Roger's street address or phone number |
| No social media | Do not frame the book around social media topics |

## Translation Guidelines (German to English)

When translating from German:
- Translate idiomatically, not literally — the text must flow naturally in English
- "Du-Form" becomes natural "you" address
- Swiss-German cultural references: adapt for international readers where needed
- Keep Roger's personal anecdotes intact (IBM, abroad, keynotes, #fragRoger, restaurant)
- Replace German-only sources with international equivalents

## Content Structure Per Chapter

1. Concrete opening scenario or anecdote from Roger's real life
2. Core concept explained clearly for an international audience
3. Research backing from internationally recognised sources (MIT, Stanford, Nature, etc.)
4. Practical exercises or "Thought Spark" sections
5. Personal reflection from Roger's perspective

## Key International Sources

See `references/international_sources.md` for the full curated list. Key references:

- Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading. Societies, 15(1), 6.
- Kosmyna, N. et al. (2025). Your brain on ChatGPT. arXiv:2506.08872
- Sparrow, B. et al. (2011). Google effects on memory. Science, 333(6043), 776–778.
- Stanford SCALE Lab (2025). ChatGPT produces more "lazy" thinkers.
- MIT Media Lab / Time (2025). ChatGPT's impact on our brains.

## BoD Format (12x19 cm)

**Page setup:** 12x19 cm | Margins: top 1.2 cm, bottom 2.0 cm, left 1.7 cm, right 1.5 cm | Header/footer: 1.25 cm

**Typography:**
- Font: Palatino Linotype
- Body: 9 pt, line spacing 12 pt exact, first-line indent 0.4 cm
- Chapter headings (##): 13 pt bold, page break before, 54 pt space above
- Sub-headings (###): 11 pt bold, 14 pt space above
- Sub-sub-headings (####): 9.5 pt bold italic, 10 pt space above
- Lists: dash (–) prefix, 0.4 cm left indent, hanging
- Footer: page number centred, 8 pt

**Front matter:** Half-title → Blank → Full title → Copyright → TOC → Content → References

**Formatting script:** `scripts/format_bod_english.py`
- Requires: `sudo pip3 install python-docx`
- Base template: `BoD-Microsoft-Word-Vorlage-12x19cm.docx`
- Adapt title/author/imprint variables at top of script

## Revision Checklist

- [ ] Author = entrepreneur (not psychologist)
- [ ] "you" address throughout
- [ ] No street address or phone number
- [ ] No social media framing
- [ ] All quotes verified in English
- [ ] ChatGPT usage = "5+ years"
- [ ] International sources only (APA 7th edition)
- [ ] BoD formatting applied (Palatino Linotype, 9pt, 12x19cm)
- [ ] References section at end of book
- [ ] Uploaded to Google Drive
