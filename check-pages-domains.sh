#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"

curl -s -X GET "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/pages/projects/thesiftguide/domains" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
domains = data.get('result', [])
for d in domains:
    print(d.get('name'), '| Status:', d.get('status'), '| Cert:', d.get('certificate_status'), '| Err:', d.get('verification_data', {}).get('error_message'))
"
