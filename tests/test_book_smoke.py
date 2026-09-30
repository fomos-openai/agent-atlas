import os
from pathlib import Path
import unittest

from pypdf import PdfReader


class BookTests(unittest.TestCase):
    def test_book_exists(self):
        path = Path(
            os.environ.get(
                "AGENT_ATLAS_BOOK_OUTPUT", "artifacts/agent-atlas-book.zh-CN.pdf"
            )
        )
        self.assertTrue(path.exists())
        self.assertGreater(path.stat().st_size, 100_000)
        self.assertTrue(80 <= len(PdfReader(str(path)).pages) <= 120)


if __name__ == "__main__":
    unittest.main()
