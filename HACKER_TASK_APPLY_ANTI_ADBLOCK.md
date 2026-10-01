# Hacker 工单：升级全站三大广告位至 Adsterra 官方 Anti-Adblock 防封域名

## 背景与目标
Adsterra 官方已正式审核通过 `thesiftguide.com` 的 Anti-Adblock 申请，并将账号下所有广告位脚本全面迁移至独立的防封专用域名 `invitationprecedingbreeches.com`。
现需将 `/home/louis/candi-tasks/thesiftguide/index.html` 中的三大广告位域名全面升级为最新防封代码。

## 升级映射清单
1. **顶部 728x90 Banner**:
   - 旧域名: `https://www.highrevenueformat.com/e34c08305944ef076210b30b1897f6eb/invoke.js`
   - 新域名: `https://invitationprecedingbreeches.com/e34c08305944ef076210b30b1897f6eb/invoke.js`
2. **中部 Native Banner**:
   - 旧域名: `https://pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js`
   - 新域名: `https://invitationprecedingbreeches.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js`
3. **底部 300x250 Banner**:
   - 旧域名: `https://www.highrevenueformat.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js`
   - 新域名: `https://invitationprecedingbreeches.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js`

## 核心任务要求
1. **就地精准替换（大文件修改铁律）**：
   - 编写并执行独立的 Python 脚本，对 `/home/louis/candi-tasks/thesiftguide/index.html` 进行就地字符串精准替换。
   - 严禁大模型单次生成全量复写 100KB+ HTML。
2. **绝对红线防护**：
   - 保留 GA4 (`G-X1ZTW8XWPG`)、Schema JSON-LD、Favicon 体系、Tailwind 3.4.17 CDN 直连、双模式传送门计算器。
3. **自动化双门禁与部署**：
   - 执行 `./run_e2e.sh --target local` 验证全部 6 大套件 11 项用例 100% PASS；
   - 使用 Cloudflare 凭证部署到生产环境（项目：`thesiftguide`，分支：`main`）；
   - 执行 `./run_e2e.sh --target live` 线上复测 100% PASS。
4. **Git 仓库推送铁律**：
   - 仅将更新同步至 `/home/louis/candi-tasks/thesiftguide-repo/` 并推送到 GitHub 私有库（`git@github.com:louis-cai/thesiftguide-private.git`）；
   - **绝对严禁推送到公开库 `origin` (`the-sift-minecraft-guide`) 或 `gitlab`！**（公开库必须保持只有纯 README 文档）。

完成后输出包含本地测试、部署输出与线上探针核验的总结报告。
