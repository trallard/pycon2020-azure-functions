# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Easy data processing on Azure with Serverless Functions"
copyright = "2020, Tania Allard"
author = "Tania Allard"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "recommonmark",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
]

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "monokai"

master_doc = "index"

html_sidebars = {
    "**": [
        "about.html",
        "localtoc.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        # "sidebar.html",
    ]
}

# -- Source -------------------------------------------------------------

import recommonmark
from recommonmark.transform import AutoStructify


def setup(app):
    app.add_config_value("recommonmark_config", {"enable_eval_rst": True}, True)
    app.add_stylesheet("custom.css")
    app.add_transform(AutoStructify)


source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}

source_suffix = [".rst", ".md"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"


html_theme_options = {
    "github_user": "trallard",
    "github_repo": "mentored-sprints-website",
    "github_type": "star",
    "github_banner": True,
    "show_relbars": True,
    "font_family": "'Inconsolata','Obliqua','Open Sans', Georgia, sans",
    "head_font_family": "'Phoreus Cherokee','Spartan', Georgia, serif",
    "code_font_family": "'Inconsolata','Anonymous Pro','Fira Code', 'Consolas', monospace",
    "logo": "images/Bit_BobRoss.png",
    "github_banner": False,
    "description": "Azure sponsored workshop: PyCon 2020",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


rst_epilog = """
.. |light| image:: _static/icons/video-game.svg
    :class: inline-image

.. |floppy| image:: _static/icons/save-file.svg
    :class: inline-image

.. |foo| replace:: foo
.. _foo: http://stackoverflow.com
"""
