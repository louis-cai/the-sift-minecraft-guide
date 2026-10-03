# Hacker 生产任务书：在 portal.html 内嵌 YouTube 视频与注入 VideoObject Schema

## 任务目标
为提升 thesiftguide.com 的 SEO/GEO 权威实体关联度与用户停留时间（Dwell Time），将新发布的官方 YouTube Short（`https://youtube.com/shorts/mdsxeO9mpd8`）反向内嵌至 `portal.html`，并注入 `VideoObject` Schema.org 结构化数据，严格执行 E2E 自动化测试门禁后部署至生产环境。

## 严格纪律
1. **分工铁律**：全部代码修改、E2E 测试与部署由 Hacker 执行。
2. **E2E 门禁铁律**：本地修改完成后，必须运行 `./run_e2e.sh --target local` 确保所有测试用例（包括新增或现有 6 个套件）100% PASS。
3. **部署与上线门禁**：通过本地测试后，执行 `./deploy_pages.sh` 部署，并执行 `./run_e2e.sh --target live` 完成线上全量回归与截图留存。

## 详细需求
1. **资产复制**：
   - 将 `/home/louis/candi-tasks/thesiftguide/youtube_shorts_thumbnail.png` 确保存在并打包在网站根目录，以作为 Schema 中的 Thumbnail 静态资源。
2. **页面内嵌 (portal.html)**：
   - 在 `portal.html` 的传送门命令与建造指南板块（Portal Construction & Commands）适当位置，新增一个自适应视频展示模块：
     - 标题：“30-Second Quickstart Video Guide”
     - 使用轻量、居中的竖屏短视频响应式容器（9:16，建议最大宽度 360px，居中，圆角，带暗黑深板岩边框与外发光）。
     - iframe 地址：`https://www.youtube-nocookie.com/embed/mdsxeO9mpd8`（采用 nocookie 域名，符合隐私合规，标题 "How to Enter The Sift in Minecraft"）。
     - 预留加载状态，避免 CLS（累积布局位移）。
3. **结构化数据 (JSON-LD VideoObject)**：
   - 在 `portal.html` 的 `<head>` 区域现有 JSON-LD 中新增或扩展 `@type`: `VideoObject`：
     - `name`: "How to Enter The Sift in Minecraft (Portal & Teleport Commands)"
     - `description`: "Quick 30-second tutorial on how to construct the portal and use exact teleport commands to enter The Sift dimension in Minecraft."
     - `thumbnailUrl`: "https://thesiftguide.com/youtube_shorts_thumbnail.png"
     - `uploadDate`: "2026-10-03T00:00:00+08:00"
     - `duration`: "PT30S"
     - `embedUrl`: "https://www.youtube-nocookie.com/embed/mdsxeO9mpd8"
     - `contentUrl`: "https://youtube.com/shorts/mdsxeO9mpd8"
4. **测试与部署**：
   - 执行 `./run_e2e.sh --target local`
   - 执行 `./deploy_pages.sh`
   - 执行 `./run_e2e.sh --target live`
   - 验证生产环境 `https://thesiftguide.com/portal.html` 正常加载。
