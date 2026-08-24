---
name: ted-key-visual-presentations
description: Create TED-inspired, cinematic, image-led presentations and slide decks from rough content, documents, agendas, or existing text-heavy slides. Use when the user asks for TED style, TEDx-like without logo, cinematic presentation design, bold visual slides, key visuals, image-based slides, less text, more design, or says that slides are too text-heavy and should become visual core-message images.
---

# TED Key-Visual Presentations

Use this skill to transform content into **cinematic, TED-inspired presentations** where each slide is a visual idea, not a text container. The goal is to create a stage-ready deck with strong key visuals, minimal wording, dramatic hierarchy and memorable core messages.

## Core Principle

A TED-style key-visual presentation does not explain everything on the slide. It makes the audience **feel the idea first**, while the presenter explains the nuance verbally.

> If a slide can be read without the presenter, it is probably too text-heavy for this skill.

## When to Use

Use this skill when the user requests any of the following:

| User intent | Apply this skill |
|---|---|
| “More TED style”, “TEDx style”, “like a keynote stage” | Yes |
| “Less text, more design”, “too much text”, “more visual” | Yes |
| “Key visuals”, “Bilder der Kernaussagen”, “image-led slides” | Yes |
| “Bold, cinematic, designed” | Yes |
| “Create a premium presentation from this agenda/article/PDF” | Yes, if visual impact matters |
| “Handout”, “manual”, “course documentation” | No, unless the user explicitly wants a visual keynote version |

## Output Philosophy

Always design for **presentation impact**, not document completeness. Reduce aggressively. One slide should normally contain:

| Element | Rule |
|---|---|
| Core message | One idea only |
| Text | Maximum 1 headline and 1 short supporting phrase |
| Visual | One dominant image metaphor |
| Mood | Cinematic, staged, high contrast |
| Function | Make the audience remember the idea |

Avoid bullet-heavy structures. Avoid tables. Avoid explanatory paragraphs. Avoid UI-looking cards unless the concept explicitly requires an interface metaphor.

## Default Visual Style

Use this style unless the user gives another brand direction:

| Design element | Standard |
|---|---|
| Background | Deep cinematic black, near `#050505` |
| Main accent | Signal red `#FF1B1C` |
| System accent | Electric blue `#00D4FF` |
| Transfer accent | Lime green `#ADFF2F` |
| Mood | TED-like stage, black void, spotlight, red haze, neon data lines |
| Texture | Subtle urban graffiti-tech scratches, cinematic smoke, light beams |
| Typography | Huge uppercase headlines, extremely short copy |
| Composition | Strong negative space, one visual metaphor, no clutter |

Do not use any TED or TEDx logo. “TED-inspired” means stage energy, bold typographic hierarchy, simplicity and emotional clarity, not brand imitation.

## Workflow

Follow this sequence for every TED key-visual deck.

### 1. Extract the Core Messages

Reduce the source material to **8 to 16 memorable statements**. If the source is a full-day course, 12 to 18 slides are usually enough. If the source is a keynote, 8 to 12 slides are usually enough.

Write each slide as a short statement, for example:

| Weak slide title | Strong key-message title |
|---|---|
| Overview of AI tools in the application process | Nicht Tools. Klarheit. |
| LinkedIn profile optimisation | LinkedIn ist dein Dossier. |
| ATS systems and keyword matching | ATS sind Filter. |
| Interview preparation with AI | KI soll herausfordern. |

### 2. Convert Each Message into a Picture

For every message, define one visual metaphor. The metaphor must be concrete enough to generate or design as an image.

| Message | Image metaphor |
|---|---|
| Nicht Tools. Klarheit. | Tool chaos sinks into darkness, one spotlight illuminates clarity |
| Das Problem ist Unschärfe. | Blurred CV pages jammed in a red scanner |
| KI verstärkt. | A prism amplifies clarity on one side and chaos on the other |
| Prompt = Briefing. | Film director chair and AI crew member on a dark set |
| LinkedIn ist dein Dossier. | Digital dossier scanned by blue AI light |
| ATS sind Filter. | Red filter gate with green pass signals |

### 3. Choose Image Mode When Visual Impact Is Primary

For this skill, prefer slide generation in **image mode** when the user wants key visuals or says “Bilder der Kernaussagen”. Use image slides because they behave like designed posters. Use HTML mode only when the user explicitly needs editable slide elements or charts.

### 4. Initialize the Deck

Create a slide outline first. Keep slide titles short. Use the first slide as a cover and the last slide as a closing moment. Prefer 12 to 16 slides for a high-impact visual deck.

Use this deck arc by default:

| Phase | Purpose |
|---|---|
| Cover | Establish topic and cinematic mood |
| Thesis | State the central shift |
| Reality check | Show the human problem |
| Problem | Name the real blocker |
| Mechanism | Show what changes |
| Method | Show the operating principle |
| System | Show external systems or algorithms |
| Practice | Show one or two exercises as visual actions |
| Transfer | Show what happens after the session |
| Closing | Leave one sentence in the room |

### 5. Generate Each Slide as a Key Visual

For each image slide prompt, include these fields:

