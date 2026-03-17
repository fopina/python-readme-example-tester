from __future__ import annotations

import argparse
from pathlib import Path

from .core import extract_fenced_code_blocks, validate_markdown_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Validate Python fenced code blocks in a Markdown file.')
    parser.add_argument('path', nargs='?', default='README.md', help='Markdown file to validate')
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path = Path(args.path)
    errors = validate_markdown_file(path)
    python_blocks = [
        block for block in extract_fenced_code_blocks(path.read_text()) if block.language in {'python', 'py'}
    ]

    if errors:
        for error in errors:
            print(f'{path}:{error.line}: {error.message}')
        return 1

    print(f'{path}: validated {len(python_blocks)} Python code block(s)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
