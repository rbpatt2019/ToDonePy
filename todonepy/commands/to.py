"""The root `to` command

The root command provides several options. 

`-s/--sort` allows you to specify how to sort added or returned tasks. Bear in mind
that this sorts the underlying file! It defaults to 'none' - best not to do anything
unless you need to!

`-f/file` allows you to specify where to store your TODOs. If you don't specify, it
defaults to `~/.todo.tsv` and will create the file if it doesn't exists. If you want
to keep your file elsewhere, you can specify that with the env var TODO_FILE

Like all good CLIs, `-v/--version` returns the version while `-h/--help` help for the
root command. Help for the subcommands can be found by calling `-h` after a subcommand,
like this: `to do -h`.

Attributes
----------
__version__ : str
    The version number, pulled from the pyproject.toml file
__todo__ : Filer
    The Filer object containing the TODOs. It first checks to see if the env var
    TODO_FILE is set. If it is, it looks there. If not, it defaults to ~/.todo.tsv.
    A hidden file is used to prevent clutter.
"""
import argparse
import os
from pathlib import Path
from typing import Optional

import poetry_version

from helpers.filer import Filer
from subcommands.do import do
from subcommands.doing import doing
from subcommands.done import done

__version__ = poetry_version.extract(source_file=__file__)
__todo__ = Filer(os.environ.get("TODO_FILE", Path.home() / ".todo.tsv"), create=True)

# The root command
to_parser = argparse.ArgumentParser(prog="to")
to_parser.add_argument(
    "-v",
    "--version",
    action="version",
    version=f"ToDonePy v{__version__}",
    help="Display the version and exit",
)
to_parser.add_argument(
    "-f", "--file", default=__todo__, type=Filer, help="Your TODO file",
)
to_parser.add_argument(
    "-s",
    "--sort",
    type=str,
    choices=["both", "none", "rank", "date"],
    default="none",
    help="How to sort TODOs",
)
subparsers = to_parser.add_subparsers(title="Sub-Commands")

# The do sub-command
do_parser = subparsers.add_parser("do", help="Add a new task")
do_parser.add_argument("rank", type=int, help="Importance of added tasks")
do_parser.add_argument(
    "tasks", type=str, nargs="*", help="Tasks to add. Each task should be in quotes"
)
do_parser.set_defaults(func=do)

# The doing sub-command
doing_parser = subparsers.add_parser("doing", help="See your current tasks")
doing_parser.add_argument(
    "-n", "--number", type=int, default=5, help="How many tasks to return"
)
doing_parser.add_argument(
    "-e",
    "--edit",
    nargs="?",
    type=bool,
    default=False,
    const=True,
    help="Launch TODO file in editor",
)
doing_parser.add_argument(
    "-r",
    "--reminder",
    nargs="?",
    type=bool,
    default=False,
    const=True,
    help="Whether to use a pop-up reminder",
)
doing_parser.set_defaults(func=doing)

# The done Sub-command
done_parser = subparsers.add_parser("done", help="Remove a completed task")
done_parser.add_argument(
    "tasks",
    type=str,
    nargs="*",
    help="The tasks to be deleted. Each task should be in quotes",
)
done_parser.set_defaults(func=done)
