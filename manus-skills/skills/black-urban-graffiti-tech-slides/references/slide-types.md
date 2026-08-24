# Slide Type HTML Templates

Ready-to-use HTML patterns for the Black Urban Graffiti Tech style. All assume the standard Google Fonts import and `.slide-container` base CSS.

---

## 1. Title Slide (with hero image overlay)

```html
<div class="slide-container" style="position:relative; background-image:url('/path/to/hero.png'); background-size:cover; background-position:center;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:linear-gradient(to right, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 55%, rgba(0,0,0,0) 100%);"></div>
    <div style="position:absolute; top:50%; left:80px; transform:translateY(-50%); max-width:720px; z-index:2;">
        <h1 style="font-family:'Montserrat',sans-serif; font-size:84px; font-weight:900; text-transform:uppercase; color:#FFFFFF; text-shadow:0 0 20px rgba(0,212,255,0.6); margin-bottom:10px;">MAIN TITLE<br><span style="color:#00D4FF;">SUBTITLE</span></h1>
        <h2 style="font-family:'Montserrat',sans-serif; font-size:48px; font-weight:700; color:#FF006E; margin-bottom:25px; letter-spacing:4px;">BRAND NAME</h2>
        <p style="font-size:26px; color:#E0E0E0; border-left:5px solid #ADFF2F; padding-left:20px; margin-bottom:14px;">Tagline here</p>
        <p style="font-size:20px; font-weight:700; color:#ADFF2F; padding-left:25px; text-transform:uppercase; letter-spacing:2px;">Sub-tagline</p>
    </div>
    <!-- Badge bottom-right -->
    <div style="position:absolute; bottom:40px; right:40px; background:rgba(0,0,0,0.85); border:2px solid #ADFF2F; padding:14px 28px; font-family:'Montserrat',sans-serif; font-weight:700; font-size:16px; color:#ADFF2F; text-transform:uppercase; letter-spacing:1px; box-shadow:5px 5px 0px #FF006E; text-align:center; line-height:1.6;">
        44 Slides · 11 Kapitel<br><span style="font-size:22px; color:#FF006E;">∞</span> Möglichkeiten
    </div>
</div>
```

---

## 2. Chapter Divider Slide

```html
<div class="slide-container" style="justify-content:center; align-items:flex-start;">
    <!-- Large chapter number background -->
    <div style="position:absolute; font-family:'Montserrat',sans-serif; font-size:300px; font-weight:900; color:#0A0A0A; line-height:1; top:-30px; right:60px; z-index:0;">03</div>
    <div style="z-index:1; margin-top:auto; margin-bottom:auto;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:14px; color:#FF006E; text-transform:uppercase; letter-spacing:4px; margin-bottom:20px;">Kapitel 03</div>
        <h1 style="font-family:'Montserrat',sans-serif; font-size:72px; font-weight:900; text-transform:uppercase; color:#FFFFFF; line-height:1.1; margin-bottom:20px;">CHAPTER<br><span style="color:#FF006E;">TITLE</span></h1>
        <p style="font-size:22px; color:#888; max-width:600px;">Brief description of what this chapter covers.</p>
    </div>
    <div style="margin-top:auto; background:#050505; border:1px solid #1A1A1A; border-left:5px solid #FF006E; padding:14px 25px;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:700; color:#FF006E; text-transform:uppercase; font-size:15px;">What you'll learn in this chapter</span>
    </div>
</div>
```

---

## 3. Problem / Pain Slide

