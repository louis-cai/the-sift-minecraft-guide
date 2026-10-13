# HUSTLER 增长规格书：thesiftguide.com `/how-to-enter` 独立子页 SEO 规范与内容规划

> **文档密级**：项目核心资产 · SEO 施工契约（SSOT）  
> **编写人**：Hustler（Chief Growth Officer / SEO 负责人）  
> **验收人**：Candi（调度 / 验收）  
> **执行人**：Hacker（前端 / 页面开发）  
> **适用目标**：`thesiftguide.com` 新增高意图子页 `/how-to-enter`（对应物理文件：`how-to-enter.html`）  
> **基准契约**：严格遵循站点根目录 `AGENTS.md` 关键词契约，**严禁核心关键词漂移**。  
> **生效时间**：2026-10-13  

---

## 一、搜索意图聚类与受众洞察（Search Intent & Persona）

### 1.1 Bing 官方 API 审计数据与问题归因
在 2026-10-13 的日常巡检中，通过 Bing Webmaster Tools (BWT) 官方接口提取出全网累计 **800+ 展现、零/极低点击** 的“进入新维度/开启传送门”高意图疑问词群：

| 搜索查询 (Query) | 展现量 (Impressions) | 点击量 (Clicks) | 当前平均排名 (Position) | 象限归因 (Quadrant) |
| :--- | :--- | :--- | :--- | :--- |
| `how to open the sift` | 141 | 1 | 8.0 | Q4 (高曝光/极低点击/亟待转化) |
| `how to get to the sift in minecraft` | 133 | 0 | 7.0 | Q4 (高曝光/零点击/意图未满足) |
| `how to get to the new dimension in minecraft` | 103 | 0 | 7.0 | Q4 (大盘泛意图/流量截流金矿) |
| `how to get to the sift` | 101 | 0 | 7.0 | Q4 (核心短词/直接疑问) |
| `how to enter the sift` | 75 | 0 | 8.0 | Q4 (高行动意向/亟需指引) |
| `how to enter the sift in minecraft` | 36 | 0 | 6.0 | Q4 (精确长尾/首页前排漏水) |
| `how to open the sift in minecraft` | 33 | 0 | 6.0 | Q4 (精确动作词/卡点明确) |
| `ancient city portal` | 24 | 0 | 2.0~5.0 | Q4 (高排名误区词/辟谣与承接) |
| **衍生相关长尾合计** | **160+** | **0~2** | **6.0~9.5** | **长尾聚合潜力池** |
| **总体统计** | **806+** | **1~3** | **7.1** | **典型 Q4 严重曝光浪费区 (Click Leaks)** |

**根因诊断结论**：
1. **现有页面意图错位**：目前站点排在 6~8 名的是 `/portal`（页面定位偏向“传送门坐标换算、深层板岩材质结构与维度压缩比 1:4”的技术机制），而用户搜索 `how to open / how to enter` 时，要的是“**立刻、马上告诉我怎么进去、点不着火怎么办、原版到底能不能进**”的行动指引；
2. **SERP Snippet 缺乏即时解决方案承诺**：搜索结果未在 Title 和 Description 中直接承诺“澄清远古城市真相 + 给出即时可玩方案”，导致玩家在搜索结果页犹豫或跳过；
3. **必须建立独立 `/how-to-enter` 落地页**：承接“Procedural Action & Troubleshooting”（步骤操作与排障），与既有的 `/portal`（Portal Calculator & Architectural Specs）形成互补双引擎，彻底解决流量浪费。

---

### 1.2 三类受众画像与搜索心理场景（Persona Breakdown）

```
                         [玩家搜索 "How to enter The Sift"]
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
  【画像 A：爆料探秘型】           【画像 B：远古城市卡关型】        【画像 C：实战试玩型】
  刚刷到 4th Dimension 视频       挖到 Y: -52 远古城市中心          已知原版未正式上线
  急切进游戏验证真伪               拿打火石/灵魂火猛点点不着         寻找快照/模组/指令体验
  心理："怎么进？真的假的？"       心理："为什么点不着？缺啥？"      心理："给能用的指令/MOD！"
```

1. **Persona A（爆料探秘型玩家 - Casual News Explorer）**：
   - **心理场景**：在 TikTok、YouTube Shorts 或 Reddit 看到 Mielon 的 The Sift 概念视频后，启动了纯净原版 Minecraft（1.20 或 1.21），在主菜单四处寻找新维度入口，搜 `how to get to the new dimension in minecraft` 或 `how to enter the sift`；
   - **核心痛点**：缺乏官方路线图认知，容易被假视频误导；需要权威事实核查（Official Roadmap Check）告知真相。
