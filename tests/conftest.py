# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict

import pytest
from helpers.filer import Filer


@pytest.fixture(autouse=True)
def doctest_filer_example(doctest_namespace: Dict[str, Filer], tmp_path: Path) -> None:
    """Fixture for instantiating an example Filer for use in doctests

    Parameters
    ----------
    doctest_namespace : Dict[str, Filer]
        `pytest.fixture` holding variables to be used in doctests
    tmp_path : Path
        `pytest.fixture` containing a temporary file path

    Returns
    -------
    None

    """
    doctest_namespace["example"] = Filer(tmp_path / ".TODO.tsv", create=True)


@pytest.fixture(scope="function")
def tmp_file(tmp_path: Path) -> Filer:
    """Fixture for automating setup of files

    Parameters
    ----------
    tmp_path : Path
        pytest.fixture. Where to create the file

    Returns
    -------
    Path
        An instantiated tsv file

    """

    tmp = tmp_path / "tmp.tsv"
    tmp.write_text(
        "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56\tOld task\n"
        "2\t1\t2019-09-24 12:57\tNew task\n"
    )
    return Filer(tmp)
