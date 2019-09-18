#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from ToDonePy.filer import Filer as Filer
import click


@click.group()
@click.option("--file", "-f", envvar='TODO_FILE', default=Path.home())
@click.version_option(version="0.2.1")
@click.pass_context
def to(ctx, file: Path) -> None:
    """Base command for managing tasks

    :param file: Location of TODO.csv. Defaults to $HOME/TODO.csv

    :note: If you use a location other than the default for --file, 
        I'd recommend an alias so as to avoid typing it every time
    """
    ctx.obj = Filer(file / "TODO.csv", create=True)


@to.command()
@click.argument('task')
@click.argument('rank')
@click.pass_obj
def do(obj, task: str, rank: int) -> None:
    """Add a task to your list

    :param task: Task to be added to your list
    :param rank: Priority to assign to this task

    """
    obj.write('.'.join([str(rank), task]))
    click.echo('successful test')