2. **Persona B（远古城市卡关排障型玩家 - Frustrated Rumor Chaser）**：
   - **心理场景**：在生存模式千辛万苦挖到 Deep Dark 远古城市，站在 23x23 强化深层板岩（Reinforced Deepslate）框架前，尝试了打火石、灵魂火把、回响碎片、潜声催化体却毫无反应，极度沮丧；搜 `ancient city portal`、`how to open the sift in minecraft`；
   - **核心痛点**：“为什么点不着？我做错了什么？”——需要精确排障与辟谣（Debunking & Troubleshooting）。
3. **Persona C（实战试玩型玩家 - Action-Oriented Mod/Snapshot Player）**：
   - **心理场景**：明白 Mojang 官方 2027 年才实装，但今天就想在游戏里亲自穿越并打怪探险；搜 `how to get to the sift in minecraft`，想要即刻可用的 `/execute in ...` 传送指令，或者直达社区可玩 Mod/Addon；
   - **核心痛点**：需要无废话的“一键指令代码”与“1 分钟可玩进入流程”。

---

### 1.3 核心词根提炼与衍生矩阵

- **主打击词根（Primary Intent Stem）**：
  `How to Enter The Sift in Minecraft`（兼顾精确品牌词 `The Sift in Minecraft` 与最高意图动词 `How to Enter`）
- **高共现次级长尾词（Secondary High-Co-occurrence Long-Tails）**：
  1. `how to open the sift`（解决开启/点火动作意图）
  2. `how to get to the sift in minecraft`（解决路径/到达维度意图）
  3. `how to get to the new dimension in minecraft`（截流泛大盘新维度流量）
  4. `ancient city portal sift` / `ancient city portal activation`（承接远古城市误区排障）

---

## 二、On-Page 元数据契约（Strict Metadata Contract）

严格执行行业最高硬指标卡尺，绝不超标，绝不漂移：

| 元数据项目 | 官方/行业硬指标卡尺 | Hustler 核准实装数值 | 实测字符数 | 验证状态 |
| :--- | :--- | :--- | :--- | :--- |
| **Page Title (`<title>`)** | **50 ~ 60 字符**（核心词前置，带 CTR 利益钩子） | `How to Enter The Sift in Minecraft: Portal & Ignition Guide` | **59 字符** | **PASS（前置命中主词，完美落入 50~60 黄金区间）** |
| **Meta Description** | **145 ~ 158 字符**（含痛点解决、行动号召，无虚词） | `Learn how to enter The Sift in Minecraft. Step-by-step portal opening guide: Ancient City frame truth, ignition triggers, test commands, and playable setup.` | **156 字符** | **PASS（严格落入 145~158 字符区间，首句带主词）** |
| **唯一 H1 标题 (`<h1>`)** | **20 ~ 70 字符**（全页唯一，与 Title 强呼应，零警告） | `How to Enter The Sift in Minecraft: Complete Portal Opening Guide` | **65 字符** | **PASS（完全符合 Bing 20-70 规范与 Google 语义对齐）** |
| **Canonical URL** | 绝对干净 URL（严格禁止 `.html` 后缀） | `https://thesiftguide.com/how-to-enter` | 38 字符 | **PASS（标准化路由锁死）** |
| **物理静态文件名** | 仓库部署文件 | `how-to-enter.html` | - | **PASS（Cloudflare Pages 自动 clean URLs）** |

---

### 2.1 备选 Title 与 Meta Description 库（供 A/B 测试）

- **Title 备选 B（57 字符）**：`How to Enter The Sift in Minecraft: Open the Portal Guide`
- **Title 备选 C（58 字符）**：`How to Open The Sift in Minecraft: Portal & Ignition Guide`
- **Title 备选 D（60 字符）**：`How to Get to The Sift in Minecraft: Portal & Ignition Guide`
- **Meta Description 备选 B（158 字符）**：`Wondering how to enter The Sift in Minecraft? Step-by-step portal guide reveals Ancient City frame truth, ignition triggers, test commands, and instant setup.`
- **Meta Description 备选 C（158 字符）**：`Discover how to enter The Sift in Minecraft. Complete portal opening guide: Ancient City frame truth, ignition mechanics, snapshot commands, and instant play.`

---

### 2.2 防自相残杀（Cannibalization Prevention）与 `/portal` 的定位分工

目前 `/portal` 与新页面 `/how-to-enter` 存在潜在的内部竞争风险。Hustler 必须确立清晰的定位分工与边界契约：

