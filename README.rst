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

`ToDonePy <https://github.com/rbpatt2019/ToDonePy/>`_ is a command-line interface for managing your to do list. It provides a root command, :ref:`to`, and three subcommands:

- :ref:`to do` adds a new task to your list at either 'low', 'med', or 'high' priority.
- :ref:`to doing` shows you what you should be doing.
- :ref:`to done` removes a completed tast from your list.

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

TODO

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
