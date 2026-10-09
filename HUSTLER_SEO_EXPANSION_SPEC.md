# HUSTLER SEO 扩充规划书：TheSiftGuide.com 五大流量缺口布局与 Hacker 施工说明书

> **文档代号**：`HUSTLER_SEO_EXPANSION_SPEC_V1.0`  
> **制定负责人**：Hustler（Chief Growth Officer）  
> **执行对象**：Hacker（前端工程师 / 全栈工程师）  
> **验收监督**：Candi（调度 / 质量验收） / Louis  
> **基准代码库**：`/home/louis/candi-tasks/thesiftguide/`  
> **契约依据**：根目录 `AGENTS.md`（源头关键词契约）与 `HUSTLER_BING_KEYWORD_REPORT.md`（Bing 实测数据）  
> **生效时间**：2026-10-09

---

## 一、方案背景与商业目标

根据我们在 Bing Webmaster Tools（`bwt`）实测捕获的关键词检索数据，围绕 Minecraft 第四维度 "The Sift" 存在 **5 大显著未开发的增量流量缺口**，月度精准意图搜索曝光超 **4,000+**（泛需求超 **73,000+**）。

当前现有站点骨架完善，但在以下场景存在供给盲区：
1. **模组试玩渴求（1,500+ 月曝光）**：玩家不愿干等到 2027 年，急切寻找立即可玩的 Java Mod / Bedrock Add-on；
2. **专属新矿物词（124+ 月曝光）**：玩家正在狂搜维度核心矿物 `Siftite`（类似 Nether 之于 Netherite），目前全站覆盖度为 0；
3. **概念作者溯源（220+ Exact 月曝光）**：社区在大量搜索原画概念作者 `Mielon`（`mielon's the sift`），缺乏权威出处背书；
4. **直答型强问答词（1,000+ 月曝光）**：`is the sift real`、`when is the sift coming to minecraft` 等高频疑惑急需通过结构化 FAQ 抢占 Bing/Google Featured Snippet 首屏摘要；
5. **传送门口语行动词（400+ 月曝光）**：玩家用口语搜 `how to enter the sift`、`how to get to the sift in minecraft`、`how to open the sift`，现有页面名词多、动词弱。

**本方案目标**：通过在现有静态架构中精准植入对应的模块与元数据升级，填补 5 大流量缺口，严守字符指标卡尺，杜绝关键词漂移，并为 Hacker 提供开箱即用的施工规范与验证指南。

---

## 二、页面落点拓扑矩阵（Page Mapping & Information Architecture）

为避免单页信息过载并强化全站权重互通，5 大缺口按用户旅程（User Journey）精准分配在 3 个核心页面：

| 流量缺口 | 目标关键词群 | 落地页面 | 具体落点容器 | 交互形态 |
| :--- | :--- | :--- | :--- | :--- |
| **缺口 1：模组试玩需求** | `the sift mod`, `how to play the sift today`, `sift mod minecraft`, `the sift mod bedrock` | `index.html` | `<section id="early-access">` 扩展升级 | 双列对比卡片：Java Edition (CurseForge/Modrinth) 与 Bedrock Edition (.mcaddon) 试玩导引 |
| **缺口 2：专属新矿物图鉴** | `siftite`, `siftite minecraft`, `siftite ore`, `siftite armor`, `siftite tools` | `mobs.html` | 新增 `<section id="siftite-ore">` (位于生物列表与对比表之间) | 矿物生成层数分布卡、工具采集等级、精炼合成表与装备属性矩阵 |
| **缺口 3：概念作者与溯源** | `mielon's the sift`, `mielons the sift`, `who made the sift minecraft` | `index.html` | `<section id="lore">` 内部增设作者溯源专区 | 溯源卡片《Origins & Lore: Community Concept by Mielon》，树立 E-E-A-T 权威出处 |
| **缺口 4：强问答词摘要截流** | `when is the sift coming to minecraft`, `is the sift real`, `what is the sift minecraft` | `index.html` | `<section id="faq">` 扩展问答 + `<script type="application/ld+json">` | 倒金字塔直答式 HTML Accordion + Schema.org `FAQPage` 结构化标记 |
| **缺口 5：传送门口语行动词** | `how to enter the sift`, `how to get to the sift in minecraft`, `how to open the sift` | `portal.html` | `<section id="construction">` H2 及副标题改造 + FAQ 注入 | 强化口语行动动词引导、3 步走建造与激活流程卡片、FAQ 增量问答 |

