# Hacker 工单：扩充 Section 3 与 FAQ（Dungeons 2 现行实装 vs 2027 原版对比）

## 业务背景与 SEO 目标
《Minecraft Dungeons 2》已于 2026 年 9 月 29 日全球正式发售，并在游戏中率先实装了 The Sift（包含官方揭秘的 Singer's Meadow 与 Carapace 两大群系、双足行走兔子型生物、红 Sculk 等）。
当前页面中 Section 3 仍标注为 "Releases Sept 29, 2026"（未更新时效）。通过本次升级：
1. 修正发布时态为「NOW AVAILABLE (Released Sept 29, 2026)」，提升 Google Freshness 评分；
2. 新增清晰的「Dungeons 2 现行实战 vs. 2027 原版展望」对比矩阵（Side-by-Side Matrix），截流 "is the sift playable now"、"singers meadow"、"carapace biome" 等长尾搜索词；
3. 在 FAQ 板块及 Schema.org JSON-LD 中注入 2 条高频长尾问答。

---

## 详细执行规范

### 1. 编写独立 Python 脚本精准原地修改（禁止整文件重写）
编写 `/tmp/expand_dungeons2_content.py`，对 `/home/louis/candi-tasks/thesiftguide/index.html` 实施修改：

#### A. Section 3 (id="early-access") 升级
- 徽章从 `Releases Sept 29, 2026` 升级为：
  `<span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 self-start sm:self-auto"><span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>OUT NOW (Sep 29, 2026)</span>`
- 在现有的 "How Dungeons II connects to The Sift" 下方，追加一个双列对比矩阵卡片：
  - **左列：Minecraft Dungeons II (Playable Now)**：
    - 接入方式：通过主线战役中的时空裂隙（Overworld Rifts）直接穿梭；
    - 独家群系：**Singer's Meadow**（从红色 Sculk 中生长的奇花异草）与 **Carapace**（遍布巨大中空骨骼化石与蓝晶巨壁的荒漠）；
    - 玩法机制：受“潮汐漂移（Shifting Tides）”影响，遭遇双足行走的奇特兔子型生物。
  - **右列：Minecraft Java & Bedrock (Coming 2027)**：
    - 接入方式：14 年来第四大官方正统维度，需搭建正统维度传送门（参考下方计算器）；
    - 规划路线：预计 2026 年底至 2027 年初开启每周开发快照（Snapshot）公开测试；
    - 玩法机制：全沙盒无限程序化生成，包含完整方块采集、合成配方与群系生存挑战。
- 样式标准：保持 Minecraft 原生深色风格（深板岩黑背景、网格背景、绿/青/金强调色、石质阴影），响应式适配（移动端 `flex-col`，桌面端 `grid-cols-1 md:grid-cols-2`），文字无横向溢出。

#### B. FAQ 板块与 Schema.org JSON-LD 注入
- 向 HTML 手风琴 FAQ 列表中追加 2 条高价值问答：
  1. **Q: Is The Sift dimension playable right now?**
     A: Yes! You can experience The Sift immediately in Minecraft Dungeons 2, which launched on September 29, 2026. The main sandbox game (Java and Bedrock editions) will receive The Sift update in 2027.
  2. **Q: What biomes are confirmed for The Sift?**
     A: Two major biomes have been revealed by Mojang: **Singer's Meadow** (a vibrant landscape where alien flora grows from red sculk) and **Carapace** (a desolate desert filled with towering blue structures and giant hollow fossils).
- 同步向 `<script type="application/ld+json">` 中的 `FAQPage` 数组追加这两条结构化问答，确保 Schema.org 语法 100% 合法无错。

---

### 2. 绝对红线资产保护（零容忍）
- [ ] 顶部 728x90 广告（`e34c08305944ef076210b30b1897f6eb`，`highrevenueformat.com`）完好无损；
- [ ] 底部 300x250 广告（`93a1b6fb1cf3809a6ddd2ccae9364526`，`highrevenueformat.com`）完好无损；
- [ ] 绝对禁止引入任何 Native Banner 或 `justverify` 等流氓跳转代码；
- [ ] GA4 测量 ID `G-X1ZTW8XWPG` 完整无损；
- [ ] Tailwind CDN 保持 `cdn.tailwindcss.com/3.4.17` 直连；
- [ ] 页面元数据（Meta、OG、Twitter、Favicon）保持完好。

---

### 3. 门禁验证与生产部署
1. 本地测试：运行 `./run_e2e.sh --target local`，确保 6 大套件 11 项用例全部 PASS；
2. 生产部署：调用 `./deploy_pages.sh` 将更新发布至 Cloudflare Pages 全球 CDN；
3. 生产复测：运行 `./run_e2e.sh --target live`，确认线上 11 项用例全部通过，移动端零溢出；
4. 仓库同步：同步最新文件至 `/home/louis/candi-tasks/thesiftguide-repo/`，仅提交并推送到私有库：
   `git push private main`（**绝对严禁推送到公开库 origin 或 gitlab**）。

完成全部流程后，输出详细报告。
