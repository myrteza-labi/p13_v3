Profiles – apps.py
==================

Ce module définit la configuration de l’application ``profiles``.

.. automodule:: profiles.apps
   :members:
   :undoc-members:
   :show-inheritance:

Classe principale
-----------------

**ProfilesConfig**
~~~~~~~~~~~~~~~~~~

- Hérite de : ``django.apps.AppConfig``  
- Définit la configuration de base de l'application ``profiles``.
- Attributs :
  - `default_auto_field` : Défini sur ``BigAutoField``, ce qui signifie que les clés primaires des modèles utiliseront des entiers auto-incrémentés 64 bits par défaut.
  - `name` : Nom de l'application tel que référencé dans `INSTALLED_APPS`.

Cette classe est automatiquement détectée par Django grâce à sa présence dans le fichier `__init__.py` de l’application ou listée dans `INSTALLED_APPS` dans `settings.py`.
