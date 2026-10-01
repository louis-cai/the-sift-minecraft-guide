#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_pages_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
export CLOUDFLARE_ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"

# Check Pages domain status
curl -s -X GET "https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/pages/projects/thesiftguide/domains" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Pages domains:', json.dumps(data.get('result', []), indent=2))
"

# Find zone id for thesiftguide.com
curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=thesiftguide.com" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
zones = data.get('result', [])
if zones:
    print('Zone ID:', zones[0]['id'], 'Status:', zones[0]['status'])
else:
    print('No zone found or token lacks Zone read permission')
"
