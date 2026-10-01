#!/usr/bin/env python3
import json, time, urllib.request, urllib.parse
import jwt

SERVICE_ACCOUNT_FILE = "/home/louis/.keys/sf-gsc-service-account.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

with open(SERVICE_ACCOUNT_FILE) as f:
    sa_info = json.load(f)

now = int(time.time())
payload = {
    "iss": sa_info["client_email"],
    "sub": sa_info["client_email"],
    "aud": "https://oauth2.googleapis.com/token",
    "iat": now,
    "exp": now + 3600,
    "scope": " ".join(SCOPES),
}

signed_jwt = jwt.encode(payload, sa_info["private_key"], algorithm="RS256")

token_data = urllib.parse.urlencode({
    "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "assertion": signed_jwt,
}).encode("utf-8")

req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_data)
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        access_token = res.get("access_token")
        print("Obtained Google Access Token successfully!")
except Exception as e:
    print("Token exchange failed:", e)
    exit(1)

# Now call Google Indexing API
indexing_url = "https://indexing.googleapis.com/v3/urlNotifications:publish"
body = json.dumps({
    "url": "https://thesiftguide.com/",
    "type": "URL_UPDATED"
}).encode("utf-8")

idx_req = urllib.request.Request(
    indexing_url,
    data=body,
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(idx_req) as resp:
        print("Google Indexing API Response:", resp.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTPError {e.code}: {e.read().decode()}")
except Exception as e:
    print("Indexing API error:", e)
