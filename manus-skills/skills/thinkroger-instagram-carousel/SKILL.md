---
name: thinkroger-instagram-carousel
description: >
  Converts articles, texts, notes, or URLs into fact-based, decision-relevant 10-slide Instagram carousels in English for an international audience under the #ThinkRoger brand.
  Use this skill whenever the user says: "#ThinkRoger", "ThinkRoger carousel", "ThinkRoger English post", "create an international ThinkRoger carousel", "fact-based English carousel", or "/thinkroger-skill".
  Output: 10 slide images in 4:5 format (dark cinematic editorial style), an English caption, source notes, and mandatory review before optional Instagram posting.
---

# #ThinkRoger Instagram Carousel - International Editorial Engine

## Purpose and Positioning

This skill creates English-language, international Instagram carousels for the **#ThinkRoger** brand. It does not merely repurpose content; it transforms source material into a fact-checked, decision-relevant argument about AI, algorithms, digital power, business models, leadership, and human agency.

The tone is informed, precise, independent, and lightly provocative. It challenges convenient assumptions without becoming cynical, partisan, alarmist, or motivational. The focus is on **evidence, context, systems thinking, and decision relevance**.

## Standard Workflow

1. **Input ingestion:** Accept text, files, or URLs. Extract facts, context, and claims.
2. **Evidence check:** Separate verified facts from reported claims, interpretations, and forecasts. Do not invent facts, numbers, or quotes.
3. **Structure generation:** Build a 10-slide editorial arc (Thesis, Why Now, Evidence, Mechanism, Hidden Assumption, Counterpoint, System View, Thinking Shift, Decision Framework, Think Again).
4. **Image generation:** Create 10 slide images in a 4:5 ratio (1080×1350px) using the dark cinematic editorial design system. Slide 1, 2, 3, and 9 MUST have strong visual motifs.
5. **Caption writing:** Write an English caption with thesis, context, implication, and exactly one hashtag (`#ThinkRoger`).
6. **Review before posting:** Present the final slides, caption, and source notes to the user. Wait for an explicit **GO**.
7. **Optional posting:** Upload images and post via Instagram MCP only after explicit approval.

## Output Standards

| Element | Requirement |
|---|---|
| Slides | Exactly 10 slides |
| Format | Instagram 4:5 ratio (1080×1350px) |
| Language | International English (no regional idioms) |
| Tone | Fact-based, analytical, precise, lightly provocative |
| Visual Style | Dark cinematic editorial (black, white, electric blue) |
| Quality Gate | Review required before posting |
| Hashtag | Only `#ThinkRoger` in the caption |

## The 10-Slide Editorial Architecture

| Slide | Type | Function and Content |
|---|---|---|
| 1 | THESIS | A sharp, defensible claim or paradox. No empty questions. |
| 2 | WHY NOW | The event, data point, shift, or tension that makes this timely. |
| 3 | EVIDENCE | One concrete fact, number, study result, or documented example. |
| 4 | MECHANISM | Explain how the system, incentive, or technology produces the outcome. |
| 5 | HIDDEN ASSUMPTION | Surface what most people miss (trade-off, second-order effect). |
| 6 | COUNTERPOINT | The strongest credible alternative explanation, limitation, or benefit. |
| 7 | SYSTEM VIEW | Connect actors, incentives, dependencies, power, or feedback loops. |
| 8 | THINKING SHIFT | The refined conclusion after weighing evidence and counterpoint. |
| 9 | FRAMEWORK | Three questions, tests, or actions that transfer beyond this single case. |
| 10 | THINK AGAIN | Invite reflection or application. End with CTA and `#ThinkRoger`. |

## Topic and Thinking Selection

Before drafting, read `references/editorial-framework.md`. Select one primary topic pillar and at least two thinking models. Record them in planning notes so that the carousel explains a system rather than merely decorating an opinion.

