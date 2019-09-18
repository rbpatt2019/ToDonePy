#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from pathlib import Path


@click.group()
@click.version_option(version="0.2.1")
@click.option("--file", "-f", default=Path.home() / "TODO.csv")
def to(file) -> None:
    """Base command for managing tasks

    :param file: Location of TODO.csv. Defaults to $HOME/TODO.csv
    :note: If you use a location other than the default for --file, 
        I'd recommend an alias so as to avoid typing it every time
    """
    click.echo(f"Hello {name}!")


@to.command()
def do():
    """Add a task to your list

    :arg1: TODO
    :returns: TODO

    """
