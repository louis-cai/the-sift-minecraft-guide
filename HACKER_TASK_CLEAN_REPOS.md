# Hacker 工单：彻底执行方案 A 源码切割与双端安全清洗（含历史覆写）

## 目标
1. **GitHub 私有库（全量资产备份）**：
   - 将现有包含全量生产源码、E2E测试、5页面HTML的完整版本，推送到新创建的私有仓库 `git@github.com:louis-cai/thesiftguide-private.git` 的 `main` 分支。
2. **GitLab 彻底下架源码（强制覆写历史）**：
   - 用户要求：“GitLab上的源码要全部卸掉。同时注意之前的提交历史，人家从提交历史上也是可以反拿到你的代码的”。
   - 将公开仓库彻底清空历史，只保留干净的初始文档 commit（只含最初的 `README.md`），杜绝历史回溯。
3. **GitHub 公开库彻底安全清洗（强制覆写历史）**：
   - 同样将 `the-sift-minecraft-guide` 公开仓库彻底回退重置到 `dafcf26`（最初仅含 README.md 文档与官网外链的版本），强制推送到 GitHub 和 GitLab，彻底抹除 `1d59f44` 提交记录及所有源码。

## 详细步骤
1. **私有仓库推送**：
   在 `/home/louis/candi-tasks/thesiftguide-repo/`：
   - 添加临时远程 `private`: `git@github.com:louis-cai/thesiftguide-private.git`
   - 推送当前完整的 `1d59f44` 到私有仓库：`git push private main -u`
   - 验证私有仓库已有完整代码。

2. **公开仓库彻底回退与强制覆写历史**：
   在 `/home/louis/candi-tasks/thesiftguide-repo/`：
   - 执行 `git reset --hard dafcf26`，彻底抹除 `1d59f44` 的 commit。
   - 验证 `git log` 当前仅剩 1 条初始 commit：`dafcf26 docs: complete guide and wiki index for The Sift in Minecraft`。
   - 检查工作区，确认只有纯文档 `README.md`，所有 HTML、脚本、测试用例全部消失。
   - 强制推送到 GitHub 公开库：`git push origin main --force`。
   - 强制推送到 GitLab 公开库：`git push gitlab main --force`。

3. **双重验证**：
   - 检查 GitHub 公开库：确认没有 HTML 文件，只有 README.md，commit 历史只有 1 条。
   - 检查 GitLab 公开库：确认没有源码，commit 历史只有 1 条。
   - 检查 GitHub 私有库：确认 56 个生产文件完整备份。
   - 检查 `/home/louis/candi-tasks/thesiftguide/`：确认本地 Cloudflare 生产部署目录完全独立未受影响。

完成后输出完整的执行报告。
