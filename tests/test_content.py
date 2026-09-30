import subprocess
import sys
import unittest


class ContentTests(unittest.TestCase):
    def test_content_validator(self):
        result = subprocess.run([sys.executable, "scripts/validate_content.py"], check=False)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
