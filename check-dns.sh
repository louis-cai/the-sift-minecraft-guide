#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

echo "=== 1. Test Token on Zone DNS ==="
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Success:', data.get('success'))
print('Errors:', data.get('errors'))
records = data.get('result', [])
print(f'Existing DNS records: {len(records)}')
for r in records:
    print(r.get('id'), r.get('type'), r.get('name'), '->', r.get('content'), 'proxied:', r.get('proxied'))
"
