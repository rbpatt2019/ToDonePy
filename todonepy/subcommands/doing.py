import argparse
import os

from helpers.external_command import external_command


# file, sort, number, reminder, edit
def doing(args: argparse.Namespace) -> None:
    """See tasks in your list

    Notes
    -----
        `--edit` opens whatever editor is specified by your `EDITOR` env var.
        If one is not set, it will default to Vim. 
    
        Currently, `--reminder` has a dependency on `notify-send`. If this
        command is absent from your system, it will failt

    Parameters
    ----------
    args : argparse.Namespace
        Args passed from argparse. For this subcommand, these include:
    args.file : Filer
        The TODO file to echo. Derived from the root `to` command
    args.sort : Literal['both', 'none', rank', 'date']
        How to sort echoed tasks. Derived from the root `to` command
    args.number : int
        How many tasks to return
    args.reminder : bool
        Whether to use notify-send to create a pop-up
    args.edit : bool
        Whether to laucn an editor with your TODO file

    Returns
    -------
    None

    Example
    -------
    $ to doing -n 3

    """
    keys = {"rank": [1], "date": [2], "both": [1, 2]}
    if args.sort != "none":
        args.file.sort(keys[args.sort], header=True)
        ids = [str(x) for x in range(1, args.file.length)]
        ids.insert(0, "ID")
        args.file.write_col(ids, 0)

    lines = args.file.read()[: args.number + 1]

    if args.edit:
        # print(args.file.path)
        __editor__ = os.environ.get("EDITOR", "vim")
        external_command([__editor__, args.file.path])
    elif args.reminder:
        external_command(
            [
                "notify-send",
                "My TODOs",
                "\n".join(["\t".join(l) for l in lines]),
                "-u",
                "low",
                "-t",
                "5000",
            ]
        )
    else:
        for l in lines:
            print("\t".join(l))
