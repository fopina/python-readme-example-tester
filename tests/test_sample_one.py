import unittest
from pathlib import Path


class TestSample(unittest.TestCase):
    def test_it(self):
        # it's actually a markdown file, not much to test there
        # just a placeholder to force testing the sample inside the sample
        # in test_some_sample.py

        contents = (Path(__file__).parent / 'sample_one.md').read_text()
        self.assertIn('<!-- example-id: tests/some_sample.py -->', contents)
