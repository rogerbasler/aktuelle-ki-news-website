---
name: black-urban-graffiti-tech-slides
description: Design system and workflow for creating presentations in the "Black Urban Graffiti Tech" style — pure black backgrounds (#000000), very dark surfaces (#050505), neon accents (Electric Blue #00D4FF, Neon Pink #FF006E, Lime Green #ADFF2F), Montserrat 900 UPPERCASE headlines, and JetBrains Mono labels. Use when the user requests: "Black Graffiti style slides", "pure black neon presentation", "dark urban tech design", "black-urban-graffiti-tech-slides", or wants a bold, high-energy visual style with maximum contrast. Also use for AI, tech, marketing, coaching, or solopreneur topics where a bold, high-contrast aesthetic is appropriate.
---

# Black Urban Graffiti Tech Slides

Design system for bold, urban-styled presentations with a pure black aesthetic. Based on the original Urban Graffiti Tech style, but optimized for pure black (#000000) backgrounds to create maximum contrast with neon accents.

## Color Palette

```
Background:   #000000  (Pure Black)
Surface:      #050505  (Very Dark Card/Panel)
Border:       #1A1A1A  (Subtle dividers)

Neon Blue:    #00D4FF  (Primary — ChatGPT, headlines, links)
Neon Pink:    #FF006E  (Secondary — chapter markers, CTAs)
Neon Green:   #ADFF2F  (Tertiary — success, tips, highlights)
Neon Orange:  #FF9F1C  (Quaternary — Mistral, EU topics, Phase 3)
Gold:         #FFD700  (Premium, awards)
Red (Pain):   #FF3333  (Problem slides only — muted palette)

Text Primary:   #FFFFFF
Text Secondary: #CCCCCC
Text Muted:     #888888
```

## Typography

Always include this Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Montserrat:wght@700;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
```

| Role | Font | Weight | Style |
|------|------|--------|-------|
| Headlines | Montserrat | 900 | UPPERCASE |
| Body | Inter | 400/600 | Normal |
| Labels/Tags/URLs | JetBrains Mono | 700 | UPPERCASE |

Font sizes — Front page: 84px / 48px / 26px. Content slides: 38px / 20px / 14px.

## Slide Setup

```css
.slide-container {
    width: 1280px;
    height: 720px;  /* use min-height in flex children */
    background: #000000;
    padding: 50px 80px;  /* NEVER use padding-bottom */
    display: flex;
    flex-direction: column;
}
```

## Signature Visual Elements

**Accent top-border on cards** (never rounded corners, never box-shadow on cards):
```css
.card { border-top: 4px solid #00D4FF; background: rgba(255,255,255,0.03); }
```

**Neon glow on headlines**:
```css
h1 { text-shadow: 0 0 15px rgba(0, 212, 255, 0.4); }
```

**Graffiti background decorator** (large, low-opacity, rotated):
```html
<div style="position:absolute; font-family:'Montserrat',sans-serif; font-size:120px; font-weight:900; color:#1A1A1A; opacity:0.4; z-index:0; transform:rotate(15deg); top:40px; right:60px;">VS</div>
```

**JetBrains Mono section label** (above every content block):
```html
<div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#666; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px;">Section Label</div>
```

**Bottom bar** (every content slide — key takeaway):
```html
<div style="background:#050505; border:1px solid #1A1A1A; border-left:5px solid #ADFF2F; padding:14px 25px; display:flex; align-items:center; justify-content:space-between;">
    <span style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:16px; color:#ADFF2F; text-transform:uppercase;">KEY TAKEAWAY HERE</span>
</div>
```

**Badge/CTA sticker** (graffiti sticker effect):
```html
<div style="background:#ADFF2F; color:#000; font-family:'Montserrat',sans-serif; font-weight:900; font-size:18px; padding:10px 20px; text-transform:uppercase; letter-spacing:2px; box-shadow:5px 5px 0px #FF006E;">BADGE TEXT</div>
```

**Slight card rotation** (pain/problem slides only, max ±0.5deg):
```css
.card:nth-child(1) { transform: rotate(-0.4deg); }
.card:nth-child(2) { transform: rotate(0.3deg); }
```

## Color Assignment by Topic

Assign one neon color per major topic — use consistently across all slides in that chapter:

| Topic | Color |
|-------|-------|
| KI Basics / ChatGPT | #00D4FF Blue |
| Prompting / Claude | #FF006E Pink |
| Custom GPTs / Automation / Value | #ADFF2F Green |
| Mistral / EU / Phase 3 | #FF9F1C Orange |
| Problems / Pain points | #FF3333 Red (muted palette) |
| Bonus / Premium | #FFD700 Gold |

## Slide Structure Pattern

Every slide: `[Header] → [Main Grid] → [Bottom Bar]`

- Header: `h1` with `border-left: 8px solid <accent>` OR `header-row` flex with badge
- Main: CSS Grid — 2-col (`1fr 1fr`), 3-col (`1fr 1fr 1fr`), or 2×2 (`repeat(2,1fr)`)
- Bottom: Always a bottom bar with the key takeaway

For detailed HTML templates for each slide type, see `references/slide-types.md`.

## Narrative Arc (Business/Coaching Topics)

1. **Title** — Brand + tagline + `[N] Slides · [N] Kapitel · ∞ Möglichkeiten` badge
2. **Pain** — "Kennst du das?" — 6 problem cards, red palette, hook at bottom
3. **Lichtblick** — Before/After 2-column comparison, pivot to hope
4. **Journey** — 3-phase horizontal roadmap (e.g., 90-day transformation)
5. **Roadmap** — Chapters overview
6. **Content chapters** — Topic slides
7. **Bonus** — Extra value
8. **Closing** — Brand slide with all chapters recap + `∞ Möglichkeiten` + tagline

## slide_initialize Parameters

```
aesthetic_direction: "Pure black urban graffiti wall meets neon-lit tech terminal — maximum contrast with raw spray-paint energy, precision grid layouts and glowing data"
color_palette: "Background #000000, Text #FFFFFF, Accent 1 #00D4FF (Electric Blue), Accent 2 #FF006E (Neon Pink), Accent 3 #ADFF2F (Lime Green)"
typography: "Montserrat 900 UPPERCASE for headlines, Inter 400/600 for body, JetBrains Mono 700 for labels/code. Front: 84px/48px/26px. Content: 38px/20px/14px."
```

## Export & Canva Upload Workflow

1. Present: `slide_present` → get `manus-slides://{id}`
2. Export: `manus-export-slides manus-slides://{id} ppt`
3. Upload: `manus-upload-file <file>.pptx` → get CDN URL
4. Import to Canva: `import-design-from-url` MCP tool with CDN URL and design name

## Absolute Rules

- NEVER `overflow: hidden` on body
- NEVER `position: absolute` for main content containers
- NEVER `padding-bottom` anywhere — use `padding-top` / `margin-top` only
- NEVER rounded corners on content cards
- NEVER box-shadow on cards (only on badge/CTA stickers)
- ALWAYS `text-transform: uppercase` on Montserrat headlines
- ALWAYS end every content slide with a bottom bar takeaway
- ALWAYS assign one accent color per chapter and stay consistent
stay consistent
