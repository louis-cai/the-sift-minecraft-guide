# 任务纠偏指令：使用 Python 脚本执行 Minecraft 风格配色升级

## 发生的问题
上一轮执行时，直接在模型输出中生成 57KB 完整 HTML 触发了模型单次输出截断（finish_reason='length'）。

## 破局铁律（工程分工最佳实践）
**严禁用 write_file 整体重写整个 57KB 的 index.html！**
请改为编写一个独立的 Python 脚本（例如 `/tmp/apply_mc_theme.py`），通过正则与字符串替换精确升级样式：

### 配色与样式修改点：
1. **背景色与面板**：
   - 全局背景从 `#070a12` 改为 **Minecraft 深板岩黑 `#111317`**
   - 卡片底色 `.glass-card` 从蓝黑改为 **Minecraft 深岩砖/平滑石面板 `#181a20`**
   - 增加 Minecraft 方块特有的微立体内发光边框：
     `border: 2px solid #2d3139; box-shadow: inset 1px 1px 0 rgba(255,255,255,0.08), inset -2px -2px 0 rgba(0,0,0,0.5);`
2. **核心标题与品牌渐变**：
   - `.title-glow` 调整为 **Minecraft 草方块绿到钻石青**：
     `linear-gradient(135deg, #a3e635 0%, #4ade80 30%, #22d3ee 70%, #38bdf8 100%)`
     投影微光使用 `rgba(74, 222, 128, 0.35)`
3. **按钮质感（Minecraft Button）**：
   - 按钮增加 Minecraft 经典 3D 浮雕按压质感：
     `box-shadow: inset 2px 2px 0 rgba(255,255,255,0.25), inset -2px -2px 0 rgba(0,0,0,0.5);`
   - 主行动按钮采用经典 **Minecraft 绿 `#46a228`**，hover 为 `#55bb32`。
4. **字体微调**：
   - 标题与重要数据增加 `font-family: ui-monospace, monospace` 或方块式粗体渲染，强化像素/方块感。

### 红线（必须严格保持）
1. GA4 `G-X1ZTW8XWPG` 完好无损
2. Schema JSON-LD 结构化数据完好无损
3. SEO Meta / Favicon 完好无损
4. Tailwind 3.4.17 保持直连

请编写并运行 `/tmp/apply_mc_theme.py`，执行并输出验收报告。
