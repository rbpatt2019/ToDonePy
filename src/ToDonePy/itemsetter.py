from typing import Any, Callable, List


def itemsetter(*items: int) -> Callable[[List, Any], None]:
    """Return a callable object sets item from its operand
    If multiple items are specified, it sets all items

    After:

        >>> x = ['a', 'b', 'c']
        >>> f = itemsetter(2)

    Then:
    
        >>> f(x, 'z')
        >>> print(x)
        ['a', 'b', 'z']

    :items: Indices to be set

    :returns: g, Callable[[List, Any], None]

    """

    def g(obj: List, *values: Any) -> None:
        for item, value in zip(items, values):
            obj[item] = value

    return g
