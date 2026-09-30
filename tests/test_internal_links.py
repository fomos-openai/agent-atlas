import subprocess
import sys
import unittest


class LinkTests(unittest.TestCase):
    def test_link_validator(self):
        result = subprocess.run([sys.executable, "scripts/validate_links.py"], check=False)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