```html
<div class="slide-container" style="background:#000000;">
    <!-- Decorative background text -->
    <div style="position:absolute; font-family:'Montserrat',sans-serif; font-size:120px; font-weight:900; color:rgba(255,51,51,0.06); top:50px; right:80px; z-index:0;">?!</div>

    <div style="display:flex; align-items:baseline; justify-content:space-between; margin-bottom:35px;">
        <h1 style="font-family:'Montserrat',sans-serif; font-size:52px; font-weight:900; text-transform:uppercase; color:#FFFFFF; text-shadow:0 0 20px rgba(255,51,51,0.4);">Kennst du das?</h1>
        <span style="font-family:'JetBrains Mono',monospace; font-size:16px; color:#555; text-transform:uppercase; letter-spacing:3px;">Das Dilemma</span>
    </div>

    <!-- 3x2 Problem Grid -->
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; flex-grow:1; margin-bottom:22px;">
        <!-- Repeat for each problem card -->
        <div style="background:#050505; border:1px solid #1A1A1A; border-top:3px solid rgba(255,51,51,0.6); padding:20px 22px; transform:rotate(-0.4deg);">
            <span style="font-size:28px; display:block; margin-bottom:10px;">⏰</span>
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:17px; color:#FFFFFF; text-transform:uppercase; margin-bottom:6px;">Problem Title</div>
            <div style="font-size:13px; color:#777; line-height:1.4;">Problem description here.</div>
        </div>
        <!-- ... repeat 5 more cards -->
    </div>

    <!-- Hook bar -->
    <div style="background:linear-gradient(90deg,rgba(255,51,51,0.15) 0%,rgba(255,51,51,0.05) 100%); border:1px solid rgba(255,51,51,0.3); border-left:5px solid #FF3333; padding:14px 25px; display:flex; align-items:center; justify-content:space-between;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:18px; color:#FFFFFF;">What if you had a <span style="color:#FF3333;">24/7 assistant</span> that never sleeps?</span>
        <span style="font-size:24px; color:#FF3333; font-weight:900;">→</span>
    </div>
</div>
```

---

## 4. Before / After Comparison Slide

```html
<div class="slide-container">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:38px; font-weight:900; text-transform:uppercase; margin-bottom:30px; color:#FFFFFF;">The Turning Point — <span style="color:#ADFF2F;">Your New Reality</span></h1>

    <div style="display:grid; grid-template-columns:1fr 80px 1fr; flex-grow:1; margin-bottom:22px;">
        <!-- LEFT: Before -->
        <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:20px; text-transform:uppercase; letter-spacing:3px; color:#555; border-bottom:2px solid #1A1A1A; padding-bottom:12px; margin-bottom:14px;">❌ Before</div>
            <!-- Rows -->
        </div>
        <!-- CENTER: Divider -->
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <div style="width:2px; flex-grow:1; background:linear-gradient(to bottom,#1A1A1A 0%,#ADFF2F 50%,#1A1A1A 100%);"></div>
            <div style="font-size:32px; color:#ADFF2F; text-shadow:0 0 15px rgba(173,255,47,0.8); flex-shrink:0; margin:8px 0;">⚡</div>
            <div style="width:2px; flex-grow:1; background:linear-gradient(to bottom,#ADFF2F 0%,#1A1A1A 100%);"></div>
        </div>
        <!-- RIGHT: After -->
        <div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:20px; text-transform:uppercase; letter-spacing:3px; color:#ADFF2F; border-bottom:2px solid #ADFF2F; padding-bottom:12px; margin-bottom:14px; text-align:right; text-shadow:0 0 10px rgba(173,255,47,0.4);">✅ After</div>
            <!-- Rows -->
        </div>
    </div>

    <div style="background:linear-gradient(90deg,rgba(0,212,255,0.08) 0%,rgba(173,255,47,0.08) 100%); border:1px solid rgba(173,255,47,0.4); padding:16px 30px; text-align:center;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:22px; color:#FFFFFF; text-transform:uppercase;">AI doesn't replace you — <span style="color:#ADFF2F;">AI makes you unstoppable.</span></span>
    </div>
</div>
```

---

## 5. Feature Card Grid (2x2)

