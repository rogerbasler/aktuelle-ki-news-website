---
name: notion-obsidian-backup
description: "Automates a weekly backup of a Notion workspace to a local Obsidian vault as Markdown files. Use when the user asks to: back up Notion to Obsidian, export Notion as Markdown, sync Notion to Obsidian, or schedule a recurring Notion backup. Handles credential setup, script execution, and scheduling via cron or Manus scheduled task."
---

# Notion → Obsidian Backup Skill

This skill exports the full Notion workspace as Markdown via the unofficial Notion export API and places the files into a local Obsidian vault folder. It is designed for regular weekly backups.

## How It Works

1. The script calls Notion's internal `enqueueTask` API to trigger a full workspace export (Markdown format).
2. It polls `getTasks` until the export is ready (typically 1–5 minutes for large workspaces).
3. It downloads the ZIP file and extracts it into a timestamped subfolder inside the Obsidian vault.
4. A scheduled Manus task or cron job runs this script every week.

## Prerequisites

- Python 3.8+ with `requests` installed (`pip install requests`)
- Notion `token_v2` cookie and `space_id` (see `references/credentials_guide.md`)
- A local Obsidian vault folder (can be any folder; Obsidian will index it)

## Setup Steps

### 1. Obtain Credentials

Read `references/credentials_guide.md` for step-by-step instructions on getting `NOTION_TOKEN_V2` and `NOTION_SPACE_ID` from the browser.

### 2. Configure Environment Variables

Create a `.env` file with:
```dotenv
NOTION_TOKEN_V2=v03:...
NOTION_SPACE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
OBSIDIAN_VAULT_PATH=/path/to/your/ObsidianVault
BACKUP_DIR=/tmp/notion_backup
```

### 3. Run the Backup Script

```bash
export $(cat .env | xargs)
python scripts/notion_to_obsidian_backup.py
```

The script creates a folder `Notion-Backup-YYYY-MM-DD` inside `OBSIDIAN_VAULT_PATH`.

### 4. Schedule Weekly Backup

**Option A – Manus Scheduled Task (recommended):**
Use the Manus `schedule` tool with a weekly cron expression:
```
cron: "0 0 7 * * 0"   # Every Sunday at 07:00
```
Prompt: "Run the Notion to Obsidian backup script at /home/ubuntu/skills/notion-obsidian-backup/scripts/notion_to_obsidian_backup.py with the configured environment variables."

**Option B – System Cron (Linux/macOS):**
```bash
# Add to crontab (crontab -e):
0 7 * * 0 cd /home/ubuntu/skills/notion-obsidian-backup && export $(cat .env | xargs) && python scripts/notion_to_obsidian_backup.py >> /tmp/notion_backup.log 2>&1
```

**Option C – GitHub Actions (for cloud-based backup):**
Use the workflow pattern from `references/credentials_guide.md` to run the backup on a GitHub-hosted runner and commit results to a private repo.

## Important Notes

- The `token_v2` cookie expires periodically (typically every 90 days). If the backup fails with a 401 error, refresh the token.
- Large workspaces (many attachments) may take 5–15 minutes to export. The script polls with a 5-minute timeout by default; increase `max_wait` in `poll_export()` if needed.
- The export does NOT include binary files (images, PDFs) by default (`includeContents: "no_files"`). Change to `"everything"` in the script if you need attachments — but this significantly increases export size and time.
- Notion's export API is unofficial and may change. If the script breaks, check for updated endpoints in the Notion community forums.

## Troubleshooting

| Error | Likely Cause | Fix |
|---|---|---|
| 401 Unauthorized | `token_v2` expired | Re-copy token from browser cookies |
| Task state "failure" | Workspace too large or API issue | Retry; check Notion status page |
| TimeoutError | Export taking too long | Increase `max_wait` parameter |
| Empty ZIP file | Space ID incorrect | Verify `NOTION_SPACE_ID` |
