import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_quarto_uses_only_content_as_manuscript(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        self.assertIn("content/01-foundations/02-paradigm-evolution.qmd", config)
        self.assertIn("content/02-core-mechanics/06-tools-contracts-and-execution.qmd", config)
        self.assertNotIn("book/manuscript", config)

    def test_all_json_contracts_parse(self):
        for path in (ROOT / "labs/contracts").glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))

    def test_map_has_cross_cutting_guarantees(self):
        data = json.loads((ROOT / "maps/agent-atlas.architecture.json").read_text(encoding="utf-8"))
        ids = {component["id"] for component in data["components"]}
        self.assertTrue({"evidence", "labs", "evaluation", "safety"} <= ids)

    def test_old_v1_content_trees_are_absent(self):
        self.assertFalse((ROOT / "knowledge").exists())
        self.assertFalse((ROOT / "book/manuscript").exists())


if __name__ == "__main__":
    unittest.main()
