# readme-example-tester

[![ci](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/python-readme-tester/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/python-readme-tester/graph/badge.svg)](https://codecov.io/github/fopina/python-readme-tester)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/readme-example-tester.svg)](https://pypi.org/project/readme-example-tester/)
[![Current version on PyPI](https://img.shields.io/pypi/v/readme-example-tester)](https://pypi.org/project/readme-example-tester/)

> **WIP**

Validate fenced Python code blocks in Markdown files, with a small CLI that is handy for README checks in local development and CI.

## Install

```bash
pip install readme-example-tester
```

## Usage

```bash
$ readme-example-tester README.md
README.md: validated 2 Python code block(s)
```

If a fenced Python block contains invalid syntax, the command exits with a non-zero status and prints the failing line:

```text
$ readme-example-tester README.md
README.md:27: '(' was never closed
```

## Python API

```python
from readme_example_tester import ReadmeTestCase

assert hasattr(ReadmeTestCase, "__name__")
```

## Development
Project setup and local checks live in [CONTRIBUTING.md](CONTRIBUTING.md).
