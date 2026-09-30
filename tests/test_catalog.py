import subprocess
import sys
import unittest


class CatalogTests(unittest.TestCase):
    def test_catalog_validator(self):
        result = subprocess.run([sys.executable, "scripts/validate_catalog.py"], check=False)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
