# Merrick 任务书：提取已通过审核的 Anti-Adblock 最新广告代码

## 背景
Adsterra 官方已通过 thesiftguide.com 的 Anti-Adblock 申请。现需你在已登录的 Adsterra 发布商后台中，检查并提取更新后的防封广告代码。

## 执行角色与技能
- **执行者**：Merrick (Mac 端 Hermes 默认 profile)
- **技能**：请使用 `ego-browser` skill 接管已在 `ego lite` 浏览器中打开的 Adsterra 发布商后台。

## 具体操作步骤
1. 打开或切换至 Adsterra Websites 页面：`https://beta.publishers.adsterra.com/websites`。
2. 刷新页面，找到 `thesiftguide.com` 这一行并展开所有广告单元（Placements）。
3. 依次检查现有的广告单元：
   - 单元 1: **728x90_1** (Banner 728x90, ID: 31469123)
   - 单元 2: **300x250_1** (Banner 300x250, ID: 31491687)
   - 单元 3: **NativeBanner_1** (Native Banner, ID: 31506645)
4. 对每个单元点击 **「Get code」**，查看弹窗中的广告脚本 URL（检查是否更新为了新的防封域名，如不再是 highrevenueformat.com）。
5. 复制并记录各个广告单元最新的完整广告代码。

## 输出要求
完成后按如下格式输出标准总结：
```text
=== ADSTERRA_UPDATED_CODES_RESULT ===
- 728x90_1 最新代码:
[代码]
- 300x250_1 最新代码:
[代码]
- NativeBanner_1 最新代码:
[代码]
=====================================
```