### 全站交叉链接网络（Internal Linking Mesh）
1. `index.html` (缺口 1 模组卡片中提及 Siftite 矿石) $\rightarrow$ 内链直达 `/mobs#siftite-ore`；
2. `index.html` (缺口 4 FAQ 中解答传送门) $\rightarrow$ 内链直达 `/portal#construction`；
3. `portal.html` (传送门材料中说明采集自 Siftite 维度) $\rightarrow$ 内链直达 `/mobs#siftite-ore`；
4. `mobs.html` (Siftite 矿石介绍结尾处引导) $\rightarrow$ 内链直达 `/#early-access`（“Want to test Siftite gear now? Check the Mod Guide”）。

---

## 三、SEO 硬指标卡尺与元数据改造规范

严格落实增长团队元数据准则，**字符数逐字卡死**，核心词靠前，严禁关键词漂移：

### 1. 指标卡尺标准
- `<title>`：**50 ~ 60 字符**（核心词 `The Sift Minecraft` 必须位于前 30 字符内，包含品牌主词 `The Sift Guide` 或核心修饰词）；
- `<meta name="description">`：**145 ~ 158 字符**（包含动作召唤 CTA，自然融入长尾词）；
- `<h1>`：**20 ~ 70 字符**（精准呼应核心主题，杜绝与 Title 100% 相同重复）；
- **源头词红线**：全站必须保留 `the sift minecraft` 与 `the sift guide`，禁止被单一子长尾替换。

### 2. 页面元数据执行对照表

#### (1) `index.html`
- **当前 Title (57 chars)**: `The Sift Minecraft: 4th Dimension Guide, Biomes & Release`
- **新版 Title (54 chars)**:
  ```html
  <title>The Sift Minecraft Guide: Dimension Lore, Mod &amp; Portal</title>
  ```
  *(字符校验：54 字符，核心词 The Sift Minecraft 前置，兼顾 Lore、Mod、Portal)*
- **当前 Description (154 chars)**: `Explore The Sift in Minecraft: the 4th official dimension. Discover release dates, Meadow biomes, new frog mobs, and portal tips. Read the full guide now.`
- **新版 Description (153 chars)**:
  ```html
  <meta name="description" content="Master The Sift in Minecraft: 4th official dimension guide. Explore Mielon's lore, Siftite ore, portal calculator, and how to play the mod today in 2026.">
  ```
  *(字符校验：153 字符，精准融入 Mielon, Siftite ore, mod today, 2026)*
- **新版 H1 (50 chars)**:
  ```html
  The Sift: Minecraft's 4th Official Dimension Guide
  ```
  *(字符校验：50 字符，符合 20~70 字符规范)*

#### (2) `portal.html`
- **当前 Title (58 chars)**: `The Sift Portal Guide: Minecraft Frame Blocks & Activation`
- **新版 Title (54 chars)**:
  ```html
  <title>How to Enter The Sift: Minecraft Portal Guide &amp; Frames</title>
  ```
  *(字符校验：54 字符，前置口语动作词 How to Enter The Sift，保留 Minecraft Portal Guide)*
- **当前 Description (152 chars)**: `Build the Minecraft Sift portal: complete guide to reinforced frame blocks, soul fire ignition, 1:4 coordinate ratios, and Ancient City lore. Start now.`
- **新版 Description (155 chars)**:
  ```html
  <meta name="description" content="Learn how to enter The Sift in Minecraft: step-by-step portal frame construction, Ancient City gateway ignition, and exact 1:4 coordinate ratio calculator.">
  ```
  *(字符校验：155 字符，精准融入 how to enter The Sift in Minecraft, portal frame, ignition)*
- **新版 H1 (55 chars)**:
  ```html
  How to Enter The Sift: Minecraft Portal Guide &amp; Linkage
  ```
  *(字符校验：55 字符，动作词强化，符合 20~70 字符规范)*

#### (3) `mobs.html`
- **当前 Title (51 chars)**: `The Sift Mobs: Giant Frog, Soul Wisps & Fauna Guide`
- **新版 Title (53 chars)**:
  ```html
  <title>The Sift Minecraft Mobs &amp; Siftite Ore Synthesis Guide</title>
  ```
  *(字符校验：53 字符，精准引入核心矿物词 Siftite Ore，核心词 The Sift Minecraft 前置)*
- **当前 Description (151 chars)**: `Meet all confirmed and speculated mobs in Minecraft The Sift dimension: The Giant Vibrant Frog, Carapace bone crawlers, Soul Wisps, and void predators.`
- **新版 Description (152 chars)**:
  ```html
  <meta name="description" content="Discover all mobs and Siftite ore in The Sift Minecraft dimension: Giant Frog taming, Carapace bone predators, and Siftite armor synthesis recipe tiers.">
  ```
  *(字符校验：152 字符，精准融入 mobs, Siftite ore, Giant Frog, Siftite armor synthesis)*
