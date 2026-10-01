# Hacker 工单：向 thesiftguide.com 嵌入 Native Banner（原生横幅）广告位

## 背景与目的
为解决部分设备/浏览器（如 Safari ITP、开启 AdBlock 用户）屏蔽传统 iframe 广告的问题，我们在 Adsterra 后台开通了全新的 **Native Banner（原生图文横幅）** 广告位（Placement ID: 31506645）。原生广告采用纯图文流，天然具有极高的防屏蔽存活率。

## 核心任务要求
1. **就地精准注入（大文件修改铁律）**：
   - 严禁全量大模型生成复写大文件。编写并运行独立的 Python 脚本，向 `/home/louis/candi-tasks/thesiftguide/index.html` 进行就地局部替换注入。
   - **注入位置**：在 `biomes` 模块结束标签（`</section>`）之后、`<!-- Section 3: How to Play Early -->` 之前。
   - **容器结构规范**（采用无缝幽灵占位，防 CLS 抖动，移动端零横向溢出）：
     ```html
    <!-- Sponsored Native Recommendation (Adsterra Native Banner) -->
    <div class="my-10 mx-auto w-full max-w-[728px] px-2 flex flex-col items-center" id="native-ad-placement">
      <div class="text-[9px] uppercase tracking-wider text-slate-600 mb-1 flex items-center gap-1 font-mono select-none">
        <span>Advertisement</span>
      </div>
      <div class="w-full flex justify-center items-center overflow-x-auto min-h-[160px] bg-transparent">
        <script async="async" data-cfasync="false" src="https://pl31607144.profitableratecpmnetwork.com/8b5c161155b921ab39efc03bbcadbaf3/invoke.js"></script>
        <div id="container-8b5c161155b921ab39efc03bbcadbaf3" class="w-full"></div>
      </div>
    </div>
     ```

2. **绝对红线防护**：
   - 保留顶部 728x90 广告容器（`e34c08305944ef076210b30b1897f6eb`）；
   - 保留底部 300x250 广告容器（`93a1b6fb1cf3809a6ddd2ccae9364526`）；
   - 保留 GA4（`G-X1ZTW8XWPG`）；
   - 保留 Schema.org JSON-LD 结构化数据；
   - 保持 Tailwind 3.4.17 CDN 直连；
   - 保持移动端无横向溢出（`scrollWidth <= innerWidth`）。

3. **测试门禁（自动化双门禁）**：
   - 执行 `./run_e2e.sh --target local` 跑通本地 Playwright 全部 6 大套件 11 项用例；
   - 使用 `~/.keys/.cloudflare_pages_token` 将变更部署到 Cloudflare Pages（项目：`thesiftguide`，生产分支：`main`）；
   - 执行 `./run_e2e.sh --target live` 跑通线上生产环境全量复测；
   - 同步更新 `/home/louis/candi-tasks/thesiftguide-repo/` 并推送到 GitHub 私有库（`git@github.com:louis-cai/thesiftguide-private.git`）。

完成后输出包含本地测试、部署输出与线上复测结果的报告。
