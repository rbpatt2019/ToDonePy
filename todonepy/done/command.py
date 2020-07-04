from typing import Tuple

import click

from todonepy.helpers.file_len import file_len


@click.command()
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
