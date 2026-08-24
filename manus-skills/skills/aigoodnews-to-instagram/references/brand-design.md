# AiGoodNews Brand Design System

## Farbpalette

| Variable | HEX | Einsatz |
|---|---|---|
| `--agn-dark` | `#0a192f` | Hintergrund (Standard) - Deep Dark Blue/Green |
| `--agn-white` | `#ffffff` | Text auf Dunkel, helle Slides |
| `--agn-green-primary` | `#00ff88` | Logo-Akzent, Trennlinien, Highlights (Neon Green) |
| `--agn-green-secondary` | `#00cc6a` | Sublines, Labels |
| `--agn-gold` | `#ffd700` | CTA-Elemente, Energie-Akzent (Neon Gold) |
| `--agn-black` | `#000000` | Dunkel-Variante als Hintergrund-Option |

Standard-Hintergrund: `#0a192f` oder `#000000` (Dark Mode first).
Gold `#ffd700` nur 1× pro Slide als Einzelakzent.

## Typografie — Avenir Bold + TEDx-Stil

**Primärschrift:** `'Avenir Next', 'Avenir', 'Barlow Condensed', sans-serif`

Avenir ist ein System-Font (macOS/iOS). Als Web-Fallback wird **Barlow Condensed 900** verwendet — optisch sehr ähnlich, extrem plakativer Charakter.

Google Fonts Import (Fallback):
```html
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800;900&family=Barlow:wght@400;600&family=JetBrains+Mono:wght@700&display=swap');
```

Font-Stack im CSS:
```css
font-family: 'Avenir Next', 'Avenir', 'Barlow Condensed', sans-serif;
```

**Grundprinzip: Schrift dominiert den Slide. Weniger Text, viel grösser. Jede Headline muss aus 2 Metern lesbar sein.**

| Schnitt | Weight | Grösse | Einsatz |
|---|---|---|---|
| Regular | 400 | 13–14px | Labels, Metainfo, Teaser |
| Regular | 400 | 17–19px | Body-Text (max. 2 Sätze) |
| SemiBold | 600 | 22–24px | Subheadlines, Callouts |
| Bold | 700 | 34–40px | Headlines (WUNDE, WARUM, WERT) |
| Black | 900 | 52–64px | Hero-Titles, Hook-Slide |

**Grössenreferenz (TEDx-Skala bei 480×600px):**
- `headline-hero`: **64px**, weight 900, UPPERCASE — Hook-Slide, max. 4–5 Wörter
- `headline-main`: **44px**, weight 800 — WUNDE/WARUM, max. 1 Zeile
- `headline-insight`: **36px**, weight 700 — WERT-Slides, max. 2 Zeilen
- `body-text`: **17px**, weight 400 (Barlow Regular) — max. 2 kurze Sätze
- `slide-label`: **12px**, weight 700, JetBrains Mono, UPPERCASE, letter-spacing 0.15em
- `slide-counter`: **11px**, weight 400

## Graffiti-Design-Elemente (IMMER einsetzen)

Das AiGoodNews Carousel verbindet **TEDx-Typografie-Dominanz** mit **Urban Graffiti Wall Ästhetik**:

### Pflicht-Elemente pro Slide

**1. Graffiti-Hintergrund-Wort** (grosses, rotiertes, low-opacity Dekowort):
```html
<div class="graffiti-bg">WORD</div>
```
```css
.graffiti-bg {
  position: absolute;
  font-family: 'Avenir Next', 'Barlow Condensed', sans-serif;
  font-size: 140px;
  font-weight: 900;
  color: #00ff88;
  opacity: 0.06;
  transform: rotate(-12deg);
  top: 60px; right: -20px;
  letter-spacing: -0.04em;
  text-transform: uppercase;
  pointer-events: none;
  user-select: none;
  line-height: 1;
}
```

**2. Neon-Glow auf Headlines** (Gold oder Green, je nach Slide):
```css
.headline-hero { text-shadow: 0 0 40px rgba(255,215,0,0.35); }
.headline-main { text-shadow: 0 0 25px rgba(0,255,136,0.3); }
```

**3. Spray-Paint-Akzentlinie** (dicker, rauer als normaler Divider):
```html
<div class="spray-line"></div>
```
```css
.spray-line {
  width: 60px; height: 4px;
  background: var(--agn-gold);
  margin: 16px 0;
  box-shadow: 0 0 12px rgba(255,215,0,0.6);
}
```

**4. Sticker-Badge** (auf Hook-Slide und AHA-Slide):
```html
<div class="sticker">GOOD NEWS</div>
```
```css
.sticker {
  display: inline-block;
  background: var(--agn-gold);
  color: #000;
  font-family: 'Avenir Next', 'Barlow Condensed', sans-serif;
  font-weight: 900;
  font-size: 13px;
  padding: 5px 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  box-shadow: 4px 4px 0px rgba(0,255,136,0.8);
  transform: rotate(-1.5deg);
}
```

**5. JetBrains Mono Label** (Slide-Label / Tag):
```css
.slide-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--agn-green-primary);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
```

**6. Deko-Nummer** (Slides 4–7, sehr gross, low-opacity):
```css
.deco-number {
  position: absolute;
  bottom: -20px; right: 10px;
  font-size: 180px;
  font-weight: 900;
  color: var(--agn-green-primary);
  opacity: 0.06;
  font-family: 'Avenir Next', 'Barlow Condensed', sans-serif;
}
```

## Layout-Prinzipien

**TEDx + Graffiti Wall:** Die Headline ist das Bild. Graffiti-Dekowörter im Hintergrund geben Tiefe. Neon-Glow auf Headlines erzeugt Energie. Sticker-Badges brechen die Rasterstruktur. Asymmetrie ist Pflicht — nie symmetrisch zentriert ausser AHA- und CTA-Slide. Body-Text ist Ergänzung, nicht Hauptinhalt — nie mehr als 2 Sätze.

## Fixe CTA-Slide (Slide 10 — IMMER IDENTISCH)

```
[AiGoodNews Logo-Emblem oben zentriert — SVG-Kreis "AGN" in #00ff88, 60px]

AiGoodNews                         [Black 900, 32px, #ffffff]
Positive KI-News für die DACH-Region [Mono 700, 13px, #00ff88]

─────────────────  [1px solid #00ff88, Breite 40%]

Du willst mehr gute News?

→  @aigoodnews auf Instagram folgen
→  aigoodnews.ai besuchen
→  Carousel speichern & teilen

─────────────────

#AiGoodNews #KI #ArtificialIntelligence
```

Design-Specs CTA-Slide:
- Hintergrund: `#0a192f`
- CTA-Zeilen: Regular 400, 14px, `#ffffff`
- Pfeile: `#ffd700`
- Hashtags: Mono 700, 11px, `#00cc6a`
