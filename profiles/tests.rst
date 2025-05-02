Profiles - Tests
================

Ce module contient les tests unitaires de l’application ``profiles``.  
Ils couvrent :

- La représentation texte du modèle ``Profile``.
- Le bon fonctionnement des vues (index, détail, 404 personnalisée).
- La résolution correcte des routes définies dans les URLs.

.. automodule:: profiles.tests
   :members:
   :undoc-members:
   :show-inheritance:


Structure des tests
-------------------

**Tests du modèle**
~~~~~~~~~~~~~~~~~~~

- :class:`ProfileModelTest`

Ce test vérifie la méthode ``__str__`` du modèle ``Profile``.

**Tests des vues**
~~~~~~~~~~~~~~~~~~

- :class:`ProfilesViewsTest`

Teste la page d’index, les détails valides et une page 404 personnalisée.

**Tests des routes**
~~~~~~~~~~~~~~~~~~~~

- :class:`ProfilesURLsTest`

Vérifie que les noms de routes ``profiles:index`` et ``profiles:detail`` pointent vers les bonnes vues.