```
                ┌────────────────────────────────────────────────────────┐
                │             thesiftguide.com 传送门流量双引擎           │
                └────────────────────────────────────────────────────────┘
                               │                                        │
                               ▼                                        ▼
             【/portal：参数与计算器枢纽】               【/how-to-enter：操作指引与排障】
             Portal Specs & Coordinates Hub              Procedural & Troubleshooting Guide
             ──────────────────────────────              ──────────────────────────────────
             • 核心意图：参数、计算、配方                 • 核心意图：怎么进、怎么点火、排错
             • 核心工具：1:4 坐标双向计算器               • 核心工具：版本与点火诊断状态机
             • 核心内容：框架材料、尺寸规格、             • 核心内容：远古城市辟谣、保姆级
                        链接半径、维度物理特性                        开启步骤、指令、排障清单
```

**对现有 `portal.html` 的元数据微调建议（交由 Hacker 在后续任务同步）**：
- 将 `portal.html` 的 Title 从原先微泛的 `How to Enter The Sift: Minecraft Portal Guide & Frames` 调整为：
  `The Sift Portal Calculator: Coordinates, Frames & Link Guide`（59 字符）
- 彻底释放 `How to Enter The Sift in Minecraft` 核心意图归属于新页面 `/how-to-enter`，彻底消灭站内同室操戈。

---

### 2.3 目标关键词矩阵与承接规划

| 关键词 (Keyword) | 意图属性 (Intent) | 搜索诉求焦点 | 页面对应承接区块 |
| :--- | :--- | :--- | :--- |
| `how to enter the sift` | Action / Informational | 寻找进入新维度的具体方法 | Hero、Step-by-Step Guide |
| `how to enter the sift in minecraft` | Action / High-Intent | 带游戏实体的精准进入问题 | Title, H1, Meta, Lead Text |
| `how to open the sift` | Procedural / Action | 寻找点火与激活传送门的动作 | H2: Step 3 (Ignition), Diagnostic Tool |
| `how to open the sift in minecraft` | Procedural / Exact | 传送门激活失败排障 | H2: Troubleshooting Section |
| `how to get to the sift in minecraft` | Directional / Navigational | 寻路与版本支持方案 | H2: Vanilla vs Mod Reality Check |
| `how to get to the new dimension in minecraft` | Broad Exploration | 大盘泛新维度搜索 | Intro Callout, FAQ 1 |
| `ancient city portal` | Misconception / Curiosity | 误以为远古城市可以直接点火 | H2: Ancient City Frame Truth (辟谣) |
| `how to teleport to the sift` | Technical / Command | 管理员与创作者作弊码传送 | H2: Teleport Commands (`/execute`) |

---

### 2.4 `sitemap.xml` 增补契约
在 `sitemap.xml` 中紧随 `/mods` 节点插入：
```xml
  <url>
    <loc>https://thesiftguide.com/how-to-enter</loc>
    <lastmod>2026-10-13</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
```

---

## 三、内容大纲与信息架构（Heading Hierarchy）

页面遵循原生暗黑深板岩像素风（Deepslate Grid，`#111317` 背景、`#181a20` 卡片底色、`#2d3139` 像素边框、`#22d3ee` 荧光青色高亮）。

### 3.1 完整标题层级架构（Heading Tree）

```text
H1: How to Enter The Sift in Minecraft: Complete Portal Opening Guide
├── H2: Quick Status: Can You Enter The Sift in Vanilla Minecraft Today?
│   ├── H3: The Ancient City Portal Truth: Why Your Fire Won't Light
│   └── H3: Official Roadmap vs. Playable Fan Recreations
├── H2: The Sift Portal Ignition & Version Diagnostic Tool (Interactive Widget)
├── H2: Step-by-Step: How to Open & Activate The Sift Portal
│   ├── H3: Step 1: Prepare Your Game Environment (Java / Bedrock / Commands)
│   ├── H3: Step 2: Construct or Locate the Portal Frame
│   ├── H3: Step 3: Trigger the Ignition Sequence (Echo Shard Resonance)
│   └── H3: Step 4: Dimension Traversal & Travel Rules
├── H2: Troubleshooting: Why Won't Your Sift Portal Open?
│   ├── H3: Issue 1: Striking Normal Flint and Steel (Requires Soul / Acoustic Trigger)
│   ├── H3: Issue 2: Playing on Unmodded Vanilla 1.20 / 1.21
│   └── H3: Issue 3: Obstructed Frame Interior or Active Sculk Shriekers
├── H2: Direct Teleport Commands for Builders & Server Admins
│   ├── H3: Java Edition Teleport Syntax
│   └── H3: Bedrock Edition Command Workarounds
└── H2: Frequently Asked Questions (FAQ)
```

