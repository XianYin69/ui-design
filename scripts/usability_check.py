"""usability_check.py — 可用性静态走查：按大纲检查状态完备性、任务步数、反馈与撤销。"""
import os, re, sys
STATES = ("空态", "加载", "错误", "无权限")
def check(outline, design):
    txt = open(outline, encoding="utf-8").read()
    parts = []
    for dp, _, fn in os.walk(design):
        for f in fn:
            if f.endswith(".html"):
                with open(os.path.join(dp, f), encoding="utf-8",
                          errors="ignore") as fh:
                    parts.append(fh.read())
    html = " ".join(parts)
    bad = []
    for st in STATES:
        if st in txt and st not in html and st.replace("态", "") not in html:
            bad.append(f"大纲要求 {st} 但界面未见实现")
    steps = [int(x) for x in re.findall(r"步数\s*[:：]\s*(\d+)", txt)]
    for n in steps:
        if n > 3: bad.append(f"关键任务 {n} 步 > 3（需标压缩点）")
    if "aria-live" not in html and "toast" not in html.lower() and "反馈" in txt:
        bad.append("大纲要求即时反馈但界面缺 aria-live/toast")
    if "撤销" in txt and "undo" not in html.lower():
        bad.append("大纲要求可撤销但界面无 undo 路径")
    return bad
def main():
    a = sys.argv[1:]
    g = lambda k, d="": a[a.index(k) + 1] if k in a else d
    outline, design = g("--flow"), g("--path") or "."
    if not outline or not os.path.exists(outline):
        print("用法: --flow tmp/outline.md [--path <design>]"); sys.exit(2)
    bad = check(outline, design)
    for w in bad: print("走查:", w)
    print("可用性问题数 =", len(bad)); sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
