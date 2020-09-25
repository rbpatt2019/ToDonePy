import argparse
from pathlib import Path

import pytest
from helpers.filer import Filer
from subcommands.done import done

from todonepy import to

expected = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "1", "2019-09-24 12:57", "New task"],
]


def test_to_done(tmp_file: Filer, capsys):
    """Check that task are appropriately deleted from the TODO file"""

    to(
        argparse.Namespace(
            func=done, file=tmp_file, create=True, tasks=["nothing", "Old task"]
        )
    )
    out, err = capsys.readouterr()

    assert tmp_file.read() == expected
    assert err == ""
    assert (
        out == 'Task "nothing" not in TODOs...\nTask "Old task" successfully deleted!\n'
    )
