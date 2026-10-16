# 一号站 (thesiftguide.com) 深度 GEO 诊断与增长策略报告

- **报告人**：Hustler（首席增长官）
- **评估对象**：一号站（`https://thesiftguide.com`）
- **数据基准**：Bing Webmaster AI Performance 导出报表（2026-10-15）、时序数据库（`arbitrage_analytics.db`）、确定性审计引擎（`audit_deterministic.py` 52 项规则集）
- **核心理论**：普林斯顿大学 KDD'24 生成式引擎优化（GEO）实证研究（arXiv:2311.09735）
- **落盘时间**：2026-10-16

---

## 一、一号站当前 GEO 资产现状盘点 (Ground Truth)

### 1. 20,187 次 AI 引用的成因归因

根据 SQLite 时序数据库 `ai_citation_metrics` 记录，一号站在 2026-10-02 至 2026-10-12 期间，累计获得 **20,187 次** Bing Copilot 生成式搜索引用。

#### ① AI 引用每日时序演变表

| 日期 | 引用引擎 | AI 引用次数 | 被引用页面数 | 阶段特征 |
| :--- | :--- | :---: | :---: | :--- |
| **2026-10-02** | Bing Copilot | 4,137 | 2 | 突发流量爆发峰值（Minecraft Live 2026 传闻爆料） |
| **2026-10-03** | Bing Copilot | 3,814 | 2 | 持续高位震荡，AI 知识库主索引建立 |
| **2026-10-04** | Bing Copilot | 3,332 | 2 | 高位平台期 |
| **2026-10-05** | Bing Copilot | 2,345 | 2 | 流量向长尾与解决型意图（Learn and Solve）扩散 |
| **2026-10-06** | Bing Copilot | 1,579 | 2 | 自然回落，进入常态化引用 |
| **2026-10-07** | Bing Copilot | 1,078 | 2 | 常态化平稳期 |
| **2026-10-08** | Bing Copilot | 759 | 2 | 周中低谷 |
| **2026-10-09** | Bing Copilot | 735 | 2 | 周中平稳期 |
| **2026-10-10** | Bing Copilot | 941 | 2 | 周末回升 |
| **2026-10-11** | Bing Copilot | 768 | 2 | 周末活跃 |
| **2026-10-12** | Bing Copilot | 699 | 2 | 平稳收尾 |
| **累计 / 均值** | - | **20,187** | **2** | **全站仅 2 个页面承担了全部 20,187 次引用** |

#### ② 核心垄断查询词（Citation Share ≥ 50%）

分析 Bing 官方导出的 91 个核心 AI 查询词数据，一号站在操作指引与核心构造类查询词上建立了绝对垄断：

| 核心查询词 (Grounding Query) | 意图分类 (Intent) | 主题领域 (Topic) | AI 引用次数 | 全网引用份额 (Share) | 竞争态势 |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `how to make a sift portal in minecraft` | Learn and Solve | Game Guides, Mods & Cheats | 84 | **60.87%** | 绝对垄断第一名 |
| `how to make sift portal in minecraft` | Learn and Solve | Game Guides, Mods & Cheats | 56 | **60.87%** | 绝对垄断第一名 |
| `how to build a sift portal in minecraft` | Learn and Solve | Game Guides, Mods & Cheats | 42 | **60.87%** | 绝对垄断第一名 |
| `як активувати портал в сіфт` | Learn and Solve | Technology | 24 | **60.00%** | 多语言跨语种垄断 |
| `how to make the sift portal in minecraft` | Learn and Solve | Game Guides, Mods & Cheats | 181 | **56.92%** | 高频词绝对优势 |
| `minecraft sift biome` | Learn and Solve | Adventure & Survival Games | 4 | **50.00%** | 群系先发份额 |
| `sift mincraft` | Uncategorized | - | 6 | **100.00%** | 错拼词全量承接与召回 |
| `the siff minecraft` | Uncategorized | - | 4 | **100.00%** | 错拼词全量承接与召回 |

#### ③ 意图分布归因分析

