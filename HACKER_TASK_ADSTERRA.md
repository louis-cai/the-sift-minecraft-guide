# 任务书：向 index.html 注入 Adsterra 728x90 Banner 广告位

## 背景
`thesiftguide.com` 的 Adsterra 发布商审核已正式通过，已获取官方 728x90 Banner 广告标签。
现需 Hacker 通过脚本向 `/home/louis/candi-tasks/thesiftguide/index.html` 嵌入广告位。

## 广告位设计与代码规范
为了完全避免 CLS（布局抖动）与移动端溢出，并保持《Minecraft》深板岩 UI 美学，广告容器必须采用以下结构：

```html
    <!-- Sponsored Placement (Adsterra 728x90) -->
    <div class="my-10 mx-auto max-w-4xl px-4 flex flex-col items-center">
      <div class="text-[10px] uppercase tracking-wider text-slate-500 mb-1.5 flex items-center gap-1 font-mono">
        <span>Advertisement</span>
      </div>
      <div class="w-full flex justify-center items-center overflow-x-auto min-h-[90px] p-2 rounded-lg bg-[#181a20] border-2 border-[#2d3139] shadow-inner">
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

## 嵌入位置
放在 Fast Facts 区域下方、正文第二板块（What is The Sift）开始之前。
这样既保证了首屏核心内容（Hero + 快速事实）的纯净阅读体验，又处在用户向下滑动的第一视觉转化黄金点。

## 🔴 绝对红线约束
1. 严禁全量 write_file 覆写大文件（避免触发模型上下文截断，必须编写 Python 脚本就地替换注入）。
2. 绝对保护已有资产：
   - GA4 探针：`G-X1ZTW8XWPG`
   - Schema JSON-LD：WebSite, Article, FAQPage
   - SEO Meta、Open Graph、Twitter Card 及 Favicon 标签
   - Tailwind 3.4.17 直连

执行完成后运行测试脚本验证并输出报告。
