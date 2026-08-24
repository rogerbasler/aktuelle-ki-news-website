# eBook Metadata and Layout Options

## Required Project Metadata

| Field | Description | Example |
|---|---|---|
| `project_name` | Short file-safe name in lowercase snake case. | `real_estate_circle_ki` |
| `title` | Main title shown on cover. | `Künstliche Intelligenz in der Immobilienbranche` |
| `subtitle` | Short explanatory subtitle. | `Realitycheck: Zahlen. Daten. Perspektiven.` |
| `event` | Event or publishing context. | `Real Estate Circle` |
| `edition` | Optional edition, anniversary or year. | `20 Jahre Real Estate Circle` |
| `author` | Author or speaker. | `Roger Basler de Roca` |
| `author_role` | Short role description. | `MSc Digital Business | PhD Candidate | Digital-Unternehmer` |
| `audience` | Primary target audience. | `Entscheider:innen der Immobilienbranche` |
| `tone` | Editorial tone. | `souverän, präzise, leicht pointiert` |
| `links` | Required links. | `fragRoger.ai, rogerbasler.ch, langdock.com` |
| `sources_required` | Whether external claims need sources. | `true` |

## Layout Presets

| Preset | Visual Character | Best For |
|---|---|---|
| `premium_light` | Warm paper, dark ink, cyan and gold accents. | Executive handouts, keynote companions, business eBooks. |
| `editorial_white` | White background, large type, magazine spacing. | Thought leadership, academic-lite reports. |
| `dark_tech` | Dark background, high contrast, neon accent. | AI, cyber, future-facing topics. Use selectively. |
| `workbook_light` | Light background, many boxes and templates. | Training guides, exercises, prompts, checklists. |
| `data_report` | Conservative layout, tables and figures. | Evidence-heavy reports with many sources. |

## Recommended Page Sequence

| Page | Type | Notes |
|---:|---|---|
| 1 | Cover | Strong visual, title, event, author. |
| 2 | Table of contents | Must be updated after rendering. |
| 3 | Foreword | Establish argument and credibility. |
| 4 | Audience and relevance | Clarify decision-maker value. |
| 5 | Realitycheck | Numbers, trends, source-backed claims. |
| 6 | Sector-specific opportunity | Translate topic into audience context. |
| 7 | Core framework | Main model or decision logic. |
| 8 | Method/framework | Prompting, governance, process logic. |
| 9 | Risk and responsibility | Data, compliance, quality control. |
| 10 | Practical instructions | Actionable routines and checks. |
| 11-13 | Prompt or template cards | Two-column prompt cards. |
| 14 | Roadmap | 30, 60 or 90-day implementation plan. |
| 15-16 | Tool/platform chapter | Only if useful for implementation. |
| 17 | About author | Credible, concise, with website link. |
| 18 | Sources and resources | References, tools, next steps. |

## Visual Components

| Component | Class Name | Use |
|---|---|---|
| Running header | `.running` | Context and chapter label. |
| Page number | `.page-number` | Bottom right. |
| Eyebrow | `.eyebrow` | Section number or category. |
| Lead paragraph | `.lead` | Executive summary of the page. |
| Quote box | `.quote` | Memorable thesis or closing line. |
| Link box | `.linkbox` | Useful next step without link spam. |
| Fact cards | `.fact-grid`, `.fact` | Evidence and headline numbers. |
| Prompt cards | `.prompt-grid`, `.prompt` | Practical prompts and templates. |
| Flow cards | `.flow` | Three-part framework. |
| Mini cards | `.mini-grid`, `.mini-card` | Four-step explanations. |
| Roadmap rows | `.road`, `.road-step` | Implementation phases. |

## Roger-Specific Link Strategy

| Link | Best Placement | Framing |
|---|---|---|
| `https://www.fragroger.ai` | Prompting, KI-Richtlinien, Use Cases, roadmap. | Practical continuation of the handout. |
| `https://www.rogerbasler.ch` | About page, final resources. | Keynotes, workshops, publications, contact. |
| `https://www.langdock.com` | Enterprise AI or platform chapter. | Unternehmenswissen, Skills, Workflows, Governance. |
| `https://crapcheck.ai` | Source checking, quality assurance. | Prüfkompetenz and fact-checking. |

## Quality Gates

Before delivery, the rendered PDF must pass these gates:

| Gate | Check |
|---|---|
| Visual | Inspect cover, TOC, dense content, prompt/tool page and final page. |
| Technical | Confirm page count with `pdfinfo`. |
| Swiss | Confirm zero `ß`. |
| Roger style | Confirm zero em dashes `—`. |
| Links | Confirm required links appear and are meaningful. |
| Sources | Confirm externally sourced claims have visible references. |
| Attachments | Deliver PDF first, then HTML, then supporting notes. |
