from typing import Any, Callable, List


def itemsetter(*items: int) -> Callable[[List, Any], None]:
    """Return a callable object that sets item from its operand
    
    This is essentially the opposite of `operator.itemgetter`_.
    If only one position is specified, the resulting callable will set that item.
    If multiple positions are specified, it sets all items

    .. _operator.itemgetter:
        https://docs.python.org/3.7/library/operator.html

    Parameters
    ----------
    *items : int
        The indices to be set. Remember, Python is 0-indexed

    Returns
    -------
    Callable[[List, Any], None]
        A function that will set the indices specified in `items` to a given value.

    Examples
    --------
    >>> x = ['a', 'b', 'c']
    >>> f = itemsetter(2)
    >>> f(x, 'z')
    >>> print(x)
    ['a', 'b', 'z']

    """

    def g(obj: List, *values: Any) -> None:
        for item, value in zip(items, values):
            obj[item] = value

    return g
