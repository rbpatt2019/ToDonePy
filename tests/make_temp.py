from pathlib import Path

def make_path(tmp_path: Path) -> str:
    """Helper function to create a pathlib Path object."""
    csv = tmp_path / "TODO.csv"
    return csv.as_posix()

def make_file(tmp_path: Path, content: str = "") -> str:
    """Helper function to create a temporary file"""
    csv = tmp_path / "TODO.csv"
    csv.write_text(content)
    return csv.as_posix()