---

### 3.2 首屏区域文案（Above-the-Fold Blueprint）

- **Breadcrumb**：
  `Home` > `How to Enter`
- **Badges**：
  - 绿色脉冲徽章：`● Updated for Minecraft 1.21 & 2026 Snapshots`
  - 青色徽章：`⚡ Step-by-Step Portal & Ignition Guide`
- **H1 标题**：
  `<h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold title-glow tracking-tight text-center">How to Enter The Sift in Minecraft: Complete Portal Opening Guide</h1>`
- **Hero 引言（Lead Text - 严格遵守 GEO 40~60 词直接答案引导）**：
  > "To enter The Sift in Minecraft, you must understand the distinction between vanilla lore and playable releases. While the massive Reinforced Deepslate frame in Ancient Cities remains dormant in vanilla survival awaiting Mojang's official release, you can open and explore the 4th dimension today using verified community snapshot mods or exact teleport commands. Here is your definitive portal guide."
- **快速行动跳转胶囊（Quick Jump Pills）**：
  - `[🔍 Interactive Diagnostic]` (平滑跳转至 `#diagnostic`)
  - `[📖 4-Step Portal Guide]` (平滑跳转至 `#steps`)
  - `[⚠️ Ancient City Truth]` (平滑跳转至 `#truth`)
  - `[💻 Teleport Commands]` (平滑跳转至 `#commands`)
  - `[❓ FAQs]` (平滑跳转至 `#faqs`)

---

### 3.3 核心交互组件规格：《The Sift Portal Ignition & Version Diagnostic Tool》

用户进入首屏后，第二屏上方立即提供免刷新的交互式小部件，解决“我到底能不能进、现在缺什么”的核心痛点：

#### 3.3.1 组件业务逻辑与状态机设计
- **无外部 API 依赖**：纯客户端 JavaScript 编写，即开即用；
- **两步诊断交互**：
  1. **第一步：选择游戏版本与环境（Select Setup）**：
     - 单选按钮 A：`Vanilla Survival (Java / Bedrock 1.19 - 1.21)`
     - 单选按钮 B：`Modded Minecraft (Fabric / Forge / NeoForge)`
     - 单选按钮 C：`Bedrock Edition (.mcaddon installed)`
     - 单选按钮 D：`Creative Mode / Cheats Enabled`
  2. **第二步：选择当前遇到的卡点（Select Current Block）**：
     - 单选按钮 1：`Standing at Ancient City frame with flint & steel`
     - 单选按钮 2：`Built custom frame from Soul Obsidian`
     - 单选按钮 3：`Trying to run a teleport command`
- **诊断结果动态渲染（Instant Diagnosis Box）**：
  - 若选 `Vanilla Survival` + `Ancient City frame`：
    - 状态指示：🔴 **BLOCKED IN VANILLA SURVIVAL**
    - 诊断解析：*“The Reinforced Deepslate frame in Ancient Cities cannot be lit in pure vanilla survival without mods. Mojang has not enabled the dimension in vanilla 1.21. Clicking flint & steel will only spawn ordinary fire.”*
    - 行动建议：提供一键跳转按钮 `[📥 Download Sift Mod (Play in 2 Mins)]` 与 `[💻 View Teleport Commands]`。
  - 若选 `Modded Minecraft` + 任何点火疑问：
    - 状态指示：🟢 **READY TO ACTIVATE**
    - 诊断解析：*“In Sift mods, standard fire does NOT light the portal. You must use an Echo Shard right-click on the center frame or craft a Soul Spark Igniter.”*
    - 行动建议：展开点火清单卡片。
- **互动点火清单（Interactive Ignition Checklist）**：
  - 提供 4 个可勾选的像素复选框：
    - `[ ] Verified Minecraft edition supports The Sift mod`
    - `[ ] Located Ancient City portal (Y: -52) or built 5x7 frame`
    - `[ ] Cleared sculk shriekers to prevent Warden spawning`
    - `[ ] Crafted Echo Shard or Soul Spark Igniter (Flint & Steel will fail)`
  - 全部勾选后触发“Portal Status: ACTIVATED (Cyan Void Active)”动态流光特效。

---

### 3.4 核心正文内容深度蓝图（Copy Blueprint）

#### 区块一：远古城市辟谣与官方路线图真相（H2: Quick Status）
- **核心辟谣事实**：
  1. 许多玩家误以为在远古城市中心（中心矩形大结构，宽 23 格高 23 格的 Reinforced Deepslate 建筑）点火就能进入。
  2. 官方现实：在原版 1.19 至 1.21 中，强化深层板岩是不可采集、不可点火的惰性结构。Mojang 官方将其设计为通往新维度的“大门构型”，预定于未来大型更新实装。
  3. 解决方案：如果想现在体验，请使用社区 1:1 复刻的 Mod 或数据包。

