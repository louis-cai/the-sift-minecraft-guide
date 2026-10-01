# Hacker Task Work Order: Build and Execute E2E Test Suite for thesiftguide.com

## Objective
Louis 指出：网页交互与跨页面流转不能依赖用户肉眼手动验证，必须将 End-to-End (E2E) 自动化测试工程化落地到项目中，形成随代码版本固化的自动化回归测试资产。

## Working Directory
`/home/louis/candi-tasks/thesiftguide`

## Deliverables
1. **测试脚本目录**: `/home/louis/candi-tasks/thesiftguide/tests/`
2. **测试脚本**:
   - `test_e2e_thesiftguide.py` (基于 Python Playwright，headless Chromium)
   - `run_e2e.sh` (一键执行入口脚本，支持传参 `--target [live|local]`)
3. **截图存证目录**: `/home/louis/candi-tasks/thesiftguide/tests/screenshots/`
   - 保存移动端和桌面端各关键交互状态的高清截图。

## E2E 自动化测试用例清单（覆盖桌面端与移动端）

### Suite 1: 桌面端核心交互测试 (Viewport: 1280x800)
1. **Case 1.1 - 首页与组件装载**:
   - 访问目标 URL（默认先测线上生产环境 `https://thesiftguide.com/`）。
   - 验证标题包含 `The Sift Minecraft`。
   - 验证关键红线元素：GA4 脚本存在、Adsterra 广告位存在、Schema JSON-LD 解析无报错。
2. **Case 1.2 - 传送门坐标计算器实时输入与换算**:
   - 定位 `#calculator`。
   - 输入自定义坐标：X=1600, Y=70, Z=-1200。
   - 切换压缩比为 `1:8 Nether Equivalent`。
   - 断言计算结果：Target X 变为 200, Target Z 变为 -150。
   - 点击 "Copy /tp Command" 按钮，断言复制反馈提示变为包含 "Copied" 或绿色反馈态。
3. **Case 1.3 - 传送门材料预算切换与计算**:
   - 点击 Tab 按钮 `#tab-btn-materials`。
   - 断言材料面板变为显示态（移除 `hidden`）。
   - 选择尺寸 `Ancient Rift Arch 7×9`。
   - 切换勾选 `Include Corner Blocks` 复选框。
   - 断言所需方块数量从 20 变为 28，材料清单实时联动。
4. **Case 1.4 - 全站导航与页面跳跃闭环**:
   - 点击顶部导航 `Portal Guide` -> 跳转至 `/portal.html`，断言 URL、H1 与 FAQ 正常。
   - 从 Portal 页点击顶部导航 `Mobs & Entities` -> 跳转至 `/mobs.html`，断言图鉴表格存在。
   - 从 Mobs 页点击顶部导航 `About` -> 跳转至 `/about.html`，断言关于与免责声明存在。
   - 从 About 页点击页脚 `Privacy Policy` -> 跳转至 `/privacy.html`，断言隐私政策正文存在。
   - 点击顶部 Logo `The Sift Guide` 返回首页 `/`。

### Suite 2: 移动端专属交互测试 (Mobile Viewport: 390x844, iPhone 13)
1. **Case 2.1 - 移动端折叠菜单与抽屉抽拉**:
   - 访问首页，断言桌面导航 `nav.hidden.md:flex` 隐藏。
   - 点击移动端汉堡包按钮 `#mobile-menu-btn`。
   - 断言移动端菜单抽屉展开并可见。
   - 点击抽屉中的 `Portal Guide` 链接，断言成功跳转至 `/portal.html`。
2. **Case 2.2 - 移动端计算器触控与零溢出**:
   - 验证 `#calculator` 容器在 390px 视口下无横向水平滚动条溢出（`document.documentElement.scrollWidth <= window.innerWidth`）。
   - 触控输入数值与点击复制按钮，操作正常无误。

## Execution Steps
1. 创建 `/home/louis/candi-tasks/thesiftguide/tests/` 目录与截图子目录。
2. 编写 `test_e2e_thesiftguide.py`（使用 `playwright.sync_api`，内置完备的断言和截图留痕逻辑）。
3. 编写 `run_e2e.sh`，赋予可执行权限 `chmod +x run_e2e.sh`。
4. 运行 `python3 tests/test_e2e_thesiftguide.py`，完整跑通全部 Desktop 与 Mobile 测试用例。
5. 验证所有测试用例均为 PASS，输出测试报告与截图文件路径清单。
