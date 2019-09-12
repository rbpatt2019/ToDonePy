#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name", help="The persion to greet.")
def hello(count: int, name: str) -> None:
    """Greet the nice person NAME COUNT times

    :param count: Number of greetings
    :param name: The person to greet
    :note: This is taken directly from the homepage of the Click package and is intended as an example
            Please visit their site at https://click.palletprojects.com/en/7.x/
    """
    for _ in range(count):
        click.echo(f"Hello {name}!")
