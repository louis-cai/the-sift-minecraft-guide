#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

echo "=== 1. Delete Old Root A Record (192.64.119.187) ==="
curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records/9f50aedb724ac2953f3b2157b336cb87" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Delete root A record:', data.get('success'))
"

echo "=== 2. Delete Old WWW CNAME Record (parkingpage) ==="
curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records/26bb765eb4e20ae9751ac92a9c30472e" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Delete www CNAME record:', data.get('success'))
"

echo "=== 3. Add CNAME root -> thesiftguide.pages.dev ==="
curl -s -X POST "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"type":"CNAME","name":"@","content":"thesiftguide.pages.dev","ttl":1,"proxied":true}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Create root CNAME:', data.get('success'), data.get('errors'))
"

echo "=== 4. Add CNAME www -> thesiftguide.pages.dev ==="
curl -s -X POST "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"type":"CNAME","name":"www","content":"thesiftguide.pages.dev","ttl":1,"proxied":true}' | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Create www CNAME:', data.get('success'), data.get('errors'))
"
