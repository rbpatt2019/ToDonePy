ToDonePY - A basic command-line tast manager
============================================

.. image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: GPLv3 License
   
.. image:: https://img.shields.io/pypi/v/todonepy
   :target: https://pypi.org/project/todonepy
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/todonepy
   :target: https://pypi.org/project/todonepy
   :alt: PyPI - Python Versions

.. image:: https://travis-ci.org/rbpatt2019/ToDonePy.svg?branch=master
   :target: https://travis-ci.org/rbpatt2019/ToDonePy
   :alt: Build Status
   
.. image:: https://readthedocs.org/projects/todonepy/badge/?version=latest
   :target: https://todonepy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   
.. image:: https://codecov.io/gh/rbpatt2019/ToDonePy/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rbpatt2019/ToDonePy
   :alt: Code Coverage

.. image:: https://pyup.io/repos/github/rbpatt2019/ToDonePy/shield.svg
     :target: https://pyup.io/repos/github/rbpatt2019/ToDonePy/
     :alt: Updates

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Codestyle: Black

Introduction
------------

Move your ToDo's to ToDone's!

`ToDonePy <https://github.com/rbpatt2019/ToDonePy/>`_ is a command-line interface for managing your to do list. It provides a root command, `to`_, and three subcommands:

- `to do`_ adds a new task to your list at different priorities.
- `to doing`_ shows you what you should be doing.
- `to done`_ removes a completed tast from your list.

Docs and Code
-------------

The documentation lives at https://ToDonePy.readthedocs.io/ .

The code lives at https://github.com/rbpatt2019/ToDonePy/ .

Installation
------------

This project has been released on `PyPI <https://pypi.org>`_, so it can be installed with `pip`:

.. code:: sh

        pip install -U ToDonePy

Alternatively, you can install the project manually by cloning the  `repo <https://github.com/rbpatt2019/ToDonePy>`_, and using the included Makefile.

.. code:: sh

    git clone https://github.com/rbpatt2019/ToDonePy/
    make install
    
If you would like to contribute to development, the install instructions are slightly different. Please see the section on `contributing <https://todonepy.readthedocs.io/en/latest/contributing.html#contributing>`_.

Usage
-----

.. _to:

The base command `to`
~~~~~~~~~~~~~~~~~~~~~

The base command `to` has a few useful features of its own. To see what version of the command you are using, call:

.. code:: sh

        to --version

As with any good command-line tool, you can get some basic help by calling:

.. code:: sh

        to --help

You can get help on any subcommand by calling `--help` after that subcommand. For example, to get help with `to doing`, call:

.. code:: sh

        to doing --help

Under the hood, `to` creates a Filer object that holds the information on the file you use for tracking you're TODOs. If you don't specify a file to use, it will default to `$HOME/.TODO.tsv`. If you would like to specify a different file to use, than call the command with the `--file/-f` flag like so:

.. code:: sh
        
        to --file /path/to/your/TODO.tsv subcommand

.. note:: If you plan to use a file other than the default, I recommend setting it by creating the environmental variable, `TODO_LIST`. 

Regardless of whether you use the default or not, calling `to` with any of the subcommands - `do`, `doing`, or `done` - will check to see if the file exists. If it does exist, `to` then pass the path on to the subcommand. If it doesn't exist, then `to` creates an empty file which it then passes on to the subcommand.

As a final note, it is worth emphasising that the contex object is only created when `to` is invoked with a subcommand. So, after a clean install, calling `to --help` or `to --version` will NOT create your `TODO.tsv` file, even if you pass the `--file/-f` flag. However, call `to do`, and it will pop into existence.

.. _to do:

Adding new tasks with `to do`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To begin tracking your TODOs, call the command as follows:

.. code:: sh

        to do rank tasks

`to` is the base command. It must be invoked to use any part of the tool. The `do` subcommand is how you add tasks to your `TODO.tsv`. After `to do`, there are two mandatory arguments: `rank` and `tasks`. The first argument is `rank`. `rank` should be a number indicating how important this task is. 1 is very important, 2 less so, etc. Though nothing explicitly bans you from using as many ranks as you want, I would reccomed using 3 for high, medium, and low priority. 

The second argument is `tasks`. Here, specify what it is you need to do. If your task takes more than one word to describe, then you need to include it in quotes. `tasks` supports an indefinite number of arguments, from 1 to as many as you want. 

.. note:: All tasks specified will be added at the same rank, so only combine tasks you want to give the same priority.

So, if you wanted to remind yourself to write an abstract for that paper you have been delaying and to email your boss, call:

.. code:: sh
        
        to do 1 'Write my abstract' 'Email boss'

