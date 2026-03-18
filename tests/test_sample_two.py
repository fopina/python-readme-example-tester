from pathlib import Path

from readme_example_tester import ReadmeTestCase


class TestReadme(ReadmeTestCase):
    README_PATH = Path(__file__).parent / 'sample_two.md'
    TESTS_DIR = Path(__file__).parent
