# How to Obtain Notion Credentials

## NOTION_TOKEN_V2 (Browser Cookie)

1. Open [notion.so](https://www.notion.so) in Chrome or Firefox and log in.
2. Open DevTools (F12 or Cmd+Option+I).
3. Navigate to **Application** (Chrome) or **Storage** (Firefox) tab.
4. Under **Cookies** → select `https://www.notion.so`.
5. Find the cookie named `token_v2` and copy its **Value**.

> ⚠️ This token grants full access to your workspace. Treat it like a password. Never commit it to a public repository.

## NOTION_SPACE_ID (Workspace ID)

**Method 1 – from the URL:**
1. Open any page in your Notion workspace.
2. Look at the URL: `https://www.notion.so/myworkspace/Page-Title-<page-id>`
3. The workspace slug is the part after `notion.so/` and before the page title.

**Method 2 – from the API (most reliable):**
1. Open DevTools → **Network** tab.
2. Reload a Notion page.
3. Filter requests by `getSpaces` or `loadUserContent`.
4. In the response JSON, find `"space"` → the first key is your `SPACE_ID` (a UUID like `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).

## OBSIDIAN_VAULT_PATH

Set this to the absolute path of your Obsidian vault folder on your computer.

Example:
- macOS: `/Users/roger/Documents/ObsidianVault`
- Windows: `C:\Users\Roger\Documents\ObsidianVault`
- Linux: `/home/roger/ObsidianVault`

The backup script will create a subfolder `Notion-Backup-YYYY-MM-DD` inside this path.

## Setting Environment Variables

Create a `.env` file in the same directory as the script:

```dotenv
NOTION_TOKEN_V2=v03:...your_token_here...
NOTION_SPACE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
OBSIDIAN_VAULT_PATH=/Users/roger/Documents/ObsidianVault
BACKUP_DIR=/tmp/notion_backup
```

Then load it before running the script:
```bash
export $(cat .env | xargs) && python notion_to_obsidian_backup.py
```

Or use `python-dotenv` by adding `from dotenv import load_dotenv; load_dotenv()` at the top of the script.
