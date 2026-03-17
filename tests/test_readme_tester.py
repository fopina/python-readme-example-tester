from readme_tester.__main__ import main
from readme_tester.core import extract_fenced_code_blocks, validate_python_blocks


def test_extract_fenced_code_blocks_filters_python_blocks():
    markdown = '# Example\n```python\nprint("hello")\n```\n```bash\necho hello\n```\n'
    blocks = extract_fenced_code_blocks(markdown)

    assert [block.language for block in blocks] == ['python', 'bash']
    assert blocks[0].start_line == 3


def test_validate_python_blocks_reports_syntax_errors():
    errors = validate_python_blocks('```python\nprint(\n```\n')

    assert len(errors) == 1
    assert errors[0].line == 2
    assert 'never closed' in errors[0].message or 'was never closed' in errors[0].message


def test_cli_validates_readme(tmp_path, capsys):
    readme = tmp_path / 'README.md'
    readme.write_text('```python\nprint("ok")\n```\n')

    exit_code = main([str(readme)])

    assert exit_code == 0
    assert capsys.readouterr().out == f'{readme}: validated 1 Python code block(s)\n'
