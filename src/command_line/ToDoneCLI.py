#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from pathlib import Path

import click

from ToDonePy.counted_echo import counted_echo as counted_echo
from ToDonePy.filer import Filer as Filer


@click.group()
@click.option(
    "--file",
    "-f",
    envvar="TODO_FILE",
    default=(Path.home() / "TODO.tsv"),
    type=click.Path(exists=False),
    help="Location of TODO.tsv",
)
@click.version_option(version="2.0.0")
@click.pass_context
def to(ctx, file: Path) -> None:
    """Base command for managing tasks

    :Note: If you use a location other than the default for --file, 
        I'd recommend setting TODO_FILE as an environemtal variable
    """
    ctx.obj = Filer(Path(file), create=True)


@to.command()
@click.option("--sort", "-s", default="both", help="How to sort added tasks", type=str)
@click.argument("rank", required=True, type=int)
@click.argument("task", required=True, type=str)
@click.pass_obj
def do(obj, sort: str, rank: int, task: str) -> None:
    """Add a task to your list

    :rank: priority to assign to this task
    :task: Task to be added to your list

    :Note: --sort defaults to "both". If must be one of :
    ["rank", "date", "both", "none"]. If none, tasks are not resorted 
    after additions

    :Note: If your task is more than 1 word long, enclose it in quotes

    :Note: A timestamp of the form %y-%m-%d %H:%M:%S is also added

    """
    date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    obj.append([[str(rank), date, task]])
    if sort != "none":
        keys = {"rank": [0], "date": [1], "both": [0, 1]}
        obj.sort(keys[sort])
    click.echo("Task added")


@to.command()
@click.option(
    "--sort", "-s", default="none", help="How to sort returned tasks", type=str
)
@click.option("--number", "-n", default=5, help="How many tasks to return", type=int)
@click.option(
    "--edit/--no-edit", "-e/-E", default=False, help="Open TODO.tsv in your editor"
)
@click.pass_obj
def doing(obj, sort: str, number: int, edit: bool) -> None:
    """See tasks in your list

    :Note: --sort defaults to "none" to preserve order in file.
    It must be one of ["rank", "date", "both", "none"].

    :Note: --no-edit is default, so does not need to be specified for 
        calls where you do NOT want an editor.

    :Note: --edit will over-ride --sort
    """
    if edit:
        click.edit(extension=".tsv", filename=str(obj.path))
    else:
        if sort != "none":
            keys = {"rank": [0], "date": [1], "both": [0, 1]}
            obj.sort(keys[sort])
        counted_echo(obj.read(), number, "\t")


@to.command()
@click.argument("task", required=True)
@click.pass_obj
def done(obj, task: str) -> None:
    """Remove a task to your list

    :task: Task to be removed from your list

    :Note: If multiple tasks match ``task``, they will all be deleted.

    :Note: If your task is more than 1 word long, enclose it in quotes

    """
    obj.delete(task)
    click.echo("Task removed")
