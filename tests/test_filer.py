#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from pathlib import Path
from typing import Callable, List, Optional, Union

import pytest

from ToDonePy.filer import Filer as Filer


@pytest.mark.parametrize(
    "create,expected",
    [
        pytest.param(False, [[]], marks=pytest.mark.xfail),
        (True, [["ID", "Rank", "Date", "Task"]]),
    ],
)
def test_Filer_no_create(
    tmp_file: Callable[[Union[str, None]], Path],
    create: bool,
    expected: List[List[Optional[str]]],
) -> None:
    """Run Filer to read a file that does not exist

    :tmp_file: Custom pytest.fixture for creating tmp files
    :create: Whether or not the file should be created, from pytest.mark.parametrize
    :expected: Expected output, from pytest.mark.parametrize

    :returns: None

    """
    file = Filer(tmp_file(None), create=create)
    assert file.read() == expected


def test_Filer_read_existing_file(
    tmp_file: Callable[[Union[str, None]], Path],
    content: str = "1\tMake Tests\n2\tRun Tests",
) -> None:
    """Run Filer to read an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files
    :content: Contents of temporary file

    :returns: None

    """
    file = Filer(tmp_file(content))
    for line, entry in zip(file.read(), [["1", "Make Tests"], ["2", "Run Tests"]]):
        assert line == entry


def test_Filer_write_existing_file(
    tmp_file: Callable[[Union[str, None]], Path],
    content: str = "1\tMake Tests\n2\tRun Tests",
    new_contents: List[List[str]] = [["3", "More tests"], ["4", "Most tests"]],
) -> None:
    """Run Filer to write to an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files
    :content: Contents of temporary file
    :new_contents: Contents to be written to file

    :returns: None

    """
    file = Filer(tmp_file(content))
    file.write(new_contents)
    for line, entry in zip(file.read(), new_contents):
        assert line == entry


def test_Filer_append_existing_file(
    tmp_file: Callable[[Union[str, None]], Path],
    content: str = "1\tMake Tests\n2\tRun Tests\n",
    new_contents: List[List[str]] = [["3", "More tests"], ["4", "Most tests"]],
) -> None:
    """Run Filer to append to an existing file

    :tmp_file: Custom pytest.fixture for freating tmp files
    :content: Contents of temporary file
    :new_contents: Contents to be added to file

    :returns: None

    """
    file = Filer(tmp_file(content))
    file.append(new_contents)
    for line, entry in zip(
        file.read(), [["1", "Make Tests"], ["2", "Run Tests"]] + new_contents
    ):
        assert line == entry


results_sort = [
    ["No.", "Task"],
    ["1", "Run Tests"],
    ["2", "Make Tests"],
    ["3", "More Tests"],
]


@pytest.mark.parametrize(
    "header,expected", [(False, results_sort[1:]), (True, results_sort)]
)
def test_Filer_sort_existing_file(
    tmp_file: Callable[[Union[str, None]], Path],
    header: bool,
    expected: List[List[str]],
) -> None:
    """Run Filer to sort an existing file

    :tmp_file: Custom pytest.fixture for creating tmp files
    :header: Whether or not the file has a header
    :expected: The expected result

    :returns: None

    """
    if header:
        content = "No.\tTask\n3\tMore Tests\n2\tMake Tests\n1\tRun Tests\n"
    else:
        content = "3\tMore Tests\n2\tMake Tests\n1\tRun Tests\n"
    file = Filer(tmp_file(content))
    file.sort([0], header=header)
    for line, entry in zip(file.read(), expected):
        assert line == entry


results_delete = [["3", "More Tests"], ["2", "Make Tests"], ["1", "Run Tests"]]


@pytest.mark.parametrize(
    "to_del,expected", [("Make Tests", results_delete[0::2]), ("nothing", results_delete)]
)
def test_Filer_delete_existing_file(
    tmp_file: Callable[[Union[str, None]], Path],
    to_del: str,
    expected: List[List[str]],
    content: str = "3\tMore Tests\n2\tMake Tests\n1\tRun Tests\n",
) -> None:
    """Run Filer to delete a line from  an existing file

    :tmp_path: Where to create temporary file
    :to_del: Line to be deleted, from pyteset.mark.parametrize
    :expected: Expected result, from pytest.mark.parametrize
    :content: Contents of temporary file

    :returns: None

    """
    file = Filer(tmp_file(content))
    file.delete(to_del)
    for line, entry in zip(file.read(), expected):
        assert line == entry
