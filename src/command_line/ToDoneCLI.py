#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from pathlib import Path

import click

from ToDonePy.filer import Filer as Filer


@click.group()
@click.option(
    "--file",
    "-f",
    envvar="TODO_FILE",
    default=(Path.home() / "TODO.csv"),
    type=click.Path(exists=False),
    help="Location of TODO.csv",
)
@click.version_option(version="1.2.0")
@click.pass_context
def to(ctx, file: Path) -> None:
    """Base command for managing tasks

    :Note: If you use a location other than the default for --file, 
        I'd recommend setting TODO_FILE as an environemtal variable
    """
    ctx.obj = Filer(Path(file), create=True)


@to.command()
@click.argument("task", required=True)
@click.argument("rank", required=True)
@click.pass_obj
def do(obj, task: str, rank: int) -> None:
    """Add a task to your list

    :task: Task to be added to your list
    :rank: priority to assign to this task

    :Note: If your task is more than 1 word long, enclose it in quotes

    :Note: A timestamp of the form %y-%m-%d %H:%M:%S is also added

    """
    date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    obj.append([",".join([str(rank), task, date])])
    click.echo("Task added")


@to.command()
@click.option(
    "--edit/--no-edit", "-e/-E", default=False, help="Open TODO.csv in your editor"
)
@click.pass_obj
def doing(obj, edit: bool) -> None:
    """See tasks in your list

    :Note: --no-edit is default, so does not need to be specified for 
        calls where you do NOT want an editor.
    """
    if edit:
        click.edit(extension=".csv", filename=str(obj.path))
    else:
        for line in obj.read():
            click.echo(line)


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
