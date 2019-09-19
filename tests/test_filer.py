#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from pathlib import Path
from typing import List

import pytest

from ToDonePy.filer import Filer as Filer
from tests.make_temp import make_file, make_path


def test_Filer_no_create(tmp_path: Path) -> None:
    """Run Filer to read a file that does not exist

    :tmp_path: Where to create temporary file
    :returns: None

    """
    with pytest.raises(OSError):
        file = Filer(make_path(tmp_path), create=False)


def test_Filer_read_new_file(tmp_path: Path) -> None:
    """Run Filer to read and create a new file

    :tmp_path: Where to create temporary file
    :returns: None

    """
    file = Filer(make_path(tmp_path), create=True)
    assert isfile(make_path(tmp_path))


def test_Filer_read_existing_file(
    tmp_path: Path, content: str = "1,Make Tests\n2,Run Tests"
) -> None:
    """Run Filer to read an existing file

    :tmp_path: Where to create temporary file
    :content: Contents of temporary file
    :returns: None

    """
    file = Filer(make_file(tmp_path, content))
    for line, entry in zip(file.read(), content.rsplit("\n")):
        assert line == entry


def test_Filer_write_existing_file(
    tmp_path: Path,
    content: str = "1,Make Tests\n2,Run Tests",
    new_contents: List[str] = ["3,More tests", "4,Most tests"],
) -> None:
    """Run Filer to write to an existing file

    :tmp_path: Where to create temporary file
    :content: Contents of temporary file
    :new_contents: Contents to be written to file
    :returns: None

    """
    file = Filer(make_file(tmp_path, content))
    file.write(new_contents)
    for line, entry in zip(file.read(), new_contents):
        assert line == entry


def test_Filer_append_existing_file(
    tmp_path: Path,
    content: str = "1,Make Tests\n2,Run Tests\n",
    new_contents: List[str] = ["3,More tests", "4,Most tests"],
) -> None:
    """Run Filer to append to an existing file

    :tmp_path: Where to create temporary file
    :content: Contents of temporary file
    :new_contents: Contents to be added to file
    :returns: None

    """
    file = Filer(make_file(tmp_path, content))
    file.append(new_contents)
    # Slice in next line drops empty string created by rsplit
    for line, entry in zip(file.read(), content.rsplit("\n")[:2] + new_contents):
        assert line == entry
