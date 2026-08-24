---
name: blog-to-heygen-vertical-video
description: "Wandelt Blog-Artikel oder Texte in fertige vertikale (Hochformat) HeyGen-Videos mit dem Avatar Kailyn um. Verwende diesen Skill immer wenn der Nutzer: HeyGen Video, Kailyn Video, vertikales Video aus Blog, Blog zu Video, Video mit Kailyn sagt. Output: Ein generiertes HeyGen-Video im Hochformat (9:16) mit Kailyn als Sprecherin, basierend auf einem Skript, das aus dem Blog-Artikel erstellt wurde."
---

# Blog to HeyGen Vertical Video (Kailyn)

Dieser Skill automatisiert den Prozess, einen Blog-Artikel oder Text in ein vertikales (Hochformat) Video mit dem HeyGen Avatar "Kailyn" umzuwandeln.

## Workflow

Befolge diese Schritte exakt in der angegebenen Reihenfolge:

### 1. Skript-Erstellung (Content Repurposing)
- Lies den vom Nutzer bereitgestellten Blog-Artikel oder Text.
- Erstelle ein kurzes, knackiges Skript (max. 60-90 Sekunden Sprechzeit, ca. 150-200 Wörter).
- **Ton & Haltung:** Sassy, charmant, witzig, aber professionell und auf den Punkt. Kailyn ist Rogers KI-Assistentin und kennt sich bestens mit seiner Agentur und KI-Themen aus.
- **Struktur:**
  - **Hook:** Ein starker Einstieg, der sofort Aufmerksamkeit erregt.
  - **Kernbotschaft:** Die wichtigsten 1-2 Punkte aus dem Blog-Artikel.
  - **Call to Action (CTA):** Ein klarer Aufruf am Ende (z.B. "Lies den ganzen Artikel auf dem Blog" oder "Folge Roger für mehr Insights").
- **Sprache:** Deutsch (Schweizer Tastatur: ä, ö, ü verwenden, keine "ß"). Keine em-Dashes (—) verwenden.

### 2. Skript-Review
- Präsentiere dem Nutzer das erstellte Skript zur Freigabe.
- **WICHTIG:** Generiere das Video erst, wenn der Nutzer das Skript ausdrücklich freigegeben hat.

### 3. Video-Generierung via HeyGen MCP
Sobald das Skript freigegeben ist, nutze das HeyGen MCP, um das Video zu generieren.

**Avatar-Details für Kailyn:**
- **Avatar ID (Look):** `d1cebf397b6a4b8691b8db668bb5c0f7` (Desk-Dwelling Professional 1, Portrait-Format)
- **Voice ID:** `6c0a95599317428a8151293305deceba` (Kailyns Default Voice)

**Tool-Aufruf:**
Verwende das Tool `create_video_from_avatar` über das HeyGen MCP.

```bash
manus-mcp-cli tool call create_video_from_avatar --server heygen --input '{
  "avatarId": "d1cebf397b6a4b8691b8db668bb5c0f7",
  "script": "HIER_DAS_FREIGEGEBENE_SKRIPT_EINfüGEN",
  "voiceId": "6c0a95599317428a8151293305deceba",
  "aspectRatio": "9:16",
  "title": "Kailyn Blog Video"
}'
```

### 4. Video-Status prüfen
- Der `create_video_from_avatar` Aufruf gibt eine `video_id` zurück.
- Das Video muss gerendert werden. Dies dauert einige Minuten.
- Nutze das Tool `get_video` über das HeyGen MCP, um den Status zu prüfen, bis der Status `completed` ist.

```bash
manus-mcp-cli tool call get_video --server heygen --input '{"videoId": "DIE_VIDEO_ID"}'
```

### 5. Auslieferung
- Sobald das Video fertig ist (`status: "completed"`), extrahiere die `video_url` aus der Antwort.
- Sende dem Nutzer eine Nachricht mit dem Link zum fertigen Video.

## Best Practices
- **Kailyns Charakter:** Kailyn ist nicht nur eine Vorleserin, sie ist eine Persönlichkeit. Lass sie ruhig mal einen frechen oder cleveren Kommentar einbauen, der zu Rogers Stil passt.
- **Hochformat:** Achte darauf, dass `aspectRatio` auf `9:16` gesetzt ist, da das Video für Plattformen wie Instagram Reels, TikTok oder YouTube Shorts gedacht ist.
- **Fehlerbehebung:** Falls die Generierung fehlschlägt, prüfe die Fehlermeldung im HeyGen MCP und informiere den Nutzer transparent.