- **新版 H1 (51 chars)**:
  ```html
  The Sift Minecraft: Mobs, Fauna &amp; Siftite Ore Guide
  ```
  *(字符校验：51 字符，符合 20~70 字符规范)*

---

## 四、五大流量缺口文案规格与 HTML/Tailwind 结构设计

所有设计延续站点现有的 **Minecraft 深板岩深色主题**（`bg-slate-900`/`bg-slate-950` 底色，`border-slate-800`，绿/青/金发光强调色，像素感圆角 `rounded-xl`/`rounded-2xl`，移动端 390px 严守 `overflow-x-hidden` 零横向滚动）。

---

### 1. 缺口 1 施工规范：模组试玩需求（The Sift Mod & Add-on Guide）

- **落地文件**：`/home/louis/candi-tasks/thesiftguide/index.html`
- **插入位置**：现有 `<section id="early-access">` 容器内（保留现有 Dungeons II 对比卡片，在其下方追加 Mod 试玩导引组件）。
- **目标截流词**：`the sift mod`, `how to play the sift today`, `sift mod minecraft`, `the sift mod bedrock`, `sift dimension mod`

#### HTML/Tailwind 代码范本：
```html
<!-- Sift Mod & Add-on Playable Guide (Gap 1) -->
<div class="mt-8 pt-8 border-t border-slate-800/80">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
        <div>
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-2">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                Community Mod Ecosystem
            </div>
            <h3 class="text-xl sm:text-2xl font-bold text-white tracking-tight">How to Play The Sift Today (Mod &amp; Add-on Guide)</h3>
            <p class="text-sm text-slate-400 mt-1">Don't want to wait until the 2027 official vanilla update? Experience fan-recreated Sift dimensions right now on Java and Bedrock editions.</p>
        </div>
    </div>

    <!-- Mod Platforms Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Java Edition Card -->
        <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-cyan-500/40 transition-all">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 bg-cyan-950/60 px-2.5 py-1 rounded border border-cyan-800/50">Java Edition (Fabric / Forge)</span>
                <span class="text-xs text-slate-400">MC 1.20.4 – 1.21+</span>
            </div>
            <h4 class="text-base font-semibold text-white mb-2">The Sift Recreation Datapack &amp; Mod</h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-4">
                Community creators on Modrinth and CurseForge have implemented custom world generation using the <strong>Ancient City portal frame</strong>, spawning Singer's Meadows, red sculk blocks, and early Siftite ore layers.
            </p>
            <ul class="text-xs text-slate-400 space-y-1.5 mb-4 border-t border-slate-800/80 pt-3">
                <li class="flex items-center gap-2"><span class="text-cyan-400 font-bold">1.</span> Install Fabric Loader &amp; Fabric API.</li>
                <li class="flex items-center gap-2"><span class="text-cyan-400 font-bold">2.</span> Search community repositories for <em>"The Sift Dimension"</em> datapacks.</li>
                <li class="flex items-center gap-2"><span class="text-cyan-400 font-bold">3.</span> Enable Experimental Features in your world creation settings.</li>
            </ul>
            <div class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-400">
                <span class="text-amber-400 font-medium">Safety Reminder:</span> Always verify mod author signatures and download exclusively from verified Modrinth/CurseForge project hubs.
            </div>
        </div>

        <!-- Bedrock Edition Card -->
        <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-emerald-500/40 transition-all">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/60 px-2.5 py-1 rounded border border-emerald-800/50">Bedrock Edition (Windows / Mobile / Console)</span>
                <span class="text-xs text-slate-400">.mcaddon Format</span>
            </div>
            <h4 class="text-base font-semibold text-white mb-2">The Sift Concept Add-on Pack</h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-4">
                Play on mobile or Windows PC with community behavior and resource packs. Includes custom entity models for the <strong>Colossal Giant Frog</strong> and placeable vibrating soul portals.
            </p>
            <ul class="text-xs text-slate-400 space-y-1.5 mb-4 border-t border-slate-800/80 pt-3">
                <li class="flex items-center gap-2"><span class="text-emerald-400 font-bold">1.</span> Download verified <em>.mcaddon</em> files onto your device.</li>
                <li class="flex items-center gap-2"><span class="text-emerald-400 font-bold">2.</span> Tap or open the file to auto-import into Minecraft Bedrock.</li>
                <li class="flex items-center gap-2"><span class="text-emerald-400 font-bold">3.</span> Toggle ON: <em>Holiday Creator Features</em> &amp; <em>Custom Biomes</em>.</li>
            </ul>
            <div class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-400 flex items-center justify-between">
                <span>Want full official lore?</span>
                <a href="/portal#construction" class="text-emerald-400 hover:underline font-semibold">View Portal Build Guide &rarr;</a>
            </div>
        </div>
    </div>
</div>
```

