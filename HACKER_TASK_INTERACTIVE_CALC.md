# Hacker Task Work Order: Add Interactive "The Sift Portal & Coordinate Calculator" to thesiftguide.com

## Objective
Embed an industrial-grade, 100% vanilla JavaScript, zero-external-dependency interactive widget into `/home/louis/candi-tasks/thesiftguide/index.html`.
This turns the page from a passive article into an interactive utility tool, dramatically increasing user session duration (Dwell Time) and lowering bounce rate.

## Target File
- `/home/louis/candi-tasks/thesiftguide/index.html`

## Hard Constraints (Mandatory Red Lines)
1. **Preserve ALL Existing Assets**:
   - Google Analytics GA4 tag (`G-X1ZTW8XWPG`)
   - Schema.org JSON-LD structured data graph
   - Open Graph (`og:image`, etc.) and Twitter Card meta tags
   - Favicon links (`favicon.svg`, `apple-touch-icon.png`, etc.)
   - Adsterra advertisement container (`key: e34c08305944ef076210b30b1897f6eb`)
   - All existing 1,158+ words of high-ranking SEO copy, headings, and FAQ.
2. **Visual Consistency (Minecraft Deepslate Palette)**:
   - Container: `#181a20` (Minecraft stone panel) with `border-2 border-[#2d3139]` and subtle block shadow (`shadow-[0_4px_0_#0d0e11]`).
   - Button states: `mc-btn-primary` (grass green `#46a228`) and `mc-btn-stone` with 3D press effect (`active:translate-y-0.5`).
   - Accent highlights: Diamond cyan (`#22d3ee`), Gold amber (`#f59e0b`), Soul blue (`#38bdf8`).
3. **Pure Vanilla JS & Zero Layout Shift (CLS = 0)**:
   - No external libraries (no React, no jQuery, no unpkg).
   - Wrap script in `(function() { ... })();` to avoid global namespace pollution.
   - Fixed or min-height containers so recalculation never causes page jumping.

## Widget Specification: "The Sift Portal & Coordinate Calculator"

### Section Placement
- Insert as an interactive tool section with `id="calculator"` and `class="scroll-mt-24"`.
- Position: Between Section 01 (What is The Sift?) and the Sponsored Adsterra Banner, OR right below Fast Facts.
- Add `<a href="#calculator">` to the top header desktop navigation and the Hero "Jump to" chips!

### Features
1. **Mode A: Cross-Dimension Coordinate Converter**:
   - Select Direction:
     - `Overworld ➔ The Sift` (Default)
     - `The Sift ➔ Overworld`
     - `Nether ➔ The Sift`
   - Coordinate Inputs:
     - `X` coordinate (number input, default 1200)
     - `Y` coordinate (number input, default 64)
     - `Z` coordinate (number input, default -800)
   - Compression Ratio Dropdown / Radio:
     - `1:4 Rift Ratio` (Speculated standard rift compression)
     - `1:8 Nether Equivalent`
     - `1:16 Deep Void Ratio`
   - Live Results Display:
     - Big pixel-styled readout for Target X, Target Y, Target Z.
     - Travel Distance / Net distance calculation.
     - "Copy /tp Command" or "Copy Coordinates" button with instant visual tooltip ("Copied!").

2. **Mode B: Portal Frame Material Estimator (Tab or toggle)**:
   - Portal Shape/Size selector:
     - `Standard 4×5 Frame` (10 blocks minimum / 14 blocks with corners)
     - `Compact 3×3 Frame` (8 blocks minimum)
     - `Ancient Rift Arch 7×9` (20 blocks minimum / 28 blocks with corners)
   - Toggle: "Include Corner Blocks" (Checkbox or switch)
   - Calculated Bill of Materials:
     - Soul-infused Deepslate / Crying Obsidian needed
     - Echo Shards required for frame charging (e.g. 4x for catalyst)
     - Soul Fire / Ignition tools required

3. **Polished Interactions**:
   - All recalculations happen instantly on input (`input` / `change` event listeners).
   - Mobile-safe: Inputs stack cleanly on narrow mobile viewports (`flex-col sm:flex-row`).
   - Fully accessible with proper labels, `aria-live="polite"` on output boxes.

## Execution Method
1. Create a safe backup of `index.html`.
2. Write a Python script to reliably insert the calculator HTML and JavaScript into the appropriate position in `index.html`.
3. Verify that the file opens cleanly, contains all required red-line tags, and syntax is valid.
4. Run `deploy-and-bind.sh` to deploy to Cloudflare Pages.
