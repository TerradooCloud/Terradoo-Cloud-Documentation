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
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Terradoo Cloud'
copyright = 'AGPL-3.0: "Juan Del Castillo Gómez" and "Contributors".'
author = 'JuanDCG (Juan Del Castillo Gómez)'
license = 'AGPL-3.0'
version= '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_rtd_theme"]

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
html_theme = 'sphinx_rtd_theme'
html_style = 'css/terradoo-cloud-style.css'
html_logo = '_themes/images/TerradooCloud-logo.png'
html_theme_options = {
    
    'canonical_url': 'https://documentation.terradoo.cloud/',
    'analytics_id': 'G-D7JWV25RNE',  #  Provided by Google in your dashboard
    'logo_only': 'True',
    'display_version': 'True',
    'prev_next_buttons_location': 'bottom',
    'style_external_links': 'True',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': 'True',
    'sticky_navigation': 'True',
    'navigation_depth': '4',
    'includehidden': 'True',
    'titles_only': 'False'               
    
}

html_context = {
    'display_github': 'True', # Integrate GitHub
    'github_user': 'TerradooCloud', # Username
    'github_repo': 'terradoo-cloud-documentation', # Repo name
    'github_version': 'main', # Version
    'conf_py_path': '/', # Path in the checkout to the docs root
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_themes']
