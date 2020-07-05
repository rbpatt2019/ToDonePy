#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
import os

import poetry_version

from subcommands.do import do
from subcommands.doing import doing
from subcommands.done import done
from helpers.filer import Filer

__version__ = poetry_version.extract(source_file=__file__)
__todo__ = Filer(os.environ.get("TODO_FILE", Path.home() / ".todo.tsv"), create=True)

# The root command
to_parser = argparse.ArgumentParser(prog="to")
to_parser.add_argument(
    "--version",
    "-v",
    action="version",
    version=f"ToDonePy v{__version__}",
    help="Display the version and exit",
)
to_parser.add_argument(
    "--file", "-f", default=__todo__, type=Filer, help="Your TODO file",
)
subparsers = to_parser.add_subparsers(title="Sub-Commands")

# The done Sub-command
done_parser = subparsers.add_parser("done", help="Remove a completed task")
done_parser.add_argument(
    "tasks",
    type=str,
    nargs="*",
    help="The tasks to be deleted. Each task should be in quotes",
)
done_parser.set_defaults(func=done)

if __name__ == "__main__":
    args = to_parser.parse_args()
    args.func(args)
