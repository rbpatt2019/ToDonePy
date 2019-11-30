# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import poetry_version
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'ToDonePy'
copyright = '2019, Ryan B Patterson'
author = 'Ryan B Patterson'
__version__ = poetry_version.extract(source_file=__file__)

# Short version (should work with bump2version)
version = __version__
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx_click.ext',
        'sphinxcontrib.fulltoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document
master_doc = 'index'

# The suffix(es) of source filenamnes.
# You can specify multiple suffixes as a list of string:
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by sphinx. Refer to documentation
# for a list of supported languages
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set the "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'
html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
