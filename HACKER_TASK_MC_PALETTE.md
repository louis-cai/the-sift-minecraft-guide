# 任务书：The Sift Guide 页面配色全面对齐《Minecraft》官方游戏风格

## 目标
根据 Louis 指示，当前的页面配色偏通用科技风，**必须全面重构为 100% 贴合《Minecraft》（我的世界）原生游戏视觉的经典配色与方块美学**。

## 角色分工原则
由 Hacker 全权负责 `/home/louis/candi-tasks/thesiftguide/index.html` 的编码与样式修改。Candi 负责规格下达与红线验收。

## Minecraft 官方游戏配色规范（严格执行）

### 1. 基础背景与面板（Stone / Bedrock / Slate）
- 全局深色底色：从泛蓝黑改为 **Minecraft 深岩/基岩黑（Deepslate / Bedrock）**：`#111215` 或 `#141619`（不再使用 SaaS 蓝灰色）。
- 卡片面板背景：**Minecraft 平滑石/深板岩色（Smooth Stone / Deepslate Tile）**：`#1c1e24` 或 `#1e2026`。
- 边框与阴影：带有 Minecraft 方块特有的微倒角立体光影：
  `border: 2px solid #2e323b`，并增加像素/方块式立体高光阴影 `box-shadow: inset 1px 1px 0 rgba(255,255,255,0.08), inset -2px -2px 0 rgba(0,0,0,0.5)`。

### 2. 核心主色调（Grass Block / Creeper Green）
- 主强调色：采用最经典的 **Minecraft 草方块/苦力怕绿（Grass Green）**：
  - 正常：`#4aa52e` / `#52b735`
  - 悬浮/深色：`#3c8824` / `#2f6e1b`
  - 文字/高光：`#68d044`
  - （彻底替换原来通用的科技蓝青渐变）。

### 3. 维度特色配色（The Sift & Portal）
- **The Sift 传送门/维度能量**：**Minecraft 钻石/下界传送门青（Diamond / Nether Rift Cyan）**：`#38bdf8` / `#22d3ee` / `#00d2d3`。
- **Carapace 群系/化石遗迹**：**Minecraft 骨块色与远古琥珀金（Bone White & Raw Gold）**：
  - 骨块白：`#e2e8f0` / `#f1f5f9`
  - 经验球/黄金：`#fbbf24` / `#f59e0b`（经典的 EXP Orb 闪光金）。
- **Meadow 群系**：**Minecraft 苔藓绿/繁茂绿（Lush Moss Green）**：`#22c55e` / `#16a34a`。

### 4. UI 质感与组件样式（Minecraft UI Aesthetic）
- **按钮样式（Minecraft Stone Button）**：
  主行动按钮采用经典的 Minecraft 绿色按钮或石质按钮微立体质感（有 3D 按压反馈）。
- **徽章/Tag（Minecraft Badge）**：
  采用深色方块底 + 像素感边框，颜色对应 绿（Grass）、黄（Gold）、青（Diamond）。
- **标题视觉**：
  主标题采用 Minecraft 标志性的双色方块发光渐变（草绿到钻石青），保持史诗感与方块游戏辨识度。

## 🔴 绝对红线约束（严禁改动以下内容）
1. **保留 GA4 探针**：`id=G-X1ZTW8XWPG`
2. **保留 Schema JSON-LD 结构化数据**：包含 WebSite, Article, FAQPage 的全部 4 个问答。
3. **保留 Favicon 链路**：favicon.svg, favicon.ico, apple-touch-icon 等。
4. **保留 SEO Meta**：Title, Description, Keywords, Canonical, OpenGraph。
5. **依赖库**：继续保持 `<script src="https://cdn.tailwindcss.com/3.4.17"></script>` 直连版本，所有 Minecraft 自定义配色与方块质感可在 `<style>` 中增强。

## 交付要求
直接更新 `/home/louis/candi-tasks/thesiftguide/index.html` 并输出修改总结。
