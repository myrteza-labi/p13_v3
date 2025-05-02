# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Orange County Lettings'
author = 'Myrteza Labi'
release = '1.0'

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
