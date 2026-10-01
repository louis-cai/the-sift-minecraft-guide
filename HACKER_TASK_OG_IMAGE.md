# 任务书：挂载 OpenGraph 与 Twitter Card 社交大图标签

## 背景
社交分享图 `/home/louis/candi-tasks/thesiftguide/og-image.png`（1200x630 高清图）已经生成就绪。
现需 Hacker 通过脚本向 `/home/louis/candi-tasks/thesiftguide/index.html` 挂载完整的 Open Graph 与 Twitter Card 标签。

## 执行要求
编写并执行一个 Python 脚本（`/tmp/inject_og_tags.py`），对 `/home/louis/candi-tasks/thesiftguide/index.html` 进行就地注入：

在 `<head>` 中原有的 `<!-- Open Graph / Social Meta -->` 区域更新/补充：
```html
    <!-- Open Graph / Facebook / Discord -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="The Sift Minecraft: Complete Guide to the 4th Dimension">
    <meta property="og:description" content="Everything announced at Minecraft Live 2026 about The Sift: Biomes, mobs, release date, and gameplay mechanics.">
    <meta property="og:url" content="https://thesiftguide.com/">
    <meta property="og:image" content="https://thesiftguide.com/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="The Sift Minecraft Guide - 4th Dimension Interactive Wiki">

    <!-- Twitter / X Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="The Sift Minecraft: Everything We Know About the 4th Dimension">
    <meta name="twitter:description" content="Complete guide to Minecraft's 4th official dimension after 14 years: biomes, mobs, release date, and gameplay mechanics.">
    <meta name="twitter:image" content="https://thesiftguide.com/og-image.png">
```

## 🔴 红线
- 严禁全量 write_file 复写 60KB HTML（避免截断，必须走脚本精确替换）。
- 保留 GA4（`G-X1ZTW8XWPG`）、Schema JSON-LD、Favicon、Tailwind 直连。

执行完成后进行检查并报告。
