#!/usr/bin/env bash
set -euo pipefail

TOKEN_FILE="$HOME/.keys/.cloudflare_pages_token"
[ -s "$TOKEN_FILE" ] || { echo "ERROR: $TOKEN_FILE missing/empty" >&2; exit 1; }

export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
export CLOUDFLARE_ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"
PROJECT_NAME="thesiftguide"
SITE_DIR="/home/louis/candi-tasks/thesiftguide"

echo "=== Step 1: Create Pages Project ==="
wrangler pages project create "$PROJECT_NAME" --production-branch=main >/dev/null 2>&1 || echo "Project already exists or created"

echo "=== Step 2: Deploy Site to Pages ==="
wrangler pages deploy "$SITE_DIR" --project-name="$PROJECT_NAME" --branch=main --commit-dirty=true

echo "=== Step 3: Add Custom Domains ==="
# Add thesiftguide.com
res_root=$(curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/pages/projects/${PROJECT_NAME}/domains" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"name":"thesiftguide.com"}')

echo "$res_root" | python3 -c "
import sys, json
data = json.load(sys.stdin)
success = data.get('success')
errors = data.get('errors', [])
print('thesiftguide.com add status:', 'SUCCESS' if success else 'FAILED', errors)
"

# Add www.thesiftguide.com
res_www=$(curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/pages/projects/${PROJECT_NAME}/domains" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"name":"www.thesiftguide.com"}')

echo "$res_www" | python3 -c "
import sys, json
data = json.load(sys.stdin)
success = data.get('success')
errors = data.get('errors', [])
print('www.thesiftguide.com add status:', 'SUCCESS' if success else 'FAILED', errors)
"

echo "=== Step 4: Check Domain Status ==="
curl -s -X GET "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/pages/projects/${PROJECT_NAME}/domains" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
domains = data.get('result', [])
for d in domains:
    print(f\"Domain: {d.get('name')} | Status: {d.get('status')} | Cert: {d.get('certificate_status')}\")
"