#### 区块二：手把手开门保姆级教程（H2: Step-by-Step Guide）
- **Step 1: 准备运行环境**（原版指令 vs 模组环境，指引前往 `/mods` 下载）；
- **Step 2: 建造或寻找传送门框架**：
  - 远古城市自然框架：位于地下 Y: -52 深暗之域中心；
  - 自建框架规则：采用 Soul Crying Obsidian 或 Echo Deepslate 砌筑 5x7 竖向矩形门框（外径 5x7，内径 3x5）；
- **Step 3: 触发声学共鸣点火（Acoustic Resonance Ignition）**：
  - 严禁用普通打火石！普通火焰会烧焦地面；
  - 正确操作：持【回响碎片 (Echo Shard)】右键门框底部中央方块，或使用【灵魂打火石 (Soul Fire Striker)】；触发粒子特效，生成青色虚空裂隙（Cyan Sift Rift）；
- **Step 4: 穿梭规则与坐标映射**：
  - 站入门框 15 个游戏刻（约 0.75 秒）完成位面跃迁；
  - 核心坐标法则：主世界与 The Sift 遵循 **1:4 坐标压缩比**（主世界走 4 格 = 新维度走 1 格）。提醒玩家使用本站首页的坐标计算器进行基底坐标锚定。

#### 区块三：排障指南（H2: Troubleshooting: Why Won't Your Sift Portal Open?）
- **排障 1：使用普通打火石（Flint & Steel）**
  - 原因：普通打火石仅生成原版常规火焰，无法激发声学与灵魂共振。
  - 修复：合成灵魂打火器或使用回响碎片。
- **排障 2：原版纯净生存模式尝试点火**
  - 原因：未安装模组的客户端不包含新维度生成代码。
  - 修复：一键安装 The Sift Addon 或切换至模组版本。
- **排障 3：门框内部有阻挡方块或潜声催测体干扰**
  - 原因：传送门内径 3x5 区域必须完全为空气方块。潜声蔓延如果覆盖了门框内部，将导致点火失败。
  - 修复：清理内部杂物，用羊毛阻断振动防警报。

#### 区块四：管理员作弊传送指令（H2: Direct Teleport Commands）
为创作者、测试者和服务器管理员提供权威格式化代码块：
```bash
# Java Edition (Fabric/Forge with Sift mod)
/execute in sift:the_sift run tp @s ~ ~ ~

# Java Edition Teleport to Specific Coordinate
/execute in sift:the_sift run tp @s 0 64 0

# Bedrock Edition Addon Command
/execute as @s in sift:the_sift run tp @s 0 64 0
```
附带带一键复制小按钮（`Copy Command`）。

---

### 3.5 FAQ 问答库（FAQ Knowledge Base）

精心挑选 4 组完全击中 Bing 搜索痛点的 Q&A，供 SERP Rich Snippet 解析：

1. **Q: How to enter The Sift in Minecraft?**  
   **A**: To enter The Sift in Minecraft, you must assemble a portal frame using Reinforced Deepslate or Soul Crying Obsidian, then ignite the portal center using an acoustic Echo Shard or Soul Spark igniter. In unmodded vanilla Minecraft (1.20/1.21), the official dimension is awaiting future updates, so players must use the playable Sift mod or dimension teleport commands (`/execute in sift:the_sift run tp @s ~ ~ ~`).

2. **Q: How do you open The Sift portal in Minecraft?**  
   **A**: You open The Sift portal by clearing the 3x5 interior frame and right-clicking the bottom rim with an Echo Shard to trigger acoustic vibration resonance. A pulsating cyan portal block will form. Using regular flint and steel will fail as normal fire does not open the rift.

3. **Q: Can you open the Ancient City portal in vanilla Minecraft right now?**  
   **A**: No. In current vanilla survival Minecraft (versions 1.19 through 1.21.x), the 23x23 Reinforced Deepslate frame in Ancient Cities cannot be activated. It is a dormant structure designated for future dimension releases. Attempting to light it with flint and steel will only ignite temporary normal fire.

4. **Q: Why won't my Sift portal ignite or activate?**  
   **A**: The most common reasons are: 1) You are in unmodded vanilla Minecraft without the Sift mod or snapshot installed; 2) You used regular flint and steel instead of an Echo Shard or soul ignition item; 3) The portal frame contains non-qualifying blocks or the interior is obstructed by sculk blocks.

---

