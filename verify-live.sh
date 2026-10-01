#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

echo "=== 1. Check Root Domain DNS Resolution ==="
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records?type=CNAME" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Success:', data.get('success'))
for r in data.get('result', []):
    print(r.get('type'), r.get('name'), '->', r.get('content'), '| proxied:', r.get('proxied'))
"

echo "=== 2. Check Live Response ==="
curl -sI https://thesiftguide.com | head -n 8
