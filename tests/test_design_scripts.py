"""test_design_scripts.py — 设计脚本单元测试：对比度算法、令牌展开、素材合规判定。"""
import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir, "scripts"))
import asset_check as ac
import contrast_check as cc
import design_tokens as dt

class TestContrast(unittest.TestCase):
    def test_black_white(self):
        self.assertAlmostEqual(cc.ratio("#000000", "#ffffff"), 21.0, places=1)

    def test_shorthand_hex(self):
        self.assertEqual(cc.rgb("#fff"), (255, 255, 255))

    def test_low_contrast_flagged(self):
        pairs = cc.pairs({"color": {"bg": "#ffffff", "accent": "#8ab4f8"}})
        self.assertTrue(any(r < 4.5 for _, _, _, r in pairs))

class TestTokens(unittest.TestCase):
    def test_flatten(self):
        f = dt.flat({"color": {"bg": "#fff"}, "space": {"md": 16}})
        self.assertEqual(f["color-bg"], "#fff")
        self.assertEqual(f["space-md"], 16)

    def test_css_units(self):
        css = dt.css({"space": {"md": 16}, "color": {"bg": "#fff"}})
        self.assertIn("--space-md: 16px", css)
        self.assertIn("--color-bg: #fff", css)

class TestAsset(unittest.TestCase):
    def _run(self, text):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                        encoding="utf-8") as fh:
            fh.write(text)
            p = fh.name
        try:
            return ac.check(p)
        finally:
            os.unlink(p)

    def test_compliant_line(self):
        self.assertEqual(self._run("i.svg | https://x.io | MIT | Acme\n"), [])

    def test_unknown_license_flagged(self):
        self.assertTrue(self._run("i.svg | https://x.io | 未知 | Acme\n"))

if __name__ == "__main__":
    unittest.main()
