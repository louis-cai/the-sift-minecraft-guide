#!/usr/bin/env bash
set -euo pipefail

TOKEN_FILE="/home/louis/.keys/.cloudflare_pages_token"
if [ ! -s "$TOKEN_FILE" ]; then
    echo "ERROR: $TOKEN_FILE missing or empty" >&2
    exit 1
fi

export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
export CLOUDFLARE_ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"
PROJECT_NAME="thesiftguide"
SITE_DIR="/home/louis/candi-tasks/thesiftguide"

echo "=== Deploying $SITE_DIR to Cloudflare Pages ($PROJECT_NAME) ==="
wrangler pages deploy "$SITE_DIR" --project-name="$PROJECT_NAME" --branch=main --commit-dirty=true
