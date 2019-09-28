from typing import List

import click


def counted_echo(lines: List[List[str]], number: int, connector: str) -> None:
    """Safely iterate over lists of unknown length

    For use in click applications

    :lines: List containing items to be echoed
    :number: Number of strings to be echoed
    :connector: For pretty printing. What to join entries with

    :returns: None

    """
    for i in range(number):
        try:
            click.echo(connector.join(lines[i]))
        except IndexError:
            click.echo(f"You don't have {number} tasks!")
            break