```html
<div class="slide-container">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:36px; font-weight:900; text-transform:uppercase; margin-bottom:30px; color:#FFFFFF;">Feature Overview — <span style="color:#ADFF2F;">4 Key Capabilities</span></h1>

    <div style="display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:20px; flex-grow:1; margin-bottom:20px;">
        <!-- Card: Blue -->
        <div style="background:rgba(255,255,255,0.03); border:1px solid #1A1A1A; border-top:4px solid #00D4FF; padding:22px 25px; display:flex; flex-direction:column;">
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:20px; color:#00D4FF; text-transform:uppercase; margin-bottom:6px;">Feature Name</div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:32px; color:#00D4FF; text-transform:uppercase; margin-bottom:8px; line-height:1;">BIG LABEL</div>
            <div style="font-size:14px; color:#AAAAAA; margin-bottom:14px; line-height:1.4;">Feature description in 1-2 sentences.</div>
            <div style="display:flex; flex-direction:column; gap:6px; margin-top:auto;">
                <div style="display:flex; align-items:center; gap:10px; font-size:14px; color:#E0E0E0;"><span style="width:6px; height:6px; border-radius:50%; background:#00D4FF; flex-shrink:0;"></span>Capability 1</div>
                <div style="display:flex; align-items:center; gap:10px; font-size:14px; color:#E0E0E0;"><span style="width:6px; height:6px; border-radius:50%; background:#00D4FF; flex-shrink:0;"></span>Capability 2</div>
            </div>
        </div>
        <!-- Repeat with #FF006E, #ADFF2F, #FF9F1C -->
    </div>

    <div style="background:#050505; border:1px solid #1A1A1A; padding:14px 25px; display:flex; align-items:center; justify-content:space-between;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:16px; color:#FFFFFF; text-transform:uppercase;">Key insight: <span style="color:#ADFF2F;">Set up once — always available.</span></span>
        <span style="font-family:'JetBrains Mono',monospace; font-size:13px; color:#666;">No more copy-paste</span>
    </div>
</div>
```

---

## 6. Three-Phase Journey / Timeline Slide

```html
<div class="slide-container">
    <h1 style="font-family:'Montserrat',sans-serif; font-size:36px; font-weight:900; text-transform:uppercase; margin-bottom:28px; color:#FFFFFF;">Your <span style="color:#ADFF2F;">90-Day Transformation</span></h1>

    <!-- Timeline bar -->
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:4px; margin-bottom:20px; height:36px;">
        <div style="background:rgba(0,212,255,0.25); border:1px solid rgba(0,212,255,0.5); display:flex; align-items:center; justify-content:center; font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:700; color:#00D4FF; text-transform:uppercase; letter-spacing:2px;">Days 1–30 · Foundation</div>
        <div style="background:rgba(255,0,110,0.25); border:1px solid rgba(255,0,110,0.5); display:flex; align-items:center; justify-content:center; font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:700; color:#FF006E; text-transform:uppercase; letter-spacing:2px;">Days 31–60 · Build</div>
        <div style="background:rgba(173,255,47,0.25); border:1px solid rgba(173,255,47,0.5); display:flex; align-items:center; justify-content:center; font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:700; color:#ADFF2F; text-transform:uppercase; letter-spacing:2px;">Days 61–90 · Scale</div>
    </div>

    <!-- Phase columns -->
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; flex-grow:1; margin-bottom:20px;">
        <!-- Phase 1: Blue -->
        <div style="background:rgba(255,255,255,0.02); border:1px solid #1A1A1A; border-top:4px solid #00D4FF; padding:20px 22px; display:flex; flex-direction:column;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00D4FF; text-transform:uppercase; letter-spacing:2px; margin-bottom:4px;">Phase 01</div>
            <div style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:26px; color:#00D4FF; text-transform:uppercase; margin-bottom:16px; line-height:1;">Foundation</div>
            <!-- Milestones -->
            <div style="display:flex; flex-direction:column; gap:9px; flex-grow:1; margin-bottom:16px;">
                <div style="display:flex; align-items:flex-start; gap:10px; font-size:14px; color:#CCCCCC; line-height:1.3;"><span style="width:7px; height:7px; border-radius:50%; background:#00D4FF; flex-shrink:0; margin-top:5px;"></span>Milestone 1</div>
            </div>
            <!-- Result -->
            <div>
                <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#555; text-transform:uppercase; letter-spacing:2px; margin-bottom:4px;">Result</div>
                <div style="background:rgba(0,212,255,0.08); border:1px solid rgba(0,212,255,0.3); padding:10px 14px; font-family:'Montserrat',sans-serif; font-weight:700; font-size:13px; color:#00D4FF; text-transform:uppercase; letter-spacing:1px;">Your stack is live</div>
            </div>
        </div>
        <!-- Repeat for Phase 2 (#FF006E) and Phase 3 (#ADFF2F) -->
    </div>

    <div style="background:#050505; border:1px solid #1A1A1A; padding:14px 30px; text-align:center;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:900; font-size:19px; color:#FFFFFF; text-transform:uppercase; letter-spacing:1px;">Day 90: You're not just a solopreneur — <span style="color:#ADFF2F;">you're an AI solopreneur.</span></span>
    </div>
</div>
```

