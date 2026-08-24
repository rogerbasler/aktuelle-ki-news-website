#!/usr/bin/env bash
# Synchronisiert lokale Manus-Skills in dieses Repository. Erst danach werden Änderungen geprüft und versioniert.
set -euo pipefail

SOURCE_DIR="${1:-/home/ubuntu/skills}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET_DIR="${EXPORT_ROOT}/skills"
CATALOG_DIR="${EXPORT_ROOT}/catalog"
GITHUB_URL="${2:-https://github.com/rogerbasler/aktuelle-ki-news-website}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  printf 'Quellverzeichnis nicht gefunden: %s\n' "${SOURCE_DIR}" >&2
  exit 2
fi

if ! find "${SOURCE_DIR}" -mindepth 2 -maxdepth 2 -type f -name SKILL.md -print -quit | grep -q .; then
  printf 'Keine SKILL.md-Dateien in %s gefunden.\n' "${SOURCE_DIR}" >&2
  exit 2
fi

STAGING_DIR="${TARGET_DIR}.staging.$$"
cleanup() {
  rm -rf "${STAGING_DIR}"
}
trap cleanup EXIT

mkdir -p "${CATALOG_DIR}"
rm -rf "${STAGING_DIR}"
mkdir -p "${STAGING_DIR}"
cp -a "${SOURCE_DIR}/." "${STAGING_DIR}/"

rm -rf "${TARGET_DIR}"
mv "${STAGING_DIR}" "${TARGET_DIR}"
trap - EXIT

python3 "${SCRIPT_DIR}/build_manifest.py" "${TARGET_DIR}" "${CATALOG_DIR}" "${GITHUB_URL}"
printf '\nAktualisierung abgeschlossen. Nächster Schritt: git diff --stat und git status prüfen, dann bewusst committen.\n'
