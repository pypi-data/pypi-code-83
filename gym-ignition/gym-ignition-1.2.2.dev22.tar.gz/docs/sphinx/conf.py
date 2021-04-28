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
from datetime import datetime
project = 'gym-ignition'
copyright = f'{datetime.now().year}, Istituto Italiano di Tecnologia'
author = 'Diego Ferigo'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    "sphinx.ext.extlinks",
    'sphinx_autodoc_typehints',
    "sphinx_multiversion",
    "sphinx_fontawesome",
    'breathe',
    'sphinx_tabs.tabs',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "repository_url": "https://github.com/robotology/gym-ignition",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs/sphinx",
    "home_page_in_toc": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'pastie'


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for breathe extension ----------------------------------------------

breathe_default_project = "scenario"

# -- Options for sphinx_multiversion extension ----------------------------------

# From: https://holzhaus.github.io/sphinx-multiversion
smv_prefer_remote_refs = False
smv_remote_whitelist = r'^(origin|upstream)$'
smv_tag_whitelist = None
smv_branch_whitelist = r'^(master|devel|docs/.*)$'
smv_released_pattern = r'^tags/.*$'
smv_outputdir_format = '{ref.name}'

html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "versions.html",
        "searchbox.html",
    ],
}

# -- Options for extlinks extension ----------------------------------
extlinks = {
    'issue': ('https://github.com/robotology/gym-ignition/issues/%s', '#'),
    'pr': ('https://github.com/robotology/gym-ignition/pull/%s', '#'),
}
