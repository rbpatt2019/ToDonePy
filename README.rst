ToDonePY - A basic command-line tast manager
============================================

.. image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active - The project has reached a stable, usable state and is being actively developed
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

.. Note:: This project has only been tested on a Unix OS. I welcome collaborations to test it for MacOS and Windows!

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

The base command ``to``
~~~~~~~~~~~~~~~~~~~~~~~

The base command ``to`` has a few useful features of its own. To see what version of the command you are using, call:

.. code:: sh

        to --version

As with any good command-line tool, you can get some basic help by calling:

.. code:: sh

        to --help

Under the hood, ``to`` creates the context object that holds the information on the file you use for tracking you're TODOs. If you don't specify a file to use, it will default to ``$HOME/TODO.csv``. If you would like to specify a different file to use, than call the command with the ``--file/-f`` flag like so:

.. code:: sh
        
        to --file /path/to/your/TODO.csv subcommand

.. note:: If you plan to use a file other than the default, I recommend setting it by creating the environmental variable, ``TODO_LIST``. 

Regardless of whether you use the default or not, calling ``to`` with any of the subcommands - ``do``, ``doing``, or ``done`` - will check to see if the file exists. If it does exist, ``to`` then pass the path on to the subcommand. If it doesn't exist, then ``to`` creates an empty file which it then passes on to the subcommand.

As a final note, it is worth emphasising that the contex object is only created when ``to`` is invoked with a subcommand. So, after a clean install, calling ``to --help`` or ``to --version`` will NOT create your ``TODO.csv`` file, even if you pass the ``--file/-f`` flag. However, call ``to do``, and it will pop into existence.

.. _to do:

Adding new tasks with ``to do``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To begin tracking your TODOs, call the command as follows:

.. code:: sh

        to do task rank        

``to`` is the base command. It must be invoked to use any part of the tool. The ``do`` subcommand is how you add tasks to your ``TODO.csv``. After ``to do``, there are two mandatory arguments: the ``task`` and the ``rank``. The first argument is ``task``. Here, specify what it is you need to do. If your task takes more than one word to describe, than you need to include it in quotes. ``rank`` should be a number indicating how important this task is. 1 is very important, 2 less so, etc. Though nothing explicitly bans you from using as many ranks as you want, I'd reccomed using 3 for high, medium, and low priority. So, if you wanted to remind yourself to write an abstract for that paper you've been delaying, call:

.. code:: sh
        
        to do 'Write my abstract' 1

This will create ``TODO.csv`` if it doesn't already exist, and add 'Write my abstract' with a rank of one to it.


.. _to doing:

Keeping track of tasks with ``to doing``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you've added some TODOs to your list, you need to make sure you stay on top of them. To see what needs to be done, call:

.. code:: sh

        to doing

This will echo your tasks to the terminal. Sometimes, however, you might want to correct an error, change a priority, or in some way edit yout ``TODO.csv``. In these cases, you can call ``to doing`` in editor mode:

.. code:: sh

        to doing --edit
        
This will open ``TODO.csv`` in your system editor. Where you would seem something like below, if you've been following along:

.. code:: sh

        1,Write my abstract,YYYY-MM-DD HH:MM:SS

Nothing fancy, just a plain csv with ``rank`` in the first column, ``task`` in the second, and the date/time of addition in the third. Now, you can make all the changes you want, then save and close the file to return to the command line.

This call opens the default editor on your system, usually defined by the environmental variable EDITOR for Linux systems. Currently, there is not support to specify a specific editor beside the default.

At the moment, ``to doing`` just lists the tasks in the order you added them. In the future, it will also be able to sort by ``rank``.

.. _to done:

Completing your tasks with ``to done``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the end of a productive work session, you've completed a task from your list. Boom! Time well spent. To remove it from your ``TODO.csv``, call:

.. code:: sh

        to done task

As with `to do`_, if your task is more than one word, you need to enclose it in quotes, like so:

.. code:: sh
        
        to done 'Write my abstract'

Under the hood, ``to done`` creates a temp file, then performs a string match to each line of your ``TODO.csv``. If ''task'' is not in a line, that line is written to the temp file. If ''task'' is in a line, that line is skipped. This way, the temp file ends up containing only those tasks that aren't completed. Once every line is checked, the temp file replaces ``TODO.csv`` with its contents. Task deleted!

.. Warning:: If two different tasks contain the same text, they will both be deleted!

Recent Changes
--------------

Please see the `CHANGELOG <https://github.com/rbpatt2019/ToDonePy/blob/master/CHANGELOG.rst>`_

Next Steps
----------

- Add a sort function for ``to doing`` to all user to return by date or priority
- Graphic notification support for use with cron
- Continue to expand README and doumentation.

Thank Yous
----------

- `Click <https://click.palletsprojects.com/en/7.x/>`_ for making an excellent package with absolutely stellar documentation.
