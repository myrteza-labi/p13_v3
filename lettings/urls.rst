Lettings – urls.py
===================

Ce module définit les routes (URLs) de l’application ``lettings``.

Il gère deux types de pages :
- L’index des locations disponibles ;
- Le détail d’une location précise via son identifiant.

.. automodule:: lettings.urls
   :members:
   :undoc-members:
   :show-inheritance:

Liste des routes
----------------

- **lettings:index**
  - URL : ``/lettings/``
  - Vue : :func:`lettings.views.index`
  - Description : Affiche la liste de toutes les locations.

- **lettings:detail**
  - URL : ``/lettings/<letting_id>/``
  - Vue : :func:`lettings.views.letting`
  - Description : Affiche les détails d’une location spécifique, identifiée par son ID.