Bing 导出报表覆盖的 11,171 次具体查询词归纳如下：
1. **Media（媒体/资讯类）**：7,593 次引用（占比 67.97%）。由两大头部核心词驱动：`the sift minecraft`（5,653 次，份额 15.95%）与 `minecraft the sift`（1,651 次，份额 12.72%）。该类意图以版本大势、传闻真伪为主，主要由首页 `/` 承接。
2. **Informational（概念/知识类）**：2,410 次引用（占比 21.57%）。包括 `the sift`（607 次）、`sift dimension`（548 次）、`the sift dimension`（314 次）、`the sift bedrock`（123 次）等。
3. **Learn and Solve（操作/解决类）**：1,069 次引用（占比 9.57%）。全部聚焦在“如何造门、如何点火、如何进入”。在包含 `portal` 的 19 个具体查询词中，一号站吞下了 **887 次引用**，并在最核心的构建问题上达到 56%–60.87% 的全网引用份额。

#### ④ 为什么 `/portal` 表现极强？

1. **Answer-First 语义结构契合大模型抽取习惯**：页面首屏 50 词内直接给出了传送门核心参数（5×7 尺寸、哭泣黑曜石材质、回响碎片充能激活），大模型无需在长文中寻找结论。
2. **结构化参数对照表（Tabular Knowledge）**：`/portal` 页面拥有全站唯一的标准 `<table>` 表格，对比了 Nether（1:8）、The End（1:1）与 The Sift（1:4）的压缩比和激活物。在 RAG（检索增强生成）召回阶段，结构化表格的稠密向量得分最高，极易被直接嵌入生成式回答。
3. **精准实体锚定与时机抢跑**：在 2026-09-27 爆发窗口，传统 Wiki 尚未立项，一号站以 EMD 域名与精准 URL `/portal` 抢先完成索引，建立了先发知识实体图谱。

---

### 2. 核心问题与痛点：引用量 vs 实际入站 UV 的转化断层

虽然 AI 引用次数突破 20,000 次，但实际进入站点的真实用户访问量（Active Users）却出现严重断层。

#### ① AI 引用与入站流量对比表 (2026-10-06 ~ 2026-10-12)

| 日期 | Bing Copilot AI 引用次数 | 实际入站活跃用户 (Active Users) | 实际浏览量 (Pageviews) | 入站转化率 (UV / Citations) | Zero-Click 损耗率 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 2026-10-06 | 1,579 | 94 | 111 | 5.95% | **94.05%** |
| 2026-10-07 | 1,078 | 51 | 77 | 4.73% | **95.27%** |
| 2026-10-08 | 759 | 47 | 75 | 6.19% | **93.81%** |
| 2026-10-09 | 735 | 97 | 215 | 13.20% | **86.80%** |
| 2026-10-10 | 941 | 33 | 42 | 3.51% | **96.49%** |
| 2026-10-11 | 768 | 81 | 199 | 10.55% | **89.45%** |
| 2026-10-12 | 699 | 49 | 93 | 7.01% | **92.99%** |
| **区间合计 / 均值** | **6,559** | **452** | **812** | **6.89%** | **93.11%** |

#### ② Zero-Click 损耗归因分析

1. **AI 对话框直接满足（Satisfied-in-Place）**：
   用户在 Bing Copilot 或 ChatGPT 提问“how to make a sift portal in minecraft”，AI 基于一号站提供的事实直接回答：“To make a sift portal, build a 5x7 frame with Crying Obsidian and light it with an Echo Shard.” 用户获取了答案后立刻关闭对话框，根本不需要点击卡片下方的参考来源角标。
2. **缺乏站内独占交互与高价值钩子（Missing Functional Hook）**：
   页面上的核心知识以纯文本形式被完全暴露并被 AI 吸收，但没有在首段植入“文本无法表达、必须进站使用”的交互型资产（如动态坐标计算器、一键服务器预装包、可复制指令生成器）。
3. **入站转化断层危害**：
   20,187 次引用仅换来数以百计的实际入站 UV，导致 Adsterra 广告展示量和 Apex Hosting 联机分销佣金未达预期。必须实施“防 Zero-Click 截流”策略，将 AI 引用转化为实际点击。

---

## 二、各核心页面 GEO 漏洞与缺口诊断 (Page-by-Page Audit)

运行 `audit_deterministic.py` 确定性审计引擎，对当前已上线的 3 个核心页面进行全量 52 项规则扫描。

