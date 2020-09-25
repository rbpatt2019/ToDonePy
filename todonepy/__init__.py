#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from typing import Optional

from commands.to import to_parser


def to(args: Optional[argparse.Namespace] = None) -> None:
    """The entry point for the CLI

    Parameters
    ----------
    args : Optional[argparse.Namespace]
        If not specified, then the command line inputs are read. This should be the default behaviour.
        The option to specify is only given to allow for testing.

    Returns
    -------
    None
    """
    if args is None:
        args = to_parser.parse_args()
    args.func(args)
