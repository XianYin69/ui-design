"""a11y_audit.py — 无障碍静态审计：alt、可访问名、标题层级、label、tabindex、lang。"""
import os, re, sys
def audit(root):
    bad = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__", "node_modules")]
        for f in fn:
            if not f.endswith(".html"): continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8", errors="ignore").read()
            rel = os.path.relpath(p, root)
            if not re.search(r"<html[^>]*\slang=", t): bad.append((rel, "缺 <html lang>"))
            for m in re.finditer(r"<img\b[^>]*>", t):
                if "alt=" not in m.group(0): bad.append((rel, "img 缺 alt: " + m.group(0)[:40]))
            for m in re.finditer(r"<(button|a)\b[^>]*>(.*?)</\1>", t, re.S):
                inner = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                if not inner and "aria-label" not in m.group(0) and "title=" not in m.group(0):
                    bad.append((rel, "控件无可访问名: " + m.group(1)))
            for m in re.finditer(r"<input\b[^>]*>", t):
                if "aria-label" not in m.group(0) and "id=" not in m.group(0):
                    bad.append((rel, "input 无关联 label"))
            hs = [int(x) for x in re.findall(r"<h([1-6])", t)]
            for i in range(1, len(hs)):
                if hs[i] - hs[i - 1] > 1: bad.append((rel, f"标题跳级 h{hs[i-1]}→h{hs[i]}"))
            if re.search(r"tabindex\s*=\s*[\"']?[1-9]", t): bad.append((rel, "正 tabindex 破坏焦点顺序"))
    return bad
def main():
    a = sys.argv[1:]
    root = a[a.index("--path") + 1] if "--path" in a else "."
    bad = audit(root)
    for p, w in bad: print("问题:", p, "|", w)
    print("无障碍问题数 =", len(bad)); sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
