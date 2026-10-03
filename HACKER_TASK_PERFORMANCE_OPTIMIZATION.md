# Hacker 工单：全站性能与 Core Web Vitals 极限提速优化

## 业务背景与目标
用户在 Google PageSpeed Insights (Lighthouse) 诊断报告中发现：
- 桌面端性能虽然高达 **94 分**（SEO 满分 100，A11y 97，Best Practices 96），
- 但移动端在模拟慢速 4G 网络下的性能评分偏低（约 49 分），存在首屏渲染阻塞（Render-blocking resources）。
Google 采用移动优先索引（Mobile-First Indexing），为了加速下周 Google 走出沙盒期的关键词放量，现需对全站 6 个 HTML 页面实施无损提速优化。

---

## 详细优化措施（按优先级执行）

### 1. 修复 SVG 路径坐标语法报错（消除 Console Error）
- 排查定位：在 `index.html` (L462) 与 `dungeons-2.html` (L480) 中的 Help 图标：
  - 错误代码：`<path d="9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>`
  - 修复为标准语法：`<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>`（补上开头的绝对移动指令 `M`）
- 目标：彻底消除 Chrome Console 中的 `<path> attribute d: Expected moveto path command` 错误，提升 Best Practices 分数。

### 2. 广告脚本异步非阻塞加载（解除 0.8s~1.5s 关键路径阻塞）
- 目前全站页面的 Adsterra `invoke.js` 均为同步阻塞加载：
  `<script src="https://www.highrevenueformat.com/.../invoke.js"></script>`
- 将所有页面（`index.html`, `portal.html`, `mobs.html`, `dungeons-2.html` 等）中的两处 `invoke.js` 统一加上异步属性：
  `<script async="async" data-cfasync="false" src="https://www.highrevenueformat.com/.../invoke.js"></script>`
- 目标：让广告脚本在后台非阻塞并行加载，不再占用主文档首屏解析关键路径，同时保持 `atOptions` 参数正常传递。

### 3. Google Web Fonts 字体异步非阻塞加载
- 目前全站使用：
  `<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">`
- 优化为标准的高性能异步加载模式：
  保留已有的 preconnect，同时为字体 stylesheet 增加异步支持：
  `<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap">`
  `<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">`
  `<noscript><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet"></noscript>`
- 目标：解除字体 CSS 对 FCP/LCP 的 800ms 网络阻塞。

### 4. 编写独立 Python 批量补丁脚本
编写 `/tmp/apply_cwv_optimizations.py`，遍历全站 6 个 HTML 页面（`index.html`, `portal.html`, `mobs.html`, `about.html`, `privacy.html`, `dungeons-2.html`）安全就地实施上述修改。

---

## 红线约束与验收测试
1. **红线资产**：
   - GA4 跟踪代码 `G-X1ZTW8XWPG` 完整无损；
   - 广告 Key `e34c08305944ef076210b30b1897f6eb` 与 `93a1b6fb1cf3809a6ddd2ccae9364526` 完整保留，广告位容器结构与幽灵占位不变；
   - Tailwind 3.4.17 运行时保持稳定；
   - 严禁引入任何第三方恶意重定向；
2. **测试门禁**：
   - 运行 `./run_e2e.sh --target local` 确保 8 项用例全部 PASS；
   - 部署至 Cloudflare Pages：`./deploy_pages.sh`；
   - 运行 `./run_e2e.sh --target live` 确保线上全部 PASS；
   - 运行 Lighthouse 审计命令核验提速效果；
3. **仓库同步**：
   - 仅提交并推送到 GitHub 私有库 `thesiftguide-private`，严禁推送至公开库。

完成后输出详细总结。
