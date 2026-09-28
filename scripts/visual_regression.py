"""visual_regression.py — 视觉回归基线：对产物做指纹快照与比对（像素级差异须浏览器环境，缺则标注未验证）。"""
import hashlib, json, os, sys
def snap(root):
    out = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__", "node_modules")]
        for f in sorted(fn):
            if not f.endswith((".html", ".css", ".svg", ".json")): continue
            p = os.path.join(dp, f)
            with open(p, "rb") as fh:
                blob = fh.read()
            key = os.path.relpath(p, root).replace("\\", "/")
            out[key] = hashlib.sha256(blob).hexdigest()[:16]
    return out
def main():
    a = sys.argv[1:]
    g = lambda k, d="": a[a.index(k) + 1] if k in a else d
    root, base = g("--path") or ".", g("--baselines")
    if not base:
        print("用法: --path <design> --baselines <dir> [--update --yes]"); sys.exit(2)
    cur, fp = snap(root), os.path.join(base, "manifest.json")
    if "--update" in a:
        if "--yes" not in a:
            print("[预览] 写入基线", fp, "| 文件数 =", len(cur)); return
        os.makedirs(base, exist_ok=True)
        json.dump(cur, open(fp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("[基线]", fp, len(cur)); return
    if not os.path.exists(fp):
        print("[无基线] 先 --update --yes 建立基线"); sys.exit(2)
    old = json.load(open(fp, encoding="utf-8"))
    diff = [k for k in set(old) | set(cur) if old.get(k) != cur.get(k)]
    for k in diff: print("差异:", k, "|", "新增" if k not in old else "删除" if k not in cur else "变更")
    print("差异文件数 =", len(diff), "| 像素级比对需浏览器环境（未运行时验证）")
    sys.exit(1 if diff else 0)
if __name__ == "__main__":
    main()
