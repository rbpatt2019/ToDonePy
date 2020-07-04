#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

import click

from todonepy.do.command import do
from todonepy.doing.command import doing
from todonepy.done.command import done
from todonepy.helpers.filer import Filer


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


# Add sub-commands
to.add_command(do)
to.add_command(doing)
to.add_command(done)
