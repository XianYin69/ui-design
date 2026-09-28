"""asset_check.py — 素材合规校验：assets.md 每行须为 `文件名 | 来源URL | 许可证 | 版权人`，缺项即违规。"""
import os, pathlib, re, sys
OK_LICENSES = ("mit", "cc0", "apache-2.0", "bsd", "ofl", "public domain",
               "公有领域", "自研", "原创", "内部授权")
def check(path):
    bad = []
    lines = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("每行") or "|" not in s: continue
        parts = [x.strip() for x in s.split("|")]
        if len(parts) < 4: bad.append((i, "字段不足四项: " + s[:40])); continue
        name, url, lic, owner = parts[:4]
        if not re.match(r"^https?://", url) and url not in ("-", "本地", "self"):
            bad.append((i, f"{name} 来源 URL 不可溯"))
        if not owner: bad.append((i, f"{name} 缺版权人"))
        if lic.lower().startswith(("未知", "unknown", "?")) or not lic:
            bad.append((i, f"{name} 许可证缺失/未知"))
        elif not any(k in lic.lower() for k in OK_LICENSES) and "商业授权" not in lic:
            bad.append((i, f"{name} 许可证未在白名单: {lic}"))
    return bad
def main():
    a = sys.argv[1:]
    p = a[a.index("--path") + 1] if "--path" in a else ""
    if not p or not os.path.exists(p):
        print("用法: --path <assets.md>"); sys.exit(2)
    bad = check(p)
    for i, w in bad: print("违规 行%s: %s" % (i, w))
    print("素材违规数 =", len(bad)); sys.exit(1 if bad else 0)
if __name__ == "__main__":
    main()