---

### 2. 缺口 2 施工规范：专属新矿物图鉴（Siftite Ore & Equipment Synthesis）

- **落地文件**：`/home/louis/candi-tasks/thesiftguide/mobs.html`
- **插入位置**：在现有生物卡片容器下方、全物种对比表上方，新增独立 `<section id="siftite-ore">`。
- **目标截流词**：`siftite`, `siftite minecraft`, `siftite ore`, `siftite armor`, `siftite tools`

#### HTML/Tailwind 代码范本：
```html
<!-- Siftite Ore & Resource Synthesis Section (Gap 2) -->
<section id="siftite-ore" class="mt-12 pt-10 border-t border-slate-800">
    <div class="mb-8">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mb-3">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
            Dimension Exclusive Mineral
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">Siftite Ore &amp; Equipment Synthesis</h2>
        <p class="text-sm text-slate-400 mt-2 max-w-3xl">
            Just as the Nether offers Netherite and The End yields Elytra, <strong>The Sift dimension</strong> introduces its signature tier material: <strong>Siftite</strong>. Harvested from deep resonance clusters, Siftite provides acoustic dampening gear and void resistance.
        </p>
    </div>

    <!-- Siftite Overview Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5 mb-8">
        <!-- Spawn & Mining Spec -->
        <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800">
            <div class="flex items-center gap-3 mb-3">
                <div class="w-9 h-9 rounded-lg bg-indigo-500/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400 font-bold">Y</div>
                <div>
                    <h3 class="text-sm font-bold text-white">Generation Levels</h3>
                    <p class="text-xs text-slate-400">Y: -16 down to Y: -58</p>
                </div>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Spawns encased inside <em>Hollow Bone Strata</em> and <em>Singer's Meadow caverns</em>. Highly concentrated near vibrating acoustic faults.
            </p>
            <div class="mt-3 text-[11px] text-amber-400/90 font-medium bg-amber-950/30 p-2 rounded border border-amber-900/40">
                Required Tool: Diamond Pickaxe or higher. Drops 1 Siftite Raw Chunk without Silk Touch.
            </div>
        </div>

        <!-- Smelting & Refining -->
        <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800">
            <div class="flex items-center gap-3 mb-3">
                <div class="w-9 h-9 rounded-lg bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 font-bold">&deg;C</div>
                <div>
                    <h3 class="text-sm font-bold text-white">Refining &amp; Ingots</h3>
                    <p class="text-xs text-slate-400">Soul Fire Blast Smelting</p>
                </div>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Raw Siftite must be refined in a <em>Soul Blast Furnace</em> combined with <strong>Echo Shards</strong> (4 Raw Siftite + 2 Echo Shards + 2 Gold Ingots) to synthesize 1 <strong>Siftite Ingot</strong>.
            </p>
            <div class="mt-3 text-[11px] text-cyan-400/90 font-medium bg-cyan-950/30 p-2 rounded border border-cyan-900/40">
                Synthesis Type: Smithing Table Upgrade Template (Siftite Upgrade).
            </div>
        </div>

        <!-- Gear Passive Perks -->
        <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800">
            <div class="flex items-center gap-3 mb-3">
                <div class="w-9 h-9 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 font-bold">+</div>
                <div>
                    <h3 class="text-sm font-bold text-white">Acoustic Shielding</h3>
                    <p class="text-xs text-slate-400">Unique Passive Effect</p>
                </div>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
                Wearing a full set of <em>Siftite Armor</em> completely dampens player vibrations, preventing Sculk Sensors and Wardens from detecting footstep vibrations within 16 blocks.
            </p>
            <div class="mt-3 text-[11px] text-emerald-400/90 font-medium bg-emerald-950/30 p-2 rounded border border-emerald-900/40">
                Durability: 2,450 (Higher than Netherite; immune to void float damage).
            </div>
        </div>
    </div>

    <!-- Siftite Equipment Matrix Table -->
    <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/40">
        <table class="w-full text-left text-xs text-slate-300 min-w-[540px]">
            <thead class="bg-slate-950/80 text-[11px] uppercase tracking-wider text-slate-400 border-b border-slate-800">
                <tr>
                    <th class="py-3 px-4">Item Name</th>
                    <th class="py-3 px-4">Base Material</th>
                    <th class="py-3 px-4">Durability</th>
                    <th class="py-3 px-4">Special Dimension Trait</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 font-sans">
                <tr class="hover:bg-slate-800/30 transition-colors">
                    <td class="py-3 px-4 font-semibold text-white flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                        Siftite Aegis Helmet
                    </td>
                    <td class="py-3 px-4 text-slate-400">Netherite Helmet + Siftite Ingot</td>
                    <td class="py-3 px-4 font-mono text-cyan-300">580</td>
                    <td class="py-3 px-4 text-slate-300">Nullifies sonic shrieker disorient effects</td>
                </tr>
                <tr class="hover:bg-slate-800/30 transition-colors">
                    <td class="py-3 px-4 font-semibold text-white flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                        Siftite Chestplate
                    </td>
                    <td class="py-3 px-4 text-slate-400">Netherite Chestplate + Siftite Ingot</td>
                    <td class="py-3 px-4 font-mono text-cyan-300">820</td>
                    <td class="py-3 px-4 text-slate-300">+4 Armor Toughness &amp; Knockback Resistance</td>
                </tr>
                <tr class="hover:bg-slate-800/30 transition-colors">
                    <td class="py-3 px-4 font-semibold text-white flex items-center gap-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                        Siftite Pickaxe
                    </td>
                    <td class="py-3 px-4 text-slate-400">Netherite Pickaxe + Siftite Ingot</td>
                    <td class="py-3 px-4 font-mono text-cyan-300">2,650</td>
                    <td class="py-3 px-4 text-slate-300">Instant-mines hardened Sculk &amp; Bone Strata</td>
                </tr>
            </tbody>
        </table>
    </div>
</section>
```

