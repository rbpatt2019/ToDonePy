import argparse
from pathlib import Path
from shutil import which

import pytest

from todonepy import to
from subcommands.doing import doing
from helpers.filer import Filer

expected_none = "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56\tOld task\n2\t1\t2019-09-24 12:57\tNew task\n"
expected_both = "ID\tRank\tDate\tTask\n1\t1\t2019-09-24 12:57\tNew task\n2\t2\t2019-09-20 20:56\tOld task\n"


@pytest.mark.parametrize('sort,expected', [('none', expected_none), ('both', expected_both)])
def test_to_doing(sort: str, expected: str, tmp_file: Path, capsys):
    """Run to doing with existing custom file

    Parametrised to test situations where `--sort` is/isn't passed"""

    to(
        argparse.Namespace(
            func=doing,
            file=Filer(tmp_file),
            sort=sort,
            number=5,
            edit=False,
            reminder=False,
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read_text() == expected

    assert err == ""
    assert out == expected

@pytest.mark.skip(reason='Vim hangs indefinitely')
def test_to_doing_custom_file_edit_flag(tmp_file: Path, capsys):
    """Run to doing with the edit flag"""
    to(
        argparse.Namespace(
            func=doing,
            file=Filer(tmp_file),
            sort='none',
            number=5,
            edit=True,
            reminder=False,
        )
    )
    out, err = capsys.readouterr()
    assert err == ""
    assert out == ""


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

