# dependence（依赖声明）
本技能**不内嵌**其他技能内容；能力经声明依赖获得。每行一条 `名称 | 类型 | 来源`，
类型为 skill|software|repo。SMS 安装时对本目录条目与本体做同样检查与净化。
```
file_ops             | skill    | local:skill_manage_system
web-design-guidelines| skill    | local
frontend-dev         | skill    | local
code-guidelines      | skill    | local
python               | software | system
git                  | software | system
```
## 用途映射
| 依赖 | 承担能力 | 触发节点 |
|---|---|---|
| file_ops | 联网搜索/抓取规范与文档（ff_lite.py search/fetch·须 :grant network） | 经验查询 / 浏览器学习 / 知识库构建 |
| web-design-guidelines | 界面与交互设计准则、可用性清单 | 大纲构建 / 分支分析 / 整体审查 |
| frontend-dev | 组件实现范式、样式工程与响应式落地 | 脚本构建 / 构建测试 |
| code-guidelines | 命名、注释、复杂度、坏味道准则 | 脚本构建 / 整体审查 |
| python | 令牌与审查脚本运行时、测试执行器 | 脚本构建 / 构建测试 |
| git | 功能分支→dev→main 版本流 | 每步收尾（见 git 工作流约束） |
## 规则
1. 依赖缺失时**降级不得静默**：记 process_chain interrupt 并向用户报告缺项，禁止伪造能力。
2. 禁止把依赖技能正文复制进本技能目录（薄技能原则）；只允许引用其名称与调用方式。
3. 新增/删除依赖须走 update 审批流并记 CHANGELOG。
- 返回 [SKILL.md](../SKILL.md) · [浏览器学习约束](../resistance/浏览器学习约束/浏览器学习约束.md)