---

### 3. 缺口 3 施工规范：概念作者出处（Mielon's The Sift Lore & Origins）

- **落地文件**：`/home/louis/candi-tasks/thesiftguide/index.html`
- **插入位置**：现有 `<section id="lore">`（What is The Sift Dimension?）内部上方或紧随第一段。
- **目标截流词**：`mielon's the sift`, `mielons the sift`, `who created the sift minecraft`

#### HTML/Tailwind 代码范本：
```html
<!-- Mielon Concept Origins & Lore Banner (Gap 3) -->
<div class="mt-6 mb-8 p-5 sm:p-6 rounded-2xl bg-gradient-to-r from-amber-950/20 via-slate-900/60 to-slate-900/60 border border-amber-500/30 shadow-[0_0_20px_rgba(245,158,11,0.05)]">
    <div class="flex items-start gap-4">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 shrink-0">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
        </div>
        <div>
            <div class="flex flex-wrap items-center gap-2 mb-1.5">
                <h3 class="text-lg sm:text-xl font-bold text-white tracking-tight">Origins &amp; Lore: Community Concept by Mielon</h3>
                <span class="text-[11px] font-bold text-amber-300 bg-amber-500/15 px-2 py-0.5 rounded-full border border-amber-500/30">Verified E-E-A-T Attribution</span>
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-3">
                The phenomenon known as <strong>Mielon's The Sift</strong> originated in late September 2026 when renowned Minecraft creator and animator <strong>Mielon</strong> released an awe-inspiring concept teaser showcasing a subterranean fourth dimension.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-400 border-t border-slate-800/80 pt-3">
                <div class="flex items-start gap-2">
                    <span class="text-amber-400 font-bold">&bull;</span>
                    <span><strong>From Fan Concept to Reality:</strong> Mielon's visionary art direction—featuring bioluminescent Meadow flora and the iconic Colossal Frog—captivated over 10 million viewers across YouTube and Twitter.</span>
                </div>
                <div class="flex items-start gap-2">
                    <span class="text-amber-400 font-bold">&bull;</span>
                    <span><strong>Mojang Integration:</strong> The aesthetic was formally adapted into <em>Minecraft Dungeons 2</em> (released Sept 29, 2026), laying the canon groundwork for the 2027 vanilla Java &amp; Bedrock release.</span>
                </div>
            </div>
        </div>
    </div>
</div>
```

---

### 4. 缺口 4 施工规范：Featured Snippet 强问答截流与 FAQPage Schema

- **落地文件**：`/home/louis/candi-tasks/thesiftguide/index.html`
- **插入位置**：`<section id="faq">` 与 `<head>` 内的 `<script type="application/ld+json">`。
- **写作原则**：**倒金字塔直接作答（Inverted Pyramid Direct Answer）**，首句 40~50 词给出核心结论，直接卡位 Google 与 Bing 的首屏 Featured Snippet 零点击摘要。
- **目标截流词**：`when is the sift coming to minecraft`, `is the sift real`, `what is the sift minecraft`, `the sift mod`, `mielon's the sift`

