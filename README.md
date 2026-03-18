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
Check out this crazy snippet:

<!-- example-id: tests/some_sample.py -->
```python
def pump_it_up(input):
    return input + 100
```
````

Then create a unit test for that README, such as:

<!-- actual-example-id: tests/test_sample_one_readme.py -->
```python
from pathlib import Path

from readme_example_tester import ReadmeTestCase


class TestReadme(ReadmeTestCase):
    # assuming test is in tests/ and README.md in root
    README_PATH = Path(__file__).parent.parent / 'README.md'
    TESTS_DIR = Path(__file__).parent
```

Whever this testcase runs, two tests are executed:
* `test_readme_example_targets_have_clis_tests`: Ensure every snippet is covered by a test case
* `test_readme_cli_code_blocks_match_tests`: Ensure every snippet matches an existing file

These 2 tests plus the enforce tests on sample files ensures that README always has working code snippets!

### Dog fooding
This project README is actually covered by [tests/test_dogfood.py](tests/test_dogfood.py)

And the inner example is in [tests/sample_one.md](tests/sample_one.md) and covered by [tests/test_sample_one_readme.py](tests/test_sample_one_readme.py)

### More usage options

> WIP - implemented but documentation pending

* Customize marker: `example-id` is the default but `README_MARKER` allows customizing it
* Assert snippet *outputs*: use `<!-- example-id-out: tests/some_sample.py someArg -->` when the code block includes the output produced by executing `tests/some_sample.py someArg`
* Partial snippets: use `README+++`/`README---` in your sample files to highlight the parts that are in the matching code block, instead of the full file - when there's boilerplate required but not meaningful to document
  * Also possible to use same sample file for different code blocks: use `README:<id>+++` in the sample file to delimit and then `<!-- example-id:<id> tests/some_sample.py -->` in the code blocks

## Development
Project setup and local checks live in [CONTRIBUTING.md](CONTRIBUTING.md).
