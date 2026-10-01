# Hacker Task Work Order: Multi-Page Expansion for thesiftguide.com

## Objective
Expand `thesiftguide.com` from a single-page website into a structured, authoritative 5-page Minecraft community wiki and utility site.
This satisfies Google HCU (Helpful Content System) multi-intent evaluation and meets Google AdSense mandatory compliance requirements.

## Directory & Files
Working Directory: `/home/louis/candi-tasks/thesiftguide`
Pages to create / update:
1. `portal.html` - Deep-dive guide to The Sift Portal (ancient city lore, frame blocks, ignition mechanics)
2. `mobs.html` - Comprehensive bestiary of The Sift (The Giant Frog, bone scavengers, soul wisps, stats table)
3. `about.html` - Project background, mission, editorial standards, and contact info (AdSense compliance requirement)
4. `privacy.html` - Standard Privacy Policy covering GA4, cookies, advertising partners, and CCPA/GDPR compliance (AdSense mandatory requirement)
5. `index.html` - Update header navigation bar and footer to link seamlessly across all 5 pages
6. `sitemap.xml` - Include all 5 URLs with proper `<loc>`, `<lastmod>`, and `<priority>` tags

## Red Lines & Shared Standards
1. **Global Assets on EVERY Page**:
   - Google Analytics GA4 tag (`G-X1ZTW8XWPG`) in `<head>`
   - Favicon links (`favicon.svg`, `favicon-32x32.png`, `apple-touch-icon.png`, `favicon.ico`)
   - Open Graph & Twitter Cards (`og:image` pointing to `https://thesiftguide.com/og-image.png`)
   - Tailwind CDN (`https://cdn.tailwindcss.com/3.4.17`) with the identical Minecraft custom theme config
   - Consistent `#111317` deepslate background, `#181a20` stone panels, and `#2d3139` borders
2. **Unified Navigation (Header & Footer)**:
   - Header Links:
     - Logo: `The Sift Guide` -> `/`
     - `Wiki Home` -> `/`
     - `Portal Guide` -> `/portal.html`
     - `Mobs & Entities` -> `/mobs.html`
     - `Calculator` -> `/#calculator`
     - `About` -> `/about.html`
   - Footer Links:
     - Includes links to `/`, `/portal.html`, `/mobs.html`, `/about.html`, and `/privacy.html`.
3. **Structured Data (Schema.org JSON-LD)**:
   - Each page must have dedicated `@type`: `Article` / `WebPage` or `FAQPage` with accurate canonical URLs.

## Content Specifications

### Page 1: `portal.html` (The Sift Portal Guide)
- Title: `The Sift Portal Guide: How to Build, Frame Blocks & Activation | The Sift Minecraft`
- Description: `Complete guide to The Sift dimension portal in Minecraft. Discover ancient city theories, frame block requirements, soul fire ignition, and rift linkage mechanics.`
- Main Sections:
  1. The Ancient City Portal Theory (Reinforced Deepslate structure in Ancient Cities, 23x23 frame, warden connection)
  2. Confirmed & Speculated Frame Blocks (Soul Crying Obsidian, Echo Shards, Sculk catalysts)
  3. Step-by-Step Portal Construction & Sizing Guide
  4. Dimensional Ratio & Linkage Rules (1:4 compression ratio vs Nether 1:8)
  5. FAQ Section with schema markup

### Page 2: `mobs.html` (The Sift Mobs & Fauna)
- Title: `The Sift Mobs & Fauna: The Giant Frog, Soul Wisps & Entities | Minecraft Guide`
- Description: `Meet all confirmed and speculated mobs in Minecraft The Sift dimension: The Giant Vibrant Frog, Carapace bone crawlers, Soul Wisps, and void predators.`
- Main Sections:
  1. Featured Creature: The Colossal Meadow Frog (behavior, soul-lily eating, tether mechanics, rideability)
  2. The Carapace Scavengers (bone fossil predators, armor piercing)
  3. Ambient Life: Soul Wisps and Spore Gliders
  4. Complete Creature Comparison Table (Health, Biome, Hostility, Drops)
  5. FAQ Section with schema markup

### Page 3: `about.html` (About & Editorial Standards)
- Title: `About Us | The Sift Minecraft Guide`
- Description: `About The Sift Guide: an independent, community-driven wiki and research project tracking Minecraft's 4th dimension announced at Minecraft Live 2026.`
- Sections: Mission statement, research methodology (official Mojang stream forensics, developer interviews, snapshot tracking), editorial disclosure (not affiliated with Mojang/Microsoft), contact channels.

### Page 4: `privacy.html` (Privacy Policy)
- Title: `Privacy Policy | The Sift Guide`
- Description: `Privacy policy for The Sift Guide explaining data collection, cookies, Google Analytics, and third-party advertising partners.`
- Standard professional policy covering log files, cookies/web beacons, Google Analytics 4, Adsterra/AdSense advertising cookies, CCPA/GDPR rights.

## Execution Steps
1. Create `portal.html`, `mobs.html`, `about.html`, and `privacy.html` following the design and layout of `index.html`.
2. Update navigation in `index.html` to link to these subpages.
3. Update `sitemap.xml` to list all 5 URLs.
4. Run verification script to check:
   - GA4, OG tags, Favicon, Schema on all 5 HTML files.
   - Inter-page links work cleanly.
5. Deploy to Cloudflare Pages using `deploy-and-bind.sh` (or wrangler deploy).
6. Verify live URLs return HTTP 200.
