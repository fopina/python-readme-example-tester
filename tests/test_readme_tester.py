import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

from readme_tester import ReadmeTestCase


class ReadmeTestCaseTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_dir = Path(self.temp_dir.name)
        self.tests_dir = self.project_dir / 'tests'
        self.tests_dir.mkdir()
        self.readme_path = self.project_dir / 'README.md'

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_case(self):
        class ExampleReadmeCase(ReadmeTestCase):
            README_PATH = self.readme_path
            TESTS_DIR = self.tests_dir

        return ExampleReadmeCase()

    def test_subclasses_require_readme_path_and_tests_dir(self):
        with self.assertRaisesRegex(TypeError, 'must define README_PATH'):

            class MissingReadmePath(ReadmeTestCase):
                TESTS_DIR = Path('tests')

        with self.assertRaisesRegex(TypeError, 'must define TESTS_DIR'):

            class MissingTestsDir(ReadmeTestCase):
                README_PATH = Path('README.md')

    def test_iter_readme_examples_parses_code_and_output_blocks(self):
        self.readme_path.write_text(
            textwrap.dedent(
                """\
                # Examples

                <!-- example-id: cli.py:setup -->
                ```python
                print("hello")
                ```

                <!-- example-id-output: cli.py -->
                ```text
                $ cli.py
                hello
                ```
                """
            ),
            encoding='utf-8',
        )

        examples = list(self.make_case()._iter_readme_examples())

        self.assertEqual(len(examples), 2)
        self.assertEqual(examples[0].cli, 'cli.py')
        self.assertEqual(examples[0].readme_id, 'setup')
        self.assertEqual(examples[0].language, 'python')
        self.assertEqual(examples[0].code, 'print("hello")')
        self.assertFalse(examples[0].is_output)
        self.assertEqual(examples[1].args, [])
        self.assertEqual(examples[1].language, 'text')
        self.assertTrue(examples[1].is_output)

    def test_readme_blocks_in_cli_file_collects_named_groups(self):
        cli_file = self.tests_dir / 'cli.py'
        cli_file.write_text(
            textwrap.dedent(
                """\
                # README:setup +++
                print("setup")
                # README:setup ---
                # README +++
                print("default")
                # README ---
                """
            ),
            encoding='utf-8',
        )

        blocks = self.make_case()._readme_blocks_in_cli_file(cli_file)

        self.assertEqual(blocks, {'setup': ['print("setup")'], None: ['print("default")']})

    @mock.patch('readme_tester.case.subprocess.run')
    def test_run_cli_output_strips_shell_prompts(self, run_mock):
        run_mock.return_value = subprocess.CompletedProcess(
            args=['cli.py'],
            returncode=0,
            stdout='$ cli.py\nhello\n',
        )

        output = self.make_case()._run_cli_output('cli.py', [])

        self.assertEqual(output, 'hello')
        run_mock.assert_called_once_with(
            ['cli.py'],
            cwd=self.project_dir,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
