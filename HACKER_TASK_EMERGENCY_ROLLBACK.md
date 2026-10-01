# Hacker 紧急工单：立即回滚下线触发流氓跳转的 Native Banner 与 Anti-Adblock 代码

## 紧急事故报告
用户在真实设备访问 `https://thesiftguide.com/` 时，页面被强制恶意重定向跳转至：
`https://www.justverify.click/Chinese/Captcha/verifynow_visitor_id?visitor_id=...&c1=31469124...`

## 根因定位
经 Candi 源码反编译与逆向分析，Adsterra 的 Native Banner 脚本及官方 Anti-Adblock 机制中内置了激进的流量变现劫持逻辑（`if (window.top) window.top.location = Tf.ou` 及 Popunder 插件）。当检测到中国访客或低填充流量时，它会无视网站意志强制将顶层窗口劫持重定向至假冒验证码/广告中转页。这严重违反了白帽 SEO 铁律，极易引发 Google Safe Browsing 恶意重定向惩罚。

## 紧急恢复动作
1. **立即回滚 index.html**：
   - 将 `/home/louis/candi-tasks/thesiftguide/index.html` 立即恢复为 `/home/louis/candi-tasks/thesiftguide/index.html.native_ad.bak` 的状态；
   - 彻底拔除 Native Banner 广告容器及所有 `invitationprecedingbreeches.com` 脚本；
   - 恢复为纯粹稳定的双 Banner 架构（顶部 728x90 `e34c08305944ef076210b30b1897f6eb` + 底部 300x250 `93a1b6fb1cf3809a6ddd2ccae9364526`，均使用幽灵无缝占位 `bg-transparent`）；
2. **红线验证**：
   - 验证 GA4 (`G-X1ZTW8XWPG`)、Schema.org JSON-LD、Favicon、Tailwind 3.4.17 CDN 直连 100% 完整；
3. **自动化测试与部署**：
   - 运行 `./run_e2e.sh --target local` 确保 11 项用例 PASS；
   - 执行 Wrangler 部署推送到 Cloudflare Pages 全球 CDN，秒级覆盖线上生产；
   - 运行 `./run_e2e.sh --target live` 线上复测通过；
4. **Git 同步与推送**：
   - 仅同步至 `/home/louis/candi-tasks/thesiftguide-repo/` 并推送到 GitHub 私有库（`thesiftguide-private`），绝对不碰公开库。

完成后立即输出报告。
