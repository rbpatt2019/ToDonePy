import argparse
from pathlib import Path
from shutil import which

import pytest

from todonepy import to
from subcommands.doing import doing
from helpers.filer import Filer

expected_none = "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56:00\tOld task\n2\t1\t2019-09-24 12:57:00\tNew task\n"
expected_both = "ID\tRank\tDate\tTask\n1\t1\t2019-09-24 12:57:00\tNew task\n2\t2\t2019-09-20 20:56:00\tOld task\n"


@pytest.mark.parametrize('sort,expected', [('none', expected_none), ('both', expected_both)])
def test_to_doing_custom_file(sort: str, expected: str, tmp_file: Path, capsys):
    """Run to doing with existing custom file

    Parametrised to test situations where `--sort` is/isn't passed"""

    to(
        argparse.Namespace(
            func=doing,
            filer=Filer(tmp_file),
            sort=sort,
            number=5,
            edit=False,
            reminder=True,
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read_text() == expected

    assert err == ""
    assert out == expected


# @pytest.mark.xfail(reason="Vim hangs the test, resulting in non-0 exit code")
# def test_to_doing_custom_file_edit_flag(tmp_file: Path):
#     """Run to doing with the edit flag

#     :tmp_file: Custom pytest.fixture. Instantiated tsv

#     :returns: None
#     """
#     runner = CliRunner()
#     with runner.isolated_filesystem():
#         result = runner.invoke(to, ["--file", f"{tmp_file}", "doing", "--edit"])
#         assert result.exit_code == 0
#         assert result.output == ""


@pytest.mark.skipif(which("notify-send") is None, reason="Requires notify-send")
def test_to_doing_custom_file_graphic_flag(tmp_file, capsys):
    """Run to doing with the `--reminder` flag"""

    to(
        argparse.Namespace(
            func=doing,
            filer=Filer(tmp_file),
            sort="none",
            number=5,
            edit=False,
            reminder=True,
        )
    )
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

