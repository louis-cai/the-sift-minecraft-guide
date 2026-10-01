#!/usr/bin/env python3
"""
apply_anti_adblock.py - Precision In-Place Updater for Adsterra Anti-Adblock Domain
Target: /home/louis/candi-tasks/thesiftguide/index.html
"""

import os
import shutil
import sys

TARGET_FILE = "/home/louis/candi-tasks/thesiftguide/index.html"
BACKUP_FILE = "/home/louis/candi-tasks/thesiftguide/index.html.anti_adblock.bak"

REPLACEMENTS = [
    (
        "Top 728x90 Banner invoke.js",
        "https://www.highrevenueformat.com/e34c08305944ef076210b30b1897f6eb/invoke.js",
        "https://invitationprecedingbreeches.com/e34c08305944ef076210b30b1897f6eb/invoke.js",
    ),
    (
        "Middle Native Banner invoke.js",
        "https://pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js",
        "https://invitationprecedingbreeches.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js",
    ),
    (
        "Bottom 300x250 Banner invoke.js",
        "https://www.highrevenueformat.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js",
        "https://invitationprecedingbreeches.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js",
    ),
]

RED_LINES = [
    ("GA4 measurement ID", "G-X1ZTW8XWPG"),
    ("Top ad container key", "e34c08305944ef076210b30b1897f6eb"),
    ("Native ad container element", 'id="container-8b5c161155b921ab39efc03bbcadbaf3"'),
    ("Bottom ad container key", "93a1b6fb1cf3809a6ddd2ccae9364526"),
    ("Schema.org JSON-LD", 'application/ld+json'),
    ("Tailwind CDN", 'cdn.tailwindcss.com'),
    ("Favicon SVG", 'favicon.svg'),
    ("Favicon 32x32 PNG", 'favicon-32x32.png'),
    ("Apple Touch Icon", 'apple-touch-icon.png'),
    ("Portal Coordinate Calculator section", 'id="calculator"'),
    ("Coordinate X input", 'id="coord-x"'),
    ("Copy /tp button", 'id="btn-copy-tp"'),
]

def main():
    if not os.path.exists(TARGET_FILE):
        print(f"ERROR: Target file {TARGET_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    print(f"[1/5] Creating backup: {BACKUP_FILE} ...")
    shutil.copyfile(TARGET_FILE, BACKUP_FILE)
    orig_size = os.path.getsize(BACKUP_FILE)
    print(f"      Original file size: {orig_size} bytes")

    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print("[2/5] Checking targets and executing in-place replacement ...")
    new_content = content
    for name, old_str, new_str in REPLACEMENTS:
        count = new_content.count(old_str)
        if count != 1:
            print(f"ERROR: Expected exactly 1 occurrence of '{name}', found {count}!", file=sys.stderr)
            sys.exit(1)
        new_content = new_content.replace(old_str, new_str, 1)
        print(f"      ✔ Replaced {name}:")
        print(f"        OLD: {old_str}")
        print(f"        NEW: {new_str}")

    print("[3/5] Verifying red lines ...")
    for name, token in RED_LINES:
        if token not in new_content:
            print(f"ERROR: Red line check failed! Missing token '{token}' for '{name}'.", file=sys.stderr)
            sys.exit(1)
        print(f"      ✔ Preserved {name}")

    print("[4/5] Verifying anti-adblock replacements ...")
    anti_adblock_domain = "https://invitationprecedingbreeches.com/"
    new_domain_count = new_content.count(anti_adblock_domain)
    if new_domain_count != 3:
        print(f"ERROR: Expected 3 occurrences of '{anti_adblock_domain}', found {new_domain_count}!", file=sys.stderr)
        sys.exit(1)
    print(f"      ✔ Verified 3 Anti-Adblock invoke.js instances on {anti_adblock_domain}")

    print("[5/5] Writing updated content to file ...")
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    new_size = os.path.getsize(TARGET_FILE)
    print(f"      Updated file size: {new_size} bytes (diff: {new_size - orig_size:+d} bytes)")
    print("SUCCESS: In-place update complete and verified.")

if __name__ == "__main__":
    main()
