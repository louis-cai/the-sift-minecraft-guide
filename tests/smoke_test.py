#!/usr/bin/env python3
"""Standalone smoke test for thesiftguide soft-404 & security-headers fix.

Zero third-party dependencies -- pure Python standard library.
Verifiable gates:
1. _headers file exists at deployment root with the exact mandated directives.
2. 404.html exists and contains mandated title / copy / noindex meta / 4 action links.
3. Real local HTTP server: nonexistent path returns HTTP 404 (soft-404 killed) and
   serves the custom 404 page body.
4. Real local HTTP server: every response carries the 4 security headers (mirrors
   Cloudflare Pages _headers injection).
5. Git side effect: commit containing 404.html + _headers exists in git history.
Exit 0 = all gates green.
"""
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import urllib.error
import urllib.request

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REQUIRED_HEADERS = {
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}

failures = []

def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))
    if not cond:
        failures.append(name)

# ---- Gate 1: _headers file ----
headers_path = os.path.join(BASE_DIR, "_headers")
check("gate1a: _headers exists", os.path.isfile(headers_path))
content = ""
if os.path.isfile(headers_path):
    with open(headers_path, encoding="utf-8") as f:
        content = f.read()
for k, v in REQUIRED_HEADERS.items():
    check(f"gate1b: _headers has {k}: {v}", f"{k}: {v}" in content)

# ---- Gate 2: 404.html content ----
html404_path = os.path.join(BASE_DIR, "404.html")
check("gate2a: 404.html exists", os.path.isfile(html404_path))
h = ""
if os.path.isfile(html404_path):
    with open(html404_path, encoding="utf-8") as f:
        h = f.read()
check("gate2b: title", "<title>404 Page Not Found | The Sift Guide</title>" in h)
check("gate2c: noindex meta", 'content="noindex, follow"' in h)
check("gate2d: lost-in-sift copy", "404 - Lost in the Sift" in h)
check("gate2e: coordinate copy", "The coordinate you navigated to doesn't exist" in h)
for link in ['href="/"', 'href="/portal.html"', 'href="/mobs.html"', 'href="/mods.html"']:
    check(f"gate2f: action link {link}", link in h)

# ---- Gates 3+4: real server behavior reproducing Cloudflare Pages ----
class CFEmulatedHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def translate_path(self, path):
        full_path = super().translate_path(path)
        if not os.path.exists(full_path) and os.path.exists(full_path + ".html"):
            return full_path + ".html"
        return full_path

    def end_headers(self):
        if os.path.exists(headers_path):
            with open(headers_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and ":" in line and not line.startswith("/*"):
                        k, v = line.split(":", 1)
                        self.send_header(k.strip(), v.strip())
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.exists(html404_path):
            self.send_response(404, "Not Found")
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(html404_path, "rb") as f:
                self.wfile.write(f.read())
            return
        super().send_error(code, message, explain)

    def log_message(self, format, *args):
        pass

class TS(socketserver.TCPServer):
    allow_reuse_address = True

with TS(("127.0.0.1", 0), CFEmulatedHandler) as srv:
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    origin = f"http://127.0.0.1:{port}"

    # Gate 3: soft-404 killed
    try:
        with urllib.request.urlopen(f"{origin}/definitely-not-a-page-xyz", timeout=10) as r:
            body = r.read().decode("utf-8", "replace")
            check("gate3: nonexistent URL returns 404", False, f"got HTTP {r.status} (soft 404)")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        check("gate3: nonexistent URL returns 404", e.code == 404, f"got HTTP {e.code}")
    check("gate3b: 404 body is custom page", "404 - Lost in the Sift" in body)

    # Gate 4: security headers on a real 200 response
    with urllib.request.urlopen(f"{origin}/", timeout=10) as r:
        for k, v in REQUIRED_HEADERS.items():
            check(f"gate4: live header {k}", r.headers.get(k) == v, f"got {r.headers.get(k)!r}")

    srv.shutdown()

# ---- Gate 5: git side effect (durable history, real commit) ----
log = subprocess.run(
    ["git", "-C", BASE_DIR, "log", "--oneline", "-3", "--", "404.html", "_headers"],
    capture_output=True, text=True,
).stdout
check("gate5: git commit touching 404.html/_headers exists",
      "fix(seo): add 404.html and _headers" in log, log.strip().splitlines()[:1].__str__())

print()
if failures:
    print(f"SMOKE RESULT: {len(failures)} FAILED -> {failures}")
    sys.exit(1)
print("SMOKE RESULT: ALL GATES GREEN (exit 0)")
sys.exit(0)
