# Hacker 工单：子页面物理隔离 —— 恢复首页稳定版并创建独立 dungeons-2.html

## 核心目标与 SEO 策略
遵循「主航母稳定，子页面抢长尾」的 SEO 铁律：
1. **首页 `index.html` 安全恢复**：将 `index.html` 恢复至 `commit 7f9d2c3` 的原始稳定版本（保护现有已排名的结构和关键词权重，仅在导航栏与 Section 3 保持与子页面的自然内链）；
2. **构建独立长尾子页面 `dungeons-2.html`**：将《Minecraft Dungeons 2》的专属内容（两大独家群系 Singer's Meadow / Carapace、时空裂隙机制、双足行走兔型生物、现行实装与 2027 原版对比矩阵、专属 FAQ）提炼为一个高质量的独立子页面；
3. **更新 `sitemap.xml`**：将 `https://thesiftguide.com/dungeons-2.html` 注册进站点地图，加速搜索引擎爬取；
4. **扩展 E2E 自动化测试**：确保 Playwright 覆盖新子页面；
5. **双门禁测试与生产部署**：完成本地与线上测试，推送至 GitHub 私有库备份。

---

## 详细执行规范

### 1. 首页 `index.html` 恢复
- 从 Git 提交 `7f9d2c3` 检出恢复原始的 `index.html`；
- 在全局导航栏中，确保拥有跳转至新子页面的入口链接（例如 `Dungeons II` 指向 `/dungeons-2.html`）；
- 保持原首页所有红线（GA4 `G-X1ZTW8XWPG`、双 Banner 广告位 `e34c08305944ef076210b30b1897f6eb` 与 `93a1b6fb1cf3809a6ddd2ccae9364526`、Tailwind 3.4.17、Schema.org）。

### 2. 独立子页面 `dungeons-2.html` 构建
- 参照 `mobs.html` 与 `portal.html` 的结构与视觉规范（Minecraft 原生深色风格、头部导航、页脚、双广告位、GA4、Favicon）；
- **SEO 标头**：
  - Title: `The Sift in Minecraft Dungeons 2: Biomes, Mobs, Rifts & 2027 Comparison | The Sift Guide`
  - Canonical: `https://thesiftguide.com/dungeons-2.html`
  - Meta Description: `Explore The Sift dimension in Minecraft Dungeons 2 (Released Sep 29, 2026). Guide to Singer's Meadow, Carapace desert biomes, Shifting Tides, and how it compares to the 2027 vanilla sandbox update.`
  - Keywords: `the sift minecraft dungeons 2, singers meadow, carapace biome, minecraft dungeons 2 the sift, how to play the sift now, the sift dimension guide`
- **页面主体内容**：
  - Hero 区域：`Minecraft Dungeons II: The Sift Dimension Hub`，标注 `OUT NOW (Released Sept 29, 2026)`；
  - 深度解析 1：**Singer's Meadow** 群系（红 Sculk 植被、环境机制）；
  - 深度解析 2：**Carapace** 群系（中空巨型骨骸沙漠、蓝晶巨壁、环境危害）；
  - 核心机制：时空裂隙（Overworld Rifts）、潮汐漂移（Shifting Tides）、双足行走兔型生物；
  - 对比矩阵：Dungeons 2 (ARPG / 现行实装) vs. Vanilla Minecraft (2027 正统沙盒更新)；
  - 专属手风琴 FAQ（配合 Schema.org FAQPage 结构化数据）；
  - 双广告位：顶部 728x90 与底部 300x250 标准 Banner（与主站一致，无缝透明幽灵占位）。

### 3. 更新 `sitemap.xml`
向 `sitemap.xml` 中追加：
```xml
  <url>
    <loc>https://thesiftguide.com/dungeons-2.html</loc>
    <lastmod>2026-10-01</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
```

### 4. 自动化测试门禁与部署
1. 更新/补充测试用例，确保 `test_e2e_thesiftguide.py` 验证 `dungeons-2.html` 访问正常、移动端无溢出；
2. 运行 `./run_e2e.sh --target local` 确保全部用例 PASS；
3. 执行 `./deploy_pages.sh` 部署至 Cloudflare Pages；
4. 运行 `./run_e2e.sh --target live` 确保线上全量通过；
5. 同步至本地仓库目录，执行 `git push private main`（绝对禁止推送至公开库）。

完成后输出详细总结。
