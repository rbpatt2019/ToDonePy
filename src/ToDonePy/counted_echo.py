from typing import Generator

import click

from ToDonePy.filer import Filer as Filer


def counted_echo(lines: Generator[str, None, None], number: int) -> None:
    """Safely iterate over generators of unknown length

    For use in click applications

    :lines: Generator containing strings to be echoed
    :number: Number of strings to be echoed

    :returns: None

    """
    for _ in lines:
        try:
            click.echo(next(lines))
        except StopIteration as stop:
            click.echo(f"You don't have {number} tasks!")
            break