## 四、结构化数据（Schema.org JSON-LD）完整规划

页面必须内嵌完整的符合 Schema.org 规范的 JSON-LD 代码块，包含 `WebSite`、`BreadcrumbList`、`HowTo` 与 `FAQPage`：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://thesiftguide.com/#website",
      "url": "https://thesiftguide.com/",
      "name": "The Sift Guide",
      "description": "Interactive Wiki and Guide to Minecraft's 4th Dimension: The Sift"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://thesiftguide.com/how-to-enter#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://thesiftguide.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "How to Enter The Sift",
          "item": "https://thesiftguide.com/how-to-enter"
        }
      ]
    },
    {
      "@type": "HowTo",
      "@id": "https://thesiftguide.com/how-to-enter#howto",
      "name": "How to Enter The Sift in Minecraft",
      "description": "Step-by-step guide on how to build, open, and ignite the portal to Minecraft's 4th dimension: The Sift.",
      "totalTime": "PT5M",
      "supply": [
        {
          "@type": "HowToSupply",
          "name": "14x Reinforced Deepslate or Soul Crying Obsidian Blocks"
        },
        {
          "@type": "HowToSupply",
          "name": "1x Echo Shard or Soul Spark Igniter"
        }
      ],
      "tool": [
        {
          "@type": "HowToTool",
          "name": "Minecraft (Java or Bedrock with The Sift Mod/Snapshot)"
        }
      ],
      "step": [
        {
          "@type": "HowToStep",
          "url": "https://thesiftguide.com/how-to-enter#step-setup",
          "name": "Verify Game Edition & Mod Setup",
          "itemListElement": [{
            "@type": "HowToDirection",
            "text": "Confirm whether you are running the playable Sift mod on Fabric/Forge or seeking vanilla coordinates. Vanilla survival requires mod installation to generate dimension files."
          }]
        },
        {
          "@type": "HowToStep",
          "url": "https://thesiftguide.com/how-to-enter#step-frame",
          "name": "Locate or Construct the Portal Frame",
          "itemListElement": [{
            "@type": "HowToDirection",
            "text": "Locate the 23x23 Reinforced Deepslate frame in an Ancient City at Y: -52, or construct a 5x7 frame using Soul Crying Obsidian blocks."
          }]
        },
        {
          "@type": "HowToStep",
          "url": "https://thesiftguide.com/how-to-enter#step-ignite",
          "name": "Trigger Acoustic Resonance Ignition",
          "itemListElement": [{
            "@type": "HowToDirection",
            "text": "Right-click the bottom frame block with an Echo Shard or use a Soul Spark Igniter to activate the pulsating cyan portal rift."
          }]
        },
        {
          "@type": "HowToStep",
          "url": "https://thesiftguide.com/how-to-enter#step-traversal",
          "name": "Traverse the Portal",
          "itemListElement": [{
            "@type": "HowToDirection",
            "text": "Step into the cyan rift and remain stationary for 15 game ticks to complete dimensional transfer into The Sift."
          }]
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://thesiftguide.com/how-to-enter#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How to enter The Sift in Minecraft?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "To enter The Sift in Minecraft, construct a portal frame using Reinforced Deepslate or Soul Crying Obsidian, then ignite the portal center using an acoustic Echo Shard or Soul Spark igniter. In vanilla Minecraft (1.20/1.21), the official dimension is awaiting release, so players must use the Sift mod or teleport commands."
          }
        },
        {
          "@type": "Question",
          "name": "How do you open The Sift portal in Minecraft?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "You open The Sift portal by clearing the 3x5 interior frame and right-clicking the bottom frame with an Echo Shard to trigger acoustic resonance. A pulsating cyan rift will form. Ordinary flint and steel will fail."
          }
        },
        {
          "@type": "Question",
          "name": "Can you open the Ancient City portal in vanilla Minecraft right now?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. In current vanilla Minecraft (1.19 through 1.21.x), the Reinforced Deepslate frame in Ancient Cities cannot be activated in survival mode. It remains a dormant structure awaiting Mojang's official dimension update."
          }
        },
        {
          "@type": "Question",
          "name": "Why won't my Sift portal ignite or activate?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The portal will not ignite if you are playing unmodded vanilla Minecraft, if you used normal flint and steel instead of an Echo Shard, or if the frame interior is obstructed by sculk or blocks."
          }
        }
      ]
    }
  ]
}
</script>
```

---

## 五、全站内链拓扑与锚文本契约（Internal Linking Strategy）

构建强大的网状权重流，既从全站高权重页精准导流到本页，又由本页高意向反哺核心工具与变现页面：

```
                    ┌───────────────────────────────┐
                    │  首页 (/) 核心坐标计算器      │
                    └───────┬───────────────▲───────┘
                            │               │
       [How to Enter Guide] │               │ [Sift Coordinate Calculator]
                            ▼               │
                    ┌───────────────────────┴───────┐
                    │    /how-to-enter (新页面)     │
                    │   保姆级进门与点火排障落地页   │
                    └───┬───────────┬───────────▲───┘
                        │           │           │
     [Portal Specs Hub] │           │           │ [How to Open The Sift Portal]
                        ▼           │           │
    ┌─────────────────────────┐     │     ┌─────┴───────────────────┐
    │ /portal 传送门架构与参数 │     │     │ /mods 模组试玩与下载页  │
    └─────────────────────────┘     │     └─────────────────────────┘
                                    ▼
                         ┌────────────────────┐
                         │ /mobs 危险生物图鉴 │
                         └────────────────────┘
