---
name: linkedin-slides
description: >
  Creates 10-slide LinkedIn presentations (carousels) in Roger's "White & Blue Graffiti" style.
  Use when the user asks for: "linkedin slides", "white and blue slides", "graffiti style linkedin",
  "Avenir font slides", or "create a linkedin carousel".
  Output: 10 highly engaging slides with Hook, Problem, Solution, Facts, and CTA, using Avenir font,
  exported as PPTX or images.
---

# LinkedIn Slides — White & Blue Graffiti Style

## Workflow Overview

1. **Extract Content** - Convert user input into a 10-slide structured JSON
2. **Draft Content** - Create a Markdown file with the slide content for review
3. **Generate Slides** - Use the `slides` tool to generate the presentation
4. **Export & Deliver** - Export as PPTX and provide to the user

---

## Step 1: Extract Content

Use the provided Python script to extract the core message and structure it into the 10-slide format.

```bash
python /home/ubuntu/skills/linkedin-slides/scripts/extract_linkedin_content.py \
  --input content.txt --output slides.json
```

### The 10-Slide Structure

| Slide | Type | Content |
|---|---|---|
| 1 | TITLE | Attention-grabbing title, subtitle, and badge. |
| 2 | HOOK | Counter-intuitive statement that stops the scroll. |
| 3 | PROBLEM | The real pain point the audience faces. |
| 4 | INSIGHT | Surprising root cause or reframe. |
| 5 | SOLUTION | The core solution or approach. |
| 6 | FACT 1 | Compelling statistic or data point. |
| 7 | FACT 2 | Second compelling statistic or data point. |
| 8 | EXAMPLE | Concrete real-world example or case study. |
| 9 | SUMMARY | 3 key takeaways. |
| 10 | CTA | Fixed CTA for Roger's brand (ki-power.me). |

---

## Step 2: Draft Content

Before generating the slides, create a Markdown file (`slide_content.md`) based on the extracted JSON.
Use the template at `templates/slide_content_template.md` as a guide for the format.

---

## Step 3: Generate Slides

Use the `slides` tool to generate the presentation.

**Mode:** Use `html` mode by default, or `image` mode if the user specifically requests image-based slides.

**Design System (White & Blue Graffiti):**
- **Font:** Avenir Next / Nunito (fallback)
- **Backgrounds:** Alternating Pure White (`#FFFFFF`) and Light Blue-Grey (`#EEF4FB`)
- **Primary Accent:** Electric Blue (`#0066CC`)
- **Signature Elements:**
  - Top accent bar (blue gradient) on every slide
  - Large, rotated, low-opacity "ghost word" in the background
  - Blue spray-paint divider lines
  - Bottom bar with a key takeaway on every content slide
- **CTA Slide:** Slide 10 is ALWAYS a dark blue background (`#0066CC`) with white text, promoting `@fragroger` and `ki-power.me`.

For full design specifications, read `references/design-system.md`.
For the exact HTML structure, refer to `templates/linkedin_slide_template.html`.

---

## Step 4: Export & Deliver

1. After generation, you will receive a URI: `manus-slides://{id}`
2. Export the presentation as a PPTX file:
   ```bash
   manus-export-slides manus-slides://{id} ppt
   ```
3. Upload the file to provide a download link:
   ```bash
   manus-upload-file presentation.pptx
   ```
4. Deliver the final result to the user.

---

## Quality Checklist

- [ ] Exactly 10 slides following the Hook-Problem-Solution-Facts-CTA structure.
- [ ] Avenir font stack used for all text.
- [ ] White/Light Blue alternating backgrounds (except Slide 10 which is Dark Blue).
- [ ] Graffiti ghost word and top accent bar on every slide.
- [ ] Bottom bar with key takeaway on slides 3-9.
- [ ] Schweizer Rechtschreibung (kein ß, ä ö ü ausgeschrieben).
- [ ] No hashtags, no emojis.
