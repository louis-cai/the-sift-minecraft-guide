#!/usr/bin/env bash
set -euo pipefail
ENV_FILE="$HOME/.keys/.env.saas-factory"
token=$(grep '^CLOUDFLARE_API_TOKEN=' "$ENV_FILE" | cut -d= -f2-)
ZONE_ID="24fcd449cca6f0f3b38e4c9ff861a3a1"

curl -s -X GET "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records" \
  -H "Authorization: Bearer ${token}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print('Success:', data.get('success'))
print('Errors:', data.get('errors'))
records = data.get('result', [])
print(f'Total records: {len(records)}')
for r in records:
    print(r.get('id'), r.get('type'), r.get('name'), '->', r.get('content'), 'proxied:', r.get('proxied'))
"
