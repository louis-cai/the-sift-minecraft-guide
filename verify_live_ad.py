#!/usr/bin/env python3
import urllib.request

req = urllib.request.Request('https://thesiftguide.com', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')

checks = [
    ('Anti-Adblock domain present (3 spots)', html.count('invitationprecedingbreeches.com') == 3),
    ('Top ad invoke.js with anti-adblock', 'https://invitationprecedingbreeches.com/e34c08305944ef076210b30b1897f6eb/invoke.js' in html),
    ('Native ad invoke.js with anti-adblock', 'https://invitationprecedingbreeches.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js' in html),
    ('Bottom ad invoke.js with anti-adblock', 'https://invitationprecedingbreeches.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js' in html),
    ('Native ad placement div', 'id="native-ad-placement"' in html),
    ('Native ad container', 'id="container-8b5c161155b921ab39efc03bbcadbaf3"' in html),
    ('Top ad key (Red line)', 'e34c08305944ef076210b30b1897f6eb' in html),
    ('Bottom ad key (Red line)', '93a1b6fb1cf3809a6ddd2ccae9364526' in html),
    ('GA4 key (Red line)', 'G-X1ZTW8XWPG' in html),
    ('Tailwind CDN (Red line)', 'cdn.tailwindcss.com' in html),
    ('Calculator section (Red line)', 'id="calculator"' in html),
]

print("=== Live Production Anti-Adblock Verification ===")
all_pass = True
for name, present in checks:
    status = "✔ PASS" if present else "✘ FAIL"
    print(f"[{status}] {name}")
    if not present:
        all_pass = False

print("Overall live verification:", "PASSED" if all_pass else "FAILED")