---

## 7. Tool Stack / Anatomy Slide

```html
<div class="slide-container">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:30px;">
        <h1 style="font-family:'Montserrat',sans-serif; font-size:36px; font-weight:900; text-transform:uppercase; color:#FFFFFF; border-left:8px solid #FF9F1C; padding-left:20px;">Tool Name — <span style="color:#FF9F1C;">Anatomy</span></h1>
        <div style="background:rgba(255,159,28,0.1); border:1px solid #FF9F1C; padding:8px 16px; font-family:'JetBrains Mono',monospace; font-size:14px; color:#FF9F1C; text-transform:uppercase; letter-spacing:2px;">🇪🇺 GDPR-Compliant</div>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:40px; flex-grow:1; margin-bottom:20px;">
        <!-- LEFT: Stack layers -->
        <div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#666; text-transform:uppercase; letter-spacing:2px; margin-bottom:14px;">Anatomy of the Tool</div>
            <!-- Layer items — stack vertically, each touching (no gap, border-bottom:none except last) -->
            <div style="background:rgba(255,159,28,0.15); border:1px solid #FF9F1C; padding:12px 16px; display:flex; align-items:center; gap:14px;">
                <span style="font-size:20px;">🧠</span>
                <div style="flex-grow:1;">
                    <div style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:15px; color:#FFFFFF;">Core Model</div>
                    <div style="font-size:12px; color:#888; margin-top:2px;">The AI engine</div>
                </div>
                <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#FF9F1C; text-transform:uppercase;">CORE</div>
            </div>
            <!-- More layers with decreasing opacity -->
        </div>
        <!-- RIGHT: Use cases + quick steps -->
        <div style="display:flex; flex-direction:column; gap:20px;">
            <div>
                <div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#666; text-transform:uppercase; letter-spacing:2px; margin-bottom:14px;">Use Cases</div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                    <div style="background:rgba(255,255,255,0.03); border:1px solid #1A1A1A; padding:16px;">
                        <div style="font-size:20px; margin-bottom:6px;">✍️</div>
                        <div style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:14px; color:#FFFFFF; margin-bottom:4px;">Use Case</div>
                        <div style="font-size:12px; color:#888; line-height:1.3;">Description</div>
                    </div>
                </div>
            </div>
            <div style="background:#050505; border:1px solid #1A1A1A; padding:16px 18px;">
                <div style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:14px; color:#FF9F1C; text-transform:uppercase; margin-bottom:12px; letter-spacing:1px;">Build in 5 Minutes</div>
                <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                    <div style="background:rgba(255,159,28,0.1); border:1px solid rgba(255,159,28,0.4); padding:6px 10px; font-family:'JetBrains Mono',monospace; font-size:12px; color:#FF9F1C;">1. Open tool</div>
                    <span style="color:#444; font-weight:700;">→</span>
                    <div style="background:rgba(255,159,28,0.1); border:1px solid rgba(255,159,28,0.4); padding:6px 10px; font-family:'JetBrains Mono',monospace; font-size:12px; color:#FF9F1C;">2. Configure</div>
                    <span style="color:#444; font-weight:700;">→</span>
                    <div style="background:rgba(255,159,28,0.1); border:1px solid rgba(255,159,28,0.4); padding:6px 10px; font-family:'JetBrains Mono',monospace; font-size:12px; color:#FF9F1C;">3. Test!</div>
                </div>
            </div>
        </div>
    </div>

    <div style="background:rgba(255,159,28,0.08); border:1px solid rgba(255,159,28,0.3); padding:12px 25px; display:flex; align-items:center; justify-content:space-between;">
        <span style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:15px; color:#FFFFFF;">Key message about this tool.</span>
        <span style="font-family:'JetBrains Mono',monospace; font-size:14px; color:#FF9F1C;">tool.url → Feature</span>
    </div>
</div>
```

