from pathlib import Path

def make_path(tmp_path: Path) -> Path:
    """Helper function to create a pathlib Path object.
    
    :temp_path: Temporary path for pytest
    :returns: Temporary file path for pytest
    
    """
    return (tmp_path / "TODO.csv")

def make_file(tmp_path: Path, content: str = "") -> Path:
    """Helper function to create a temporary file

    :temp_path: Temporary path for pytest
    :contets: Contents to be written to temporary file
    :returns: Temporary file for pytest

    """
    csv = tmp_path / "TODO.csv"
    csv.write_text(content)
    return csv
