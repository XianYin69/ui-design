"""contrast_check.py — WCAG 对比度校验：按令牌前景/背景组合算比值，AA 正文 4.5 / 大字 3.0。"""
import json, os, sys
def rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3: h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b
def ratio(a, b):
    la, lb = lum(rgb(a)), lum(rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)
def pairs(tokens):
    colors = tokens.get("color", {})
    bg = colors.get("bg", "#ffffff")
    out = []
    for k, v in colors.items():
        if k in ("bg", "surface") or not isinstance(v, str): continue
        out.append((f"{k}/bg", v, bg, ratio(v, bg)))
    return out
def main():
    a = sys.argv[1:]
    spec = a[a.index("--tokens") + 1] if "--tokens" in a else ""
    aa = float(a[a.index("--min") + 1]) if "--min" in a else 4.5
    if not spec or not os.path.exists(spec):
        print("用法: --tokens tokens.json [--min 4.5]"); sys.exit(2)
    bad = []
    for name, fg, bg, r in pairs(json.load(open(spec, encoding="utf-8"))):
        print(("OK " if r >= aa else "低 ") + f"{name}: {r:.2f}:1 ({fg} on {bg})")
        if r < aa: bad.append(name)
    print("未达 AA 组合数 =", len(bad)); sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