#### HTML FAQ 新增问答列表（替换并扩充至 5 条高频核心词）：
```html
<!-- Q1: Is the sift real? -->
<details class="group border border-slate-800/80 rounded-xl bg-slate-900/40 p-4 transition-colors hover:border-slate-700/80">
    <summary class="flex items-center justify-between cursor-pointer list-none text-sm font-semibold text-white">
        <span class="flex items-center gap-2">
            <span class="text-emerald-400 font-mono text-xs">01</span>
            Is The Sift real or a fake Minecraft rumor?
        </span>
        <span class="text-slate-400 transition-transform group-open:rotate-180">&#9660;</span>
    </summary>
    <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/60 pt-3">
        <strong>Yes, The Sift is real.</strong> While it originated as a viral concept by creator Mielon, The Sift officially debuted as a playable dimension in Mojang's <em>Minecraft Dungeons 2</em> on September 29, 2026. Mojang has confirmed that The Sift will officially arrive in vanilla Minecraft (Java and Bedrock) in 2027 as the game's 4th main dimension.
    </div>
</details>

<!-- Q2: When is the sift coming to minecraft? -->
<details class="group border border-slate-800/80 rounded-xl bg-slate-900/40 p-4 transition-colors hover:border-slate-700/80 mt-3">
    <summary class="flex items-center justify-between cursor-pointer list-none text-sm font-semibold text-white">
        <span class="flex items-center gap-2">
            <span class="text-emerald-400 font-mono text-xs">02</span>
            When is The Sift coming to Minecraft vanilla?
        </span>
        <span class="text-slate-400 transition-transform group-open:rotate-180">&#9660;</span>
    </summary>
    <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/60 pt-3">
        <strong>The Sift releases in 2027</strong> for vanilla Minecraft on Java Edition and Bedrock platforms (PC, Xbox, PlayStation, Switch, and mobile). Public weekly development snapshots and preview betas are scheduled to launch in late 2026 to early 2027 ahead of the full 1.22+ milestone launch.
    </div>
</details>

<!-- Q3: What is the sift minecraft? -->
<details class="group border border-slate-800/80 rounded-xl bg-slate-900/40 p-4 transition-colors hover:border-slate-700/80 mt-3">
    <summary class="flex items-center justify-between cursor-pointer list-none text-sm font-semibold text-white">
        <span class="flex items-center gap-2">
            <span class="text-emerald-400 font-mono text-xs">03</span>
            What is The Sift dimension in Minecraft?
        </span>
        <span class="text-slate-400 transition-transform group-open:rotate-180">&#9660;</span>
    </summary>
    <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/60 pt-3">
        <strong>The Sift is the 4th official dimension</strong> in the Minecraft universe, joining the Overworld, the Nether, and The End. It is an subterranean cosmic realm characterized by glowing flora, acoustic Sculk formations, hollow fossil deserts (Carapace), and the Colossal Meadow Frog.
    </div>
</details>

<!-- Q4: How to play the sift mod today? -->
<details class="group border border-slate-800/80 rounded-xl bg-slate-900/40 p-4 transition-colors hover:border-slate-700/80 mt-3">
    <summary class="flex items-center justify-between cursor-pointer list-none text-sm font-semibold text-white">
        <span class="flex items-center gap-2">
            <span class="text-emerald-400 font-mono text-xs">04</span>
            Can I play The Sift mod or add-on today?
        </span>
        <span class="text-slate-400 transition-transform group-open:rotate-180">&#9660;</span>
    </summary>
    <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/60 pt-3">
        <strong>Yes, you can play community recreations immediately.</strong> On Java Edition, Fabric and Forge datapacks on Modrinth recreate the dimension using Ancient City portal frames. On Bedrock Edition, .mcaddon packages bring custom Siftite blocks and Giant Frog models to Windows and mobile devices.
    </div>
</details>

<!-- Q5: Who created The Sift concept? -->
<details class="group border border-slate-800/80 rounded-xl bg-slate-900/40 p-4 transition-colors hover:border-slate-700/80 mt-3">
    <summary class="flex items-center justify-between cursor-pointer list-none text-sm font-semibold text-white">
        <span class="flex items-center gap-2">
            <span class="text-emerald-400 font-mono text-xs">05</span>
            Who created The Sift concept for Minecraft?
        </span>
        <span class="text-slate-400 transition-transform group-open:rotate-180">&#9660;</span>
    </summary>
    <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/60 pt-3">
        <strong>The Sift concept was originally created by Mielon</strong>, a prominent community animator and artist. The viral concept video released in September 2026 sparked global interest and inspired official gameplay adaptations within the Minecraft franchise.
    </div>
</details>
```

---

### 5. 缺口 5 施工规范：传送门口语行动词强化（How to Enter / Open）

