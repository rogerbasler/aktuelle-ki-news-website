---
name: roger-book-german
description: >
  Workflow for writing, revising, and formatting professional German-language
  non-fiction books by Roger Basler de Roca in BoD (Books on Demand) format.
  Use when writing or rewriting German book chapters, formatting a manuscript
  for BoD 12x19cm, or ensuring consistent author voice and factual accuracy.
---

# Roger Basler de Roca – German Book Workflow

## Author Profile

Roger Basler de Roca is a **Swiss entrepreneur and digital expert**, not a psychologist or academic. Always present him accurately:

- 25+ years of experience in business and digital transformation
- Started career at IBM; lived and worked in China, USA, Spain, Canada (12+ years abroad)
- Speaks 6 languages; founder of multiple companies; restaurant owner (Barcelona)
- Keynote speaker with 1,000+ talks worldwide
- Creator of #fragRoger community (1M+ members)
- Uses ChatGPT and AI tools since 5+ years (before public release)
- Core quote: "Denken ist wie ChatGPT, nur krasser."
- Core quote: "Wer versteht, kann bewegen. Wer nicht versteht, bleibt stehen."
- Website: www.rogerbasler.ch

**Never invent quotes, credentials, or biographical details.** Only use verified facts.

## Writing Rules

| Rule | Detail |
|---|---|
| Language | German (Swiss standard) |
| Reader address | **Du-Form** throughout (never "Sie") |
| ss vs ß | Replace all "ß" with **ss** |
| Quotes | Use „ " (German quotation marks) |
| Tone | Entrepreneurial, direct, practical, occasional humour |
| Paragraph length | Min. 4–6 paragraphs per sub-chapter (~1,000 characters) |
| Citations | APA 7th edition; all sources must be verifiable |
| No address | Never include Roger's street address or phone number |
| No social media | Do not frame the book around social media topics |

## Content Structure Per Chapter

1. Concrete opening scenario or anecdote from Roger's real life (IBM, abroad, keynotes, restaurant, #fragRoger)
2. Core concept explained clearly
3. Research backing (verified, international sources preferred)
4. Practical exercises or "Thought Spark" sections
5. Personal reflection from Roger's perspective

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

**Front matter:** Half-title → Blank → Full title → Imprint → TOC → Content

**Formatting script:** `scripts/format_bod.py`
- Requires: `sudo pip3 install python-docx`
- Base template: `BoD-Microsoft-Word-Vorlage-12x19cm.docx`
- Adapt title/author/imprint variables at top of script

## Revision Checklist

- [ ] Author = entrepreneur (not psychologist)
- [ ] Du-Form throughout
- [ ] No "ß" — use "ss"
- [ ] No street address or phone number
- [ ] No social media framing
- [ ] All quotes verified
- [ ] ChatGPT usage = "5+ years"
- [ ] APA 7th edition citations
- [ ] BoD formatting applied
- [ ] Uploaded to Google Drive (DENK - FRAG - KLICK > DE)

## Sources

See `references/sources_template.md` for verified research sources on AI, cognitive offloading, and digital transformation.