Use this skill especially for AI and human agency, algorithmic power, digital business models, leadership and governance, AI literacy, work design, technology and society, digital sovereignty, hype versus evidence, and cross-regional digital developments.

## Writing Guidelines (International English)

- Write in clear, concrete International English.
- Use active verbs and sentence case for body text.
- Avoid hype words ("game-changer", "revolutionary", "AI is changing everything").
- Do not use DACH-only references unless comparing regions.
- Apply at least two thinking models (e.g., "Incentives over intentions", "Mechanism, not metaphor", "First- vs. second-order effects").
- Use constructions like: "The real problem is not X. It is Y." or "What is often underestimated is..."
- Keep text short and punchy. Maximum 1-2 lines per slide (except Slide 9).

## Design System & Prompting

Read `references/brand-design.md` before generating slides. The design is **Dark Cinematic Editorial**. It evolves the cyberpunk look into intelligent, serious tension.

**Constants for Image Generation Prompts:**
- **Style:** Dark cinematic editorial poster, serious tech analysis, high contrast.
- **Colors:** Super dark background (`#000000` or deep graphite), white text (`#ffffff`), single Electric Blue (`#00aaff`) accent. No pink.
- **Typography:** Massive uppercase condensed headlines (Avenir Next / Barlow Condensed). Text must dominate 45-70% of the canvas. No negative line spacing.
- **Layout:** Plakat-Modus. Headline first, image integrated. No thin separator lines, no underlines, no soft SaaS cards.
- **Motifs:** Slides 1, 2, 3, and 9 MUST feature concrete visual motifs (systems, decisions, evidence, trade-offs, human agency). No generic glowing brains or random code.

*Example Prompt Fragment:*
`Generate one Instagram carousel slide (4:5 ratio, 1080x1350px) in a dark cinematic editorial style. Super dark graphite background, massive uppercase white typography, subtle film grain, deep shadows. One keyword highlighted in Electric Blue #00aaff. The text must be huge and dominate the layout. Include a strong visual motif representing [CONCEPT]. No thin lines, no borders, no pink.`

## Caption and Sourcing Rules

**Caption Structure:**
1. **Thesis:** 1 sentence (reflecting Slide 1).
2. **Context:** 2-3 sentences of core facts.
3. **Implication:** 1-2 sentences on what this means for decision-makers.
4. **Sources:** Briefly list primary sources if facts were used.
5. **Hashtag:** Exactly one hashtag: `#ThinkRoger`.

**Evidence Standard:**
- Do not invent facts, numbers, or quotes.
- If the input lacks hard facts, search for primary/secondary sources to support the argument.
- Distinguish clearly between verified facts, reported claims, and interpretations.

## Bundled Resources

| Resource | Use |
|---|---|
| `references/editorial-framework.md` | Read before planning topics, selecting thinking models, checking evidence, or adapting a regional story for an international audience. |
| `references/brand-design.md` | Read before generating or laying out any slide image. |
| `references/platform-rules.md` | Read before exporting, packaging, or posting an Instagram carousel. |
| `scripts/extract_blog_content.py` | Use to produce a first JSON draft from text or a public article URL. Review and fact-check the output before design. |

## Quality Check Before Review

- [ ] Exactly 10 slides generated in 4:5 ratio.
- [ ] Language is International English.
- [ ] One primary topic pillar and at least two thinking models are named in planning notes.
- [ ] Every consequential claim is classified as fact, reported claim, interpretation, forecast, or open question.
- [ ] Slide 1 contains a strong thesis and a concrete visual motif.
- [ ] Slide 6 contains a credible counterpoint.
- [ ] Slide 9 contains a transferable decision framework with a strong visual motif.
- [ ] No facts, numbers, or quotes were invented.
- [ ] Design is dark cinematic editorial (black/white/electric blue, no pink).
- [ ] Typography is massive, readable, and uses no underlines.
- [ ] Caption uses only `#ThinkRoger`.
- [ ] Review package (Preview, Images, Caption, Source notes) is ready for user approval.
