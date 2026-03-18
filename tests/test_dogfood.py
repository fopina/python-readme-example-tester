from pathlib import Path

from readme_example_tester import ReadmeTestCase


class TestReadme(ReadmeTestCase):
    # assuming test is in tests/ and README.md in root
    README_PATH = Path(__file__).parent.parent / 'README.md'
    TESTS_DIR = Path(__file__).parent
    README_MARKER = 'actual-example-id'