| Prompt field | Instruction |
|---|---|
| Title | Exact short headline to render on the slide |
| Key text | Optional supporting phrase, maximum one line |
| Visual elements | Concrete image metaphor, scene, lighting and objects |
| Layout preference | Where the headline, subject and negative space should sit |
| Text hierarchy | Which words must be largest and most readable |
| Continuity note | Keep black stage, red spotlight, blue data lines and lime accents consistent |

## Image Prompt Template

Use this template for image-based slides:

```text
Title: [SHORT CORE MESSAGE]
Key text: [OPTIONAL SHORT PHRASE]
Visual Elements: [Concrete scene, metaphor, objects, lighting, emotional tension, cinematic staging.]
Layout Preference: [Where title sits, where the image focus sits, how much negative space, 16:9 composition.]
Text Hierarchy: [Which text is largest, which word is highlighted, what must remain readable.]
Continuity Note: Maintain cinematic black stage, signal red spotlight, electric-blue data light, lime-green accent sparks, bold uppercase typography, urban graffiti-tech scratches, high contrast, no logo, no clutter.
```

## Quality Rules

Always enforce these rules:

| Rule | Why |
|---|---|
| One slide, one idea | Prevents PowerPoint prose |
| One dominant image metaphor | Makes the slide memorable |
| Maximum two text elements | Keeps the audience listening |
| Use black space intentionally | Creates stage presence |
| Make text readable at distance | Presentation first, poster second |
| Avoid dense UI mockups | They become visual noise |
| Avoid small pseudo-text | It looks messy and is unreadable |
| Avoid logos unless provided by user | Prevents brand and copyright issues |

## Text Reduction Rules

When transforming a text-heavy slide, reduce it as follows:

| Source content | Keep |
|---|---|
| Paragraph | One sentence |
| Bullet list | One metaphor |
| Five key points | One contradiction or shift |
| Tool list | One operating logic |
| Exercise instructions | One action verb |
| Framework | One visual structure |

Examples:

| Text-heavy input | TED key-visual output |
|---|---|
| “Participants learn how to use AI tools strategically in applications.” | Nicht Tools. Klarheit. |
| “The LinkedIn algorithm now evaluates profile, content and engagement contextually.” | LinkedIn ist dein Dossier. |
| “ATS systems parse CVs and compare keywords with job descriptions.” | ATS sind Filter. |
| “AI can simulate interviews and give feedback.” | KI soll herausfordern. |

## Default Slide Count

If the user gives no slide count, choose based on purpose:

| Purpose | Default count |
|---|---:|
| Short visual keynote | 8 to 10 |
| Course opener or concept deck | 12 to 14 |
| Full-day workshop visual backbone | 14 to 18 |
| Social carousel adaptation | 8 to 10 |

Do not create 30+ text slides unless the user explicitly requests a documentation deck. For this skill, shorter is usually stronger. Ja, die Folie darf atmen. Sie ist kein Steuerformular.

## Common Mistakes to Avoid

Do not simply make text slides prettier. Do not add decorative stock icons around long content. Do not preserve every point from the source material. Do not turn exercises into instruction manuals. Do not make every slide look like a dashboard. Do not use TED/TEDx logos. Do not create “corporate clean” layouts when the user asked for bold cinematic design.

## Delivery

Present the completed deck through the slide presentation flow. If possible, also export a PPTX. If PPTX export times out, retry once before delivering. If export still fails, deliver the slide presentation link and explain briefly that the export can be retried.

## Example Arc: AI Application Course

Use this as a reusable pattern for AI, LinkedIn and self-marketing topics:

| Slide | Message | Visual metaphor |
|---:|---|---|
| 1 | KI im Bewerbungsprozess | Black stage with CVs, data streams and red spotlight |
| 2 | Nicht Tools. Klarheit. | Tool chaos sinking into shadow, clarity in spotlight |
| 3 | Das Problem ist Unschärfe. | Blurred profile and CV stuck in red scanner |
| 4 | KI verstärkt. | Prism amplifies clarity or chaos |
| 5 | Prompt = Briefing. | Director chair and AI crew member on film set |
| 6 | LinkedIn ist dein Dossier. | Digital dossier scanned by blue AI light |
| 7 | Vom Zählen zum Verstehen. | Old metric machine versus neural context reader |
| 8 | ATS sind Filter. | Red filter gate with green pass signals |
| 9 | Match, nicht Märchen. | Burning fake CV versus precise match scan |
| 10 | KI soll herausfordern. | Candidate in spotlight facing AI interview simulator |
| 11 | 7 Tage. 7 Outputs. | Mission-control wall with seven output tiles |
| 12 | KI ersetzt dich nicht. | Human silhouette sharpened by AI light structure |

## Final Check Before Delivery

Before presenting, verify that the deck passes these questions:

| Check | Pass condition |
|---|---|
| Can the audience grasp each slide in three seconds? | Yes |
| Does every slide have one dominant visual idea? | Yes |
| Is there any paragraph text? | No |
| Could a presenter talk over the slide naturally? | Yes |
| Does the deck feel like a stage experience, not a PDF? | Yes |
| Is the logo-free TED-inspired style respected? | Yes |
