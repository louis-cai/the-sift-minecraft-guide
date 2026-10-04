#!/usr/bin/env python3
"""
/tmp/restore_sync_ads.py - Restore Adsterra invoke.js to standard synchronous loading
Across 6 HTML files in thesiftguide:
- index.html
- portal.html
- mobs.html
- about.html
- privacy.html
- dungeons-2.html

Keeps Google Fonts async preloading and SVG path fixes untouched.
Validates red line assets: GA4 tag, Adsterra placement keys, Schema.org.
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

# Regex to match async invoke.js:
# <script async="async" data-cfasync="false" src="https://www.highrevenueformat.com/([a-f0-9]+)/invoke.js"></script>
ASYNC_INVOKE_PATTERN = re.compile(
    r'<script\s+async="async"\s+data-cfasync="false"\s+src="https://www\.highrevenueformat\.com/([a-f0-9]+)/invoke\.js">\s*</script>'
)

REQUIRED_GA4 = "G-X1ZTW8XWPG"
AD_KEYS = ["e34c08305944ef076210b30b1897f6eb", "93a1b6fb1cf3809a6ddd2ccae9364526"]
FONT_PRELOAD_MARKER = 'onload="this.media=\'all\'"'
SVG_FIX_MARKER = 'd="M9.09'


def process_file(filename: str):
    filepath = os.path.join(TARGET_DIR, filename)
    if not os.path.isfile(filepath):
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    changes = []

    # 1. Check if async invoke.js exists and replace
    matches = ASYNC_INVOKE_PATTERN.findall(content)
    if matches:
        new_content, count = ASYNC_INVOKE_PATTERN.subn(
            r'<script src="https://www.highrevenueformat.com/\1/invoke.js"></script>',
            content
        )
        content = new_content
        changes.append(f"Restored {count} invoke.js script(s) to synchronous loading")

    # 2. Red lines and integrity checks
    if REQUIRED_GA4 in original_content and REQUIRED_GA4 not in content:
        raise ValueError(f"RED LINE BREACH: GA4 tracking ID missing in {filename}!")

    for key in AD_KEYS:
        if key in original_content and key not in content:
            raise ValueError(f"RED LINE BREACH: Ad key {key} missing in {filename}!")

    # Check font preload marker
    if FONT_PRELOAD_MARKER in original_content and FONT_PRELOAD_MARKER not in content:
        raise ValueError(f"INTEGRITY ERROR: Font preloading was modified in {filename}!")

    # Check SVG fix
    if SVG_FIX_MARKER in original_content and SVG_FIX_MARKER not in content:
        raise ValueError(f"INTEGRITY ERROR: SVG path fix was modified in {filename}!")

    # Verify no async invoke.js remaining
    remaining_async = ASYNC_INVOKE_PATTERN.findall(content)
    if remaining_async:
        raise ValueError(f"ERROR: Unreplaced async invoke.js found in {filename}: {remaining_async}")

    # Write changes if modified
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✔ {filename}: Successfully updated")
        for ch in changes:
            print(f"    ↳ {ch}")
    else:
        print(f"• {filename}: No async ads found or already synchronous (verified untouched)")

    return True


def main():
    print("=" * 60)
    print("  Restoring Adsterra invoke.js to Standard Synchronous Loading")
    print(f"  Target directory: {TARGET_DIR}")
    print("=" * 60)

    success = True
    for fname in HTML_FILES:
        try:
            if not process_file(fname):
                success = False
        except Exception as e:
            print(f"✘ {fname}: {e}", file=sys.stderr)
            success = False

    if not success:
        print("\nProcess failed due to errors above.", file=sys.stderr)
        sys.exit(1)

    print("\n" + "=" * 60)
    print("  Post-Execution Verification")
    print("=" * 60)

    total_sync_ads = 0
    total_async_ads = 0

    sync_pattern = re.compile(
        r'<script\s+src="https://www\.highrevenueformat\.com/[a-f0-9]+/invoke\.js">\s*</script>'
    )

    for fname in HTML_FILES:
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        sync_matches = sync_pattern.findall(text)
        async_matches = ASYNC_INVOKE_PATTERN.findall(text)
        has_font = FONT_PRELOAD_MARKER in text
        has_svg = SVG_FIX_MARKER in text
        has_ga4 = REQUIRED_GA4 in text

        total_sync_ads += len(sync_matches)
        total_async_ads += len(async_matches)

        print(f"{fname:<16}: Sync ads={len(sync_matches)} | Async ads={len(async_matches)} | Fonts={has_font} | SVG={has_svg} | GA4={has_ga4}")

    print("-" * 60)
    print(f"Total Sync Ads: {total_sync_ads} (Expected: 6)")
    print(f"Total Async Ads: {total_async_ads} (Expected: 0)")

    if total_sync_ads != 6 or total_async_ads != 0:
        print("ERROR: Total ad counts do not match expected standard!", file=sys.stderr)
        sys.exit(1)

    print("ALL CHECKS PASSED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
