import argparse
from shutil import which

import pytest

from todonepy import to
from subcommands.doing import doing
from helpers.filer import Filer

expected_none = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "2", "2019-09-20 20:56", "Old task"],
    ["2", "1", "2019-09-24 12:57", "New task"],
]
expected_both = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "1", "2019-09-24 12:57", "New task"],
    ["2", "2", "2019-09-20 20:56", "Old task"],
]


@pytest.mark.parametrize(
    "sort,expected", [("none", expected_none), ("both", expected_both)]
)
def test_to_doing(sort: str, expected: str, tmp_file: Filer, capsys):
    """Run to doing with existing custom file

    Parametrised to test situations where `--sort` is/isn't passed"""

    to(
        argparse.Namespace(
            func=doing,
            file=tmp_file,
            sort=sort,
            number=5,
            edit=False,
            reminder=False,
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read() == expected

    assert err == ""
    assert out == "\n".join(["\t".join(i) for i in expected]) + "\n"


@pytest.mark.skip(reason="Vim hangs indefinitely")
def test_to_doing_custom_file_edit_flag(tmp_file: Filer, capsys):
    """Run to doing with the edit flag"""
    to(
        argparse.Namespace(
            func=doing,
            file=tmp_file,
            sort="none",
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
            file=tmp_file,
            sort="none",
            number=5,
            edit=False,
            reminder=True,
        )
    )
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

