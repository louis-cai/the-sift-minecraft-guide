# Merrick 任务书：在 Adsterra 后台提交 Anti-AdBlock 官方申请

## 背景
根据上一轮排查，Adsterra 后台 Websites 页面顶部明确提供了「REQUEST ANTI-ADBLOCK」功能申请按钮。现需你在浏览器中点击此按钮，正式向官方提交 Anti-Adblock 防封域名分配申请。

## 执行角色与技能
- **执行者**：Merrick (Mac 端 Hermes 默认 profile)
- **技能**：请使用 `ego-browser` skill 接管已在 `ego lite` 浏览器中打开的 Adsterra 发布商后台。

## 具体操作步骤
1. 打开或切换至 Adsterra Websites 页面：`https://beta.publishers.adsterra.com/websites`。
2. 找到页面顶部「Get Anti-Adblock to increase your revenue」区域。
3. 定位到 **「REQUEST ANTI-ADBLOCK」** 按钮。
4. 点击该按钮；如果弹出确认对话框或选项弹窗，确认提交。
5. 检查页面反馈，确认请求已成功提交（例如按钮变为 Pending / Under review / Request submitted 或出现成功提示 Toast）。

## 输出要求
完成后按如下格式输出结果：
```text
=== ADSTERRA_REQUEST_ANTI_ADBLOCK_RESULT ===
- 申请操作状态: [成功提交 / 需填写补充信息 / 其他状态]
- 页面反馈说明: [描述点击后的页面提示或按钮状态]
============================================
```
