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

Mark the code blocks that you want to test.

<!-- actual-example-id: tests/sample_one.md -->
````markdown
Check out this crazy snippet:

<!-- example-id: tests/sample_pump_it_up.py -->
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

Whenever this test case runs, 3 tests are executed:
* `test_readme_example_targets_have_tests`: ensures every snippet is covered by a test case
* `test_readme_code_blocks_match_example_targets`: ensures every snippet matches an existing file
* `test_examples_are_still_in_use`: ensures all files inside `TESTS_DIR` matching `SAMPLE_FILE_GLOB` (`sample_*`) are still being used in the README

These tests, plus the sample-file coverage checks, keep README examples honest.

### Dogfooding
This project README is actually covered by [tests/test_dogfood.py](tests/test_dogfood.py)

And the inner example is in [tests/sample_one.md](tests/sample_one.md) and covered by [tests/test_sample_one_readme.py](tests/test_sample_one_readme.py)

### Advanced usage

#### Custom marker

```python
class DemoReadme(ReadmeTestCase):
    README_PATH = Path(__file__).parent / 'README.md'
    TESTS_DIR = Path(__file__).parent
    README_MARKER = 'demo-id'
```

````text
<!-- demo-id: tests/some_sample.py -->
```python
def pump_it_up(input):
    return input + 100
```
````

#### Assert snippet outputs

Expanding the previous example to be executable
<!-- actual-example-id: tests/sample_pump_it_up_cli.py -->
```python
#!/usr/bin/env python3


def pump_it_up(input):
    return input + 100


def main(argv):
    if not argv:
        print('No pump')
    else:
        print(pump_it_up(int(argv[0])))


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
```

<!-- actual-example-id-output: tests/sample_pump_it_up_cli.py -->
```text
$ tests/test_show_greeting.py
dogfood
```

#### Partial snippets

Use `# README+++` / `# README---` in a sample file to narrow the excerpt that matches the README block when the source file has extra boilerplate. If one sample file feeds multiple README blocks, use `# README:<id>+++` / `# README:<id>---` to split the source into named sections. This README's inner example is backed by [tests/sample_one.md](tests/sample_one.md).

#### Non-sample sample files

If you have a test file that matches SAMPLE_FILE_GLOB but it is not expected to be used in README, you can add `# README-EXCLUDE`

## Development
Project setup and local checks live in [CONTRIBUTING.md](CONTRIBUTING.md).
