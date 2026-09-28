# WCAG 2.1 AA 关键判据（摘要）

出处：W3C WAI《Understanding Success Criterion 1.4.3: Contrast (Minimum)》
https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html （[联网] 2026-09-28 访问，页面标题与 SC 编号已确证；正文为 JS 渲染，数值细节按 [本地] 常识记录，实现前须复核）。

## 条目（[本地]·待复核）
- **1.4.3 Contrast (Minimum) AA**：正文文本与图像文本对比度 ≥ 4.5:1；大字（≥18pt 或 14pt 粗体）≥ 3:1。
- **1.4.11 Non-text Contrast AA**：UI 组件可识别状态与图形 ≥ 3:1。
- **1.4.1 Use of Color A**：不得仅用颜色传达信息。
- **2.4.7 Focus Visible AA**：键盘焦点指示可见。
- **2.5.5 / 触控目标**：目标尺寸建议 ≥ 44×44 CSS px（AAA 级 2.5.5；移动端实践按 AA 底线执行）。

## 本技能落地映射
- 1.4.3 → `contrast_check.py --tokens tokens.json --min 4.5`
- 1.4.11 → `contrast_check.py --min 3`（对 accent/边框色）
- 2.4.7 / 键盘 → `a11y_audit.py`（禁正 tabindex、要求可访问名）
- 2.5.5 → `layout_lint.py`（<44px 按钮告警）

## 使用规则
引用本条目实现前，须由 [浏览器学习](../../branch/流程/浏览器学习/浏览器学习.md) 复核官方数值；
未复核部分不得当作已验证事实写入交付说明。
