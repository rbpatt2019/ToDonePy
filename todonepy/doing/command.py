import click
from helpers.file_len import file_len
from helpers.notify import notify_send

@click.command()
@click.option(
    "--sort", "-s", default="none", help="How to sort returned tasks", type=str
)
@click.option("--number", "-n", default=5, help="How many tasks to return", type=int)
@click.option(
    "--graphic/--no-graphic",
    "-g/-G",
    default=False,
    help="Send a graphic remider instead of echoing to the terminal",
)
@click.option(
    "--edit/--no-edit", "-e/-E", default=False, help="Open TODO.tsv in your editor"
)
@click.pass_obj
def doing(obj, number: int, graphic: bool, edit: bool, sort: str = "none") -> None:
    """See tasks in your list

    :Note: --sort defaults to "none" to preserve order in file.
    It must be one of ["rank", "date", "both", "none"].

    :Note: --sort calls before --graphic or --editor

    :Note: --graphic has a dependency on notify-send and is Linux/Mac Specific

    :Note: --no-edit is default, so does not need to be specified for 
        calls where you do NOT want an editor.

    """
    keys = {"rank": [1], "date": [2], "both": [1, 2]}
    if sort != "none":
        obj.sort(keys[sort], header=True)
        ids = [str(x) for x in range(1, file_len(obj.path))]
        ids.insert(0, "ID")
        obj.write_col(ids, 0)

    lines = obj.read()[:number]

    if edit:
        click.edit(extension=".tsv", filename=str(obj.path))
    elif graphic:  # number + 1 accounts for header
        notify_send(
            "My TODOs", "\n".join(["\t".join(l) for l in lines]), "low", 5000,
        )
    else:
        for l in lines:
            click.echo("\t".join(l))
