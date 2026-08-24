---
name: thinkroger-instagram-carousel-purple
description: >
  Converts articles, texts, notes, or URLs into fact-based, constructive, and positive 10-slide Instagram carousels in English for an international audience under the #ThinkRoger brand.
  Use this skill whenever the user says: "/thinkroger-instagram-carousel-purple", "ThinkRoger purple carousel", "constructive English carousel", or explicitly requests the purple #ThinkRoger style.
  Output: 10 slide images in 4:5 format (dark cinematic editorial style with Bright Purple #8B5CF6 accent), an English caption, source notes, and mandatory review before optional Instagram posting.
---

# #ThinkRoger Instagram Carousel - Constructive Editorial Engine (Purple)

## Purpose and Positioning

This skill creates English-language, international Instagram carousels for the **#ThinkRoger** brand. It transforms source material into a fact-checked, decision-relevant argument about AI, digital power, business models, leadership, and human agency, but with a specifically **informative, constructive, and positive** focus.

The tone is informed, precise, independent, and optimistic without being naïve. It highlights opportunities, value creation, and successful systems. The focus is on **evidence, context, systems thinking, and actionable positive insights**.

## Standard Workflow

1. **Input ingestion:** Accept text, files, or URLs. Extract facts, context, and claims.
2. **Evidence check:** Separate verified facts from reported claims, interpretations, and forecasts. Do not invent facts, numbers, or quotes.
3. **Structure generation:** Build a 10-slide constructive editorial arc (Thesis, Why Now, Evidence, Mechanism, Hidden Opportunity, Counterpoint, System View, Thinking Shift, Decision Framework, Think Again).
4. **Image generation:** Create 10 slide images in a 4:5 ratio (1080×1350px) using the dark cinematic editorial design system with Bright Purple `#8B5CF6` accents. Slide 1, 2, 3, and 9 MUST have strong visual motifs.
5. **Caption writing:** Write an English caption with thesis, context, constructive implication, and exactly one hashtag (`#ThinkRoger`).
6. **Review before posting:** Present the final slides, caption, and source notes to the user. Wait for an explicit **GO**.
7. **Optional posting:** Upload images and post via Instagram MCP only after explicit approval.

## Output Standards

| Element | Requirement |
|---|---|
| Slides | Exactly 10 slides |
| Format | Instagram 4:5 ratio (1080×1350px) |
| Language | International English (no regional idioms) |
| Tone | Fact-based, constructive, positive, precise |
| Visual Style | Dark cinematic editorial (black, white, Bright Purple `#8B5CF6`) |
| Quality Gate | Review required before posting |
| Hashtag | Only `#ThinkRoger` in the caption |

## The 10-Slide Constructive Editorial Architecture

| Slide | Type | Function and Content |
|---|---|---|
| 1 | THESIS | A sharp, defensible, constructive claim or opportunity. No empty questions. |
| 2 | WHY NOW | The event, data point, shift, or success that makes this timely. |
| 3 | EVIDENCE | One concrete fact, number, study result, or documented positive example. |
| 4 | MECHANISM | Explain how the system, incentive, or technology produces the value. |
| 5 | HIDDEN OPPORTUNITY | Surface what most people miss (a delayed benefit, a positive second-order effect). |
| 6 | COUNTERPOINT | The strongest credible limitation, boundary condition, or necessary trade-off. |
| 7 | SYSTEM VIEW | Connect actors, incentives, dependencies, and positive feedback loops. |
| 8 | THINKING SHIFT | The refined conclusion after weighing evidence and opportunity. |
| 9 | FRAMEWORK | Three questions, tests, or actions that transfer this success beyond this single case. |
| 10 | THINK AGAIN | Invite reflection or constructive application. End with CTA and `#ThinkRoger`. |

## Topic and Thinking Selection

Before drafting, read `references/editorial-framework.md`. Select one primary topic pillar and at least two thinking models. Record them in planning notes so that the carousel explains a constructive system rather than merely decorating an opinion.

## Writing Guidelines (International English)

- Write in clear, concrete International English.
- Use active verbs and sentence case for body text.
- Focus on what works, how value is created, and how leaders can build better systems.
- Avoid alarmism, cynicism, or pure hype ("revolutionary", "magic").
- Apply at least two thinking models.
- Keep text short and punchy. Maximum 1-2 lines per slide (except Slide 9).

## Design System & Prompting

Read `references/brand-design.md` before generating slides. The design is **Dark Cinematic Editorial** with **Bright Purple `#8B5CF6`** as the sole accent colour.

**Constants for Image Generation Prompts:**
- **Style:** Dark cinematic editorial poster, serious tech analysis, high contrast.
- **Colours:** Super dark background (`#000000` or deep graphite), white text (`#ffffff`), single Bright Purple (`#8B5CF6`) accent. No electric blue, no pink.
- **Typography:** Massive uppercase condensed headlines (Avenir Next / Barlow Condensed). Text must dominate 45-70% of the canvas. No negative line spacing.
- **Layout:** Plakat-Modus. Headline first, image integrated. No thin separator lines, no underlines, no soft SaaS cards.
- **Motifs:** Slides 1, 2, 3, and 9 MUST feature concrete visual motifs (systems, decisions, evidence, human agency). No generic glowing brains or random code.

## Caption and Sourcing Rules

**Caption Structure:**
1. **Thesis:** 1 sentence (reflecting Slide 1).
2. **Context:** 2-3 sentences of core facts.
3. **Constructive Implication:** 1-2 sentences on what this means for decision-makers to build better systems.
4. **Sources:** Briefly list primary sources if facts were used.
5. **Hashtag:** Exactly one hashtag: `#ThinkRoger`.

## Bundled Resources

| Resource | Use |
|---|---|
| `references/editorial-framework.md` | Read before planning topics, selecting thinking models, or checking evidence. |
| `references/brand-design.md` | Read before generating or laying out any slide image. |
| `references/platform-rules.md` | Read before exporting, packaging, or posting an Instagram carousel. |
| `scripts/extract_blog_content.py` | Use to produce a first structured draft from text or a public article URL. Review and fact-check it before design. |

## Quality Check Before Review

- [ ] Exactly 10 slides generated in 4:5 ratio.
- [ ] Tone is informative, constructive, and positive.
- [ ] Every consequential claim is classified as fact, reported claim, interpretation, forecast, or open question.
- [ ] Slide 1 contains a strong constructive thesis and a concrete visual motif.
- [ ] Slide 5 focuses on a Hidden Opportunity rather than just a hidden cost.
- [ ] Slide 9 contains a transferable decision framework with a strong visual motif.
- [ ] Design is dark cinematic editorial (black/white/Bright Purple `#8B5CF6`, no electric blue).
- [ ] Bright Purple is visibly saturated, used on at least one large decision cue per slide, and never rendered as dark plum or magenta.
- [ ] Typography is massive, readable, and uses no underlines.
- [ ] Caption uses only `#ThinkRoger`.
- [ ] Review package (Preview, Images, Caption, Source notes) is ready for user approval.
