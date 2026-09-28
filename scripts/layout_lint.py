"""layout_lint.py — 布局静态体检：视口声明、固定宽度、触控热区、溢出与截断风险。"""
import os, re, sys
def files(root, exts):
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__", "node_modules")]
        out += [os.path.join(dp, f) for f in fn if f.endswith(exts)]
    return out
def audit(root):
    bad = []
    for p in files(root, (".html",)):
        t = open(p, encoding="utf-8", errors="ignore").read()
        if "viewport" not in t: bad.append((p, "缺 viewport meta"))
        for m in re.finditer(r"width\s*[:=]\s*([5-9]\d\d|1\d{3,})px", t):
            bad.append((p, "疑似固定大宽度 " + m.group(0)))
    for p in files(root, (".css",)):
        t = open(p, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r"[^{}]*\{[^{}]*\}", t):
            blk = m.group(0)
            for d in re.finditer(r"(min-height|height|padding)\s*:\s*(\d+)px", blk):
                if int(d.group(2)) < 44 and "btn" in blk.split("{")[0].lower():
                    bad.append((p, f"按钮 {d.group(1)}={d.group(2)}px < 44 触控底线"))
            if re.search(r"overflow\s*:\s*hidden", blk) and "text-overflow" not in blk:
                bad.append((p, "overflow:hidden 无截断提示（长文本风险）"))
    return bad
def main():
    a = sys.argv[1:]
    root = a[a.index("--path") + 1] if "--path" in a else "."
    bad = audit(root)
    for p, w in bad: print("问题:", os.path.relpath(p, root), "|", w)
    print("布局问题数 =", len(bad)); sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
