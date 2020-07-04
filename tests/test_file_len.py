from pathlib import Path

import pytest

from helpers.file_len import file_len


def test_file_len(tmp_path: Path, contents: str = "a\nb\nc\nd\ne\n") -> None:
    """Run helpers.file_len on a file with 5 lines

    :tmp_path: pytest.fixture. Where to create temporary file
    :contents: What to write to temporary file

    :returns: None

    """
    file = tmp_path / "tmp.txt"
    file.write_text(contents)
    assert file_len(file) == 5


def test_file_len_raise_error() -> None:
    """Run helpers.file_len on a file that doesn't exist

    :returns: None

    """
    with pytest.raises(IOError):
        file_len(Path("abc"))
