import pytest
from typing import List, Union, Callable
from pathlib import Path


@pytest.fixture(scope="function")
def list_of_lists() -> List[List[str]]:
    """Fixture for creating a simple list of lists"""
    return [list("abc"), list("def"), list("ghi")]


@pytest.fixture(scope="function")
def tmp_file(tmp_path: Path) -> Path:
    """Fixture for automating setup of files

    :tmp_path: pytest.fixture. Where to create the file

    :returns: An instantiated tsv file
    """

    tmp = tmp_path / "tmp.tsv"
    tmp.write_text(
        "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56:00\tOld task\n"
        "2\t1\t2019-09-24 12:57:00\tNew task\n"
    )
    return tmp
