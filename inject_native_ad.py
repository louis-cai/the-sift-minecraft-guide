#!/usr/bin/env python3
"""
inject_native_ad.py
Safely injects the Adsterra Native Banner container into /home/louis/candi-tasks/thesiftguide/index.html
between Section 2 (biomes) and Section 3 (How to Play Early).
Enforces protection of all baseline red-line assets.
"""

import os
import re
import shutil
import sys

TARGET_HTML = "/home/louis/candi-tasks/thesiftguide/index.html"
BACKUP_HTML = "/home/louis/candi-tasks/thesiftguide/index.html.native_ad.bak"

NATIVE_AD_SNIPPET = """        <!-- Sponsored Native Recommendation (Adsterra Native Banner) -->
        <div class="my-10 mx-auto w-full max-w-[728px] px-2 flex flex-col items-center" id="native-ad-placement">
          <div class="text-[9px] uppercase tracking-wider text-slate-600 mb-1 flex items-center gap-1 font-mono select-none">
            <span>Advertisement</span>
          </div>
          <div class="w-full flex justify-center items-center overflow-x-auto min-h-[160px] bg-transparent">
            <script async="async" data-cfasync="false" src="https://pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js"></script>
            <div id="container-8b5c161155b921ab39efc03bbcadbaf3" class="w-full"></div>
          </div>
        </div>
"""

RED_LINE_ASSERTIONS = [
    ("Top 728x90 Adsterra key", "e34c08305944ef076210b30b1897f6eb"),
    ("Bottom 300x250 Adsterra key", "93a1b6fb1cf3809a6ddd2ccae9364526"),
    ("GA4 measurement ID", "G-X1ZTW8XWPG"),
    ("Schema.org JSON-LD tag", '<script type="application/ld+json">'),
    ("Tailwind 3.4.17 CDN", "cdn.tailwindcss.com/3.4.17"),
    ("Calculator section container", 'id="calculator"'),
]


def main():
    if not os.path.exists(TARGET_HTML):
        print(f"Error: {TARGET_HTML} does not exist", file=sys.stderr)
        sys.exit(1)

    with open(TARGET_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    # Pre-check red-line assets
    print("Verifying baseline red-line assets before injection...")
    for label, pattern in RED_LINE_ASSERTIONS:
        if pattern not in content:
            print(f"FAILED pre-check: {label} missing in {TARGET_HTML}", file=sys.stderr)
            sys.exit(1)
        print(f"  ✔ [PRE-CHECK PASS] {label}")

    # Check if native ad already injected
    if "native-ad-placement" in content or "container-8b5c161155b921ab39efc03bbcadbaf3" in content:
        print("Notice: native-ad-placement already exists in index.html. Skipping duplicate injection.")
        return

    # Locate Section 2 biomes closing and Section 3 start
    # Pattern: Section 2 ends with </section> followed by optional whitespace/newlines, then <!-- Section 3: How to Play Early -->
    pattern = r"(</section>\s*\n\s*)(<!-- Section 3: How to Play Early -->)"
    match = re.search(pattern, content)
    if not match:
        print("Error: Could not locate Section 2 biomes closing and Section 3 marker.", file=sys.stderr)
        sys.exit(1)

    # Backup original file
    shutil.copyfile(TARGET_HTML, BACKUP_HTML)
    print(f"Created backup at {BACKUP_HTML}")

    # Injection replacement
    replacement = f"\\1\n{NATIVE_AD_SNIPPET}\n        \\2"
    new_content, count = re.subn(pattern, replacement, content, count=1)
    if count != 1:
        print(f"Error: Expected 1 replacement, got {count}", file=sys.stderr)
        sys.exit(1)

    # Post-check red-line assets & new injection
    print("\nVerifying red-line assets and new Native Banner post-injection...")
    for label, pat in RED_LINE_ASSERTIONS:
        if pat not in new_content:
            print(f"FAILED post-check: {label} was damaged during injection!", file=sys.stderr)
            sys.exit(1)
        print(f"  ✔ [POST-CHECK PASS] {label}")

    NEW_ASSERTS = [
        ("Native Banner placement container id", 'id="native-ad-placement"'),
        ("Native Banner invoke.js script", "https://pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js"),
        ("Native Banner container div", 'id="container-8b5c161155b921ab39efc03bbcadbaf3"'),
    ]
    for label, pat in NEW_ASSERTS:
        if pat not in new_content:
            print(f"FAILED post-check: New asset {label} not found!", file=sys.stderr)
            sys.exit(1)
        print(f"  ✔ [POST-CHECK PASS] {label}")

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSUCCESS: Safely injected Native Banner into {TARGET_HTML} ({len(content)} -> {len(new_content)} bytes).")


if __name__ == "__main__":
    main()
