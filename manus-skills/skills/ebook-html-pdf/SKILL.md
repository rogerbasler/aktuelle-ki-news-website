---
name: ebook-html-pdf
description: >
  Workflow for creating premium A4 HTML eBooks and handouts that are exported
  as PDF. Use when the user asks for an eBook-like handout, PDF report,
  conference handout, executive guide, workbook, keynote companion, or visually
  designed document with cover, table of contents, chapter pages, callouts,
  prompt cards, workflows, resource links, sources, and final PDF export.
---

# HTML eBook to PDF Skill

## Purpose

This skill creates **premium A4 eBook-style handouts** using HTML and CSS, then renders them into a print-ready PDF. It is designed for documents that need stronger visual hierarchy than a standard Word document, while remaining precise, professional and easy to update.

Use this skill when the user asks for a **handout, eBook, executive guide, workshop guide, conference companion, keynote companion, PDF workbook or visually designed report**. The core idea is simple: write the content with the rigour of a strategic document, design it with the clarity of a magazine, and export it as a stable PDF. Fancy enough to look intentional, sober enough not to scream "template from a webinar funnel".

## Core Output

The default output is a folder containing the final PDF, the editable HTML source, optional Markdown blueprint files, preview images and a short layout quality-check note.

| File | Purpose |
|---|---|
| `project_name_ebook.pdf` | Final PDF for the user. |
| `project_name_ebook.html` | Editable source file with print-optimised HTML and CSS. |
| `content_blueprint.md` | Structured content draft before final layout. |
| `layout_pruefung.md` | Notes from visual and technical quality checks. |
| `preview/page-XX.png` | Rendered preview pages for visual inspection. |

## Language and Style Rules for Roger

When the user is Roger Basler de Roca or the document is German-language professional content, apply Swiss German writing conventions and Roger's preferred editorial style.

| Rule | Implementation |
|---|---|
| Swiss keyboard and spelling | Always write ä, ö, ü directly. Use `ss`, never `ß`. |
| No em dashes | Avoid `—`. Use commas, colons, semicolons or short hyphens where needed. |
| Tone | Souverän, präzise, respektvoll, leicht pointiert. |
| Structure | Start with a clear thesis, then context, reasoning and implication. |
| Substance | Avoid buzzwords without explanation. Show consequences for decision-makers. |
| Voice | Clear, dense and practical. Subtle wit is allowed, self-parody is not. |

## Default Document Architecture

Create the eBook in phases. Do not start with layout before the argument is clear. The HTML should be a vessel for thinking, not a glitter coffin for thin content.

| Section | Purpose | Typical Length |
|---|---|---:|
| Cover | Event, topic, title, author, visual framing. | 1 page |
| Table of contents | Orientation and page structure. | 1 page |
| Foreword | Establish perspective, credibility and intent. | 1 page |
| Target audience | Clarify who the document is for and why it matters. | 1 page |
| Realitycheck or evidence page | Numbers, trends, data and what they do not say. | 1 to 2 pages |
| Core framework | Main model, principle or decision logic. | 1 to 3 pages |
| Practical instructions | Step-by-step guidance, checklists, routines. | 1 to 3 pages |
| Prompt or tool cards | Practical templates or resources. | 1 to 4 pages |
| Workflow or roadmap | Implementation plan, phases and responsibilities. | 1 to 2 pages |
| Partner/tool chapter | If relevant: explain platform, use cases and workflows. | 1 to 2 pages |
| About page | Professional author or speaker page. | 1 page |
| Sources/resources | References, tools and next steps. | 1 page |

## Layout Options

Use a consistent A4 print system. Design choices should support reading and decision-making.

| Option | Recommended Use | Notes |
|---|---|---|
| `premium_light` | Executive handouts, reports, conference guides. | Light paper background, dark typography, blue/gold accents. Default for Roger. |
| `dark_tech` | Futuristic or high-impact tech topics. | Dark background, neon accents, use sparingly for readability. |
| `magazine_editorial` | Thought leadership reports and whitepapers. | Large titles, strong spacing, editorial pull quotes. |
| `workbook` | Exercises, prompts, checklists, templates. | More boxes, tables, writable structures. |
| `data_report` | Source-heavy reports with charts. | Strong tables, figures, notes, conservative design. |

