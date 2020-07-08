"""The `done` subcommand for the `to` main command"""
import argparse


def done(args: argparse.Namespace) -> None:
    """Remove a task to your list

    This command uses the supplied tasks to look for matches in your TODO
    list. A helpful message lets you know if the task(s) was(were) found and deleted.
    
    Note
    ----
        If your task contains more than one word, then each task must be enclosed in
        quotes. Otherwise, the CLI treats each word as a task. Also note that if
        multiple lines match a task, they will ALL be deleted.

    Parameters
    ----------
    args : argparse.Namespace
        Arguments forwarded from the CLI. For this subcommand, this includes:
    args.file : Filer
        The TODO file to be searched. From the root `to` command
    args.task : List[str]
        The list of tasks to be deleted
 
    Returns
    -------
    None
        Though a message will be echoed letting you know if the task(s) was(were)
        deleted successfully.

    Example
    -------
    $ to done 'An example' 'Is always helpful'

    """
    for item in args.tasks:
        if args.file.delete(item):
            ids = [str(x) for x in range(1, args.file.length)]
            ids.insert(0, "ID")
            args.file.write_col(ids, 0)
            print(f'Task "{item}" successfully deleted!')
        else:
            print(f'Task "{item}" not in TODOs...')
