# readme-tester

[![ci](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/python-readme-tester/graph/badge.svg)](https://codecov.io/github/fopina/python-readme-tester)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/readme-tester.svg)](https://pypi.org/project/readme-tester/)
[![Current version on PyPI](https://img.shields.io/pypi/v/readme-tester)](https://pypi.org/project/readme-tester/)

Validate fenced Python code blocks in Markdown files, with a small CLI that is handy for README checks in local development and CI.

## Install

```bash
pip install readme-tester
```

## Usage

```bash
$ readme-tester README.md
README.md: validated 2 Python code block(s)
```

If a fenced Python block contains invalid syntax, the command exits with a non-zero status and prints the failing line:

```text
$ readme-tester README.md
README.md:27: '(' was never closed
```

## Python API

```python
from readme_tester.core import validate_python_blocks

markdown = """```python
print("hello from the README")
```"""

errors = validate_python_blocks(markdown)
assert errors == []
```

## Development

Project setup and local checks live in [CONTRIBUTING.md](CONTRIBUTING.md).
