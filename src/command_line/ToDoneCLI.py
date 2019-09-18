#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
)
@click.version_option(version="0.2.1")
@click.pass_context
def to(ctx, file: Path) -> None:
    """Base command for managing tasks

    :param file: Location of TODO.csv. Defaults to $HOME/TODO.csv

    :note: If you use a location other than the default for --file, 
        I'd recommend setting TODO_FILE as an environemtal variable
    """
    ctx.obj = Filer(file, create=True)


@to.command()
@click.argument("task", required=True)
@click.argument("rank", required=True)
@click.pass_obj
def do(obj, task: str, rank: int) -> None:
    """Add a task to your list

    :param task: Task to be added to your list
    :param rank: Priority to assign to this task

    """
    obj.append([",".join([str(rank), task])])
    click.echo("Task added")
