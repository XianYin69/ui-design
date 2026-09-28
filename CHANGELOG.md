# CHANGELOG
## 0.1.0 — 初版（ui-design）
- 新增：创建路径 12 节点（复刻 general-programming：初始化→需求确认→经验查询→大纲构建→分支分析→
  脚本构建→构建测试→知识库构建→浏览器学习→约束编写→整体审查→收尾）+ 独立修改流程。
- 新增：五大机制约束（垃圾回收 / 上下文压缩 / 逻辑链 / 过程链存取 / 惩罚）与沙盒机制。
- 新增：UI 专属约束三条 —— `resistance/无障碍约束/`（WCAG AA 底线）、
  `resistance/视觉一致性约束/`（令牌单一真源）、`resistance/素材版权约束/`（溯源与许可证白名单）。
- 新增：`dependence/` 薄技能依赖声明（file_ops / web-design-guidelines / frontend-dev /
  code-guidelines / python / git），能力经声明获取，本体不内嵌他技能正文。
- 新增：`scripts/` 设计类脚本 8 个（scaffold_design / design_tokens / contrast_check /
  a11y_audit / layout_lint / asset_check / usability_check / visual_regression），
  加机制与知识类共 24 个，全部 ≤50 行、英文命名。
- 新增：`references/` 知识库九域（视觉层次 / 栅格与布局 / 色彩与对比 / 字体排印 / 交互与状态 /
  设计系统治理 / 无障碍 / 可用性与人因 / 动效与反馈）。
- 联网取证缺口：本环境 `knowledge_fetch.py` 与 `file_ops/ff_lite.py` 均不可达（WinError 10060），
  仅 w3.org 可经网关取页；除 WCAG 条目已确证页面标题与 SC 编号外，其余条目一律标注 `[本地]`，
  引用前须经浏览器学习复核，禁止当作已验证事实。
- 新增：MIT `LICENSE`（工作区根 + tmp 镜像）。
- 违规后果：见各约束文件；约束变更须走 [update 审批流](update/update.md)。
