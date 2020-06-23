#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import pytest

from ToDonePy.counted_list import counted_list as counted_list


@pytest.mark.parametrize(
    "number,output",
    [
        (2, ["a b c", "d e f"]),
        (3, ["a b c", "d e f", "g h i"]),
        (4, ["a b c", "d e f", "g h i", "You do not have 4 tasks!"]),
    ],
)
def test_counted_list_less_than(
    list_of_lists: List[List[str]], number: int, output: List[str],
) -> None:
    """Run counted_list with number less than, equal to, and greater than length

    :list_of_lists: Pytest fixture
    :number: Number of strings to be echoed, from pytest.mark.parametrize
    :output: Expected output, from pytest.mark.parametrize

    :returns: None

    """
    assert counted_list(list_of_lists, number, " ") == output
