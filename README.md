# readme-example-tester

[![ci](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/python-readme-tester/graph/badge.svg)](https://codecov.io/github/fopina/python-readme-tester)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/readme-example-tester.svg)](https://pypi.org/project/readme-example-tester/)
[![Current version on PyPI](https://img.shields.io/pypi/v/readme-example-tester)](https://pypi.org/project/readme-example-tester/)

Do not let your README/documentation examples become invalid: unit test them!

## Install

```bash
pip install readme-example-tester
```

## Usage

Mark the code blocks that you want to test

<!-- actual-example-id: tests/sample_one.md -->
````markdown
Simple snippet using this awesome package:

<!-- example-id: tests/some_sample.py -->
```python
import thislib

def some_method():
    return thislib.magic_twist('hello')
```
````

Then create a unit test for that markdown file, such as:

```python
from pathlib import Path

from readme_example_tester import ReadmeTestCase


class TestReadme(ReadmeTestCase):
    # assuming test is in tests/ and README.md in root
    README_PATH = Path(__file__).parent.parent / 'README.md'
    TESTS_DIR = Path(__file__).parent
```

**Note**: this example is actually covered in (TBD sample file) and (TBD unit test).

## Development
Project setup and local checks live in [CONTRIBUTING.md](CONTRIBUTING.md).
