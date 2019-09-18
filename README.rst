ToDonePY - A basic command-line tast manager
============================================

.. image:: https://www.repostatus.org/badges/latest/wip.svg
   :alt: Project Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
   :target: https://www.repostatus.org/#wip
   
.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: GPLv3 License
   
.. image:: https://codecov.io/gh/rbpatt2019/ToDonePy/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rbpatt2019/ToDonePy
   :alt: Code Coverage

.. image:: https://travis-ci.org/rbpatt2019/ToDonePy.svg?branch=master
   :target: https://travis-ci.org/rbpatt2019/ToDonePy
   :alt: Build Status
   
.. image:: https://readthedocs.org/projects/todonepy/badge/?version=latest
   :target: https://todonepy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   
.. image:: https://pyup.io/repos/github/rbpatt2019/ToDonePy/shield.svg
   :target: https://pyup.io/repos/github/rbpatt2019/ToDonePy/
   :alt: Updates
     
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Codestyle: Black

Note
----

.. Warning:: This project is in early development and is not yet released. Feel free to check back for updates, but do not use yet - unless you want to contribute to development.

Introduction
------------

Move your ToDo's to ToDone's!

.. Note:: This project has only been test on a Unix OS. I welcome collaborations to test it for MacOS and Windows!

`ToDonePy <https://github.com/rbpatt2019/ToDonePy/>`_ is a command-line interface for managing your to do list. It provides a root command, `to`_, and three subcommands:

- `to do`_ adds a new task to your list at either 'low', 'med', or 'high' priority.
- `to doing`_ doing` shows you what you should be doing.
- `to done`_ removes a completed tast from your list.

Docs and Code
-------------

The documentation lives at https://ToDonePy.readthedocs.io/ .

The code lives at https://github.com/rbpatt2019/ToDonePy/ .

Installation
------------

This project is not yet released on PyPi.

You can install the project manually by cloning the  `repo <https://github.com/rbpatt2019/ToDonePy>`_, and using the included Makefile.

.. code:: sh

    git clone https://github.com/rbpatt2019/ToDonePy/
    make install
    
If you would like to contribute to development, the install instructions are slightly different. Please see the section on  :ref:`contributing`.

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

TODO

.. _to doing:

Keeping track of tasks with ``to doing``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

.. _to done:

Completing your tasks with ``to done``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

Recent Changes
--------------

Please see the `CHANGELOG <https://github.com/rbpatt2019/ToDonePy/blob/master/CHANGELOG.rst>`_

Next Steps
----------

- Develop command line interface structure, as described in this document
- Continue to expand README and doumentation.

Thank Yous
----------

- `Click <https://click.palletsprojects.com/en/7.x/>`_ for making an excellent package with absolutely stellar documentation.