### Default A4 Page Settings

Use CSS that works reliably with WeasyPrint. Avoid unsupported shorthand like `inset` for critical page positioning.

```css
@page { size: A4; margin: 0; }
body { margin: 0; background: #d8dde3; }
.page {
  position: relative;
  width: 210mm;
  height: 297mm;
  margin: 0 auto;
  background: #f7f5ef;
  overflow: hidden;
  page-break-after: always;
}
.content {
  position: absolute;
  top: 22mm;
  left: 18mm;
  right: 18mm;
  bottom: 18mm;
}
.running {
  position: absolute;
  top: 9mm;
  left: 18mm;
  right: 18mm;
}
.page-number {
  position: absolute;
  bottom: 9mm;
  right: 18mm;
}
```

## Reusable Page Types

### Cover Page

A strong cover includes event context, title, subtitle, author and visual metaphor. For business and real estate topics, a subtle grid, architecture line drawing, data-network motif or geometric abstraction works well.

Required cover elements:

| Element | Example |
|---|---|
| Event | `Real Estate Circle · 20 Jahre Real Estate Circle` |
| Format | `Handout zum Vortrag` |
| Main title | `Künstliche Intelligenz in der Immobilienbranche` |
| Subtitle | `Realitycheck: Zahlen. Daten. Perspektiven.` |
| Author | `Roger Basler de Roca` |
| Role | `MSc Digital Business | PhD Candidate | Digital-Unternehmer, Buchautor und Top-100-Speaker` |

### Table of Contents

Use clean rows with chapter number, title and page number. Update manually after rendering if needed. Keep the TOC readable and do not overfill it.

### Foreword

The foreword should answer three questions: Why this document, why now, and what should the reader do differently afterwards?

For Roger-style documents, use a crisp thesis and a memorable closing quote. Avoid generic gratitude rituals. This is a handout, not a wedding speech.

### Realitycheck Page

Use four or six data cards. Each card should have one number, one label and one interpretation. Always include sources when using external data.

Recommended card structure:

| Field | Description |
|---|---|
| Number | The core figure, visually dominant. |
| Label | Short meaning of the figure. |
| Interpretation | What the figure implies and what it does not prove. |
| Source marker | Reference number if needed. |

### Framework Page

Use tables, three-column flows or formula blocks for core models. Good framework pages are remembered because they reduce complexity without flattening it.

Examples:

| Framework | Use |
|---|---|
| `Daten + Prompts + Prüfung = Kontext` | Explaining AI adoption quality. |
| `GCES` | Prompt structure: Goal, Context, Expectation, Sources. |
| `VIP` | Data governance: Vertraulich, Intern, Personenbezogen. |
| `CRAP` | Source review: Current, Reliable, Authority, Purpose. |

### Prompt Cards

Prompt pages should use compact cards in a two-column grid. Each card needs a use case, full prompt and practical tip.

Card fields:

| Field | Description |
|---|---|
| Number and use case | Example: `01 · Exposé`. |
| Framework tag | Example: `GCES`. |
| Prompt text | Specific enough to be useful. |
| Tip | Operational advice or risk warning. |

### Tool or Platform Chapter

When a tool such as Langdock is relevant, explain it through the lens of the user's audience, not as a generic product description.

For Langdock-style chapters, use this sequence:

| Layer | Explanation |
|---|---|
| Unternehmenswissen anbinden | Internal documents, guidelines, object data and process knowledge become usable. |
| Skills erstellen | Repeatable AI capabilities for recurring tasks are defined. |
| Workflows bauen | Multi-step processes connect input, structuring, review, release and documentation. |
| Governance sichern | Access, data classes and approvals become controllable. |

### About Page