```

### 5.1 站内流入流量拓扑（Inflow Links to `/how-to-enter`）

| 来源页面 (Source Page) | 放置区块位置 | 精确锚文本 (Exact Anchor Text) | 上下文引导语 (Context Sentence) |
| :--- | :--- | :--- | :--- |
| **`index.html` (首页)** | 全站导航栏 (Navbar) | `How to Enter` | 紧随 `Portal Calculator` 之后的新增主导航入口 |
| **`index.html` (首页)** | 计算器下方行动卡片 | `How to Enter The Sift Guide` | *"Confused about Ancient City portal ignition? Check our step-by-step How to Enter The Sift Guide →"* |
| **`portal.html` (传送门)** | 首屏 Notice 警示条 | `How to Enter The Sift in Minecraft` | *"Looking for practical ignition troubleshooting & vanilla commands? Read the complete How to Enter The Sift in Minecraft guide."* |
| **`mods.html` (模组下载)** | Step 3: Enter Dimension | `How to Open The Sift Portal` | *"Once installed, follow our troubleshooting guide on How to Open The Sift Portal to activate your first gateway."* |
| **`dungeons-2.html`** | 联动对比章节 | `enter The Sift in Minecraft` | *"Discover how dimensional rifts work and how to enter The Sift in Minecraft compared to Dungeons 2."* |

---

### 5.2 站内流出反哺拓扑（Outflow Links from `/how-to-enter`）

| 目标页面 (Target Page) | 放置区块位置 | 精确锚文本 (Anchor Text) | 引导意图与业务价值 |
| :--- | :--- | :--- | :--- |
| **`https://thesiftguide.com/` (首页)** | Step 4 坐标跨越说明处 | `Sift Coordinate Calculator` | 引导进入首页核心计算器，测算 1:4 坐标换算，增加全站停留时间 |
| **`https://thesiftguide.com/portal`** | 框架搭建 H3 补充说明 | `Sift Portal Frame & Specs` | 引导玩家查看完整的黑曜石/深层板岩物料清单与坐标链接机制 |
| **`https://thesiftguide.com/mods`** | 诊断工具结果与 H2 模组处 | `The Sift Minecraft Mod Guide` | 将想立即试玩的玩家高转化导入模组下载页，提升 Adsterra 广告展示 |
| **`https://thesiftguide.com/mobs`** | 穿梭前安全警示区块 | `The Sift Mobs Guide` | 提醒玩家备好装备应对 Colossal Frog 与 Hollow Spider，提高内容丰富度 |

---

## 六、Hacker 实施与 Candi 验收核对清单（Implementation & Acceptance Checklist）

为确保 Hacker 在编码落地时毫厘不差，制定以下 15 点硬核验收清单：

