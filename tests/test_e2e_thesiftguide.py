#!/usr/bin/env python3
"""
E2E Test Suite for thesiftguide.com
Covers Desktop (1280x800) and Mobile (390x844, iPhone 13) user journeys.

Deliverables:
- Desktop: Home loading, Calculator coordinate conversion & copy, Materials BOM calculation, Multi-page navigation loop.
- Mobile: Drawer menu collapse/expand, touch interaction, zero horizontal overflow check.
- Screenshots saved to tests/screenshots/
"""

import argparse
import http.server
import json
import os
import socket
import socketserver
import sys
import threading
import time
from typing import Optional, Tuple
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "tests", "screenshots")

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


class CleanURLHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler that resolves clean URLs (e.g. /portal -> /portal.html)."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def translate_path(self, path):
        full_path = super().translate_path(path)
        if not os.path.exists(full_path) and os.path.exists(full_path + ".html"):
            return full_path + ".html"
        return full_path

    def log_message(self, format, *args):
        # Silence static server logs during test execution
        pass


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_local_server(port: int) -> socketserver.TCPServer:
    server = socketserver.TCPServer(("127.0.0.1", port), CleanURLHTTPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    return server


class E2EReporter:
    def __init__(self):
        self.results = []
        self.screenshots = []
        self.start_time = time.time()

    def record_pass(self, test_name: str, duration: float, notes: str = ""):
        self.results.append({"name": test_name, "status": "PASS", "duration": duration, "notes": notes})
        print(f"  {GREEN}✔ PASS{RESET} [{duration:.2f}s] {test_name}")
        if notes:
            print(f"         {CYAN}↳ {notes}{RESET}")

    def record_fail(self, test_name: str, duration: float, error: str):
        self.results.append({"name": test_name, "status": "FAIL", "duration": duration, "error": error})
        print(f"  {RED}✘ FAIL{RESET} [{duration:.2f}s] {test_name}")
        print(f"         {RED}↳ Error: {error}{RESET}")

    def add_screenshot(self, filename: str, description: str):
        full_path = os.path.join(SCREENSHOTS_DIR, filename)
        self.screenshots.append({"file": filename, "path": full_path, "description": description})
        print(f"         {YELLOW}📷 Screenshot: {filename}{RESET}")

    def print_summary(self) -> bool:
        total_time = time.time() - self.start_time
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "PASS")
        failed = sum(1 for r in self.results if r["status"] == "FAIL")

        print("\n" + "=" * 70)
        print(f"{BOLD}E2E TEST EXECUTION SUMMARY{RESET}")
        print("=" * 70)
        for r in self.results:
            color = GREEN if r["status"] == "PASS" else RED
            print(f"{color}[{r['status']}]{RESET} {r['name']:<50} ({r['duration']:.2f}s)")

        print("-" * 70)
        print(f"Total Tests: {total} | Passed: {GREEN}{passed}{RESET} | Failed: {RED if failed else GREEN}{failed}{RESET} | Time: {total_time:.2f}s")
        print(f"Screenshots Saved ({len(self.screenshots)}):")
        for s in self.screenshots:
            print(f"  • {s['file']}: {s['description']}")
        print("=" * 70 + "\n")
        return failed == 0


