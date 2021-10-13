# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme

project = 'Manny Manual'
# copyright = '2021, Damon'
author = 'Damon'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.youtube'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {'prev_next_buttons_location': 'both'}

html_logo = "images/horizons.ico"

html_favicon = "https://www.horizons.govt.nz/App_Themes/Default/Images/favicon.ico"

html_last_updated_fmt = ""

#References
# rst file editor http://rst.ninjs.org/#
# rst file docs https://docutils.sourceforge.io/docs/ref/rst/directives.html
# sphinx tutorial https://sphinx-tutorial.readthedocs.io/
# readthedocs theme options https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# text table generator https://www.tablesgenerator.com/text_tables#
# stl thumbnails https://3dprintbeginner.com/how-to-enable-stl-thumbnails-in-windows-10/
# rtd config page https://readthedocs.org/projects/manny-manual/
# manny-manual https://manny-manual.readthedocs.io/en/latest/