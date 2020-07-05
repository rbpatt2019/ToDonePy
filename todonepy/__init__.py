#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
import os

import poetry_version

from do.command import do
from doing.command import doing
from done.command import done
from helpers.filer import Filer

__version__ = poetry_version.extract(source_file=__file__)
__todo__ = os.environ.get("TODO_FILE", Path.home() / ".todo.tsv")

# The root command
to = argparse.ArgumentParser(prog="to")
to.add_argument(
    "--version",
    "-v",
    action="version",
    version=f"ToDonePy v{__version__}",
    help="Display the version and exit",
)
to.add_argument(
    "--file",
    "-f",
    default=__todo__,
    type=argparse.FileType("w"),
    help="Your TODO file",
)
to_sub = to.add_subparsers(help='Sub-commands')

# The do Sub-command

if __name__ == "__main__":
    args = to.parse_args()
    print(args)
