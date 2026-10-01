# Hacker 工单：同步 thesiftguide 完整代码至 GitHub 仓库

## 背景与目的
目前 `/home/louis/candi-tasks/thesiftguide/` 目录中包含了网站最新的全部代码（5个HTML页面、Tailwind配置、双广告位、Favicon图标族、Playwright E2E测试套件等）。
为了防止代码丢失，并在 GitHub 上规范管理后续的 Issue 与版本历史，需要将全部最新产物同步至已关联的 GitHub 仓库并推送到远程。

## 仓库上下文
- 现有 Git 仓库路径：`/home/louis/candi-tasks/thesiftguide-repo/`
- 远程仓库关联：
  - `origin`: `git@github.com:louis-cai/the-sift-minecraft-guide.git` (GitHub)
  - `gitlab`: `git@gitlab.com:louis.cai.cn/the-sift-minecraft-guide.git` (GitLab)

## 实施任务
1. 将 `/home/louis/candi-tasks/thesiftguide/` 下的所有最新源码及配置（忽略备份文件 *.bak 等杂质），同步拷贝至 `/home/louis/candi-tasks/thesiftguide-repo/`。
2. 确保 `.gitignore` 包含必要的排除项（如 `.wrangler/`、`*.bak`、`__pycache__/` 等）。
3. 检查仓库状态，执行 `git add .`。
4. 提交规范的 Commit：
   `feat: sync complete multi-page guide with dual ad slots, E2E tests, and Minecraft game theme`
5. 推送到 GitHub（`git push origin main`）及 GitLab（`git push gitlab main`）。
6. 输出推送结果与 GitHub 仓库 URL。
