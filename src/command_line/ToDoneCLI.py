#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from pathlib import Path
from typing import Tuple

import click

from ToDonePy.counted_list import counted_list as counted_list
from ToDonePy.file_len import file_len as file_len
from ToDonePy.filer import Filer as Filer
from ToDonePy.notify import notify_send as notify_send


@click.group()
@click.option(
    "--file",
    "-f",
    envvar="TODO_FILE",
    default=(Path.home() / "TODO.tsv"),
    type=click.Path(exists=False),
    help="Location of TODO.tsv",
)
@click.version_option()
@click.pass_context
def to(ctx, file: Path) -> None:
    """Base command for managing tasks

    :Note: If you use a location other than the default for --file, 
        I'd recommend setting TODO_FILE as an environemtal variable
    """
    ctx.obj = Filer(Path(file), create=True)


@to.command()
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


@to.command()
@click.option(
    "--sort", "-s", default="none", help="How to sort returned tasks", type=str
)
@click.option("--number", "-n", default=5, help="How many tasks to return", type=int)
@click.option(
    "--graphic/--no-graphic",
    "-g/-G",
    default=False,
    help="Send a graphic remider instead of echoing to the terminal",
)
@click.option(
    "--edit/--no-edit", "-e/-E", default=False, help="Open TODO.tsv in your editor"
)
@click.pass_obj
def doing(obj, number: int, graphic: bool, edit: bool, sort: str = "none") -> None:
    """See tasks in your list

    :Note: --sort defaults to "none" to preserve order in file.
    It must be one of ["rank", "date", "both", "none"].

    :Note: --sort calls before --graphic or --editor

    :Note: --graphic has a dependency on notify-send and is Linux/Mac Specific

    :Note: --no-edit is default, so does not need to be specified for 
        calls where you do NOT want an editor.

    """
    keys = {"rank": [1], "date": [2], "both": [1, 2]}
    if sort != "none":
        obj.sort(keys[sort], header=True)
        ids = [str(x) for x in range(1, file_len(obj.path))]
        ids.insert(0, "ID")
        obj.write_col(ids, 0)
    if edit:
        click.edit(extension=".tsv", filename=str(obj.path))
    elif graphic:  # number + 1 accounts for header
        lines = obj.read()
        notify_send(
            "My TODOs",
            "\n".join(
                counted_list(lines[0], 1, "\t") + counted_list(lines[1:], number, "\t")
            ),
            "low",
            5000,
        )
    else:
        lines = obj.read()
        click.echo("\t".join(lines[0]))
        for task in counted_list(lines[1:], number, "\t"):
            click.echo(task)


@to.command()
@click.argument("tasks", nargs=-1, required=True, type=str)
@click.pass_obj
def done(obj, tasks: Tuple[str]) -> None:
    """Remove a task to your list

    :tasks: Task(s) to be added to your list. Supports any number of arguments

    :Note: If multiple lines match an of the ``tasks``, they will all be deleted.

    :Note: If your task is more than 1 word long, enclose it in quotes

    :Note: If a task is not found, then the CLI will say so

    """
    for item in tasks:
        if obj.delete(item):
            ids = [str(x) for x in range(1, file_len(obj.path))]
            ids.insert(0, "ID")
            obj.write_col(ids, 0)
            click.echo(f'Task "{item}" successfully deleted!')
        else:
            click.echo(f'Task "{item}" not in TODO.tsv...')
