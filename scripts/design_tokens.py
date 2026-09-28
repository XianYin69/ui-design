"""design_tokens.py — 设计令牌单一真源：tokens.json → tokens.css / tailwind 片段；默认预览。"""
import json, os, sys
def flat(d, pre=""):
    out = {}
    for k, v in d.items():
        key = f"{pre}-{k}" if pre else str(k)
        if isinstance(v, dict): out.update(flat(v, key))
        else: out[key] = v
    return out
def css(tokens):
    lines = [":root {"]
    for k, v in flat(tokens).items():
        num = isinstance(v, (int, float))
        unit = k.startswith(("space", "font", "radius", "motion"))
        val = f"{v}px" if num and unit else v
        lines.append(f"  --{k}: {val};")
    lines.append("}")
    return "\n".join(lines) + "\n"
def main():
    a = sys.argv[1:]
    g = lambda k, d="": a[a.index(k) + 1] if k in a else d
    spec, out = g("--spec"), g("--out")
    if not spec or not out:
        print("用法: --spec tokens.json --out <file> [--yes]（默认预览）"); sys.exit(2)
    tokens = json.load(open(spec, encoding="utf-8"))
    body = css(tokens)
    if "--yes" not in a:
        print("[预览]", out); print(body); return
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write(body)
    print("[写入]", out, "| 令牌数 =", len(flat(tokens)))
if __name__ == "__main__":
    main()
