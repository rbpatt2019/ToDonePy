import argparse
from pathlib import Path

import pytest
from freezegun import freeze_time

from helpers.filer import Filer
from subcommands.do import do
from todonepy import to

expected_none = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "2", "2019-09-20 20:56", "Old task"],
    ["2", "1", "2019-09-24 12:57", "New task"],
    ["3", "1", "2020-07-08 17:00", "Newer task"],
]
expected_both = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "1", "2019-09-24 12:57", "New task"],
    ["2", "1", "2020-07-08 17:00", "Newer task"],
    ["3", "2", "2019-09-20 20:56", "Old task"],
]


@pytest.mark.parametrize(
    "sort,expected", [("none", expected_none), ("both", expected_both)],
)
@freeze_time("2020-07-08 17:00")
def test_to_do(sort: str, expected: str, tmp_file: Filer, capsys):
    """Check that tasks are appropriately added and sorted

    Parametrized to check various calls to the `--sort` flag"""

    to(
        argparse.Namespace(
            func=do, file=tmp_file, sort=sort, rank=1, tasks=["Newer task"]
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read() == expected

    assert err == ""
    assert out == "1 task(s) added!\n"
