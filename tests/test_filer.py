#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from pathlib import Path
from typing import Callable, List, Optional, Union

import pytest

from helpers.filer import Filer

results_txt = [
    ["ID", "Rank", "Date", "Task"],
    ["1", "2", "2019-09-20 20:56:00", "Old task"],
    ["2", "1", "2019-09-24 12:57:00", "New task"],
]


@pytest.mark.parametrize(
    "create,expected",
    [
        pytest.param(False, [[]], marks=pytest.mark.xfail),
        (True, [["ID", "Rank", "Date", "Task"]]),
    ],
)
def test_Filer_no_create(
    tmp_path: Path, create: bool, expected: List[List[Optional[str]]],
) -> None:
    """Run Filer to read a file that does not exist

    :tmp_path: pytest.fixture. Where to create the file
    :create: Whether or not the file should be created, from pytest.mark.parametrize
    :expected: Expected output, from pytest.mark.parametrize

    :returns: None

    """
    file = Filer(tmp_path / "tmp.tsv", create=create)
    assert file.read() == expected


def test_Filer_read_existing_file(tmp_file: Path,) -> None:
    """Run Filer to read an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files

    :returns: None

    """
    file = Filer(tmp_file)
    for line, entry in zip(file.read(), results_txt):
        assert line == entry


def test_Filer_write_existing_file(tmp_file: Path,) -> None:
    """Run Filer to write to an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files

    :returns: None

    """
    written = [["3", "3", "2020-06-24 08:53:00", "Newer task"]]
    file = Filer(tmp_file)
    file.write(written)
    for line, entry in zip(file.read(), written):
        assert line == entry


def test_Filer_append_existing_file(tmp_file: Path) -> None:
    """Run Filer to append to an existing file

    :tmp_file: Custom pytest.fixture for freating tmp files

    :returns: None

    """
    added = [["3", "3", "2020-06-24 08:53:00", "Newer task"]]
    file = Filer(tmp_file)
    file.append(added)
    for line, entry in zip(file.read(), results_txt + added):
        assert line == entry


@pytest.mark.parametrize(
    "header,expected",
    [(False, results_txt[:0:-1]), (True, [results_txt[i] for i in [0, 2, 1]])],
)
def test_Filer_sort_existing_file(
    tmp_file: Path, header: bool, expected: List[List[str]],
) -> None:
    """Run Filer to sort an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files
    :header: Whether or not the file has a header, from pytest.mark.parametrize
    :expected: The expected result, from pytest.mark.parametrize

    :returns: None

    """
    file = Filer(tmp_file)
    if not header:  # As tmp file comes with header, delete if necessary
        file.delete("Rank")
    file.sort([1], header=header)
    for line, entry in zip(file.read(), expected):
        assert line == entry


@pytest.mark.parametrize(
    "to_del,expected", [("Old task", results_txt[0::2]), ("nothing", results_txt)],
)
def test_Filer_delete_existing_file(
    tmp_file: Path, to_del: str, expected: List[List[str]],
) -> None:
    """Run Filer to delete a line from  an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files
    :to_del: Line to be deleted, from pyteset.mark.parametrize
    :expected: Expected result, from pytest.mark.parametrize

    :returns: None

    """
    file = Filer(tmp_file)
    file.delete(to_del)
    for line, entry in zip(file.read(), expected):
        assert line == entry