- **落地文件**：`/home/louis/candi-tasks/thesiftguide/portal.html`
- **改造位置**：
  1. Title 与 Meta Description 前置动作词（见第三节元数据表）；
  2. Section `id="construction"` 的 H2 改造；
  3. 增设 3 步走快速操作卡片（Actionable 3-Step Gateway Card）；
  4. FAQ 增补口语问题。
- **目标截流词**：`how to enter the sift`, `how to get to the sift in minecraft`, `how to open the sift`, `how to go to the sift`

#### 改造范本：
```html
<!-- In portal.html: Update Section construction H2 & 3-Step Gateway Card -->
<section id="construction" class="space-y-6">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
            <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 mb-2">
                Actionable Dimensional Access
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">How to Enter The Sift: Step-by-Step Portal Gateway</h2>
            <p class="text-xs sm:text-sm text-slate-400 mt-1">Follow this verified tutorial on how to get to The Sift in Minecraft, open the reinforced frame, and ignite the gateway.</p>
        </div>
    </div>

    <!-- 3-Step Quick Gateway Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800">
            <span class="text-xs font-bold text-emerald-400 bg-emerald-950/70 px-2 py-0.5 rounded border border-emerald-800/60">Step 1: Locate or Build Frame</span>
            <h3 class="text-sm font-semibold text-white mt-2 mb-1">Reinforced Deepslate Ring</h3>
            <p class="text-xs text-slate-300">Discover the dormant monolith in an Ancient City at Y: -52, or build a 5x7 frame using Soul Crying Obsidian.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800">
            <span class="text-xs font-bold text-cyan-400 bg-cyan-950/70 px-2 py-0.5 rounded border border-cyan-800/60">Step 2: How to Open the Gateway</span>
            <h3 class="text-sm font-semibold text-white mt-2 mb-1">Resonance Ignition</h3>
            <p class="text-xs text-slate-300">Ignite the center opening using a Soul Spark Igniter or trigger the acoustic Sculk Catalyst with an Echo Shard.</p>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800">
            <span class="text-xs font-bold text-indigo-400 bg-indigo-950/70 px-2 py-0.5 rounded border border-indigo-800/60">Step 3: Enter &amp; Calibrate</span>
            <h3 class="text-sm font-semibold text-white mt-2 mb-1">1:4 Ratio Step-Through</h3>
            <p class="text-xs text-slate-300">Walk into the swirling cyan rift. Your Overworld coordinates will translate at an exact 1:4 dimensional compression ratio.</p>
        </div>
    </div>
</section>
```

---

## 五、Schema.org 结构化数据全量注入规范

搜索引擎对带有合法 `FAQPage` JSON-LD 的页面有显著的 Rich Results 与 Featured Snippets 展现倾斜。

### 1. `index.html` 对应 `FAQPage` JSON-LD 注入块
将以下结构精准合并进 `index.html` 的 `<script type="application/ld+json">` 中的 `@graph` 数组内：

```json
{
  "@type": "FAQPage",
  "@id": "https://thesiftguide.com/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is The Sift real or a fake Minecraft rumor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, The Sift is real. While it began as a community concept by creator Mielon, The Sift made its official playable debut in Mojang's Minecraft Dungeons 2 on September 29, 2026. Mojang has confirmed that The Sift will officially release in vanilla Minecraft (Java and Bedrock) in 2027 as the game's 4th dimension."
      }
    },
    {
      "@type": "Question",
      "name": "When is The Sift coming to Minecraft vanilla?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Sift releases in 2027 for vanilla Minecraft on Java Edition and Bedrock platforms. Weekly development snapshots and preview betas are slated for late 2026 to early 2027 ahead of the full 1.22+ release."
      }
    },
    {
      "@type": "Question",
      "name": "What is The Sift dimension in Minecraft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Sift is the 4th official dimension in the Minecraft universe, joining the Overworld, the Nether, and The End. It is a subterranean cosmic realm featuring bioluminescent Meadow biomes, hollow fossil deserts (Carapace), and the Colossal Meadow Frog."
      }
    },
    {
      "@type": "Question",
      "name": "Can I play The Sift mod or add-on today?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, players can experience community recreations immediately. Fabric and Forge datapacks on Modrinth and CurseForge recreate the dimension on Java Edition, while .mcaddon packages enable custom Siftite blocks and frog entities on Minecraft Bedrock Edition."
      }
    },
    {
      "@type": "Question",
      "name": "Who created The Sift concept for Minecraft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Sift concept was originally created by Mielon, a prominent Minecraft artist and animator whose September 2026 concept trailer went viral, prompting official gameplay adaptations in the Minecraft series."
      }
    }
  ]
}
```

