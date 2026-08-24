# LinkedIn Slides — Design System Reference
## fragRoger White & Blue Graffiti Style

---

## Color Palette

```
Background Primary:   #FFFFFF  (Pure White — Slides 1, 2, 4, 6, 8, 10)
Background Alt:       #EEF4FB  (Light Blue-Grey — Slides 3, 5, 7, 9)
Surface Card:         #F0F7FF  (Very light blue card panels)
Border Subtle:        #D0E4F7  (Card borders)

Electric Blue:        #0066CC  (Primary accent — headlines, dividers, badges)
Deep Blue:            #003D7A  (Secondary — dark text accents, labels)
Sky Blue:             #4A9FE0  (Tertiary — ghost words, decorative elements)
White:                #FFFFFF  (Text on dark badges)

Text Primary:         #0D1B2A  (Near Black — main headlines)
Text Secondary:       #2C4A6E  (Dark Blue — body text)
Text Muted:           #6B8CAE  (Medium Blue-Grey — labels, counters)

Accent Spark:         #FF6B35  (Orange — used ONCE per deck for the most important number/stat)
```

---

## Typography — Avenir Font Stack

LinkedIn slides use Avenir (system) with web fallbacks:

```css
/* Avenir stack — always use this order */
font-family: 'Avenir Next', 'Avenir', 'Nunito', 'Nunito Sans', sans-serif;
```

Google Fonts fallback (when Avenir not available):
```html
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Nunito+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
```

| Role | Font | Weight | Style |
|------|------|--------|-------|
| Main Headlines | Avenir Next / Nunito | 900 | UPPERCASE |
| Sub-Headlines | Avenir Next / Nunito | 700 | UPPERCASE |
| Body Text | Avenir / Nunito Sans | 600 | Normal |
| Labels / Tags | Avenir Next / Nunito | 800 | UPPERCASE, letter-spacing: 3px |
| Stats / Numbers | Avenir Next / Nunito | 900 | Normal |
| Counters / URLs | Avenir Next / Nunito | 700 | Normal |

Font sizes:
- Title slide: 72px headline / 32px subtitle / 18px label
- Content slides: 42px headline / 22px body / 14px label / 80px stat number

---

## Slide Dimensions

LinkedIn Document/Carousel: **1080x1080px (1:1 square)**
HTML slide container: **1280x720px (16:9)** — rendered and exported as square via slides tool

```css
.slide-container {
    width: 1280px;
    height: 720px;
    background: #FFFFFF;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    font-family: 'Avenir Next', 'Avenir', 'Nunito', sans-serif;
    position: relative;
    overflow: hidden;
}
```

---

## Signature Visual Elements

### Top Accent Bar (every slide — MANDATORY)
```html
<div style="height:6px; background:linear-gradient(90deg, #0066CC 0%, #4A9FE0 60%, #D0E4F7 100%); margin-bottom:30px; border-radius:0;"></div>
```

### Graffiti Ghost Word (every slide — MANDATORY)
Large, rotated, very low-opacity word in background:
```html
<div style="position:absolute; font-family:'Avenir Next','Nunito',sans-serif; font-size:160px; font-weight:900; color:#4A9FE0; opacity:0.06; z-index:0; transform:rotate(-8deg); top:20px; right:-20px; text-transform:uppercase; letter-spacing:-5px; pointer-events:none; white-space:nowrap;">[GHOST_WORD]</div>
```

### Blue Spray-Paint Divider (on key slides)
```html
<div style="width:80px; height:4px; background:linear-gradient(90deg, #0066CC, #4A9FE0); margin:16px 0; border-radius:2px;"></div>
```

### Slide Counter (top-right — every slide)
```html
<div style="position:absolute; top:20px; right:30px; font-family:'Avenir Next','Nunito',sans-serif; font-weight:700; font-size:13px; color:#6B8CAE; letter-spacing:1px;">[N] / 10</div>
```

### Badge / Sticker (Slides 1, 2, 8)
```html
<div style="display:inline-block; background:#0066CC; color:#FFFFFF; font-family:'Avenir Next','Nunito',sans-serif; font-weight:900; font-size:14px; padding:8px 18px; text-transform:uppercase; letter-spacing:3px; transform:rotate(-2deg); box-shadow:4px 4px 0px #003D7A;">[BADGE_TEXT]</div>
```

