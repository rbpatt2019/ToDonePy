import argparse
from pathlib import Path

import pytest
from freezegun import freeze_time

from helpers.filer import Filer
from subcommands.do import do
from todonepy import to

expected_none = "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56\tOld task\n2\t1\t2019-09-24 12:57\tNew task\n3\t1\t2020-07-08 17:00\tNewer task\n"
expected_both = "ID\tRank\tDate\tTask\n1\t1\t2019-09-24 12:57\tNew task\n2\t1\t2020-07-08 17:00\tNewer task\n3\t2\t2019-09-20 20:56\tOld task\n"


@pytest.mark.parametrize(
    "sort,expected",
    [("none", expected_none), ("both", expected_both)],
)
@freeze_time("2020-07-08 17:00")
def test_to_do(sort: str, expected: str, tmp_file: Path, capsys):
    """Check that tasks are appropriately added and sorted

    Parametrized to check various calls to the `--sort` flag"""

    to(
        argparse.Namespace(
            func=do, file=Filer(tmp_file), sort=sort, rank=1, tasks=["Newer task"]
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read_text() == expected

    assert err == ""
    assert out == "1 task(s) added!\n"
