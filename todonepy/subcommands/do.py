import argparse
from datetime import datetime as dt

from helpers.filer import Filer


def do(args: argparse.Namespace) -> None:
    """Add some tasks to your list

    `do` supports an unlimited number of tasks, but requires that tasks of more than 1
    word in length be enclosed in quotes. Single or double are fine - use whichever!
    To keep track of how long tasks have been on the list,  a timestamp of the form
    %y-%m-%d %H:%M is also added.

    Notes
    -----
        All tasks added at the same time will be added at the same rank. If you need to
        add multiple tasks at different ranks, you must call `to do` multiple times.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments forwarded from the CLI. For this subcommand, this includes:
    args.file : Filer
        The TODO file to add to. From the root `to` command
    args.rank : int
        The importance to assign the new tasks.
    args.sort : Literal["rank", "date", "both", "none"]
        How to sort new tasks added to the list. From the root `to` command
    args.tasks : List[str]
        The task(s) to add to your list

    Returns
    -------
    None
        However, a confirmation message will be echoed to the terminal

    Examples
    --------
    $ to -s rank do 2 "An example task" "I'm very busy"

    """
    date = dt.now().strftime("%Y-%m-%d %H:%M")
    args.file.append([["", str(args.rank), date, item] for item in args.tasks])
    if args.sort != "none":
        keys = {"rank": [1], "date": [2], "both": [1, 2]}
        args.file.sort(keys[args.sort], header=True)
    ids = [str(x) for x in range(1, args.file.length)]
    ids.insert(0, "ID")
    args.file.write_col(ids, 0)
    print(f"{len(args.tasks)} task(s) added!")