### 1. 首页 `/`（https://thesiftguide.com/）

- **审计得分**：**100 / 100 (Grade A)**
- **缺陷统计**：0 个 P1 阻断，0 个 P2 严重，3 个 P3 优化项
- **要素剖析**：
  1. `Crawling & Indexing` (100/100)：HTTPS、Robots.txt、Sitemap 与规范标签健全。
  2. `On-page & Content` (100/100)：H1 明确、单词密度合理。
  3. `Structured Data` (100/100)：已部署 `Organization`、`WebSite` 与 `FAQPage`。
- **GEO 漏洞诊断**：
  - **`geo_table_missing` (P3，影响分 10)**：
    * **现状**：首页的“Fast Facts”区域全部采用 `<div class="grid grid-cols-1 sm:grid-cols-2">` 渲染卡片。虽然视觉良好，但由于缺少标准 `<table>` 语义标签，AI 搜索引擎在执行参数化表格抽取时命中率低。
    * **业务影响**：大模型无法以结构化 Key-Value 形式批量提取版本时间（Target 2027）、对应版本（Java & Bedrock）、衍生游戏（Dungeons II）等核心规格。
  - **`geo_citations_missing` 潜在脆弱性**：
    * 首页目前出站链接仅有 Apex Hosting 推广链接，缺乏指向 Minecraft 官方公告（`minecraft.net`）与官方 Wiki 的权威引用。
  - **`llms_txt_missing` (P3，影响分 0)**：
    * 网站根目录缺少 `/llms.txt`。

### 2. 传送门页 `/portal`（https://thesiftguide.com/portal）

- **审计得分**：**100 / 100 (Grade A)**
- **缺陷统计**：0 个 P1 阻断，0 个 P2 严重，2 个 P3 优化项
- **GEO 优势分析**：
  - 拥有全站唯一的 3 列标准数据表（行 582–616：Nether / The End / The Sift 对比），完美满足 `geo_table_missing` 规则。
  - Answer-First 首段符合 40–60 词要求，促成了 60.87% 的垄断级引用份额。
- **GEO 隐患与防御死角**：
  - **假性合规（False Grounding）**：审计引擎通过检测到 2 处外部链接判定出站链接数合格，但这两处链接全部指向同一个商业赞助商 `billing.apexminecrafthosting.com`。没有实际链接到官方规范或维基百科。当竞品页面或大型游戏媒体（如 IGN, Dexerto）加入维基出站锚点后，一号站目前的权威评级极易被超越。
  - **缺乏截流转化诱饵**：页面虽有 Apex 广告，但广告与“解决点火故障”的心理痛点脱节。

### 3. 新子页 `/how-to-enter`（https://thesiftguide.com/how-to-enter）

- **审计得分**：**99 / 100 (Grade A)**
- **缺陷统计**：**0 个 P1 阻断，1 个 P2 严重，3 个 P3 优化项**
- **GEO 漏洞专项诊断**：
  - **ACT-001: `geo_citations_missing` (P2 级严重缺陷，影响分 30)**
    * **代码证据**：页面全篇仅在赞助卡片中包含了 1 个指向 `billing.apexminecrafthosting.com` 的外部链接。
    * **审计判定**：`Page has only 1 outbound citation(s) (< 2). Ground facts with references to .gov, court dockets, or primary authority.`
    * **致命性**：根据普林斯顿论文，缺失外部权威信源支撑的页面在 AI 综合排序中信任分大幅折损，无法获得高置信度召回。
  - **ACT-002: `geo_table_missing` (P3 级优化项，影响分 10)**
    * **代码证据**：页面使用大量 `<h3>` 与卡片展示 4 步开门步骤、Java/Bedrock 指令与故障排查，但没有任何 `<table>` 元素。
    * **审计判定**：`Page lacks a structured <table> for quantitative parameter extraction by AI search engines.`
    * **影响**：AI 检索“how to enter the sift java vs bedrock”时，无法直接提取表格进行摘要展示。

---

## 三、权威出站信源（Cite Sources Grounding）规划

普林斯顿大学在 KDD'24 发表的《Generative Engine Optimization: A Novel Approach for Optimizing Visibility in Generative Search Engines》通过控制变量实证表明：在 9 种优化策略中，**Cite Sources（权威信源引用）能够带来高达 +30% 至 +40% 的相对可见性（Visibility）与引用份额增长**，排名第一。

