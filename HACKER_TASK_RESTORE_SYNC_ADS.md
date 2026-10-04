# Hacker 工单：广告脚本恢复标准同步加载（保障广告 100% 渲染展示）

## 背景与目标
在上一轮 Core Web Vitals 优化中，Adsterra 的 `invoke.js` 广告脚本被加上了 `async="async" data-cfasync="false"` 属性。
经实测诊断发现：Adsterra 官方的 iframe 生成机制深度依赖全局变量 `atOptions`。当页面有两处广告且脚本被赋予 `async` 异步加载时，浏览器在弱网和多核并发下会触发 JS 执行时序竞态（变量被覆盖或脚本先于变量执行），导致 iframe 广告无法渲染（展示量断崖式下滑）。
现需将全站 6 个 HTML 页面（`index.html`, `portal.html`, `mobs.html`, `about.html`, `privacy.html`, `dungeons-2.html`）中的 Adsterra `invoke.js` 恢复为官方标准同步引入方式，同时严格保留已有的 Google Web Fonts 异步预加载优化与 SVG 语法修复。

---

## 详细执行规范

### 1. 编写独立 Python 批量恢复脚本
编写 `/tmp/restore_sync_ads.py`，遍历全站 6 个 HTML 页面：
- 将所有的：
  `<script async="async" data-cfasync="false" src="https://www.highrevenueformat.com/([a-f0-9]+)/invoke.js"></script>`
- 原地精准替换为标准同步形式：
  `<script src="https://www.highrevenueformat.com/\1/invoke.js"></script>`
- 保持已优化生效的高性能字体预加载（`<link rel="preload" as="style" ... onload="this.media='all'">`）与 SVG 修复不变。

### 2. 真实渲染核验
在本地 Chromium Headless 中模拟访问页面，验证广告脚本结构正确，且无语法或控制台报错。

### 3. 门禁测试与生产部署
1. 运行 `./run_e2e.sh --target local` 确保 8 项用例全部 PASS；
2. 执行 `./deploy_pages.sh` 部署至 Cloudflare Pages 全球 CDN；
3. 运行 `./run_e2e.sh --target live` 确保线上 8 项用例全量通过；
4. 将最新代码同步至 `/home/louis/candi-tasks/thesiftguide-repo/`，仅提交并推送到 GitHub 私有库：
   `git push private main`（**绝对严禁推送到公开库 origin 或 gitlab**）。

完成后输出详细总结。
