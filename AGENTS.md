# Project Notes

## Scope

- This repository currently exposes a small public API from `readme_example_tester`: `ReadmeTestCase` and `ReadmeExample`.
- The main implementation lives in `readme_example_tester/case.py`.
- There is no `readme_example_tester.core` or `readme_example_tester.__main__` module in this checkout, so tests and changes should target `readme_example_tester.case` / `readme_example_tester`.

## Environment

- Use `uv sync --dev` to set up the local environment.
- Run tests with `make test`.
- Run lint/format checks with `make lint` or `make lint-check`.

## Testing Conventions

- Prefer `unittest.TestCase` style tests in this project.
- Keep tests focused on the actual package surface and helper behavior in `ReadmeTestCase`.
- When filesystem setup is needed, use `tempfile.TemporaryDirectory()` and write files with explicit `encoding='utf-8'`.

## Implementation Notes

- `ReadmeTestCase` subclasses must define both `README_PATH` and `TESTS_DIR`.
- README markers use `# README +++` / `# README ---` blocks, with optional IDs like `# README:setup +++`.
- README example comments use HTML comments such as `<!-- example-id: cli.py -->` and `<!-- example-id-output: cli.py -->`.

## Style

- Ruff is configured with a 120-character line length and single quotes in formatted code.