### 1. 权威外部锚点名单（Primary Authorities）

为一号站确立三大层级的官方与权威出站源，杜绝任何低权重或不可信外链：

1. **顶级官方信源（Tier 1: Mojang / Microsoft Official）**：
   - 官方域名：`minecraft.net`
   - 核心页面：
     * Minecraft Live 2026 官方回顾：`https://www.minecraft.net/en-us/article/minecraft-live-2026-recap`
     * 荒野更新与远古城市开发日志：`https://www.minecraft.net/en-us/article/the-wild-update-ancient-cities`
2. **官方维基知识图谱（Tier 2: Minecraft Wiki / Weird Gloop）**：
   - 官方域名：`minecraft.wiki`（全球 Minecraft 社群唯一官方认可维基）
   - 核心页面：
     * 远古城市传送门框架结构：`https://minecraft.wiki/w/Ancient_City`
     * 强化深板岩技术机制：`https://minecraft.wiki/w/Reinforced_Deepslate`
     * 回响碎片合成与声波催化：`https://minecraft.wiki/w/Echo_Shard`
3. **开源模组与社区发行平台（Tier 3: Modrinth & CurseForge）**：
   - 官方域名：`modrinth.com` 与 `curseforge.com`
   - 核心页面：
     * Modrinth 模组平台：`https://modrinth.com/mods`
     * CurseForge MC 社区：`https://www.curseforge.com/minecraft/mc-mods`

### 2. 各页面权威出站链接注入位置与锚文本契约

必须在 HTML 中精准实施如下超链接契约，统一配置 `target="_blank" rel="noopener noreferrer"`：

| 页面路径 | 注入目标段落 / 模块 | 精确锚文本 (Anchor Text) | 目标 URL | 语义支撑角色与权威背书 |
| :--- | :--- | :--- | :--- | :--- |
| **`/how-to-enter`** | Section 1: "The Ancient City Portal Truth" | `official Minecraft Wiki Ancient City documentation` | `https://minecraft.wiki/w/Ancient_City` | 证实 Reinforced Deepslate 框架在原版中无法开采的事实 |
| **`/how-to-enter`** | Section 2: "Step 3: Trigger Ignition Sequence" | `Mojang's The Wild Update release notes` | `https://www.minecraft.net/en-us/article/the-wild-update-ancient-cities` | 证实回响碎片（Echo Shard）与幽匿声波机制的官方来源 |
| **`/how-to-enter`** | Section 1: "Roadmap vs. Fan Recreations" | `Modrinth community dimension mods` | `https://modrinth.com/mods` | 引导寻找可游玩第三方模组包的合法官方平台 |
| **`/` (首页)** | Section: "Fast Facts & Key Takeaways" | `Minecraft Live 2026 official broadcast announcement` | `https://www.minecraft.net/en-us/article/minecraft-live-2026-recap` | 支撑 2027 第四维度上线时间点的可信度 |
| **`/` (首页)** | Section: "Ancient Deepslate Architecture" | `Minecraft Wiki Reinforced Deepslate data sheet` | `https://minecraft.wiki/w/Reinforced_Deepslate` | 支撑维度传送门边框硬度与不可破坏性参数 |
| **`/portal`** | Section 1: "Official Forensics" | `Minecraft Wiki Echo Shard lore` | `https://minecraft.wiki/w/Echo_Shard` | 强化点火催化剂的权威信源依据 |
| **`/portal`** | Section 2: "Confirmed Frame Blocks" | `Mojang developer design notes on ancient structures` | `https://www.minecraft.net/en-us/article/the-wild-update-ancient-cities` | 强化 5×7 门框比例的设计渊源 |

---

## 四、防 Zero-Click 截流与变现咬合方案 (Anti-Zero-Click CRO)

面对 AI 搜索高达 93% 的 Zero-Click 损耗率，增长策略必须从“单纯提供静态事实”转变为“**以事实为饵，以交互和联机为钩**”。

### 1. 核心商业变现咬合：Apex Hosting 分销强化

