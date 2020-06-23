import pytest
from typing import List, Union, Callable
from pathlib import Path


@pytest.fixture(scope="function")
def list_of_lists() -> List[List[str]]:
    """Fixture for creating a simple list of lists"""
    return [list("abc"), list("def"), list("ghi")]


@pytest.fixture(scope="function")
def tmp_file(tmp_path: Path) -> Callable[[Union[str, None]], Path]:
    """Fixture for automating setup of files

    By returning a callable, it can be used in situations where 
    the contents of the file need to differe
    
    :tmp_path: pytest.fixture. Where to create the file

    :returns: An instantiated tsv file
    """
    
    def _make_file(content: Union[str, None]) -> Path:
        """Hidden function for initialising files

        :content: What is to be written to the file. Pass None to create empty
        """
        file = tmp_path / "tmp.tsv"
        if content is not None:
            file.write_text(content)
        return file

    return _make_file
