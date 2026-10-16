# Hustler Task: 一号站 (thesiftguide.com) 深度 GEO (生成式引擎优化) 诊断与增长策略报告

## 1. 任务背景与目标
一号站（`https://thesiftguide.com`）作为突发流量套利首站，在 Bing Copilot 等 AI 搜索引擎上已取得了惊人的先发引用成绩（10月2日–12日累计 **20,187 次 AI 引用**，并在核心问题如 `how to make a sift portal in minecraft` 上取得了 **60.87% 的垄断级全网引用份额**）。
然而，目前站内各页面在面对新一代 AI 搜索（ChatGPT Search, Perplexity, Bing Copilot, Google AIO）时，依然存在权威信源出站锚定不足、表格化事实缺失以及 Zero-Click 截流防御薄弱等问题。

作为首席增长官（Hustler），请基于普林斯顿大学 GEO 顶会论文实证、Bing 官方 AI Performance 导出真实数据及 `audit_deterministic.py` 确定性审计指标，对一号站进行一次**全方位的 GEO 深度诊断与落地升级规划**。

---

## 2. 诊断依据与数据源
1. **Bing 官方 AI Performance 真实报表**：
   - Mac 端落盘数据：`/Users/cailu/Downloads/thesiftguide.com_AISearchQueriesReport_10_15_2026.csv`
   - SQLite 时序数据：`~/.hermes/data/arbitrage_analytics.db` 表 `ai_citation_metrics`
2. **确定性审计引擎现状**：
   - 运行 `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/`
   - 运行 `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/portal`
   - 运行 `python3 /home/louis/.hermes/skills/web/seo-engine/scripts/audit_deterministic.py --url https://thesiftguide.com/how-to-enter`
3. **一号站实际代码**：`/home/louis/candi-tasks/thesiftguide/`

---

## 3. 诊断输出报告核心要求
产出完整的 Markdown 报告，落盘至：
`/home/louis/candi-tasks/thesiftguide/HUSTLER_GEO_DIAGNOSTIC_REPORT.md`

必须涵盖以下 5 大核心章节：

### 一、一号站当前 GEO 资产现状盘点 (Ground Truth)
- 分析 20,187 次 AI 引用的成因归因（为什么 `/portal` 表现极强？哪些词占到了 50%+ 份额？）；
- 核心问题与痛点（引用量 vs 实际入站 UV 的转化断层、Zero-Click 损耗率分析）。

### 二、各核心页面 GEO 漏洞与缺口诊断 (Page-by-Page Audit)
- **首页 `/`**：当前得分、结构化数据、缺少事实表格的原因与影响；
- **传送门页 `/portal`**：为什么被 AI 青睐？如何进一步巩固垄断地位？
- **新子页 `/how-to-enter`**：为什么被审计引擎判定 P2 缺陷（`geo_citations_missing` 缺失权威出站、`geo_table_missing` 缺失参数表）？

### 三、权威出站信源（Cite Sources Grounding）规划
- 根据普林斯顿论文（Cite Sources 提升 30%–40% AI 曝光），为一号站各页面制定权威外部锚点名单：
  * Mojang 官方文档 / 更新公告（`minecraft.net`）
  * Minecraft 官方维基（`minecraft.wiki`）
  * CurseForge / Modrinth 官方发布页
  * 制定具体注入位置与锚文本契约。

### 四、防 Zero-Click 截流与变现咬合方案 (Anti-Zero-Click CRO)
- 如何在给 AI 喂饱事实的同时，把深度联机与模组玩家引导至 Apex Hosting（15% 循环佣金，优惠码 `APEX25`）；
- 设计更具吸引力的交互钩子（Hook）与指令一键复制入口。

### 五、Hacker 工程实施清单与优先级 (Action Plan)
- 列出明确的改动项，供 Hacker 直接按清单落地；
- 验收指标（全站 3 个核心页面在 `audit_deterministic.py` 中全部达到 100 满分，0 个 P1/P2/P3 缺陷）。

---

## 4. 交付与流转
完成后，将报告落盘并调用 `hermes kanban request-review <task_id>` 申请 Candi 验收。