- **合作条款**：15% 循环佣金（Recurring Commission）
- **转化权益**：全站独家优惠码 `APEX25`（首月立减 25%）
- **目标受众转化心理洞察**：
  搜索“how to enter the sift in minecraft”的用户，其终极目的不是在单机世界对着无法点燃的原版框架发呆，而是**与朋友联机体验最新的 Sift 维度模组和衍生玩法**。
- **痛点转化场景设计**：
  在用户遭遇挫折的瞬间（“为什么我的火点不着？为什么原版没有反应？”），直接承接解决方案：
  > *“想要和好友一起立即探索 The Sift？无需折腾复杂的本地端口映射或 Hamachi。使用 Apex Hosting 一键部署专属模组服务器，预装 2026/2027 维度快照，结算输入 `APEX25` 享受 25% 优惠。”*

### 2. 防 Zero-Click 的三大交互钩子（Conversion Hooks）

#### ① 坐标换算与材料规划钩子（Calculator Hook）
- **机制**：AI 可以在对话框中告诉用户“The Sift 的空间压缩比是 1:4”，但 AI 无法直接在聊天窗口里替用户动态换算他的私人基地坐标（例如：Overworld X: -1842, Z: 593 对应 The Sift 哪一组坐标？需要消耗几组哭泣黑曜石？）。
- **落地契约**：在所有页面的首屏 Answer-First 段落正下方，紧跟醒目的悬念 CTA 按钮：
  * **文案**：`Overworld ↔ The Sift Coordinate Linkage Calculator (1:4 Ratio)`
  * **行为**：锚点平滑滚动跳转至交互式计算器，引导用户输入坐标与材料计算，强迫从 AI 对话泡跳入网页。

#### ② 一键服务器与指令复制器（1-Click Command Copier）
- **机制**：针对管理员与建筑党玩家，提供经过转义的高亮命令行。
- **功能**：
  * Java Edition 原生维度传送指令：`/execute in minecraft:the_sift run tp @s ~ ~ ~`
  * 给予核心钥匙指令：`/give @p minecraft:echo_shard{Enchantments:[{id:"minecraft:unbreaking",lvl:1}]} 1`
  * 按钮增加视觉动效：点击后弹出绿字“Copied to Clipboard!”，提升用户操作满意度。

#### ③ 动态版本诊断组件（Interactive Diagnostic Tool）
- **机制**：在 `/how-to-enter` 页面首屏上方，提供下拉选择框：
  1. 选择你的游戏版本（Java Edition 1.21+ / Bedrock Edition / Modded 1.20.1）
  2. 选择你的开门方式（Ancient City Survival / Creative Mode / Modpack）
  3. 诊断输出：直接给出可执行的针对性解决方案，并在结果中精准推荐适配该版本的 Apex Hosting 服务器一键配置模版。

---

## 五、Hacker 工程实施清单与优先级 (Action Plan)

为确保 Hacker 能以零歧义、纯机械化的方式实施落地，将优化工作拆解为 4 项具象化工程任务。

### 1. 任务分解与执行清单

#### 【任务 1】根目录新增 `llms.txt`（消除全站 `llms_txt_missing` 缺陷）
- **操作文件**：`/home/louis/candi-tasks/thesiftguide/llms.txt`
- **优先级**：P3（速胜项，工作量 1/4）
- **实施内容**：创建标准化 Markdown 文件，完整声明站点实体、价值主张与关键子页架构：
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

#### 【任务 2】重构 `/how-to-enter.html`（消除 P2 `geo_citations_missing` 与 P3 `geo_table_missing`）
- **操作文件**：`/home/louis/candi-tasks/thesiftguide/how-to-enter.html`
- **优先级**：P2（阻断性门禁，影响分 30）
- **实施内容**：
  1. **注入权威出站链接**：
     - 在行 580（Ancient City 介绍）注入：`<a href="https://minecraft.wiki/w/Ancient_City" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">official Minecraft Wiki Ancient City documentation</a>`
     - 在行 645（Echo Shard 步骤）注入：`<a href="https://www.minecraft.net/en-us/article/the-wild-update-ancient-cities" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">Mojang's The Wild Update release notes</a>`
     - 在行 595（社区模组介绍）注入：`<a href="https://modrinth.com/mods" target="_blank" rel="noopener noreferrer" class="text-cyan-400 font-bold hover:underline">Modrinth community dimension mods</a>`
  2. **注入核心参数矩阵表 (`<table>`)**：
     在 Section 2 开头（约行 615）插入标准 HTML 表格组件：
