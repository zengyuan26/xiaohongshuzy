from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PortableSkillContractTest(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        path = ROOT / relative_path
        self.assertTrue(path.is_file(), f"missing required file: {relative_path}")
        return path.read_text(encoding="utf-8")

    def test_portable_package_has_required_entrypoints(self):
        skill = self.read("SKILL.md")
        self.assertIn("name: xiaohongshu-carousel-creator", skill)
        self.assertIn("description: Use when", skill)
        self.read("README.md")
        self.read("references/carrier-selection.md")
        self.read("references/xiaohongshu-research.md")
        self.read("references/carousel-production.md")
        self.read("references/delivery-contract.md")
        self.read("references/example.md")

    def test_skill_routes_before_it_writes(self):
        skill = self.read("SKILL.md")
        self.assertIn("先判断是否适合图文", skill)
        self.assertIn("R0", skill)
        self.assertIn("R3", skill)
        self.assertIn("主类型", skill)
        self.assertIn("主证明单元", skill)

    def test_failure_scenarios_have_explicit_routes(self):
        research = self.read("references/xiaohongshu-research.md")
        production = self.read("references/carousel-production.md")
        delivery = self.read("references/delivery-contract.md")
        self.assertIn("链接打不开", research)
        self.assertIn("不得声称", research)
        self.assertIn("健康", research)
        self.assertIn("食品安全", research)
        self.assertIn("只改封面", research)
        self.assertIn("连续语言因果", production)
        self.assertIn("明确授权", delivery)

    def test_default_delivery_is_complete_but_not_auto_publish(self):
        delivery = self.read("references/delivery-contract.md")
        self.assertIn("发布标题", delivery)
        self.assertIn("五个话题标签", delivery)
        self.assertIn("发布描述", delivery)
        self.assertIn("3:4", delivery)
        self.assertIn("不会自动发布", delivery)

    def test_cross_runtime_installation_is_documented(self):
        readme = self.read("README.md")
        self.assertIn("Codex", readme)
        self.assertIn("Claude Code", readme)
        self.assertIn(".agents/skills", readme)
        self.assertIn(".claude/skills", readme)


if __name__ == "__main__":
    unittest.main()