This will create `TODO.tsv` if it does not already exist, and add 'Write my abstract' and 'Email boss', both with a rank of one, to `TODO.tsv`. `to do` also logs the date and time the task was added, so that you always know how old a task is.

Sometimes, you want to sort your tasks as you add them. You can do that with the `--sort/-s` option. This specifies how to sort your list after a new task is added. It must be one of: `[rank, date, both, none]`. `both` sorts by rank and then date, and `none` does not sort, simply appending tasks to the end of your list. It defaults to `none`, on the grounds its better not to do something unless you ask. `Explicit is better than implicit <https://www.python.org/dev/peps/pep-0020/>`_, as they say. If you just wanted to sort by date after adding a new task, then you could call:

.. code:: sh

        to --sort do date 1 'Important work'

.. note:: `--sort` follows the root command `to` as it directly impacts the file and is an option accessible to all subcommands.


.. _to doing:

Keeping track of tasks with `to doing`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have added some TODOs to your list, you need to make sure you stay on top of them. To see what needs to be done, call:

.. code:: sh

        to doing

This should echo the 5 tasks at the top of your `TODO.tsv` to the terminal.

You can specify how to sort your tasks by passing the `--sort/-s` flag with one of: `[rank, date, both, none]`. It defaults to `none`, thus preserving the order in your `TODO.tsv`. Any call to sort will also change the order currently in your `TODO.tsv`, not just the order they are echoed.

Also, specifying the `--number/-n` flag will let you change how many tasks are returned, and it defaults to 5. So, if you want to return 3 tasks sorted by rank, call:

.. code:: sh
        
        to -s rank doing -n 3

.. note:: Remember, `-s` is a root command option!

Maybe you prefer a graphic reminder instead of echoing in the terminal - I find this useful for spawning reminders while I am coding in VIM. `ToDonePy` has that covered, too! Just call:

.. code:: sh
        
        to doing --reminder

to trigger a notification window. By default, it stays up for 5 seconds. Currently, you can not set the time, though that's in the works!

.. Note:: The graphic flag makes a system call to `notify-send`. If you don't have that installed, the command will fail. It should be installed on most Linux systems, though.

Sometimes, you might want to correct an error, change a priority, or in some way edit yout `TODO.tsv`. In these cases, you can call `to doing` in editor mode:

.. code:: sh

        to doing --edit
        
This will open `TODO.tsv` in your system editor. Where you would see something like below, if you have been following along:

.. code:: sh

        ID      Rank    Date    Task
        1       1       YYYY-MM-DD HH:MM     Write my abstract
        2       1       YYYY-MM-DD HH:MM     Email boss
        3       1       YYYY-MM-DD HH:MM     Important work

Nothing fancy, just a plain tsv with `ID` in the first column, `rank` in the second column, the date/time of addition in the third, and `task` in the fourth. Now, you can make all the changes you want, then save and close the file to return to the command line.

Calling `--edit` will trump any calls to `sort` or `number` made in the same command.      

This call opens the default editor on your system, usually defined by the environmental variable EDITOR for Linux systems. If this variable is undefined, then it defaults to VIM - which should be your choice anyways! :P If that command is not found, then it will thros an OSError.


.. _to done:

Completing your tasks with `to done`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the end of a productive work session, you have completed a task from your list. Boom! Time well spent. To remove it from your `TODO.tsv`, call:

.. code:: sh

        to done tasks

As with `to do`_, `to done` suports an indefinite number of tasks, as long as all multi-word tasks are enclosed in quotes. For example, if you emailed your boss that finished abstract, then you can remove those tasks like so:

.. code:: sh
        
        to done 'Write my abstract' 'Email boss'

If `to done` finds these tasks in your `TODO.tsv`, it'll remove them! If it can't find the tasks, it will print a message saying which ones couldn't be removed.

Under the hood, `to done` creates a temp file, then performs a string match to each line of your `TODO.tsv`. If a perfect match to ''task'' is not in a line, that line is written to the temp file. If ''task'' is in a line, that line is skipped. This way, the temp file ends up containing only those tasks that aren't completed. Once every line is checked, the temp file replaces `TODO.tsv` with its contents. Task deleted!

.. Warning:: If two different tasks contain the same text, they will both be deleted!

Known Bugs
----------
- Test hang when testing 

Recent Changes
--------------

Please see the `CHANGELOG <https://github.com/rbpatt2019/ToDonePy/blob/master/CHANGELOG.rst>`_

Next Steps
----------

- Addition of TODOs from file parsing
- Support removal of tasks by task ID number
- Full, OS-independent graphic interface