---

## 8. Closing / Brand Slide

```html
<div class="slide-container">
    <!-- Brand header -->
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:28px; border-bottom:2px solid #1A1A1A; padding-bottom:20px;">
        <div>
            <div style="font-family:'Montserrat',sans-serif; font-size:52px; font-weight:900; text-transform:uppercase; letter-spacing:3px; background:linear-gradient(90deg,#00D4FF 0%,#FF006E 60%,#ADFF2F 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1;">Brand Name</div>
            <div style="font-family:'Montserrat',sans-serif; font-size:18px; font-weight:700; color:#AAAAAA; text-transform:uppercase; letter-spacing:4px; margin-top:6px;">Tagline — <span style="color:#ADFF2F;">Sub-tagline</span></div>
        </div>
        <div style="text-align:right;">
            <div style="font-family:'Montserrat',sans-serif; font-size:80px; font-weight:900; color:#FF006E; line-height:1; text-shadow:0 0 20px rgba(255,0,110,0.5);">∞</div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:13px; color:#555; text-transform:uppercase; letter-spacing:2px;">Possibilities</div>
        </div>
    </div>

    <!-- Chapter recap grid (2 columns) -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px 40px; flex-grow:1; align-content:start; margin-bottom:25px;">
        <!-- Chapter chip -->
        <div style="display:flex; align-items:center; gap:12px; border-bottom:1px solid #1A1A1A; padding:8px 0;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:700; color:#444; min-width:28px;">01</span>
            <span style="width:8px; height:8px; border-radius:50%; background:#00D4FF; flex-shrink:0;"></span>
            <span style="font-family:'Montserrat',sans-serif; font-weight:700; font-size:15px; color:#FFFFFF; flex-grow:1;">Chapter Name</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#666; text-align:right;">Tool · Tool</span>
        </div>
        <!-- Repeat for all chapters -->
    </div>

    <!-- CTA bar -->
    <div style="background:#050505; border:1px solid #1A1A1A; padding:16px 30px; display:flex; align-items:center; justify-content:space-between;">
        <div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#555; text-transform:uppercase; letter-spacing:2px; margin-bottom:4px;">More Info & Community</div>
            <div style="font-family:'Montserrat',sans-serif; font-size:26px; font-weight:900; color:#00D4FF; text-transform:uppercase; letter-spacing:2px; text-shadow:0 0 10px rgba(0,212,255,0.4);">your-brand.com</div>
        </div>
        <div style="text-align:right;">
            <div style="font-family:'Montserrat',sans-serif; font-size:18px; font-weight:700; color:#FFFFFF; text-transform:uppercase; letter-spacing:1px;">Not Hype — <span style="color:#FF006E;">Real Need.</span></div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:13px; color:#666; margin-top:4px;">44 Slides · 11 Chapters · ∞ Possibilities</div>
        </div>
    </div>
</div>