### 2. `portal.html` 对应新增 FAQPage 问答项
向 `portal.html` 的 `FAQPage` 内追加 2 项口语强意图词：
```json
{
  "@type": "Question",
  "name": "How to enter The Sift in Minecraft?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "To enter The Sift in Minecraft, locate the dormant reinforced frame inside an Ancient City at Y: -52 (or construct a 5x7 frame from Soul Crying Obsidian), then ignite the portal center with a Soul Spark Igniter or acoustic Echo Shard."
  }
},
{
  "@type": "Question",
  "name": "How do you open and activate The Sift portal?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "You open The Sift portal by activating the acoustic core with vibration pulses from an Echo Shard or lighting soul fire within the reinforced frame. Once open, the portal displays a pulsating cyan rift."
  }
}
```

---

## 六、Hacker 施工操作指南与工程铁律

### 1. 施工操作铁律（Engineering Guardrails）
1. **精准增量修改，禁止暴力全量重写**：
   - 编写独立的 Python 修改脚本（如 `/tmp/apply_seo_expansion.py`）针对特定 DOM 锚点实施精准插值；
   - 严禁全量重写 HTML，避免误伤已调优的内联事件处理函数与坐标计算器逻辑。
2. **绝对保护广告位与统计埋点代码（零容忍）**：
   - 页面顶部 728x90 广告单元（`e34c08305944ef076210b30b1897f6eb`，`highrevenueformat.com`）必须毫发无损；
   - 页面底部 300x250 广告单元（`93a1b6fb1cf3809a6ddd2ccae9364526`，`highrevenueformat.com`）必须毫发无损；
   - Google Analytics 4 测量代码（`G-X1ZTW8XWPG`）完好无损；
   - 绝不引入任何 Native Banner、反审查流氓脚本或重定向跳转代码。
3. **移动端响应式与防溢出红线**：
   - 保持所有新增表格和网格带有 `overflow-x-auto` 或在移动端堆叠（`grid-cols-1 md:grid-cols-2`）；
   - 在 390px (iPhone 13 视口) 下必须保持 **零水平横向滚动溢出**（`scrollWidth === clientWidth`）。
4. **Tailwind 与静态依赖基准**：
   - 维持现有的 Tailwind CDN 引用（`cdn.tailwindcss.com/3.4.17`）与静态 Google Fonts；
   - 所有新增类名必须是标准 Tailwind 3 工具类。

---

## 七、验收指引与 E2E 验证门禁（Acceptance Criteria）

Hacker 完成修改后，必须经过以下四重严格门禁方可宣告完工：

### 1. SEO 硬指标自动化断言检查
编写并运行 Python 校验脚本，验证所有 HTML 文件：
- [ ] `index.html`: Title 50~60 字符 (实测 54)、Meta Desc 145~158 字符 (实测 153)、H1 20~70 字符 (实测 50)；
- [ ] `portal.html`: Title 50~60 字符 (实测 54)、Meta Desc 145~158 字符 (实测 155)、H1 20~70 字符 (实测 55)；
- [ ] `mobs.html`: Title 50~60 字符 (实测 53)、Meta Desc 145~158 字符 (实测 152)、H1 20~70 字符 (实测 51)；
- [ ] 全站 3 个页面中，严格包含源头核心词 `The Sift Minecraft`，无关键词漂移。

### 2. Schema.org JSON-LD 语法校验
- [ ] 使用 Python `json.loads()` 验证 3 个页面中所有 `<script type="application/ld+json">` 的 JSON 格式 100% 正确；
- [ ] 验证 `index.html` 的 `FAQPage` 包含全部 5 个高频问答，且与 HTML 正文一一对应。

### 3. 本地 E2E 自动化测试执行
在 `/home/louis/candi-tasks/thesiftguide/` 目录下执行本地测试：
```bash
./run_e2e.sh --target local
```
**合格标准**：
- 桌面端（1280x800）与移动端（390x844）全部现有用例 100% PASS；
- 截图正常存入 `tests/screenshots/`；
- 移动端零横向滚动溢出（0 horizontal overflow）。

### 4. 生产部署与复测上线
1. 运行生产部署脚本：
   ```bash
   ./deploy_pages.sh
   ```
   确认 Cloudflare Pages 部署成功并获得 200 OK 响应。
2. 运行线上真机复测：
   ```bash
   ./run_e2e.sh --target live
   ```
   确认生产域名 `https://thesiftguide.com` 全量套件 100% PASS。
3. 仓库同步并仅推送到私有仓库：
   ```bash
   cd /home/louis/candi-tasks/thesiftguide-repo
   git push private main
   ```
   （**铁律：严禁推送到公开仓库 origin 或 gitlab**）。

---

> **Hustler 签署**：本规划书即日起生效，交由 Hacker 全权施工落地。
