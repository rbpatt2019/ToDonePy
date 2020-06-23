import pytest
from typing import List
from pathlib import Path


@pytest.fixture(scope="function")
def list_of_lists() -> List[List[str]]:
    """Fixture for creating a simple list of lists"""
    return [list("abc"), list("def"), list("ghi")]
