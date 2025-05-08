# docs/conf.py

import os
import sys
from datetime import datetime

# Inclure le répertoire parent (racine du projet)
sys.path.insert(0, os.path.abspath('..'))

# Informations sur le projet
project = 'Orange County Lettings'
author = 'Myrteza Labi'
release = '1.0'
copyright = f'{datetime.now().year}, {author}'

# Extensions Sphinx
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Pour supporter les docstrings style Google/Numpy
    'sphinx.ext.viewcode',  # Ajoute des liens vers le code source
]

# Chemins
templates_path = ['_templates']
exclude_patterns = []

# Thème HTML
html_theme = 'alabaster'
language = 'fr'
html_static_path = ['_static']

# Autodoc config optionnelle (facultatif)
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}
