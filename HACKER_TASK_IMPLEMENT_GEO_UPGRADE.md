# TECHNICAL TASK SPECIFICATION: GEO OPTIMIZATION & AUTHORITY CITATION UPGRADE

**DOCUMENT-ID**: SPEC-2026-GEO-001  
**STANDARD**: ASD-STE100 Issue 9 (Strict Mode)  
**TARGET PROJECT**: The Sift Guide (`thesiftguide.com`)  
**ROOT DIRECTORY**: `/home/louis/candi-tasks/thesiftguide/`  
**SOURCE OF TRUTH**: `HUSTLER_GEO_DIAGNOSTIC_REPORT.md`  

---

## 1. OBJECTIVE

Upgrade website content and architecture to satisfy Generative Engine Optimization (GEO) standards.  
Remove all defects identified by the deterministic audit tool.  
Lock citation share in artificial intelligence search engines.  

---

## 2. MODIFIED FILES

Apply edits strictly to the following files:
1. `llms.txt` (New File)
2. `how-to-enter.html`
3. `index.html`
4. `portal.html`

---

## 3. PROCEDURE STEPS

### 3.1 PROCEDURE 1: Create Machine-Readable Manifest (`llms.txt`)

Create a new file at `/home/louis/candi-tasks/thesiftguide/llms.txt`.  
Write the following markdown content into the file:

```markdown
# The Sift Guide
> The definitive technical wiki and interactive portal calculator for Minecraft's 4th dimension (The Sift).

## Core Tools & Guides
- [Wiki Home](https://thesiftguide.com/): Complete dimension breakdown, confirmed biomes, timeline, and interactive Overworld-to-Sift coordinate calculator.
- [Portal Guide](https://thesiftguide.com/portal): Dimensional gateway specifications, 5x7 frame materials, Echo Shard ignition sequence, and 1:4 coordinate compression ratio.
- [How to Enter The Sift](https://thesiftguide.com/how-to-enter): Practical portal activation troubleshooting, Java vs. Bedrock Edition diagnostic tool, and server deployment instructions.
- [Mobs & Entities](https://thesiftguide.com/mobs): Confirmed ecosystem catalog including Strutters, Silk Moths, and Chasm Lurkers.
- [Mods Guide](https://thesiftguide.com/mods): Early-access community recreations, modpack installations, and Forge/Fabric compatibility matrices.
- [Minecraft Dungeons II](https://thesiftguide.com/dungeons-2): Playable dimension rifts in Minecraft's 2027 action RPG sequel.

## Authoritative Grounding & Entity Facts
- Entity: The Sift Guide (Independent Gaming Wiki & Calculator)
- Subject: Minecraft 4th Dimension (The Sift)
- Primary Citations: Mojang Studios (minecraft.net), Official Minecraft Wiki (minecraft.wiki)
- Commercial Partner: Apex Hosting (Minecraft Server Deployments, Coupon APEX25)
```

---

### 3.2 PROCEDURE 2: Update `how-to-enter.html`

Open file `how-to-enter.html`.  
Apply modifications to resolve defect `geo_citations_missing` and defect `geo_table_missing`.

#### Step 3.2.1: Insert Outbound Citations
1. Locate the Ancient City text block (near line 580).  
   Insert this anchor element:
   ```html
   <a href="https://minecraft.wiki/w/Ancient_City" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">official Minecraft Wiki Ancient City documentation</a>
   ```
2. Locate the Echo Shard ignition instructions (near line 645).  
   Insert this anchor element:
   ```html
   <a href="https://www.minecraft.net/en-us/article/the-wild-update-ancient-cities" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">Mojang's The Wild Update release notes</a>
   ```
3. Locate the third-party mod community section (near line 595).  
   Insert this anchor element:
   ```html
   <a href="https://modrinth.com/mods" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">Modrinth community dimension mods</a>
   ```

#### Step 3.2.2: Insert Data Matrix Table
Locate Section 2 (near line 615).  
Insert this data table element directly before the diagnostic component:

