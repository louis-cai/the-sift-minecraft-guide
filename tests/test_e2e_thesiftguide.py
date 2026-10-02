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

        # Check GA4 script
        ga4_count = page.locator('script[src*="googletagmanager.com/gtag/js?id=G-X1ZTW8XWPG"]').count()
        if ga4_count == 0:
            # Fallback check inline GA4 snippet
            page_content = page.content()
            assert "G-X1ZTW8XWPG" in page_content, "GA4 measurement ID (G-X1ZTW8XWPG) not found"

        # Check Adsterra ad slot
        adsterra_count = page.locator('script[src*="invoke.js"], script:has-text("e34c08305944ef076210b30b1897f6eb")').count()
        assert adsterra_count > 0, "Adsterra ad placement container not found"

        # Check Schema JSON-LD parsing
        json_lds = page.locator('script[type="application/ld+json"]').all_inner_texts()
        assert len(json_lds) > 0, "No Schema.org JSON-LD scripts found"
        for idx, jtext in enumerate(json_lds):
            data = json.loads(jtext)
            assert ("@context" in data or "@graph" in data), f"JSON-LD #{idx} invalid structure"

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
        # Step 1: Nav to /portal.html
        page.locator('header nav a[href*="portal.html"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/portal" in page.url, f"URL did not contain '/portal': '{page.url}'"
        h1_text = page.locator("h1").inner_text().strip()
        assert "The Sift Portal Guide" in h1_text, f"Portal H1 mismatch: '{h1_text}'"
        assert page.locator('#faq, section:has-text("Frequently Asked Questions")').count() > 0, "Portal FAQ not found"

        ss_portal = "04_desktop_nav_portal.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_portal), full_page=False)
        reporter.add_screenshot(ss_portal, "Desktop Nav: Portal Guide page loaded")

        # Step 2: Nav to /mobs.html
        page.locator('header nav a[href*="mobs.html"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/mobs" in page.url, f"URL did not contain '/mobs': '{page.url}'"
        assert page.locator("table").count() > 0 and page.locator("table").first.is_visible(), "Mobs bestiary table not found or not visible"

        ss_mobs = "05_desktop_nav_mobs.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_mobs), full_page=False)
        reporter.add_screenshot(ss_mobs, "Desktop Nav: Mobs & Entities bestiary page loaded")

        # Step 3: Nav to /dungeons-2.html
        page.locator('header nav a[href*="dungeons-2.html"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/dungeons-2" in page.url, f"URL did not contain '/dungeons-2': '{page.url}'"
        d2_h1 = page.locator("h1").inner_text().strip()
        assert "Minecraft Dungeons II" in d2_h1, f"Dungeons II H1 mismatch: '{d2_h1}'"

        ss_d2 = "05b_desktop_nav_dungeons2.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_d2), full_page=False)
        reporter.add_screenshot(ss_d2, "Desktop Nav: Dungeons II Guide page loaded")

        # Step 4: Nav to /about.html
        page.locator('header nav a[href*="about.html"]:visible').click()
        page.wait_for_load_state("networkidle")
        assert "/about" in page.url, f"URL did not contain '/about': '{page.url}'"
        disclosure_section = page.locator('#disclosure, section:has-text("Editorial Independence")')
        assert disclosure_section.count() > 0, "About editorial independence / disclaimer section not found"

        ss_about = "06_desktop_nav_about.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_about), full_page=False)
        reporter.add_screenshot(ss_about, "Desktop Nav: About & Legal Disclaimers page loaded")

        # Step 5: Nav to /privacy.html from footer
        privacy_link = page.locator('footer a[href*="privacy.html"]').first
        privacy_link.scroll_into_view_if_needed()
        privacy_link.click()
        page.wait_for_load_state("networkidle")
        assert "/privacy" in page.url, f"URL did not contain '/privacy': '{page.url}'"
        privacy_h1 = page.locator("h1").inner_text().strip()
        assert "Privacy Policy" in privacy_h1, f"Privacy H1 mismatch: '{privacy_h1}'"

        ss_privacy = "07_desktop_nav_privacy.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_privacy), full_page=False)
        reporter.add_screenshot(ss_privacy, "Desktop Nav: Privacy Policy page loaded")

        # Step 6: Click Logo to return to Home /
        logo_link = page.locator('header a[href="/"]:visible').first
        logo_link.click()
        page.wait_for_load_state("networkidle")
        assert (page.url.rstrip("/") == base_url.rstrip("/") or page.url.endswith("/index.html") or page.url == f"{base_url}/"), f"Expected home URL, got '{page.url}'"
        assert page.locator("#calculator").is_visible(), "Calculator not found after returning home"

        ss_home_ret = "08_desktop_nav_home_returned.png"
        page.screenshot(path=os.path.join(SCREENSHOTS_DIR, ss_home_ret), full_page=False)
        reporter.add_screenshot(ss_home_ret, "Desktop Nav: Returned to Home via Header Logo")
        reporter.record_pass("Case 1.4 - Full Site Navigation & Inter-Page Loop", time.time() - t0, "Home ➔ Portal ➔ Mobs ➔ Dungeons II ➔ About ➔ Privacy ➔ Home closed-loop verified")
    except Exception as e:
        reporter.record_fail("Case 1.4 - Full Site Navigation & Inter-Page Loop", time.time() - t0, str(e))

    # -------------------------------------------------------------
    # Case 1.5: Dungeons 2 Subpage Verification
    # -------------------------------------------------------------
    t0 = time.time()
    try:
        page.goto(f"{base_url}/dungeons-2.html", wait_until="networkidle")
        title = page.title()
        assert "The Sift in Minecraft Dungeons 2" in title, f"Dungeons 2 title mismatch: '{title}'"

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
        reporter.record_pass("Case 1.5 - Dungeons 2 Subpage Verification", time.time() - t0, "dungeons-2.html loaded, SEO Title/GA4/Dual Ads/JSON-LD/Biomes/Accordion verified")
    except Exception as e:
        reporter.record_fail("Case 1.5 - Dungeons 2 Subpage Verification", time.time() - t0, str(e))

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
        portal_item = page.locator('#mobile-nav a[href*="portal.html"]').first
        portal_item.click()
        page.wait_for_load_state("networkidle")

        assert "/portal" in page.url, f"Mobile URL did not contain '/portal': '{page.url}'"
        portal_h1 = page.locator("h1").inner_text().strip()
        assert "The Sift Portal Guide" in portal_h1, f"Mobile portal H1 mismatch: '{portal_h1}'"

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
        page.goto(f"{base_url}/dungeons-2.html", wait_until="networkidle")

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
