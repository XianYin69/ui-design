"""scaffold_design.py — 设计工程脚手架：tokens/screens/assets/tests 布局与占位文件，默认预览。"""
import os, sys
TOKENS = ('{\n  "color": {"bg": "#ffffff", "fg": "#111111", "accent": "#0b57d0"},\n'
          '  "space": {"xs": 4, "sm": 8, "md": 16, "lg": 24, "xl": 32},\n'
          '  "font": {"base": 16, "scale": 1.25},\n'
          '  "radius": {"sm": 4, "md": 8},\n  "motion": {"fast": 120, "base": 200}\n}\n')
SCREEN = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
          '<link rel="stylesheet" href="../tokens/tokens.css">\n<title>Screen</title>\n'
          '</head>\n<body>\n<main>\n  <h1>标题</h1>\n  <p>正文</p>\n</main>\n</body>\n</html>\n')
ASSET = ('# assets（素材清单）\n\n每行一条：`文件名 | 来源URL | 许可证 | 版权人`。\n'
         '无许可证记录的素材禁止使用。\n')
TEST = ('import os, sys, unittest\n'
        'sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir,\n'
        '                                os.pardir, "scripts"))\n\n\n'
        'class TestScaffold(unittest.TestCase):\n'
        '    def test_placeholder(self):\n        self.assertTrue(True)\n\n\n'
        'if __name__ == "__main__":\n    unittest.main()\n')
README = ("# 设计工程\n\n- 令牌真源: tokens/tokens.json\n- 界面: screens/\n"
          "- 素材: assets/assets.md\n")
TPL = {"tokens/tokens.json": TOKENS, "screens/index.html": SCREEN,
       "assets/assets.md": ASSET, "tests/test_scaffold.py": TEST,
       "tests/__init__.py": "",
       "README.md": README}

def main():
    a = sys.argv[1:]
    g = lambda k, d="": a[a.index(k) + 1] if k in a else d
    tgt = g("--target")
    if not tgt:
        print("用法: --target <dir> [--layout tokens,screens,assets,tests] [--yes]")
        sys.exit(2)
    lay = [x for x in g("--layout", "tokens,screens,assets,tests").split(",") if x]
    for rel, body in TPL.items():
        if rel != "README.md" and rel.split("/")[0] not in lay:
            continue
        p = os.path.join(tgt, rel)
        if "--yes" not in a:
            print("[预览]", p)
            continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if os.path.exists(p):
            print("[跳过] 已存在", p)
            continue
        open(p, "w", encoding="utf-8").write(body)
        print("[写入]", p)
    print("[脚手架]", tgt, "| 下一步：按大纲替换占位实现")
if __name__ == "__main__":
    main()
