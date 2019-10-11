#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from ToDonePy.counted_list import counted_list as counted_list


def test_counted_list_less_than(
    lines: List[List[str]] = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
    number: int = 2,
    connector: str = " ",
) -> None:
    """Run counted_list with number less than length

    :lines: List containing items to be echoed
    :number: Number of strings to be echoed
    :connector: For pretty printing. What to join entries with

    :returns: None

    """
    result = counted_list(lines, number, connector)
    assert result == ["a b c", "d e f"]

def test_counted_list_greater_than(
    lines: List[List[str]] = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
    number: int = 4,
    connector: str = " ",
) -> None:
    """Run counted_list with number greater than length

    :lines: List containing items to be echoed
    :number: Number of strings to be echoed
    :connector: For pretty printing. What to join entries with

    :returns: None

    """
    result = counted_list(lines, number, connector)
    assert result == ["a b c", "d e f", 'g h i', 'You do not have 4 tasks!']

def test_counted_list_equal_to(
    lines: List[List[str]] = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
    number: int = 3,
    connector: str = " ",
) -> None:
    """Run counted_list with number greater than length

    :lines: List containing items to be echoed
    :number: Number of strings to be echoed
    :connector: For pretty printing. What to join entries with

    :returns: None

    """
    result = counted_list(lines, number, connector)
    assert result == ["a b c", "d e f", 'g h i']
