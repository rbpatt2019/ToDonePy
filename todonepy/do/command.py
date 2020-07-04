from datetime import datetime as dt
from typing import Tuple

import click

from helpers.file_len import file_len


@click.command()
@click.option("--sort", "-s", default="both", help="How to sort added tasks", type=str)
@click.argument("rank", nargs=1, required=True, type=int)
@click.argument("tasks", nargs=-1, required=True, type=str)
@click.pass_obj
def do(obj, sort: str, rank: int, tasks: Tuple[str]) -> None:
    """Add some tasks to your list

    :rank: priority to assign to this task
    :tasks: Task(s) to be added to your list. Supports any number of arguments

    :Note: All tasks will be added at the same rank

    :Note: --sort defaults to "both". If must be one of :
    ["rank", "date", "both", "none"]. If none, tasks are not resorted 
    after additions

    :Note: If your task is more than 1 word long, enclose it in quotes

    :Note: A timestamp of the form %y-%m-%d %H:%M:%S is also added

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
