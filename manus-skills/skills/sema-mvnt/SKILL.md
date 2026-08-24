---
name: sema-mvnt
description: >-
  Spezialisierter Skill fuer das Pilates Studio SEMA MVNT in Mexiko. Enthaelt das vollstaendige Angebot (digitale Infrastruktur, Module, Preise), Brand-Guidelines (Farben, Typografie, Bildsprache, Logo-Pfade) und KI-Bild-Prompts. Verwende diesen Skill immer wenn der Nutzer SEMA MVNT, Sema, Pilates Mexiko Angebot, SEMA Praesentation, SEMA Bilder, SEMA Logo oder SEMA Angebot sagt oder Inhalte fuer diesen Kunden erstellt. Output: Angebots-Praesentationen, Mood-Bilder, Social Media Posts, E-Mails, Angebots-Updates im SEMA MVNT CI/CD.
---

# SEMA MVNT Skill

Skill für alle Aufgaben rund um das Pilates Studio **SEMA MVNT** in Mexiko.

## Kontext

SEMA MVNT ist ein neu gegründetes Premium-Pilates-Studio in Mexiko, das sich an Expats und internationale Kundschaft richtet. Roger Basler de Roca / Analytics Agentur ist der digitale Infrastruktur-Partner.

## Ressourcen

Vor jeder Aufgabe die relevante Referenz laden:

| Aufgabe | Referenz laden |
|---|---|
| Angebot, Preise, Module | `/home/ubuntu/skills/sema-mvnt/references/angebot.md` |
| Bilder, Design, Logo, Farben | `/home/ubuntu/skills/sema-mvnt/references/brand.md` |
| Logo (schwarz) | `/home/ubuntu/skills/sema-mvnt/templates/logo_black.png` |
| Logo (weiss) | `/home/ubuntu/skills/sema-mvnt/templates/logo_white.png` |

## Workflow: Präsentation erstellen

1. `angebot.md` und `brand.md` laden
2. Mood-Bilder generieren (Stil aus `brand.md`, Prompt-Vorlage verwenden)
3. Slides im `image`-Modus erstellen — Bebas Neue Headlines, Inter Bold Body
4. Logo einbauen: weiss auf schwarzen Hintergründen (Standard)
5. Präsentation via `slide_present` ausgeben

## Workflow: Mood-Bilder generieren

1. `brand.md` laden — Prompt-Vorlage verwenden
2. **Immer:** keine Gesichter, Hände/Schultern/Rücken im Fokus, schwarze Activewear
3. **Stil:** Dark, High-Contrast, dramatisches Licht, Orange Rim-Light von der Seite
4. Aspektverhältnis: 16:9 für Räume/Gruppen, 3:4 für Personen-Details
5. Mood-Bilder speichern unter `/home/ubuntu/sema_mvnt/mood_[name].jpg`

## Workflow: Angebot aktualisieren

1. `angebot.md` laden
2. Änderungen direkt in `angebot.md` vornehmen
3. Präsentation neu generieren oder einzelne Slides aktualisieren

## Workflow: Social Media Post

1. `brand.md` laden — Bildsprache und Zielgruppe beachten
2. Sprache: Englisch (primär), Spanisch (sekundär) oder bilingual
3. Ton: Confident, bold, direkt — kein Wellness-Geflüster, kein Fitness-Bro-Slang
4. Hashtags: #PilatesMexico #BoutiqueFitness #SEMAMVNT #MexicoCity #WellnessLifestyle

## Design-Regeln (immer einhalten)

| Element | Wert |
|---|---|
| Hintergrund | `#0A0A0A` (fast schwarz) |
| Primärakzent | `#C94B00` (Dark Orange) |
| Energie-Akzent | `#FF6B1A` (Burnt Orange) |
| Weiss | `#FFFFFF` für Headlines |
| Body-Text | `#F0EDE8` (Off-White) |
| Headline-Font | Bebas Neue, All-Caps, 60–80px |
| Body-Font | Inter Bold/Black (min. 700 Weight) |
| Akzentlinien | 3px, `#C94B00` unter Titeln |
| Bilder-Stil | High-Contrast, dramatisch, Orange Rim-Light |
| Personen | Kein Gesicht — Hände, Schultern, Rücken, Silhouetten |
| Logo | Weiss auf schwarzem Hintergrund (Standard) |

**Verboten:** Pastelltöne, weiche Rundungen, Light-Fonts, Beige/Creme als Hauptfarbe, Verläufe.

## Kontakt & Angebot

- **Anbieter:** Roger Basler de Roca | analytics-agentur.ch | fragroger.ai
- **E-Mail:** roger@analytics-agentur.ch
- **Briefing-Call:** calendly.com/rogerbasler/30-minuten
- **Gesamtpaket:** CHF 6.800 (mit 15 % Kombi-Rabatt)
- **Einstiegspaket:** CHF 4.900 (CI/CD + Module 1 + 2 + 4)
- **Angebot gültig:** 30 Tage
