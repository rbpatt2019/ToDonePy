import pytest
from pathlib import Path
from ToDonePy.file_len import file_len as file_len
from tests.make_temp import make_file

def test_file_len(tmp_path: Path, contents: str = 'a\nb\nc\nd\ne\n') -> None:
    """Run ToDonePy.file_len on a file with 5 lines

    :tmp_path: Where to create temporary file
    :contents: What to write to temporary file

    :returns: None

    """
    file = make_file(tmp_path, contents)
    result = file_len(file)
    assert  result == 5
    
def test_file_len_raise_error() -> None:
    """Run ToDonePy.file_len on a file that doesn't exist

    :returns: None

    """
    with pytest.raises(IOError):
        file_len(Path('abc'))
    
