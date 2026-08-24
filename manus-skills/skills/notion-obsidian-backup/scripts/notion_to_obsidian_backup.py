#!/usr/bin/env python3
"""
Notion to Obsidian Backup Script
---------------------------------
Exports the full Notion workspace as Markdown via the unofficial Notion export API,
then unzips and places the files into a local Obsidian vault folder.

Requirements:
    pip install requests

Environment variables (set in .env or directly):
    NOTION_TOKEN_V2    - Notion token_v2 cookie value (from browser DevTools)
    NOTION_SPACE_ID    - Notion workspace/space ID (from browser URL or API)
    OBSIDIAN_VAULT_PATH - Absolute path to the Obsidian vault backup folder
    BACKUP_DIR         - Temporary download directory (default: /tmp/notion_backup)

Usage:
    python notion_to_obsidian_backup.py

How to get credentials:
    1. Open Notion in Chrome/Firefox
    2. Open DevTools → Application → Cookies → notion.so
    3. Copy the value of 'token_v2' → NOTION_TOKEN_V2
    4. Open DevTools → Network → look for any API call → find 'spaceId' in payload → NOTION_SPACE_ID
"""

import os
import time
import zipfile
import shutil
import requests
from pathlib import Path
from datetime import datetime

# --- Configuration ---
TOKEN_V2 = os.environ.get("NOTION_TOKEN_V2", "")
SPACE_ID = os.environ.get("NOTION_SPACE_ID", "")
OBSIDIAN_VAULT_PATH = os.environ.get("OBSIDIAN_VAULT_PATH", "")
BACKUP_DIR = os.environ.get("BACKUP_DIR", "/tmp/notion_backup")

NOTION_API = "https://www.notion.so/api/v3"
HEADERS = {
    "Content-Type": "application/json",
    "Cookie": f"token_v2={TOKEN_V2}",
}

def enqueue_export():
    """Request a full workspace export from Notion."""
    payload = {
        "task": {
            "eventName": "exportSpace",
            "request": {
                "spaceId": SPACE_ID,
                "exportOptions": {
                    "exportType": "markdown",
                    "timeZone": "Europe/Zurich",
                    "locale": "de",
                    "flattenExportFiletree": False,
                    "includeContents": "no_files",
                },
            },
        }
    }
    resp = requests.post(f"{NOTION_API}/enqueueTask", json=payload, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()["taskId"]


def poll_export(task_id: str, max_wait: int = 300) -> str:
    """Poll until the export task is done and return the download URL."""
    print(f"Polling export task {task_id}...")
    for _ in range(max_wait // 5):
        time.sleep(5)
        resp = requests.post(
            f"{NOTION_API}/getTasks",
            json={"taskIds": [task_id]},
            headers=HEADERS,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if not results:
            continue
        task = results[0]
        state = task.get("state")
        print(f"  State: {state}")
        if state == "success":
            return task["status"]["exportURL"]
        elif state in ("failure", "cancelled"):
            raise RuntimeError(f"Export task failed: {task}")
    raise TimeoutError("Export task timed out after waiting.")


def download_export(url: str, dest_dir: str) -> str:
    """Download the export ZIP file."""
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    zip_path = os.path.join(dest_dir, "notion_export.zip")
    print(f"Downloading export to {zip_path}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return zip_path


def unzip_to_vault(zip_path: str, vault_path: str):
    """Unzip the export and copy Markdown files to the Obsidian vault."""
    extract_dir = os.path.join(BACKUP_DIR, "extracted")
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    
    print(f"Extracting to {extract_dir}...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_dir)
    
    # Create a timestamped subfolder in the vault
    timestamp = datetime.now().strftime("%Y-%m-%d")
    dest = os.path.join(vault_path, f"Notion-Backup-{timestamp}")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    shutil.copytree(extract_dir, dest)
    print(f"Backup placed in Obsidian vault: {dest}")
    return dest


def main():
    if not TOKEN_V2 or not SPACE_ID or not OBSIDIAN_VAULT_PATH:
        print("ERROR: Missing required environment variables.")
        print("  NOTION_TOKEN_V2, NOTION_SPACE_ID, OBSIDIAN_VAULT_PATH must all be set.")
        raise SystemExit(1)
    
    print(f"[{datetime.now().isoformat()}] Starting Notion → Obsidian backup...")
    
    task_id = enqueue_export()
    print(f"Export task enqueued: {task_id}")
    
    export_url = poll_export(task_id)
    print(f"Export ready: {export_url}")
    
    zip_path = download_export(export_url, BACKUP_DIR)
    
    dest = unzip_to_vault(zip_path, OBSIDIAN_VAULT_PATH)
    
    # Cleanup temp files
    os.remove(zip_path)
    shutil.rmtree(os.path.join(BACKUP_DIR, "extracted"), ignore_errors=True)
    
    print(f"[{datetime.now().isoformat()}] Backup complete! Files at: {dest}")


if __name__ == "__main__":
    main()
