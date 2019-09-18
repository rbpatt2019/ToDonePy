from pathlib import Path

def make_path(tmp_path: Path) -> Path:
    """Helper function to create a pathlib Path object."""
    return (tmp_path / "TODO.csv")

def make_file(tmp_path: Path, content: str = "") -> Path:
    """Helper function to create a temporary file"""
    csv = tmp_path / "TODO.csv"
    csv.write_text(content)
    return csv