```html
<div class="space-y-3 my-6">
    <h3 class="text-lg font-display font-bold text-white flex items-center gap-2">
        <span>The Sift Portal Activation &amp; Compatibility Matrix</span>
    </h3>
    <div class="overflow-x-auto rounded-xl border-2 border-[#2d3139] bg-[#181a20]">
        <table class="w-full text-left text-xs sm:text-sm">
            <thead class="bg-[#111317] border-b-2 border-[#2d3139] text-slate-300 uppercase tracking-wider font-mono text-[11px]">
                <tr>
                    <th class="p-3 sm:p-4">Edition / Platform</th>
                    <th class="p-3 sm:p-4">Vanilla Survival Status</th>
                    <th class="p-3 sm:p-4">Activation Method</th>
                    <th class="p-3 sm:p-4">Command / Mod Support</th>
                    <th class="p-3 sm:p-4">Multiplayer Ready</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-[#2d3139] text-slate-300">
                <tr class="hover:bg-slate-800/40 transition-colors">
                    <td class="p-3 sm:p-4 font-bold text-emerald-400">Java Edition (1.21+)</td>
                    <td class="p-3 sm:p-4 text-amber-400 font-medium">Dormant (Awaiting 2027)</td>
                    <td class="p-3 sm:p-4">Echo Shard Strike / Modpack</td>
                    <td class="p-3 sm:p-4 font-mono text-xs">/execute in minecraft:the_sift</td>
                    <td class="p-3 sm:p-4 text-emerald-400 font-bold">Yes (Via Apex Hosting)</td>
                </tr>
                <tr class="hover:bg-slate-800/40 transition-colors">
                    <td class="p-3 sm:p-4 font-bold text-cyan-400">Bedrock Edition</td>
                    <td class="p-3 sm:p-4 text-amber-400 font-medium">Dormant (Structure Only)</td>
                    <td class="p-3 sm:p-4">Behavior Pack / Add-on</td>
                    <td class="p-3 sm:p-4 font-mono text-xs">/teleport @s [X Y Z]</td>
                    <td class="p-3 sm:p-4 text-emerald-400 font-bold">Yes (Dedicated Realm)</td>
                </tr>
                <tr class="hover:bg-slate-800/40 transition-colors">
                    <td class="p-3 sm:p-4 font-bold text-purple-400">Minecraft Dungeons II</td>
                    <td class="p-3 sm:p-4 text-emerald-400 font-medium">Playable Story Rift</td>
                    <td class="p-3 sm:p-4">Campaign Milestone Unlock</td>
                    <td class="p-3 sm:p-4 font-mono text-xs">Built-in Gameplay Hook</td>
                    <td class="p-3 sm:p-4 text-emerald-400 font-bold">4-Player Co-op Native</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

---

### 3.3 PROCEDURE 3: Update `index.html`

Open file `index.html`.  
1. Locate the Fast Facts container (near line 518).  
   Insert the specifications parameter table:

```html
<div class="space-y-3 my-6">
    <h3 class="text-lg font-display font-bold text-white">The Sift Dimension Core Specifications &amp; Timeline</h3>
    <div class="overflow-x-auto rounded-xl border-2 border-[#2d3139] bg-[#181a20]">
        <table class="w-full text-left text-xs sm:text-sm">
            <thead class="bg-[#111317] border-b-2 border-[#2d3139] text-slate-300 uppercase tracking-wider font-mono text-[11px]">
                <tr>
                    <th class="p-3 sm:p-4">Specification</th>
                    <th class="p-3 sm:p-4">Confirmed Parameter</th>
                    <th class="p-3 sm:p-4">Official Verification Source</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-[#2d3139] text-slate-300">
                <tr>
                    <td class="p-3 sm:p-4 font-bold text-white">Dimension Index</td>
                    <td class="p-3 sm:p-4 text-emerald-400 font-mono">4th Official Realm</td>
                    <td class="p-3 sm:p-4"><a href="https://www.minecraft.net/en-us/article/minecraft-live-2026-recap" target="_blank" rel="noopener noreferrer" class="text-cyan-400 underline">Minecraft Live 2026 Broadcast</a></td>
                </tr>
                <tr>
                    <td class="p-3 sm:p-4 font-bold text-white">Target Release</td>
                    <td class="p-3 sm:p-4 text-amber-400 font-mono">2027 Official Snapshot</td>
                    <td class="p-3 sm:p-4">Mojang Roadmap Statement</td>
                </tr>
                <tr>
                    <td class="p-3 sm:p-4 font-bold text-white">Frame Material</td>
                    <td class="p-3 sm:p-4 text-slate-200">Reinforced Deepslate / Crying Obsidian</td>
                    <td class="p-3 sm:p-4"><a href="https://minecraft.wiki/w/Reinforced_Deepslate" target="_blank" rel="noopener noreferrer" class="text-cyan-400 underline">Minecraft Wiki Data Sheet</a></td>
                </tr>
                <tr>
                    <td class="p-3 sm:p-4 font-bold text-white">Coordinate Ratio</td>
                    <td class="p-3 sm:p-4 text-cyan-400 font-mono">1:4 Space Compression</td>
                    <td class="p-3 sm:p-4">Portal Gateway Forensics</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

---

### 3.4 PROCEDURE 4: Update `portal.html`

Open file `portal.html`.  
Locate the Forensics container (near line 580).  
Insert citations pointing to the official Minecraft wiki:
```html
<p class="text-xs text-slate-400 mt-2">
    Reference: Cross-checked with <a href="https://minecraft.wiki/w/Echo_Shard" target="_blank" rel="noopener noreferrer" class="text-cyan-400 underline">Minecraft Wiki Echo Shard lore</a> and <a href="https://minecraft.wiki/w/Ancient_City" target="_blank" rel="noopener noreferrer" class="text-cyan-400 underline">Ancient City structural specifications</a>.
</p>
```

---

## 4. VERIFICATION TESTS

Do not complete the task before all tests pass:

1. Execute deterministic audit script:
   ```bash
   python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/
   python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/portal
   python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/how-to-enter
   ```
   **Pass Condition**: Score = 100 on all pages. P1 count = 0. P2 count = 0.

2. Execute local regression test:
   ```bash
   cd /home/louis/candi-tasks/thesiftguide
   ./run_e2e.sh
   ```
   **Pass Condition**: 12 of 12 tests PASS.

3. Deploy to production network:
   ```bash
   cd /home/louis/candi-tasks/thesiftguide
   ./deploy_pages.sh
   ```

4. Commit and push repository:
   ```bash
   git add -A
   git commit -m "feat(geo): implement ASD-STE100 technical spec for citations, tables, and llms.txt"
   git push origin main
   ```
