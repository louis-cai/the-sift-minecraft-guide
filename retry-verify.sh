#!/usr/bin/env bash
set -euo pipefail
TOKEN_FILE="$HOME/.keys/.cloudflare_token"
export CLOUDFLARE_API_TOKEN="$(cat "$TOKEN_FILE")"
ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"

# Retry verification on thesiftguide.com
res1=$(curl -s -X PATCH "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/pages/projects/thesiftguide/domains/thesiftguide.com" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}")
echo "Retry thesiftguide.com:"
echo "$res1" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('success'), d.get('result', {}).get('status'), d.get('errors'))"

# Retry verification on www.thesiftguide.com
res2=$(curl -s -X PATCH "https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/pages/projects/thesiftguide/domains/www.thesiftguide.com" \
  -H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}")
echo "Retry www.thesiftguide.com:"
echo "$res2" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('success'), d.get('result', {}).get('status'), d.get('errors'))"
