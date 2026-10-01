# UI/UX 优化任务书：The Sift Minecraft Guide (thesiftguide.com)

## 背景
`thesiftguide.com` 是针对 Minecraft 官方在 Minecraft Live 2026 宣布的第 4 维度「The Sift」的垂直单页指南与互动 Wiki。当前页面内容完整（1158词），已成功编入 Google 索引。现需进行专业的 UI/UX 与交互视觉优化。

## 目标
利用已挂载的 `ui-ux-pro-max` skill，对 `/home/louis/candi-tasks/thesiftguide/index.html` 进行前端视觉与交互体验升级。

## 执行要求与工作流
1. 使用 `ui-ux-pro-max` 工具检索设计规范：
   ```bash
   python /home/louis/skills-vendor/ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max/scripts/search.py "gaming entertainment dark wiki interactive" --design-system -p "The Sift Guide"
   ```
2. 依据检索出的配色（Emerald/Cyan/Amber 暗黑奇幻风格）、间距、卡片质感、排版与微交互，重构/升级 `/home/louis/candi-tasks/thesiftguide/index.html`。
3. 增强点：
   - Hero 区域：震撼的视觉冲击，标题发光字，副标题与快速导航。
   - 快速概览卡片（Fast Facts）：数据化、徽章化、清晰易读。
   - 机制与群系（Biomes & Mobs）：图文卡片排版、群系色彩对比（Meadow 绿色系 vs Carapace 蓝色系）。
   - 交互体验：平滑滚动、微动效（hover 悬浮微光）、FAQ 展开折叠或清晰卡片布局。
   - 移动端适配：确保手机上无横向滚动，触摸区域 ≥ 44px。

## 🔴 绝对红线约束（严禁篡改或删除以下内容）
1. **必须保留 GA4 探针**：
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-X1ZTW8XWPG"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-X1ZTW8XWPG');
   </script>
   ```
2. **必须保留 Schema JSON-LD 结构化数据**：
   完整的 `<script type="application/ld+json">` 及其中的 WebSite、Article、FAQPage（4 个问题）必须完好保留。
3. **必须保留 SEO Meta 与 Favicon 标签**：
   Title、Description、Keywords、Canonical、OpenGraph、favicon.svg、favicon.ico 等全套标签。
4. **CSS 依赖规范**：
   使用官方直连带版本的 CDN：
   `<script src="https://cdn.tailwindcss.com/3.4.17"></script>`
   任何自定义增强样式写入 `<style>` 标签中。

## 验收交付物
- 更新后的 `/home/louis/candi-tasks/thesiftguide/index.html` 文件。
- 一份简明优化汇报：说明采用了哪些 UI/UX Pro Max 规范与具体的视觉/交互提升点。
