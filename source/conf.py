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

project = 'Terradoo Cloud'
copyright = '2020, JuanDCG, Apache License 2.0'
author = 'JuanDCG'
license = 'Apache License 2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {

    'logo': 'images/TerradooCloud-logo.png',
    'body_text_align': 'left',
    'canonical_url': 'https://documentation.terradoo.cloud/',
    'description': 'Odoo Community Infrastructures with Open Source',
    'analytics_id':'G-D7JWV25RNE',
    'github_banner': 'True',
    'github_repo': 'terradoo-cloud-documentation',
    'github_user': 'TerradooCloud',
    'sidebar_collapse': 'True',
    'fixed_sidebar': 'True',
    'show_related': 'True',
    'show_powered_by': 'True',
    'show_relbars': 'True',
                    
    
}






# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']