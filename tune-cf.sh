#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

# Force HTTPS redirect on Cloudflare edge
curl -s -X PATCH "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings/always_use_https" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"value":"on"}' | python3 -c "import sys, json; print('Always Use HTTPS:', json.load(sys.stdin).get('success'))"

# Set Automatic HTTPS Rewrites
curl -s -X PATCH "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings/automatic_https_rewrites" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"value":"on"}' | python3 -c "import sys, json; print('Automatic HTTPS Rewrites:', json.load(sys.stdin).get('success'))"
