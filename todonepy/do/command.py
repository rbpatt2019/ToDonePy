from datetime import datetime as dt
from typing import Tuple

import click
from typing_extensions import Literal

from helpers.file_len import file_len
from helpers.filer import Filer


@click.command()
@click.option("--sort", "-s", default="both", help="How to sort added tasks", type=str)
@click.argument("rank", nargs=1, required=True, type=int)
@click.argument("tasks", nargs=-1, required=True, type=str)
@click.pass_obj
def do(
    obj: Filer,
    sort: Literal["rank", "date", "both", "none"],
    rank: int,
    tasks: Tuple[str],
) -> None:
    """Add some tasks to your list

    `do` supports an unlimited number of tasks, but requires that tasks of more than 1
    word in length be enclosed in quotes. Single or double are fine - use whichever!
    To keep track of how long tasks have been on the list,  a timestamp of the form
    %y-%m-%d %H:%M:%S is also added.

    Notes
    -----
        All tasks added at the same time will be added at the same rank. If you need to
        add multiple tasks at different ranks, you must call `to do` multiple times.

    Parameters
    ----------
    obj : Filer
        The click context object that points to TODO.tsv
    sort : Literal["rank", "date", "both", "none"]
        How to sort new tasks added to the list
        Click will default this to "both"
    rank : int
        The importance to assign the new tasks.
    tasks : Tuple[str]
        The task(s) to add to your list

    Returns
    -------
    None
        However, a confirmation message will be echoed to the terminal

    Examples
    --------
    >>> to do -s rank 2 "An example task"

    """
    date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    obj.append([["", str(rank), date, item] for item in tasks])
    if sort != "none":
        keys = {"rank": [1], "date": [2], "both": [1, 2]}
        obj.sort(keys[sort], header=True)
    ids = [str(x) for x in range(1, file_len(obj.path))]
    ids.insert(0, "ID")
    obj.write_col(ids, 0)
    click.echo(f"{len(tasks)} task(s) added!")
