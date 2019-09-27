from typing import Generator

import click


def counted_echo(lines: Generator[str, None, None], number: int) -> None:
    """Safely iterate over generators of unknown length

    For use in click applications

    :lines: Generator containing strings to be echoed
    :number: Number of strings to be echoed

    :returns: None

    """
    for _ in range(number):
        try:
            click.echo(next(lines))
        except StopIteration:
            click.echo(f"You don't have {number} tasks!")
            break
