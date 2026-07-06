import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "Opt Modeling Lab"
author = "Jay M. Appleton"
release = "0.1.0"
copyright = "2026, Jay M. Appleton"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
]

html_theme = "sphinx_book_theme"

html_title = "Opt Modeling Lab"
html_short_title = "Opt Lab"

html_theme_options = {
    "repository_url": "https://github.com/Jay-A/opt-modeling-lab",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "home_page_in_toc": True,
    "navigation_with_keys": True,
}

html_static_path = ["_static"]

html_css_files = [
    "custom.css",
]

templates_path = ["_templates"]

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

nitpicky = False