### Bottom Bar — Key Takeaway (every content slide — MANDATORY)
```html
<div style="margin-top:auto; background:#F0F7FF; border:1px solid #D0E4F7; border-left:5px solid #0066CC; padding:14px 24px; display:flex; align-items:center; justify-content:space-between;">
    <span style="font-family:'Avenir Next','Nunito',sans-serif; font-weight:800; font-size:15px; color:#0D1B2A; text-transform:uppercase; letter-spacing:1px;">[KEY TAKEAWAY]</span>
    <span style="font-family:'Avenir Next','Nunito',sans-serif; font-weight:700; font-size:12px; color:#6B8CAE;">ki-power.me</span>
</div>
```

### Stat Number (Fact slides 6 & 7)
```html
<div style="font-family:'Avenir Next','Nunito',sans-serif; font-weight:900; font-size:96px; color:#0066CC; line-height:1; letter-spacing:-3px;">[STAT]</div>
<div style="font-family:'Avenir Next','Nunito',sans-serif; font-weight:800; font-size:18px; color:#003D7A; text-transform:uppercase; letter-spacing:3px; margin-top:4px;">[STAT_LABEL]</div>
```

### Checklist Items (Summary slide 9)
```html
<div style="display:flex; align-items:flex-start; gap:14px; margin-bottom:16px;">
    <div style="width:24px; height:24px; background:#0066CC; border-radius:4px; display:flex; align-items:center; justify-content:center; flex-shrink:0; margin-top:2px;">
        <span style="color:#FFFFFF; font-weight:900; font-size:14px;">✓</span>
    </div>
    <span style="font-family:'Avenir Next','Nunito',sans-serif; font-weight:700; font-size:20px; color:#0D1B2A;">[TAKEAWAY]</span>
</div>
```

---

## Slide-by-Slide Background Rules

| Slide | Type | Background | Ghost Word Color |
|-------|------|------------|-----------------|
| 1 | TITLE | #FFFFFF | #4A9FE0 (6% opacity) |
| 2 | HOOK | #FFFFFF | #4A9FE0 (6% opacity) |
| 3 | PROBLEM | #EEF4FB | #4A9FE0 (8% opacity) |
| 4 | INSIGHT | #FFFFFF | #4A9FE0 (6% opacity) |
| 5 | SOLUTION | #EEF4FB | #4A9FE0 (8% opacity) |
| 6 | FACT 1 | #FFFFFF | #4A9FE0 (6% opacity) |
| 7 | FACT 2 | #EEF4FB | #4A9FE0 (8% opacity) |
| 8 | EXAMPLE | #FFFFFF | #4A9FE0 (6% opacity) |
| 9 | SUMMARY | #EEF4FB | #4A9FE0 (8% opacity) |
| 10 | CTA | #0066CC | #003D7A (20% opacity) |

Note: Slide 10 (CTA) is the ONLY dark slide — deep blue background with white text.

---

## CTA Slide 10 — Fixed Structure (ALWAYS IDENTICAL)

```
Background: #0066CC (Electric Blue)
Ghost Word: "ROGER" — #003D7A, 20% opacity, rotated -10deg
Top bar: white gradient (white to transparent)
Circle logo badge: white circle, "RB" in blue inside
Large white uppercase: "WANT MORE?"
Small white monospace: "KI-LITERACY FÜR DIE DACH-REGION"
White horizontal divider
Three lines with white arrow: "→ @fragroger auf LinkedIn folgen"
                               "→ www.ki-power.me besuchen"
                               "→ Carousel speichern & teilen"
Bottom: "www.ki-power.me" in white, small
Counter: "10 / 10" in light blue
```

---

## Absolute Design Rules

1. White/light background on slides 1-9; ONLY slide 10 uses blue background
2. UPPERCASE headlines in #0D1B2A (near black) on white slides
3. Graffiti ghost word + blue spray divider on every slide
4. Badge sticker on slides 1, 2, and 8 only
5. Top accent bar (blue gradient) on every slide
6. Bottom bar key takeaway on every content slide (3-9)
7. Avenir/Nunito font stack — NEVER use Montserrat or other fonts
8. Electric Blue #0066CC is the PRIMARY accent — use consistently
9. Orange #FF6B35 used ONCE per deck maximum (for the most impactful stat)
10. Slide 10 CTA is always identical — Roger's brand, ki-power.me
11. No hashtags, no emoji, no ß
12. Schweizer Rechtschreibung — ä ö ü always written out
13. Max 2 sentences body text per slide (except summary)
14. NEVER overflow:hidden on body, NEVER padding-bottom