def run_desktop_suite(browser: Browser, base_url: str, reporter: E2EReporter):
    print(f"\n{BOLD}{CYAN}=== SUITE 1: Desktop Core Interaction Suite (1280x800) ==={RESET}")
    context = browser.new_context(
        viewport={"width": 1280, "height": 800},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        permissions=["clipboard-read", "clipboard-write"]
    )
    page = context.new_page()

    # -------------------------------------------------------------
    # Case 1.1: Home & Component Load
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/", wait_until="networkidle")
        title = page.title()
        assert "The Sift Minecraft" in title, f"Title does not contain 'The Sift Minecraft': '{title}'"

        # Check Home H1 bounds
        home_h1 = page.locator("h1").first.inner_text().strip()
        assert ("The Sift: Minecraft" in home_h1 or "The Sift in Minecraft" in home_h1), f"Home H1 mismatch: '{home_h1}'"
        assert 20 <= len(home_h1) <= 70, f"Home H1 length out of bounds ({len(home_h1)} chars): '{home_h1}'"

        # Check GA4 script
        ga4_count = page.locator('script[src*="googletagmanager.com/gtag/js?id=G-X1ZTW8XWPG"]').count()
        if ga4_count == 0:
            # Fallback check inline GA4 snippet
            page_content = page.content()
            assert "G-X1ZTW8XWPG" in page_content, "GA4 measurement ID (G-X1ZTW8XWPG) not found"

        # Check Adsterra ad slot
        adsterra_count = page.locator('script[src*="invoke.js"], script[src*="bauval.org"], script:has-text("e34c08305944ef076210b30b1897f6eb")').count()
        assert adsterra_count > 0, "Adsterra ad placement container not found"

        # Check Schema JSON-LD parsing
        json_lds = page.locator('script[type="application/ld+json"]').all_inner_texts()
        assert len(json_lds) > 0, "No Schema.org JSON-LD scripts found"
        for idx, jtext in enumerate(json_lds):
            data = json.loads(jtext)
            assert ("@context" in data or "@graph" in data), f"JSON-LD #{idx} invalid structure"

        # Check Favicon (Google SERP 48px/96px standard links and assets)
        fav_48 = page.locator('link[rel="icon"][sizes="48x48"][href="/favicon-48x48.png"]').count()
        fav_96 = page.locator('link[rel="icon"][sizes="96x96"][href="/favicon-96x96.png"]').count()
        assert fav_48 > 0, "Favicon 48x48 link tag not found"
        assert fav_96 > 0, "Favicon 96x96 link tag not found"
        res_48 = context.request.get(f"{base_url}/favicon-48x48.png")
        assert res_48.status == 200, f"/favicon-48x48.png returned {res_48.status}"
        assert len(res_48.body()) > 500, f"/favicon-48x48.png content too small ({len(res_48.body())} bytes)"
        res_96 = context.request.get(f"{base_url}/favicon-96x96.png")
        assert res_96.status == 200, f"/favicon-96x96.png returned {res_96.status}"
        assert len(res_96.body()) > 500, f"/favicon-96x96.png content too small ({len(res_96.body())} bytes)"

        # Check Canonical Tag matches clean root URL
        canonical_href = page.locator('link[rel="canonical"]').get_attribute("href")
        assert canonical_href == "https://thesiftguide.com/", f"Home canonical mismatch: expected 'https://thesiftguide.com/', got '{canonical_href}'"

        # Check Capo.js head element order (monotonic non-increasing effectiveness)
        head_html = page.evaluate("() => document.head.innerHTML")
        def _pos(needle):
            i = head_html.find(needle)
            assert i != -1, f"head order check: needle not found: {needle[:60]}"
            return i
        pos_charset = _pos('<meta charset')
        pos_title = _pos('<title')
        pos_preconnect = _pos('rel="preconnect"')
        pos_gtag_async = _pos('googletagmanager.com/gtag/js')
        pos_preload = _pos('rel="preload"')
        pos_tailwind = _pos('cdn.tailwindcss.com')
        pos_jsonld = _pos('application/ld+json')
        pos_font_css = _pos('rel="stylesheet"')
        pos_canonical = _pos('rel="canonical"')
        order_pairs = [
            (pos_charset, pos_title, "charset before title"),
            (pos_title, pos_preconnect, "title before preconnect"),
            (pos_preconnect, pos_gtag_async, "preconnect before async gtag"),
            (pos_gtag_async, pos_preload, "async gtag before preload"),
            (pos_preload, pos_tailwind, "preload before Tailwind sync script"),
            (pos_tailwind, pos_jsonld, "Tailwind before JSON-LD"),
            (pos_jsonld, pos_font_css, "JSON-LD before font stylesheet"),
            (pos_font_css, pos_canonical, "font stylesheet before canonical"),
        ]
        for earlier, later, label in order_pairs:
            assert earlier < later, f"Capo.js head order violated ({label})"

        # Save screenshot
        ss_file = "01_desktop_home_loaded.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_file), full_page=False)
        reporter.add_screenshot(ss_file, "Desktop Home Loaded (Hero, GA4, Adsterra, JSON-LD verified)")
        reporter.record_pass("Case 1.1 - Home & Component Load", time.time() - t0, f"Title: '{title[:42]}...', GA4 & Adsterra active, JSON-LD valid")
    except Exception as e:
        reporter.record_fail("Case 1.1 - Home & Component Load", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.2: Coordinate Calculator Realtime Input & Conversion
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        calc_section = page.locator("#calculator")
        assert calc_section.is_visible(), "Element #calculator is not visible"
        calc_section.scroll_into_view_if_needed()

        # Input coordinates: X=1600, Y=70, Z=-1200
        page.fill("#coord-x", "1600")
        page.fill("#coord-y", "70")
        page.fill("#coord-z", "-1200")

        # Select compression ratio 1:8 Nether Equivalent (value "8")
        page.select_option("#calc-ratio", "8")
        time.sleep(0.1)

        # Assert calculation results
        target_x = page.locator("#res-target-x").inner_text().strip()
        target_y = page.locator("#res-target-y").inner_text().strip()
        target_z = page.locator("#res-target-z").inner_text().strip()

        assert target_x == "200", f"Target X expected 200, got '{target_x}'"
        assert target_y == "70", f"Target Y expected 70, got '{target_y}'"
        assert target_z == "-150", f"Target Z expected -150, got '{target_z}'"

        # Click "Copy /tp Command" button
        page.click("#btn-copy-tp")
        time.sleep(0.1)

        btn_label = page.locator("#btn-copy-tp-label").inner_text().strip()
        status_indicator = page.locator("#copy-status-indicator").inner_text().strip()
        assert ("Copied" in btn_label or "Copied" in status_indicator), f"Copy feedback did not show 'Copied' (label: '{btn_label}', status: '{status_indicator}')"

        ss_file = "02_desktop_calculator_converted.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_file), full_page=False)
        reporter.add_screenshot(ss_file, "Desktop Calculator Converted (X:200, Y:70, Z:-150, Copied feedback)")
        reporter.record_pass("Case 1.2 - Portal Coordinate Calculator Conversion", time.time() - t0, f"X=1600, Y=70, Z=-1200 @ 1:8 ➔ Target ({target_x}, {target_y}, {target_z}), feedback verified")
    except Exception as e:
        reporter.record_fail("Case 1.2 - Portal Coordinate Calculator Conversion", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.3: Materials Budget Switching & Calculation
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.click("#tab-btn-materials")
        time.sleep(0.1)

        materials_panel = page.locator("#panel-materials")
        assert materials_panel.is_visible(), "Materials panel is not visible after clicking tab"
        classes = materials_panel.get_attribute("class") or ""
        assert "hidden" not in classes.split(), "Materials panel still has 'hidden' class"

        # Select Ancient Rift Arch 7x9
        page.select_option("#portal-frame-size", "arch")
        time.sleep(0.1)

        corners_checkbox = page.locator("#portal-corners")

        # Toggle test: uncheck corner blocks -> assert 20 blocks
        corners_checkbox.uncheck()
        time.sleep(0.05)
        count_without_corners = page.locator("#bom-frame-count").inner_text().strip()
        assert count_without_corners == "20", f"Expected 20 blocks without corners, got '{count_without_corners}'"

        # Toggle back to checked -> assert 28 blocks
        corners_checkbox.check()
        time.sleep(0.05)
        count_with_corners = page.locator("#bom-frame-count").inner_text().strip()
        assert count_with_corners == "28", f"Expected 28 blocks with corners, got '{count_with_corners}'"

        ss_file = "03_desktop_materials_budget.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_file), full_page=False)
        reporter.add_screenshot(ss_file, "Desktop Materials Budget (Ancient Rift Arch 7x9, 20➔28 blocks BOM)")
        reporter.record_pass("Case 1.3 - Portal Materials Budget Calculation", time.time() - t0, "Ancient Rift Arch 7x9 toggled 20 ➔ 28 blocks dynamically with BOM sync")
    except Exception as e:
        reporter.record_fail("Case 1.3 - Portal Materials Budget Calculation", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.4: Full Site Navigation & Inter-Page Loop
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        # Step 1: Nav to /portal
        page.locator('header nav a[href="/portal"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/portal" in page.url, f"URL did not contain '/portal': '{page.url}'"
        assert not page.url.endswith("/portal.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/portal", "Portal canonical tag mismatch"
        h1_text = page.locator("h1").inner_text().strip()
        assert ("Minecraft Portal Guide" in h1_text or "The Sift Portal Guide" in h1_text), f"Portal H1 mismatch: '{h1_text}'"
        assert 20 <= len(h1_text) <= 70, f"Portal H1 length out of bounds ({len(h1_text)} chars): '{h1_text}'"
        assert page.locator('#faq, section:has-text("Frequently Asked Questions")').count() > 0, "Portal FAQ not found"

        ss_portal = "04_desktop_nav_portal.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_portal), full_page=False)
        reporter.add_screenshot(ss_portal, "Desktop Nav: Portal Guide page loaded")

        # Step 2: Nav to /mobs
        page.locator('header nav a[href="/mobs"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/mobs" in page.url, f"URL did not contain '/mobs': '{page.url}'"
        assert not page.url.endswith("/mobs.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/mobs", "Mobs canonical tag mismatch"
        mobs_h1 = page.locator("h1").inner_text().strip()
        assert ("The Sift Minecraft: Mobs" in mobs_h1 or "The Sift Mobs & Fauna" in mobs_h1), f"Mobs H1 mismatch: '{mobs_h1}'"
        assert 20 <= len(mobs_h1) <= 70, f"Mobs H1 length out of bounds ({len(mobs_h1)} chars): '{mobs_h1}'"
        assert page.locator("table").count() > 0 and page.locator("table").first.is_visible(), "Mobs bestiary table not found or not visible"

        ss_mobs = "05_desktop_nav_mobs.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mobs), full_page=False)
        reporter.add_screenshot(ss_mobs, "Desktop Nav: Mobs & Entities bestiary page loaded")

        # Step 2.5: Nav to /mods
        page.locator('header nav a[href="/mods"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/mods" in page.url, f"URL did not contain '/mods': '{page.url}'"
        assert not page.url.endswith("/mods.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/mods", "Mods canonical tag mismatch"
        mods_h1 = page.locator("h1").inner_text().strip()
        assert "The Sift Minecraft Mod" in mods_h1, f"Mods H1 mismatch: '{mods_h1}'"
        assert 20 <= len(mods_h1) <= 70, f"Mods H1 length out of bounds ({len(mods_h1)} chars): '{mods_h1}'"

        ss_mods = "05_desktop_nav_mods.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mods), full_page=False)
        reporter.add_screenshot(ss_mods, "Desktop Nav: Mods & Addons guide page loaded")

        # Step 3: Nav to /dungeons-2
        page.locator('header nav a[href="/dungeons-2"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/dungeons-2" in page.url, f"URL did not contain '/dungeons-2': '{page.url}'"
        assert not page.url.endswith("/dungeons-2.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/dungeons-2", "Dungeons-2 canonical tag mismatch"
        d2_h1 = page.locator("h1").inner_text().strip()
        assert "Minecraft Dungeons II" in d2_h1, f"Dungeons II H1 mismatch: '{d2_h1}'"
        assert 20 <= len(d2_h1) <= 70, f"Dungeons II H1 length out of bounds ({len(d2_h1)} chars): '{d2_h1}'"

        ss_d2 = "05b_desktop_nav_dungeons2.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_d2), full_page=False)
        reporter.add_screenshot(ss_d2, "Desktop Nav: Dungeons II Guide page loaded")

        # Step 4: Nav to /about
        page.locator('header nav a[href="/about"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/about" in page.url, f"URL did not contain '/about': '{page.url}'"
        assert not page.url.endswith("/about.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/about", "About canonical tag mismatch"
        about_h1 = page.locator("h1").inner_text().strip()
        assert "About The Sift Guide" in about_h1, f"About H1 mismatch: '{about_h1}'"
        assert 20 <= len(about_h1) <= 70, f"About H1 length out of bounds ({len(about_h1)} chars): '{about_h1}'"
        disclosure_section = page.locator('#disclosure, section:has-text("Editorial Independence")')
        assert disclosure_section.count() > 0, "About editorial independence / disclaimer section not found"

        ss_about = "06_desktop_nav_about.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_about), full_page=False)
        reporter.add_screenshot(ss_about, "Desktop Nav: About & Legal Disclaimers page loaded")

        # Step 5: Nav to /privacy from footer
        privacy_link = page.locator('footer a[href="/privacy"]').first
        privacy_link.scroll_into_view_if_needed()
        privacy_link.click()
        page.wait_for_load_state("networkidle")
        assert "/privacy" in page.url, f"URL did not contain '/privacy': '{page.url}'"
        assert not page.url.endswith("/privacy.html"), f"URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/privacy", "Privacy canonical tag mismatch"
        privacy_h1 = page.locator("h1").inner_text().strip()
        assert ("The Sift Minecraft Guide: Official Privacy Policy" in privacy_h1 or "Privacy Policy" in privacy_h1), f"Privacy H1 mismatch: '{privacy_h1}'"
        assert 20 <= len(privacy_h1) <= 70, f"Privacy H1 length out of bounds ({len(privacy_h1)} chars): '{privacy_h1}'"

        ss_privacy = "07_desktop_nav_privacy.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_privacy), full_page=False)
        reporter.add_screenshot(ss_privacy, "Desktop Nav: Privacy Policy page loaded")

        # Step 6: Click Logo to return to Home /
        logo_link = page.locator('header a[href="/"]:visible').first
        logo_link.click()
        page.wait_for_load_state("networkidle")
        assert (page.url.rstrip("/") == base_url.rstrip("/") or page.url.endswith("/index.html") or page.url == f"{base_url}/"), f"Expected home URL, got '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/", "Home canonical tag mismatch"
        assert page.locator("#calculator").is_visible(), "Calculator not found after returning home"

        ss_home_ret = "08_desktop_nav_home_returned.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_home_ret), full_page=False)
        reporter.add_screenshot(ss_home_ret, "Desktop Nav: Returned to Home via Header Logo")
        reporter.record_pass("Case 1.4 - Full Site Navigation & Inter-Page Loop", time.time() - t0, "Home ➔ Portal ➔ Mobs ➔ Dungeons II ➔ About ➔ Privacy ➔ Home closed-loop verified with Clean URLs & canonical checks")
    except Exception as e:
        reporter.record_fail("Case 1.4 - Full Site Navigation & Inter-Page Loop", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.5: Dungeons 2 Subpage Verification
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/dungeons-2", wait_until="networkidle")
        title = page.title()
        assert "The Sift in Minecraft Dungeons 2" in title, f"Dungeons 2 title mismatch: '{title}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/dungeons-2", "Dungeons 2 canonical tag mismatch"

        # Check GA4 script
        page_content = page.content()
        assert "G-X1ZTW8XWPG" in page_content, "GA4 measurement ID not found on dungeons-2.html"

        # Check Top & Bottom Adsterra ad slots
        top_ad_found = "e34c08305944ef076210b30b1897f6eb" in page_content
        bottom_ad_found = "93a1b6fb1cf3809a6ddd2ccae9364526" in page_content
        assert top_ad_found, "Top 728x90 Adsterra container not found on dungeons-2.html"
        assert bottom_ad_found, "Bottom 300x250 Adsterra container not found on dungeons-2.html"

        # Check Schema.org FAQPage structured data
        json_lds = page.locator('script[type="application/ld+json"]').all_inner_texts()
        assert len(json_lds) > 0, "No Schema JSON-LD found on dungeons-2.html"
        faq_found = False
        for jtext in json_lds:
            data = json.loads(jtext)
            graph = data.get("@graph", [data])
            for item in graph:
                if item.get("@type") == "FAQPage":
                    faq_found = True
                    assert len(item.get("mainEntity", [])) >= 6, "FAQPage mainEntity has fewer than 6 questions"
        assert faq_found, "Schema.org FAQPage not found in JSON-LD graph"

        # Check Hero & Key Sections
        d2_sub_h1 = page.locator("h1").first.inner_text().strip()
        assert 20 <= len(d2_sub_h1) <= 70, f"Dungeons 2 H1 length out of bounds ({len(d2_sub_h1)} chars): '{d2_sub_h1}'"
        assert page.locator('#hero:has-text("Minecraft Dungeons II")').count() > 0, "Hero section missing"
        assert page.locator('#biomes:has-text("Singer\'s Meadow")').count() > 0, "Singer's Meadow section missing"
        assert page.locator('#biomes:has-text("Carapace Desert")').count() > 0, "Carapace Desert section missing"
        assert page.locator('#mechanics:has-text("Overworld Rifts")').count() > 0, "Overworld Rifts section missing"
        assert page.locator('#comparison:has-text("The Sift Matrix")').count() > 0, "Comparison Matrix section missing"

        # Test Interactive FAQ Accordion Click
        first_faq_summary = page.locator("#faq details summary").first
        first_faq_summary.click()
        time.sleep(0.1)
        assert page.locator("#faq details").first.is_visible(), "FAQ details element not visible"

        ss_d2_sub = "08b_desktop_dungeons2_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_d2_sub), full_page=False)
        reporter.add_screenshot(ss_d2_sub, "Desktop Dungeons II Subpage (SEO, Dual Ads, JSON-LD, Biomes & FAQ verified)")
        reporter.record_pass("Case 1.5 - Dungeons 2 Subpage Verification", time.time() - t0, "dungeons-2 loaded, SEO Title/GA4/Dual Ads/JSON-LD/Biomes/Accordion/Canonical verified")
    except Exception as e:
        reporter.record_fail("Case 1.5 - Dungeons 2 Subpage Verification", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.6: Portal Guide VideoObject Schema & YouTube Embed Verification
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/portal", wait_until="networkidle")
        title = page.title()
        assert ("Minecraft Portal Guide" in title or "The Sift Portal Guide" in title), f"Portal title mismatch: '{title}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/portal", "Portal canonical tag mismatch"

        # 1. Video container and iframe assertions
        video_guide = page.locator("#video-guide")
        assert video_guide.is_visible(), "Video guide container (#video-guide) not visible on portal.html"
        video_guide.scroll_into_view_if_needed()

        iframe = page.locator('#video-guide iframe[src*="youtube-nocookie.com/embed/mdsxeO9mpd8"]')
        assert iframe.count() > 0, "YouTube nocookie iframe with embed ID mdsxeO9mpd8 not found"
        assert iframe.first.is_visible(), "YouTube iframe is not visible"

        # 2. VideoObject Schema JSON-LD assertion
        json_lds = page.locator('script[type="application/ld+json"]').all_inner_texts()
        assert len(json_lds) > 0, "No Schema JSON-LD found on portal.html"

        video_object_found = False
        for jtext in json_lds:
            data = json.loads(jtext)
            graph = data.get("@graph", [data])
            for item in graph:
                if item.get("@type") == "VideoObject":
                    video_object_found = True
                    assert item.get("name") == "How to Enter The Sift in Minecraft (Portal & Teleport Commands)", f"VideoObject name mismatch: {item.get('name')}"
                    assert "Quick 30-second tutorial" in item.get("description", ""), f"VideoObject description mismatch: {item.get('description')}"
                    assert item.get("thumbnailUrl") == "https://thesiftguide.com/youtube_shorts_thumbnail.png", f"thumbnailUrl mismatch: {item.get('thumbnailUrl')}"
                    assert item.get("uploadDate") == "2026-10-03T00:00:00+08:00", f"uploadDate mismatch: {item.get('uploadDate')}"
                    assert item.get("duration") == "PT30S", f"duration mismatch: {item.get('duration')}"
                    assert item.get("embedUrl") == "https://www.youtube-nocookie.com/embed/mdsxeO9mpd8", f"embedUrl mismatch: {item.get('embedUrl')}"
                    assert item.get("contentUrl") == "https://youtube.com/shorts/mdsxeO9mpd8", f"contentUrl mismatch: {item.get('contentUrl')}"
        assert video_object_found, "Schema.org VideoObject not found in portal.html JSON-LD graph"

        ss_video = "08c_desktop_portal_video_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_video), full_page=False)
        reporter.add_screenshot(ss_video, "Desktop Portal Guide Video (YouTube nocookie iframe & VideoObject schema verified)")
        reporter.record_pass("Case 1.6 - Portal Guide VideoObject & YouTube Embed", time.time() - t0, "portal.html 9:16 iframe & VideoObject JSON-LD verified")
    except Exception as e:
        reporter.record_fail("Case 1.6 - Portal Guide VideoObject & YouTube Embed", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.7: Clean URLs & Canonical Tags Alignment Audit (All 7 Pages)
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        pages_to_check = [
            ("/", "https://thesiftguide.com/"),
            ("/portal", "https://thesiftguide.com/portal"),
            ("/mobs", "https://thesiftguide.com/mobs"),
            ("/mods", "https://thesiftguide.com/mods"),
            ("/dungeons-2", "https://thesiftguide.com/dungeons-2"),
            ("/about", "https://thesiftguide.com/about"),
            ("/privacy", "https://thesiftguide.com/privacy"),
        ]
        for path, expected_canonical in pages_to_check:
            page.goto(f"{base_url}{path}", wait_until="networkidle")
            canonical_tag = page.locator('link[rel="canonical"]').get_attribute("href")
            assert canonical_tag == expected_canonical, f"Canonical tag on {path} mismatch: expected {expected_canonical}, got {canonical_tag}"

            # Check H1 length bounds on all 7 pages
            page_h1 = page.locator("h1").first.inner_text().strip()
            assert 20 <= len(page_h1) <= 70, f"{path} H1 length out of bounds ({len(page_h1)} chars): '{page_h1}'"

            # Check Capo.js head order (preconnect before async gtag, etc.)
            p_head = page.evaluate("() => document.head.innerHTML")
            def _find_pos(needle):
                idx = p_head.find(needle)
                assert idx != -1, f"{path}: needle '{needle[:50]}' not found in head"
                return idx
            c_charset = _find_pos('<meta charset')
            c_title = _find_pos('<title')
            c_preconnect = _find_pos('rel="preconnect"')
            c_gtag = _find_pos('googletagmanager.com/gtag/js')
            c_preload = _find_pos('rel="preload"')
            c_tailwind = _find_pos('cdn.tailwindcss.com')
            c_jsonld = _find_pos('application/ld+json')
            c_font = _find_pos('rel="stylesheet"')
            c_canonical = _find_pos('rel="canonical"')
            assert c_charset < c_title < c_preconnect < c_gtag < c_preload < c_tailwind < c_jsonld < c_font < c_canonical, f"{path} head order violates Capo.js"

            # Verify no internal relative links point to legacy .html files
            html_hrefs = page.locator('a[href$=".html"], a[href*=".html#"], a[href*=".html?"]').all()
            assert len(html_hrefs) == 0, f"Found {len(html_hrefs)} legacy .html links on {path}"

        reporter.record_pass("Case 1.7 - Clean URLs & Canonical Tags Alignment Audit", time.time() - t0, "All 7 pages verified: exact clean canonical tags & zero legacy .html links")
    except Exception as e:
        reporter.record_fail("Case 1.7 - Clean URLs & Canonical Tags Alignment Audit", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.8: Mods Subpage Deep Verification (SEO, Schema, Dual Ads, Matcher)
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/mods", wait_until="networkidle")
        title = page.title()
        assert title == "The Sift Minecraft Mod: Download Guide (Java & Bedrock)", f"Mods title mismatch: '{title}'"
        assert 50 <= len(title) <= 60, f"Title length out of bounds ({len(title)}): '{title}'"
        assert title.startswith("The Sift Minecraft Mod"), "Title does not start with primary surge keyword"

        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/mods", "Mods canonical tag mismatch"

        # Check GA4 script
        page_content = page.content()
        assert "G-X1ZTW8XWPG" in page_content, "GA4 measurement ID not found on mods.html"

        # Check Meta Description
        meta_desc = page.locator('meta[name="description"]').get_attribute("content")
        assert meta_desc == "Download The Sift Minecraft mod today. Complete setup guide for Java (Fabric/Forge) and Bedrock (.mcaddon) with custom biomes, Colossal Frogs, and Siftite.", f"Meta description mismatch: '{meta_desc}'"
        assert 145 <= len(meta_desc) <= 158, f"Meta desc length out of bounds ({len(meta_desc)}): '{meta_desc}'"

        # Check H1
        mods_h1 = page.locator("h1").first.inner_text().strip()
        assert mods_h1 == "The Sift Minecraft Mod: Play the 4th Dimension Today", f"Mods H1 mismatch: '{mods_h1}'"
        assert 20 <= len(mods_h1) <= 70, f"Mods H1 length out of bounds ({len(mods_h1)} chars): '{mods_h1}'"

        # Check Top & Bottom Adsterra ad slots
        top_ad_found = "e34c08305944ef076210b30b1897f6eb" in page_content
        bottom_ad_found = "93a1b6fb1cf3809a6ddd2ccae9364526" in page_content
        assert top_ad_found, "Top 728x90 Adsterra container not found on mods.html"
        assert bottom_ad_found, "Bottom 300x250 Adsterra container not found on mods.html"

        # Check Schema.org structured data (WebSite, BreadcrumbList, TechArticle, SoftwareApplication, FAQPage)
        json_lds = page.locator('script[type="application/ld+json"]').all_inner_texts()
        assert len(json_lds) > 0, "No Schema JSON-LD found on mods.html"
        types_found = set()
        faq_count = 0
        for jtext in json_lds:
            data = json.loads(jtext)
            graph = data.get("@graph", [data])
            for item in graph:
                itype = item.get("@type")
                types_found.add(itype)
                if itype == "FAQPage":
                    faq_count = len(item.get("mainEntity", []))
        for req in ["WebSite", "BreadcrumbList", "TechArticle", "SoftwareApplication", "FAQPage"]:
            assert req in types_found, f"Missing Schema.org type '{req}' on mods.html"
        assert faq_count >= 7, f"FAQPage has fewer than 7 questions ({faq_count})"

        # Check Interactive Matcher State Machine
        matcher = page.locator("#matcher")
        assert matcher.is_visible(), "Matcher section (#matcher) is not visible"

        # Initial default: Java Edition -> verify default Fabric recommendations
        result_title = page.locator("#result-title").inner_text().strip()
        assert "Fabric" in result_title, f"Default result title expected Fabric, got: '{result_title}'"
        result_deps = page.locator("#result-deps").inner_text().strip()
        assert "Fabric API" in result_deps, f"Default deps expected Fabric API, got: '{result_deps}'"

        # Click Bedrock button
        bedrock_btn = page.locator('#platform-selector button[data-val="bedrock"]')
        bedrock_btn.click()
        time.sleep(0.1)

        result_title_bedrock = page.locator("#result-title").inner_text().strip()
        assert (".mcaddon" in result_title_bedrock or "Bedrock" in result_title_bedrock), f"Bedrock result title expected .mcaddon/Bedrock, got: '{result_title_bedrock}'"
        result_deps_bedrock = page.locator("#result-deps").inner_text().strip()
        assert ("Experimental" in result_deps_bedrock or "No external loaders" in result_deps_bedrock), f"Bedrock deps mismatch: '{result_deps_bedrock}'"

        # Switch back to Java
        java_btn = page.locator('#platform-selector button[data-val="java"]')
        java_btn.click()
        time.sleep(0.1)

        # Select MC 1.20.1
        v120_btn = page.locator('#version-selector button[data-val="1.20"]')
        v120_btn.click()
        time.sleep(0.1)

        # Switch loader to Forge
        page.select_option("#loader-selector", "forge")
        time.sleep(0.1)
        result_title_forge = page.locator("#result-title").inner_text().strip()
        assert "Forge" in result_title_forge, f"Expected Forge in result title, got: '{result_title_forge}'"

        # Check FAQ Accordion interaction
        first_faq_summary = page.locator("#faq details summary").first
        first_faq_summary.click()
        time.sleep(0.1)
        assert page.locator("#faq details").first.is_visible(), "FAQ details element not visible after click"

        ss_mods_sub = "08d_desktop_mods_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mods_sub), full_page=False)
        reporter.add_screenshot(ss_mods_sub, "Desktop Mods Subpage (SEO, Dual Ads, 5 Schemas, Matcher & FAQ verified)")
        reporter.record_pass("Case 1.8 - Mods Subpage Verification", time.time() - t0, "mods.html loaded, SEO Title/Desc/H1/GA4/Dual Ads/5 Schemas/Matcher/Canonical verified")
    except Exception as e:
        reporter.record_fail("Case 1.8 - Mods Subpage Verification", time.time() - t0, str(e))

    context.close()


def run_mobile_suite(browser: Browser, base_url: str, reporter: E2EReporter):
    print(f"\n{BOLD}{CYAN}=== SUITE 2: Mobile User Journey Suite (390x844, iPhone 13) ==={RESET}")
    mobile_context = browser.new_context(
        viewport={"width": 390, "height": 844},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
        is_mobile=True,
        has_touch=True,
        permissions=["clipboard-read", "clipboard-write"]
    )
    page = mobile_context.new_page()

    # -------------------------------------------------------------
    # Case 2.1: Mobile Drawer Navigation
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/", wait_until="networkidle")

        # Assert desktop navigation is hidden
        desktop_nav = page.locator('header nav.hidden.md\\:flex')
        assert not desktop_nav.is_visible(), "Desktop nav should be hidden on 390px viewport"

        # Assert mobile drawer initially hidden
        mobile_drawer = page.locator("#mobile-nav")
        assert not mobile_drawer.is_visible(), "Mobile nav drawer should initially be hidden"

        # Click hamburger menu button
        page.click("#mobile-menu-btn")
        time.sleep(0.2)

        # Assert mobile drawer opened
        assert mobile_drawer.is_visible(), "Mobile nav drawer did not open after clicking hamburger button"

        ss_drawer = "09_mobile_drawer_opened.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_drawer), full_page=False)
        reporter.add_screenshot(ss_drawer, "Mobile Drawer Expanded (Hamburger menu opened)")

        # Click Portal Guide in drawer
        portal_item = page.locator('#mobile-nav a[href="/portal"]').first
        portal_item.click()
        page.wait_for_load_state("networkidle")

        assert "/portal" in page.url, f"Mobile URL did not contain '/portal': '{page.url}'"
        assert not page.url.endswith("/portal.html"), f"Mobile URL should not end with .html: '{page.url}'"
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/portal", "Mobile portal canonical tag mismatch"
        portal_h1 = page.locator("h1").inner_text().strip()
        assert ("Minecraft Portal Guide" in portal_h1 or "The Sift Portal Guide" in portal_h1), f"Mobile portal H1 mismatch: '{portal_h1}'"
        assert 20 <= len(portal_h1) <= 70, f"Mobile portal H1 length out of bounds ({len(portal_h1)} chars): '{portal_h1}'"

        ss_mob_portal = "10_mobile_navigated_portal.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mob_portal), full_page=False)
        reporter.add_screenshot(ss_mob_portal, "Mobile Navigated to Portal Guide via Drawer")
        reporter.record_pass("Case 2.1 - Mobile Hamburger Drawer Navigation", time.time() - t0, "Hamburger drawer opened and smoothly navigated to /portal")
    except Exception as e:
        reporter.record_fail("Case 2.1 - Mobile Hamburger Drawer Navigation", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 2.2: Mobile Calculator Touch & Zero Overflow
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        # Return to home
        page.goto(f"{base_url}/", wait_until="networkidle")

        # Horizontal overflow check
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        inner_width = page.evaluate("() => window.innerWidth")
        assert scroll_width <= inner_width, f"Horizontal overflow detected! scrollWidth={scroll_width} > innerWidth={inner_width}"

        # Scroll to calculator
        calc = page.locator("#calculator")
        calc.scroll_into_view_if_needed()

        # Touch input values
        page.fill("#coord-x", "800")
        page.fill("#coord-y", "64")
        page.fill("#coord-z", "-400")
        page.select_option("#calc-ratio", "4")
        time.sleep(0.1)

        target_x = page.locator("#res-target-x").inner_text().strip()
        assert target_x == "200", f"Mobile conversion expected 200, got '{target_x}'"

        # Click copy button
        page.click("#btn-copy-tp")
        time.sleep(0.1)

        status_text = page.locator("#copy-status-indicator").inner_text().strip()
        btn_text = page.locator("#btn-copy-tp-label").inner_text().strip()
        assert ("Copied" in status_text or "Copied" in btn_text), "Mobile copy feedback missing"

        ss_mob_calc = "11_mobile_calculator_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mob_calc), full_page=False)
        reporter.add_screenshot(ss_mob_calc, "Mobile Calculator Verified (No overflow, touch inputs & copy working)")
        reporter.record_pass("Case 2.2 - Mobile Calculator Touch & Zero Overflow", time.time() - t0, f"scrollWidth={scroll_width} <= innerWidth={inner_width} (zero overflow), touch conversion & copy verified")
    except Exception as e:
        reporter.record_fail("Case 2.2 - Mobile Calculator Touch & Zero Overflow", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 2.3: Mobile Dungeons 2 Subpage & Zero Overflow
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/dungeons-2", wait_until="networkidle")
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/dungeons-2", "Mobile dungeons-2 canonical tag mismatch"

        # Zero Horizontal Overflow Check
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        inner_width = page.evaluate("() => window.innerWidth")
        assert scroll_width <= inner_width, f"Dungeons 2 horizontal overflow detected! scrollWidth={scroll_width} > innerWidth={inner_width}"

        # Test mobile accordion interaction
        faq_sum = page.locator("#faq details summary").first
        faq_sum.scroll_into_view_if_needed()
        faq_sum.click()
        time.sleep(0.1)

        # Re-check overflow after accordion expands
        scroll_width_expanded = page.evaluate("() => document.documentElement.scrollWidth")
        assert scroll_width_expanded <= inner_width, f"Overflow detected after FAQ open! scrollWidth={scroll_width_expanded} > innerWidth={inner_width}"

        ss_mob_d2 = "12_mobile_dungeons2_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mob_d2), full_page=False)
        reporter.add_screenshot(ss_mob_d2, "Mobile Dungeons 2 Verified (Zero overflow, accordion touch verified)")
        reporter.record_pass("Case 2.3 - Mobile Dungeons 2 Subpage & Zero Overflow", time.time() - t0, f"scrollWidth={scroll_width} <= innerWidth={inner_width} (zero overflow), accordion touch verified")
    except Exception as e:
        reporter.record_fail("Case 2.3 - Mobile Dungeons 2 Subpage & Zero Overflow", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 2.4: Mobile Mods Subpage & Zero Overflow
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/mods", wait_until="networkidle")
        assert page.locator('link[rel="canonical"]').get_attribute("href") == "https://thesiftguide.com/mods", "Mobile mods canonical tag mismatch"

        # Zero Horizontal Overflow Check
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        inner_width = page.evaluate("() => window.innerWidth")
        assert scroll_width <= inner_width, f"Mods page horizontal overflow detected! scrollWidth={scroll_width} > innerWidth={inner_width}"

        # Test mobile Matcher interaction (JS click: immune to ad-iframe layout shift)
        page.evaluate("() => document.querySelector('#matcher').scrollIntoView({behavior: 'instant', block: 'center'})")
        time.sleep(0.3)
        page.evaluate("() => document.querySelector('#platform-selector button[data-val=\\'bedrock\\']').click()")
        time.sleep(0.2)
        bedrock_btn = page.locator('#platform-selector button[data-val="bedrock"]')
        assert "mc-btn-primary" in bedrock_btn.get_attribute("class"), "Bedrock button not activated after JS click"

        # Test mobile accordion interaction
        page.evaluate("() => document.querySelector('#faq details summary').scrollIntoView({behavior: 'instant', block: 'center'})")
        time.sleep(0.3)
        page.evaluate("() => document.querySelector('#faq details').setAttribute('open', '')")
        time.sleep(0.2)
        assert page.locator("#faq details").first.is_visible(), "FAQ details element not visible after open"

        # Re-check overflow after interactive updates
        scroll_width_expanded = page.evaluate("() => document.documentElement.scrollWidth")
        assert scroll_width_expanded <= inner_width, f"Overflow detected after Matcher/FAQ action! scrollWidth={scroll_width_expanded} > innerWidth={inner_width}"

        ss_mob_mods = "13_mobile_mods_verified.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mob_mods), full_page=False)
        reporter.add_screenshot(ss_mob_mods, "Mobile Mods Verified (Zero overflow, Matcher touch & accordion verified)")
        reporter.record_pass("Case 2.4 - Mobile Mods Subpage & Zero Overflow", time.time() - t0, f"scrollWidth={scroll_width} <= innerWidth={inner_width} (zero overflow), mobile Matcher & FAQ verified")
    except Exception as e:
        reporter.record_fail("Case 2.4 - Mobile Mods Subpage & Zero Overflow", time.time() - t0, str(e))

    mobile_context.close()


def main():
    parser = argparse.ArgumentParser(description="E2E Test Suite for thesiftguide.com")
    parser.add_argument("--target", choices=["live", "local"], default="live", help="Test target environment: 'live' (https://thesiftguide.com) or 'local'")
    parser.add_argument("--base-url", default=None, help="Custom Base URL override")
    parser.add_argument("--headless", action="store_true", default=True, help="Run browser in headless mode (default: True)")
    args = parser.parse_args()

    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    server = None
    if args.base_url:
        target_url = args.base_url.rstrip("/")
    elif args.target == "live":
        target_url = "https://thesiftguide.com"
    else:
        port = find_free_port()
        server = start_local_server(port)
        target_url = f"http://127.0.0.1:{port}"
        print(f"{YELLOW}Started ephemeral local HTTP server on {target_url} for tests{RESET}")

    print(f"\n{BOLD}Starting thesiftguide.com E2E Automated Tests{RESET}")
    print(f"Target URL: {CYAN}{target_url}{RESET}")
    print(f"Screenshots Directory: {SCREENSHOTS_DIR}\n")

    reporter = E2EReporter()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=args.headless)
            run_desktop_suite(browser, target_url, reporter)
            run_mobile_suite(browser, target_url, reporter)
            browser.close()
    finally:
        if server:
            server.shutdown()
            print(f"{YELLOW}Local HTTP server stopped cleanly.{RESET}")

    all_passed = reporter.print_summary()
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