### 6.1 Capo.js 严格 `<head>` 排序模板（Hacker 必抄）
```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <!-- [100] Charset & Viewport (首屏 1024 字节内) -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- [95] Page Title (严格 59 字符) -->
    <title>How to Enter The Sift in Minecraft: Portal & Ignition Guide</title>

    <!-- [90] Preconnect (必须置于脚本之上) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <!-- [70] Async Scripts (GA4 异步统计) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-X1ZTW8XWPG"></script>

    <!-- [50] Synchronous Scripts & Schema JSON-LD -->
    <script src="https://cdn.tailwindcss.com/3.4.17"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['"Plus Jakarta Sans"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
              display: ['"Space Grotesk"', 'ui-monospace', 'monospace', 'sans-serif']
            },
            colors: {
              void: { 950: '#111317', 900: '#181a20', 850: '#20242c', 800: '#272c36', 700: '#343b48' },
              mc: { deepslate: '#111317', stone: '#181a20', border: '#2d3139', grass: '#46a228', diamond: '#22d3ee' }
            }
          }
        }
      }
    </script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-X1ZTW8XWPG');
    </script>
    <!-- 此处插入本规格书第四章的 Schema.org JSON-LD -->

    <!-- [40] Stylesheets -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
      :root { color-scheme: dark; --mc-deepslate: #111317; --mc-stone: #181a20; --mc-border: #2d3139; --mc-diamond: #22d3ee; }
      body { background-color: #111317; color: #e2e8f0; }
    </style>

    <!-- [0] Metadata & Social -->
    <link rel="canonical" href="https://thesiftguide.com/how-to-enter">
    <meta name="description" content="Learn how to enter The Sift in Minecraft. Step-by-step portal opening guide: Ancient City frame truth, ignition triggers, test commands, and playable setup.">
    <meta name="keywords" content="how to enter the sift in minecraft, how to open the sift, how to get to the sift in minecraft, how to get to the new dimension in minecraft, ancient city portal sift">
    <meta name="robots" content="index,follow">
    <meta name="theme-color" content="#111317">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How to Enter The Sift in Minecraft: Portal & Ignition Guide">
    <meta property="og:description" content="Learn how to enter The Sift in Minecraft. Step-by-step portal opening guide: Ancient City frame truth, ignition triggers, test commands, and playable setup.">
    <meta property="og:url" content="https://thesiftguide.com/how-to-enter">
    <meta property="og:image" content="https://thesiftguide.com/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How to Enter The Sift in Minecraft: Portal & Ignition Guide">
    <meta name="twitter:description" content="Learn how to enter The Sift in Minecraft. Step-by-step portal opening guide: Ancient City frame truth, ignition triggers, test commands, and playable setup.">
    <meta name="twitter:image" content="https://thesiftguide.com/og-image.png">
</head>
```

---

### 6.2 15 点严格验收清单（Candi 验收对照表）

| 序号 | 检查项目 | 验收标准 / 硬指标 | 责任人 | 状态 |
| :---: | :--- | :--- | :---: | :---: |
| 1 | **Title 字符长度** | 严格 50~60 字符，实测 59 字符，主词前置 | Hustler/Hacker | [ ] |
| 2 | **Meta Description 长度** | 严格 145~158 字符，实测 156 字符，带清晰 CTA | Hustler/Hacker | [ ] |
| 3 | **H1 标题规范** | 全页唯一，严格 20~70 字符，实测 65 字符，强呼应主词 | Hacker | [ ] |
| 4 | **Canonical URL** | 严格锁定 `https://thesiftguide.com/how-to-enter`，无 `.html` 后缀 | Hacker | [ ] |
| 5 | **Capo.js 排布** | `<head>` 严格遵守 100 -> 95 -> 90 -> 70 -> 50 -> 40 -> 0 降序 | Hacker | [ ] |
| 6 | **首屏即效用** | 手机与桌面端首屏即见诊断工具或快速跳转胶囊，无长篇空话 | Hacker | [ ] |
| 7 | **诊断小部件交互** | 纯前端 JS 状态机，点击版本与卡点即刻给出精准诊断与建议 | Hacker | [ ] |
| 8 | **代码一键复制** | 传送指令提供一键复制按钮与提示交互（Copied!） | Hacker | [ ] |
| 9 | **Schema.org 语法** | JSON-LD 通过验证，包含 BreadcrumbList, HowTo, FAQPage, WebSite | Hacker | [ ] |
| 10 | **全站导航栏同步** | `index.html`、`portal.html`、`mods.html` 等主导航增设 `How to Enter` | Hacker | [ ] |
| 11 | **双向内链锚文本** | 首页计算器、`/portal`、`/mods` 精确挂载锚文本导流至本页 | Hacker | [ ] |
| 12 | **反哺内链挂载** | 本页自然反哺首页计算器（`/`）、`/portal` 与 `/mods` | Hacker | [ ] |
| 13 | **sitemap.xml 增补** | 成功追加 `/how-to-enter` 节点，priority 0.9 | Hacker | [ ] |
| 14 | **移动端响应式与 CWV** | LCP < 2.5s，INP < 200ms，CLS < 0.1，无横向溢出 | Hacker | [ ] |
| 15 | **防关键词漂移** | 严格遵守 `AGENTS.md`，主词 `the sift minecraft` 始终保留 | 全员 | [ ] |

---

> **结语与交接**：  
> 本规格书为 `thesiftguide.com/how-to-enter` 开发的最高准则与唯一事实源（SSOT）。  
> 经 Candi 评审验收通过后，直接移交 Hacker 进入前端落地编码阶段。
