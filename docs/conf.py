import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "Opt Modeling Lab"
author = "Jay Appleton"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

html_theme = "furo"
html_title = "Opt Modeling Lab"
html_short_title = "Opt Lab"

html_sidebars = {
    "**": ["sidebar/brand.html", "sidebar/navigation.html"]
}

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}