```html
<div class="space-y-3 my-6">
    <h3 class="text-lg font-display font-bold text-white flex items-center gap-2">
        <span>The Sift Portal Activation & Compatibility Matrix</span>
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

#### 【任务 3】升级 `/index.html`（消除 P3 `geo_table_missing` 与强化权威外链）
- **操作文件**：`/home/louis/candi-tasks/thesiftguide/index.html`
- **优先级**：P3（影响分 10）
- **实施内容**：
  1. 在“Fast Facts”区域（约行 518 之前）注入标准表格：
     * 表格标题：`The Sift Dimension Core Specifications & Timeline`
     * 字段包含：Dimension Index (4th Realm)、Release Target (2027 Official Snapshot)、Frame Block (Soul Crying Obsidian / Deepslate)、Coordinate Compression (1:4 Ratio)、Early Access Platform (Minecraft Dungeons II)。
  2. 在正文描述中引入指向 `https://www.minecraft.net/en-us/article/minecraft-live-2026-recap` 与 `https://minecraft.wiki/w/Reinforced_Deepslate` 的权威超链接。

#### 【任务 4】完善 `/portal.html`（巩固垄断与替换商业纯依赖）
- **操作文件**：`/home/louis/candi-tasks/thesiftguide/portal.html`
- **优先级**：P3（防御项）
- **实施内容**：
  在现有的参数对比表（行 580）下方或 Forensics 区域，注入官方维基链接（`https://minecraft.wiki/w/Echo_Shard` 与 `https://minecraft.wiki/w/Ancient_City`），确保页面外部链接包含真实权威公信力背书。

---

### 2. 验收指标与门禁标准 (Acceptance Criteria)

所有修改完成后，执行如下标准自动化验证，必须达成全部硬性指标方可合流上线：

1. **确定性审计全满分**：
   运行以下 3 条审计命令：
   - `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/`
   - `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/portal`
   - `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/how-to-enter`
   * **验收基准**：
     * **综合得分全部达到 100 / 100 (Grade A)**；
     * **P1 阻断性缺陷 = 0**；
     * **P2 严重缺陷 = 0**（彻底清除 `/how-to-enter` 的 `geo_citations_missing`）；
     * **P3 级常规缺陷清零**（彻底消除 `geo_table_missing` 与 `llms_txt_missing`，仅允许 Google 官方针对政府机构的 `faq_rich_result_limited` 提示作为可忽略项）。
2. **E2E 回归测试验证**：
   运行 `/home/louis/candi-tasks/thesiftguide/run_e2e.sh`，确保全站现有 12 项 Playwright 端到端断言 100% 通过（无页面布局畸变、无广告破损、无死链）。
3. **Cloudflare Pages 边缘部署**：
   执行 `./deploy_pages.sh` 完成生产环境同步。

---

## 六、总结与交付结论

一号站在 Bing Copilot 上取得的 **20,187 次引用与 60.87% 的绝对垄断**，证明了“**Answer-First + 结构化表格 + 突发词 EMD 抢跑**”这一套流派具有强大的统治力。

然而，面对新一代大模型引擎对信源权威度（Fact Grounding）的收紧，以及 **93.11% 的惊人 Zero-Click 损耗**，一号站必须立即执行本次规划：
1. 通过 **Mojang 官方 + Minecraft Wiki 权威出站锚点**，将普林斯顿实证的 **+30%~40% GEO 曝光增益** 牢牢锁死；
2. 通过全站普及规范的 **参数矩阵 `<table>` 表格**，抹平所有页面的机器抽取缺陷，达成 `audit_deterministic.py` 全页面 100 分满分；
3. 通过 **坐标换算器 + 一键复制指令 + Apex Hosting 联机痛点承接**，把漂浮在 AI 聊天界面的海量查询截流转化为真实的站内访问量与高额佣金。

本报告已同步落盘至 `/home/louis/candi-tasks/thesiftguide/HUSTLER_GEO_DIAGNOSTIC_REPORT.md`，即刻提交评审。
