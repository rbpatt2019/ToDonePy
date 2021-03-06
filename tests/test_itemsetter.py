# -*- coding: utf-8 -*-
from helpers.itemsetter import itemsetter


def test_itemsetter() -> None:
    """Test itemsetter with basic inputs

    :returns: None

    """

    x = list("abc")
    f = itemsetter(2)
    f(x, "z")
    assert x == ["a", "b", "z"]
