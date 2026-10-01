#!/usr/bin/env python3
import urllib.request

req = urllib.request.Request('https://thesiftguide.com', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')

checks = [
    ('Native ad placement div', 'id="native-ad-placement"'),
    ('Native ad container', 'id="container-8b5c161155b921ab39efc03bbcadbaf3"'),
    ('Native ad invoke script', 'pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js'),
    ('Top ad key (Red line)', 'e34c08305944ef076210b30b1897f6eb'),
    ('Bottom ad key (Red line)', '93a1b6fb1cf3809a6ddd2ccae9364526'),
    ('GA4 key (Red line)', 'G-X1ZTW8XWPG'),
]

print("=== Live Production HTML Verification ===")
all_pass = True
for name, token in checks:
    present = token in html
    status = "✔ PASS" if present else "✘ FAIL"
    print(f"[{status}] {name}")
    if not present:
        all_pass = False

print("Overall live verification:", "PASSED" if all_pass else "FAILED")
