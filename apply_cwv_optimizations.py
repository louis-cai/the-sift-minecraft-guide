#!/usr/bin/env python3
"""
apply_cwv_optimizations.py - Batch in-place Core Web Vitals optimization script
Applies:
1. SVG path command syntax fix (<path d="9.09... -> <path d="M9.09...)
2. Adsterra invoke.js asynchronous non-blocking loading (async="async" data-cfasync="false")
3. Google Web Fonts asynchronous non-blocking loading (preload + media="print" onload + noscript)
"""

import os
import re
import sys

TARGET_DIR = "/home/louis/candi-tasks/thesiftguide"
HTML_FILES = [
    "index.html",
    "portal.html",
    "mobs.html",
    "about.html",
    "privacy.html",
    "dungeons-2.html",
]

OLD_FONT_SNIPPET = (
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">'
)

NEW_FONT_SNIPPET = (
    '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap">\n'
    '    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media=\'all\'">\n'
    '    <noscript><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet"></noscript>'
)

OLD_SVG_PATTERN = r'<path d="9\.09 9a3 3 0 0 1 5\.83 1c0 2-3 3-3 3"'
NEW_SVG_SNIPPET = r'<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"'

# Regex for invoke.js without async
# Match <script src="https://www.highrevenueformat.com/.../invoke.js"></script>
INVOKE_REGEX = re.compile(
    r'<script\s+src="(https://(?:www\.highrevenueformat\.com|invitationprecedingbreeches\.com|pl31607144\.profitableratecpmnetwork\.com)/[^"]+/invoke\.js)">\s*</script>'
)


def optimize_file(filename: str):
    filepath = os.path.join(TARGET_DIR, filename)
    if not os.path.isfile(filepath):
        print(f"Error: {filepath} does not exist", file=sys.stderr)
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    changes = []

    # 1. SVG fix
    if re.search(OLD_SVG_PATTERN, content):
        content, count = re.subn(OLD_SVG_PATTERN, NEW_SVG_SNIPPET, content)
        changes.append(f"Fixed {count} SVG path command(s)")

    # 2. Fonts async
    if OLD_FONT_SNIPPET in content:
        content = content.replace(OLD_FONT_SNIPPET, NEW_FONT_SNIPPET)
        changes.append("Optimized Google Web Fonts to async non-blocking preload")
    elif 'onload="this.media=\'all\'"' in content:
        changes.append("Google Web Fonts already optimized")
    else:
        print(f"Warning: Old font snippet not found in {filename}", file=sys.stderr)

    # 3. Adsterra invoke.js async
    matches = INVOKE_REGEX.findall(content)
    if matches:
        def replace_invoke(match):
            src_url = match.group(1)
            return f'<script async="async" data-cfasync="false" src="{src_url}"></script>'

        content, count = INVOKE_REGEX.subn(replace_invoke, content)
        changes.append(f"Made {count} invoke.js script(s) async non-blocking")

    # Safety checks
    # Red lines: GA4 intact, Ad keys intact if they were present originally
    if "G-X1ZTW8XWPG" in original_content and "G-X1ZTW8XWPG" not in content:
        raise ValueError(f"Red Line Breached: GA4 tracking code removed from {filename}!")
    
    for key in ["e34c08305944ef076210b30b1897f6eb", "93a1b6fb1cf3809a6ddd2ccae9364526"]:
        if key in original_content and key not in content:
            raise ValueError(f"Red Line Breached: Ad key {key} removed from {filename}!")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✔ {filename}: Updated")
        for ch in changes:
            print(f"    ↳ {ch}")
    else:
        print(f"- {filename}: No changes needed (already up to date)")

    return True


def main():
    print(f"=== Applying CWV & Performance Optimizations to {len(HTML_FILES)} HTML Pages ===")
    print(f"Target Directory: {TARGET_DIR}")
    for fname in HTML_FILES:
        optimize_file(fname)

    print("\n=== Verification ===")
    all_ok = True
    for fname in HTML_FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        # Check font optimization
        if 'onload="this.media=\'all\'"' not in text or 'rel="preload" as="style"' not in text:
            print(f"✘ {fname}: Fonts not properly optimized!")
            all_ok = False

        # Check synchronous invoke.js
        sync_invokes = INVOKE_REGEX.findall(text)
        if sync_invokes:
            print(f"✘ {fname}: Found {len(sync_invokes)} synchronous invoke.js script(s)!")
            all_ok = False

        # Check SVG syntax
        if re.search(OLD_SVG_PATTERN, text):
            print(f"✘ {fname}: Still contains broken SVG path command!")
            all_ok = False

        # Verify Red Lines
        if "G-X1ZTW8XWPG" not in text:
            print(f"✘ {fname}: Missing GA4 code!")
            all_ok = False

    if all_ok:
        print("✔ ALL 6 HTML pages successfully optimized & verified!")
    else:
        print("✘ Some verifications failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
