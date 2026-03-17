from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CodeBlock:
    language: str
    code: str
    start_line: int


@dataclass(frozen=True)
class ValidationError:
    line: int
    message: str


def extract_fenced_code_blocks(markdown: str) -> list[CodeBlock]:
    blocks: list[CodeBlock] = []
    in_block = False
    block_language = ''
    block_start = 0
    block_lines: list[str] = []

    for line_number, line in enumerate(markdown.splitlines(), start=1):
        if line.startswith('```'):
            if in_block:
                blocks.append(CodeBlock(language=block_language, code='\n'.join(block_lines), start_line=block_start))
                in_block = False
                block_language = ''
                block_lines = []
            else:
                in_block = True
                block_language = line[3:].strip().lower()
                block_start = line_number + 1
            continue

        if in_block:
            block_lines.append(line)

    return blocks


def validate_python_blocks(markdown: str) -> list[ValidationError]:
    errors: list[ValidationError] = []

    for block in extract_fenced_code_blocks(markdown):
        if block.language not in {'python', 'py'}:
            continue

        try:
            compile(block.code, f'<markdown:{block.start_line}>', 'exec')
        except SyntaxError as exc:
            error_line = block.start_line + max((exc.lineno or 1) - 1, 0)
            errors.append(ValidationError(line=error_line, message=exc.msg))

    return errors


def validate_markdown_file(path: str | Path) -> list[ValidationError]:
    return validate_python_blocks(Path(path).read_text())
