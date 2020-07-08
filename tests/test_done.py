import argparse
from pathlib import Path

import pytest

from todonepy import to
from subcommands.done import done
from helpers.filer import Filer



def test_to_done(tmp_file: Path, capsys):
    """Check that task are appropriately deleted from the TODO file"""
    
    to(argparse.Namespace(func=done, file=Filer(tmp_file, create=True), tasks=['nothing', 'Old task']))
    out, err = capsys.readouterr()
    
    assert (
        tmp_file.read_text()
        == "ID\tRank\tDate\tTask\n1\t1\t2019-09-24 12:57\tNew task\n"
    )
    
    assert err == ''
    assert out == 'Task "nothing" not in TODOs...\nTask "Old task" successfully deleted!\n'