The about page should be concise and credible. For Roger, use verified biographical framing only and link to `https://www.rogerbasler.ch`. Avoid invented achievements, inflated claims or overly breathless speaker-marketing language.

## Workflow

### 1. Clarify Inputs

Ask for or infer the following information before final writing if it is missing.

| Input | Why it matters |
|---|---|
| Event and audience | Determines tone and examples. |
| Main topic and thesis | Prevents generic content. |
| Desired length | Controls page count and density. |
| Existing text or slides | Preserves the user's voice and structure. |
| Required links or tools | Ensures resources are embedded logically. |
| Source requirements | Determines research depth and citation format. |

### 2. Create a Content Blueprint

Write a Markdown blueprint first. Include title, target audience, table of contents, foreword, chapter summaries, frameworks, prompts, roadmap and sources. This blueprint is the thinking layer. The HTML is the visual layer.

### 3. Build the HTML

Use one HTML file with embedded CSS unless the project is unusually large. Page sections should use `<section class="page">`. Keep CSS print-friendly and avoid properties that WeasyPrint ignores for critical layout.

### 4. Render to PDF

Use WeasyPrint and create PNG previews from the PDF.

```bash
weasyprint project_ebook.html project_ebook.pdf
mkdir -p preview
pdftoppm -png -r 120 project_ebook.pdf preview/page
```

### 5. Visually Inspect

Inspect at least the cover, table of contents, one dense content page, one prompt/tool page and the final page. Save observations to `layout_pruefung.md`.

### 6. Technical Quality Check

Run checks for Swiss spelling, page count and unwanted characters.

```bash
pdfinfo project_ebook.pdf | awk '/Pages/ {print $2}'
grep -o '—' project_ebook.html | wc -l
grep -o 'ß' project_ebook.html | wc -l
```

For Roger, both counts must be zero.

## Link Placement Rules

Links should be placed where they help the reader take the next step. Do not create link farms.

| Link Type | Placement |
|---|---|
| User website | About page and final resource page. |
| Tool website | Tool chapter and resource table. |
| Practice hub | Framework, prompting, instructions or roadmap pages. |
| Sources | Evidence pages and source page. |

For Roger's KI documents, typical links are:

| Resource | Use |
|---|---|
| `https://www.fragroger.ai` | KI-Richtlinien, Prompting, Use Cases, practical resources. |
| `https://www.rogerbasler.ch` | About Roger, keynotes, workshops, publications. |
| `https://www.langdock.com` | Enterprise AI platform, governance, knowledge, skills and workflows. |
| `https://crapcheck.ai` | Fact-checking and source review support. |

## Quality Checklist

Before delivery, confirm the following:

| Check | Requirement |
|---|---|
| Cover | Strong title hierarchy, event visible, author visible. |
| TOC | Page numbers match the rendered PDF. |
| Layout | No overlap between running headers and titles. |
| Readability | Dense pages remain readable at A4 size. |
| Links | Links are meaningful and not excessive. |
| Sources | Factual claims with external data are sourced. |
| Swiss German | No `ß`; umlauts are written directly. |
| No em dashes | No `—` in German content for Roger. |
| Final files | Attach PDF, HTML and useful supporting files. |

## Common Pitfalls

Avoid these mistakes:

| Pitfall | Better Approach |
|---|---|
| Starting with design before argument | Create the content blueprint first. |
| Too many decorative graphics | Use visuals to clarify structure, not to decorate uncertainty. |
| Generic tool promotion | Explain tools through audience-specific workflows. |
| Long prompt pages without structure | Use prompt cards with use case, prompt and tip. |
| Unchecked PDF rendering | Always inspect rendered pages, not just the HTML. |
| Overfilled A4 pages | Split dense sections into multiple pages. |
| Unverified sources | Use credible sources and cite them visibly. |

## Delivery Message

The final user-facing message should be concise and mention what was created, what files are attached and any notable checks passed. Avoid long explanations in the message body; the deliverable should carry the substance.
