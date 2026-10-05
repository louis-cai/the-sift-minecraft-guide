# Hacker 工单：升级 Google SERP 标准 48px/96px Favicon 并全站部署

## 业务背景与目标
用户在 Google 搜索结果中发现 `thesiftguide.com` 目前显示的是 Google 默认的地球占位符，而不是我们设计的绿色传送门方块 Logo。
排查定位：
1. Google 官方文档明确说明 Google 搜索结果的 Favicon 不支持 SVG 格式（仅支持 PNG/ICO/GIF 等位图）；
2. Google 官方明确推荐尺寸为 **48px 的倍数（48x48, 96x96 等）**，现有站点缺少 48x48 和 96x96 的声明，且 SVG 标签排在第一位导致 Googlebot-Image 无法提取。
现需从 `icon-512.png` 高清母图生成 48x48 和 96x96 标准位图，并就地批量更新全站 6 个 HTML 页面的 Favicon 声明标签。

---

## 详细执行规范

### 1. 生成标准尺寸图标
使用 Python PIL 从 `/home/louis/candi-tasks/thesiftguide/icon-512.png` 导出：
- `/home/louis/candi-tasks/thesiftguide/favicon-48x48.png` (48x48 PNG, RGBA, 质量最高抗锯齿 Lanczos)
- `/home/louis/candi-tasks/thesiftguide/favicon-96x96.png` (96x96 PNG, RGBA, 质量最高抗锯齿 Lanczos)

### 2. 批量更新 6 个 HTML 页面的 Favicon 标签
编写 `/tmp/patch_google_favicons.py`，遍历：
- `index.html`
- `portal.html`
- `mobs.html`
- `about.html`
- `privacy.html`
- `dungeons-2.html`

将旧的 Favicon 区域（从 `<!-- Favicon` 到 `<link rel="shortcut icon"`）：
替换为 Google 搜索结果最优顺位规范：
```html
    <!-- Favicon & App Icons (Optimized for Google Search SERP 48px standard) -->
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
```

### 3. 严格保护已有红线资产（严禁动弹）
- [ ] GA4 测量代码 `G-X1ZTW8XWPG` 完整无损；
- [ ] Schema.org 结构化数据完整保留；
- [ ] Adsterra 官方标准同步脚本（顶部 728x90 `e34c08305944ef076210b30b1897f6eb`、底部 300x250 `93a1b6fb1cf3809a6ddd2ccae9364526`）保持同步；
- [ ] Tailwind 3.4.17 直连与 Web Fonts 预加载保持不变；
- [ ] 移动端零横向溢出。

### 4. 门禁验证与部署流程
1. 本地 Playwright 测试：运行 `./run_e2e.sh --target local` 确保全部用例 PASS；
2. 生产部署：运行 `./deploy_pages.sh` 部署至 Cloudflare Pages 全球 CDN；
3. 线上生产复测：运行 `./run_e2e.sh --target live` 确保全量通过；
4. 验证线上响应：通过 curl 确认 `https://thesiftguide.com/favicon-48x48.png` 和 `favicon-96x96.png` 均为 HTTP/2 200 OK；
5. 仓库同步：同步最新生产文件至 `/home/louis/candi-tasks/thesiftguide-repo/`，仅提交并推送至 GitHub 私有库：
   `git push private main`（**绝对严禁推送到公开库 origin 或 gitlab**）。

完成后输出详细总结。
