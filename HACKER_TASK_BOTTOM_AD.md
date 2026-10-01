# Hacker 工单：为 thesiftguide.com 注入底部第 2 个 Adsterra 广告位并完成上线门禁

## 背景与任务
Merrick 已在 Mac 端 Adsterra 发布商后台为 `thesiftguide.com` 成功申请并通过了第 2 个官方广告单元（300x250 Medium Rectangle Banner，Placement ID: `31491687` / `300x250_1`，状态 Active）。
现需 Hacker 将该广告位安全嵌入页面底部，并通过 Playwright E2E 自动化测试全量门禁后部署上线。

## 广告代码规范
在 `/home/louis/candi-tasks/thesiftguide/index.html` 中，找到 `<!-- Footer -->`（大约第 1214 行 `<footer` 标签之前），在其上方安全嵌入以下规范的 300x250 广告容器：

```html
    <!-- Sponsored Placement Bottom (Adsterra 300x250) -->
    <div class="my-12 mx-auto max-w-4xl px-4 flex flex-col items-center" id="bottom-ad-placement">
      <div class="text-[10px] uppercase tracking-wider text-slate-500 mb-1.5 flex items-center gap-1 font-mono">
        <span>Advertisement</span>
      </div>
      <div class="w-full flex justify-center items-center overflow-x-auto min-h-[250px] p-2 rounded-lg bg-[#181a20] border-2 border-[#2d3139] shadow-inner">
        <script>
          atOptions = {
            'key' : '93a1b6fb1cf3809a6ddd2ccae9364526',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {}
          };
        </script>
        <script src="https://www.highrevenueformat.com/93a1b6fb1cf3809a6ddd2ccae9364526/invoke.js"></script>
      </div>
    </div>
```

## 🔴 绝对红线约束（4 项）
1. **严禁全量 write_file 覆写大文件**（105KB 会直接触发模型截断）。必须编写独立 Python 脚本对 `index.html` 进行精准就地替换插入。
2. **保护已有全部资产**：
   - 顶部 728x90 广告位（Key `e34c08305944ef076210b30b1897f6eb`）必须完好保留。
   - GA4 衡量 ID（`G-X1ZTW8XWPG`）完好保留。
   - Schema JSON-LD 结构化数据完好保留。
   - SEO Meta、Open Graph、Twitter Card、Favicon 全套保留。
   - 5 页面多页架构流转及计算器功能（Nether-to-Sift & Frame BOM）完好可用。
3. **E2E 自动化测试门禁铁律（Louis 09-30 定）**：
   - 修改完成后，必须在本地运行 `./run_e2e.sh --target local`。
   - 必须确认 11 项用例全部 PASS，生成最新截图证据。
4. **构建与上线部署**：
   - 本地 E2E 测试全绿后，执行 Cloudflare Pages 部署：
     ```bash
     export CLOUDFLARE_API_TOKEN="$(cat ~/.keys/.cloudflare_pages_token)"
     export CLOUDFLARE_ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"
     wrangler pages deploy /home/louis/candi-tasks/thesiftguide --project-name=thesiftguide --branch=main --commit-dirty=true
     ```
   - 部署完成后运行 `./run_e2e.sh --target live` 验证线上生产环境全绿。

完成后输出完整的优化与测试总结。
