# Merrick 任务书：在 Adsterra 后台配置 Native Banner 与排查 Anti-AdBlock

## 背景与目标
针对当前 `thesiftguide.com` 上 iframe 广告在部分安装了拦截器（或苹果 Safari ITP）的设备上被屏蔽的问题，需要你在 Adsterra 发布商后台执行两项核心排障与新广告位创建：
1. **排查官方 Anti-Adblock 选项**：检查后台是否有 Anti-Adblock 功能入口、开关或独立域名说明。
2. **新建 Native Banner（原生图文横幅）单元**：原生横幅是纯图文流，天然免疫大多数基于 iframe 的拦截规则。创建并提取其完整广告代码。

## 执行角色与技能
- **执行者**：Merrick (Mac 端 Hermes 默认 profile)
- **技能**：请使用 `ego-browser` skill 接管已在 `ego lite` 浏览器中打开的 Adsterra 后台。

## 具体操作步骤
1. 打开或切换至 Adsterra Websites 页面：`https://beta.publishers.adsterra.com/websites`。
2. **排查 Anti-AdBlock**：
   - 检查 `thesiftguide.com` 展开项中、或者页面顶部/侧边导航（如 Settings / Profile / Help）中是否有关于 "Anti-AdBlock" 的专属选项、开关或说明；
   - 记录排查结果（是否有此功能，若需联系 Support 亦请注明）。
3. **新建 Native Banner 单元**：
   - 在 `thesiftguide.com` 这一行右侧点击 **「Add unit」**；
   - 在 Available Ad Units 中选择 **「Native Banners」**（原生横幅）；
   - 过滤设置中：保持 Adult ads 关闭（维持屏蔽 Erotic ads、Software alerts 等敏感广告）；
   - 点击 **Add** 提交保存。
4. **获取代码**：
   - 等待约 1~2 分钟后刷新页面；
   - 展开 `thesiftguide.com` 列表，找到刚创建的 Native Banners 单元（确认状态转为 Active）；
   - 点击右侧 **「Get code」**，完整复制弹窗内的广告代码（包含调用脚本与渲染容器）。

## 输出要求
完成后按如下格式输出标准总结：
```text
=== ADSTERRA_ANTI_ADBLOCK_RESULT ===
- Anti-Adblock 后台排查结果: [描述后台是否有开关、说明或入口]
- Native Banner Placement ID / 名称: [例如 3149xxxx / Native Banners]
- 完整广告代码:
[在此处完整粘贴提取到的 Native Banner 代码]
====================================
```
