.. _CHANGELOG:

CHANGELOG for ToDonePy
======================

v4.0.5
------
- No changes to user.
- Migrate to iSort 5
- Improve linting
- Expand pre-commit hooks
- Update dependencies

v4.0.4
------
- Migrate to pytest 6.0. No changes to user.

v4.0.3
------
- Dependency update. No changes to user.

v4.0.2
------
- Fix build error

v4.0.1
------
- Fix build error

v4.0.0
------
- BREAKING: Refactor from Click to Argparse
- BREAKING: Python must be >=3.7 to all for caught output from `subprocess.run()`
- BREAKING: Timestamp now only to mintes. Previously, was to seconds
- Vastly improved documentation, using numpy docstrings and Napoleon

v3.2.1
------

- Refactor tests. No impact to user.

v3.2.0
------
- Resume active development
- Incorporate marks for testing
- Update requirements

v3.0.0
------
- BREAKING: Migrate to poetry for development
- BREAKING: Add delimiter parameter to Filer class
- BREAKING: Add headings to ``TODO.tsv``
- BREAKING: Add ID column to ``TODO.tsv``
- Add Filer.write_col method
- Add itemsetter function
- Filer.sort can now ignore headers

v2.3.1
------
- Update requirements

v2.3.0
------
- Adds ``--graphic`` flag for ``to doing`` allowing the user to spawn notification windows

v2.2.1
------
- Requirements update

v2.2.0
------
- ``to done`` notifies you when it can't delete a task

v2.1.1
------
- Remove ``pandas`` requirement in setup.py

v2.1.0
------
- Suport nargs for the ``tasks`` parameter of ``to do`` and ``to done``

v2.0.0
------
- BREAKING: Move to ``TODO.tsv`` for prettier printing.
- BREAKING: Args are now passed for to in reversed order. Call as ``to do {rank} {task}``
- BREAKING: ``to do`` now sorts new tasks automatically, unless told not to
- Commands now type check inputs
- Pandas dependency now longer required for sorting
- Filer class now uses ``csv`` module for handling files

v1.3.2
------
- Add ``pandas`` to setup.py

v1.3.1
------
- Remove broken test

v1.3.0
------
- Add ``--sort`` flag to ``to doing``

v1.2.1
------
- Update documentation

v1.2.0
------
- Add editor option to ``to doing``

v1.1.0
------
- Add timestamp to ``to do``

v1.0.2
------
- Config .travis.yml

v1.0.1
------
- Correct dist error caused by ref tag in README

v1.0.0
------
- First public release. Project status now alpha.

v0.6.0
------
- Update test structure

v0.5.5
------
- Update docstrings

v0.5.4
------
- Correct erroneous new line in Filer.append. Closes issue #10

v0.5.3
------
- Update TOCtree for sphinx

v0.5.2
------
- Update documentation in README.rst
- Update TOCtree for sphinx

v0.5.1
------
- Changed .travis.yml
- Changed internal references in README.rst

v0.5.0
------
- Add subcommand ``to done``

v0.4.1
------
-Correct docstring for ``to doing``

v0.4.0
------
- Add subcommand ``to doing``
- Add tests for new commands

v0.3.0
------
- Create group command structure
  - Add main command ``to``
  - Add subcommand ``to do``
- Add tests for new commands
- Move to using Path type for file inputs

v0.2.1
------
- Update documentation structure

v0.2.0
------
- Add Filer class for context handling in CLI
- Add tests for Filer

v0.1.1
------
- Corrected some naming and structure inconsistencies in the docs

v0.1.0
------

-  Full project outline complete.
-  Integrated:

   -  Travis CI for builds
   -  CodeCov for test coverage
   -  ReadTheDocs for doc building/hosting

-  Integrate mypy, instafail, and coverage ito PyTest
