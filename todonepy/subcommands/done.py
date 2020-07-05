from helpers.file_len import file_len


def done(args) -> None:
    """Remove a task to your list

    :tasks: Task(s) to be added to your list. Supports any number of arguments

    :Note: If multiple lines match an of the ``tasks``, they will all be deleted.

    :Note: If your task is more than 1 word long, enclose it in quotes

    :Note: If a task is not found, then the CLI will say so

    """
    for item in args.tasks:
        if args.file.delete(item):
            ids = [str(x) for x in range(1, file_len(args.file.path))]
            ids.insert(0, "ID")
            args.file.write_col(ids, 0)
            print(f'Task "{item}" successfully deleted!')
        else:
            print(f'Task "{item}" not in TODOs...')
