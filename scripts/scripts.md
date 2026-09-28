# scripts（脚本库）

本目录存放可执行的辅助脚本：校验、生成、快照、审计工具等。

## 应存什么

- 独立运行的 Python / Shell / PowerShell 脚本；工具本身 ≤ 50 行（超则拆「入口 + 模块」）。
- 文件名小写英文；任何写盘脚本默认预览，落盘须显式 `--yes`。

## 当前内容

### 机制类（五大机制 + 基线）
- [`logic_chain.py`](logic_chain.py) 逻辑链 / [`process_chain.py`](process_chain.py) 过程链
- [`context_compress.py`](context_compress.py) 上下文压缩 / [`garbage_collect.py`](garbage_collect.py) 垃圾回收
- [`penalty.py`](penalty.py) 惩罚熔断 / [`sandbox.py`](sandbox.py) 沙盒 create/list/deliver/clean
- [`check_links.py`](check_links.py) 悬空链接 / [`self_update.py`](self_update.py) 自更新
- [`deps_check.py`](deps_check.py) 依赖自检 / [`flowchart_helper.py`](flowchart_helper.py) 草图澄清

### 知识类
- [`browser_learn.py`](browser_learn.py) 派 file_ops 联网取证 / [`knowledge_fetch.py`](knowledge_fetch.py) 白名单抓取
- [`knowledge_convert.py`](knowledge_convert.py) HTML→md 摘要

### 设计类（ui-design 专用）
- [`scaffold_design.py`](scaffold_design.py) 脚手架 / [`design_tokens.py`](design_tokens.py) 令牌真源 json→css
- [`contrast_check.py`](contrast_check.py) WCAG 对比度 / [`a11y_audit.py`](a11y_audit.py) 无障碍静态审计
- [`layout_lint.py`](layout_lint.py) 布局体检 / [`asset_check.py`](asset_check.py) 素材版权溯源
- [`usability_check.py`](usability_check.py) 可用性走查 / [`visual_regression.py`](visual_regression.py) 视觉基线
- [`run_tests.py`](run_tests.py) 测试执行 / [`lint_check.py`](lint_check.py) 体量与坏味道自查

## 运行约定

1. 使用项目默认 Python（`python -B`）。
2. 写盘动作一律先预览、后 `--yes`。
3. 运行前先看 [resistance](../resistance/resistance.md) 确认权限与回滚策略。
