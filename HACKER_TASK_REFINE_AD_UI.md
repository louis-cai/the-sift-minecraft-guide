# Hacker 工单：优化 thesiftguide.com 广告容器视觉样式（Ghost Placeholder 幽灵无缝占位）

## 背景
用户反馈当前页面上的广告容器在未填充或被 AdBlock 拦截时，显眼的深灰底色（`bg-[#181a20]`）和硬质边框（`border-2 border-[#2d3139]`）会呈现出一个突兀、怪异的空盒子，影响视觉体验。

## 优化目标
将顶部 728x90 和底部 300x250 的广告容器重构为 **无缝自然的幽灵占位（Ghost Placeholder）**：
1. **尺寸精确贴合**：外层容器宽度严格限制为对应广告尺寸（728px 与 300px），避免全宽撑大造成过多留白。
2. **去除突兀外框与亮底色**：移除 `border-2 border-[#2d3139]`、`bg-[#181a20]` 和 `shadow-inner`，底色改为透明或与全站深板岩底色完全一致（`bg-transparent`）。
3. **保留防 CLS 布局抖动**：保留 `min-h-[90px]` 和 `min-h-[250px]`，保证广告加载时不发生跳动。
4. **精简柔和的标签**：保留微小的 `Advertisement` 标签，但颜色调至更加克制、自然的暗灰（`text-slate-600`），广告未加载时融于页面背景，不显突兀。

## 具体代码设计

### 1. 顶部 728x90 容器（替换现有对应块）：
```html
    <!-- Sponsored Placement (Adsterra 728x90) -->
    <div class="my-8 mx-auto w-full max-w-[728px] px-2 flex flex-col items-center">
      <div class="text-[9px] uppercase tracking-wider text-slate-600 mb-1 flex items-center gap-1 font-mono select-none">
        <span>Advertisement</span>
      </div>
      <div class="w-full flex justify-center items-center overflow-x-auto min-h-[90px] bg-transparent">
        <script>
          atOptions = {
            'key' : 'e34c08305944ef076210b30b1897f6eb',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
          };
        </script>
        <script src="https://www.highrevenueformat.com/e34c08305944ef076210b30b1897f6eb/invoke.js"></script>
      </div>
    </div>
```

### 2. 底部 300x250 容器（替换现有对应块）：
```html
    <!-- Sponsored Placement Bottom (Adsterra 300x250) -->
    <div class="my-10 mx-auto w-full max-w-[300px] px-2 flex flex-col items-center" id="bottom-ad-placement">
      <div class="text-[9px] uppercase tracking-wider text-slate-600 mb-1 flex items-center gap-1 font-mono select-none">
        <span>Advertisement</span>
      </div>
      <div class="w-full flex justify-center items-center overflow-x-auto min-h-[250px] bg-transparent">
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
1. **严禁全量 write_file 覆写大文件**（避免模型截断风险）。必须编写独立 Python 脚本对 `/home/louis/candi-tasks/thesiftguide/index.html` 就地替换。
2. **严禁破坏广告代码本身**：
   - 顶部 Key: `e34c08305944ef076210b30b1897f6eb`
   - 底部 Key: `93a1b6fb1cf3809a6ddd2ccae9364526`
   - 保持 GA4、Schema JSON-LD、SEO Meta、Favicon、双模式计算器完整无损。
3. **E2E 自动化测试门禁铁律（Louis 09-30 定）**：
   - 修改完成后，必须在本地运行 `./run_e2e.sh --target local`。
   - 必须确认 11 项用例全部 PASS，生成最新截图。
4. **构建与生产部署**：
   - 本地测试全绿后，执行 Cloudflare Pages 部署：
     ```bash
     export CLOUDFLARE_API_TOKEN="$(cat ~/.keys/.cloudflare_pages_token)"
     export CLOUDFLARE_ACCOUNT_ID="978519e17a5f285aaf6e3d0280c5efc0"
     wrangler pages deploy /home/louis/candi-tasks/thesiftguide --project-name=thesiftguide --branch=main --commit-dirty=true
     ```
   - 部署完成后运行 `./run_e2e.sh --target live` 线上实测全绿。

完成后输出完整的优化与测试总结。
