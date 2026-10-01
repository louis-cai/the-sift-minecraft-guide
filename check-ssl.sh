#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

# Check SSL setting
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings/ssl" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('SSL setting:', data.get('result', {}).get('value'))
"

# Set SSL setting to "full" (Pages supports full SSL)
curl -s -X PATCH "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/settings/ssl" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"value":"full"}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Update SSL to full:', data.get('success'), data.get('result', {}).get('value'))
"
