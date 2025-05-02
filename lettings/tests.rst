Lettings – Tests
================

Ce module contient les tests unitaires de l’application ``lettings``.  
Ils couvrent :

- La représentation texte des modèles ``Address`` et ``Letting``.
- Le bon fonctionnement des vues (index, détail, 404 personnalisée).
- La résolution correcte des routes définies dans les URLs.

.. automodule:: lettings.tests
   :members:
   :undoc-members:
   :show-inheritance:

Structure des tests
-------------------

**Tests des modèles**
~~~~~~~~~~~~~~~~~~~~~

- :class:`AddressModelTest`
- :class:`LettingModelTest`

Ces tests vérifient que la méthode ``__str__`` de chaque modèle retourne une valeur correcte.

**Tests des vues**
~~~~~~~~~~~~~~~~~~

- :class:`LettingsViewsTest`

Vérifie :

- Le code de statut et le template utilisé pour la vue index.
- Le bon affichage des détails d’un letting existant.
- L’utilisation d’une page 404 personnalisée pour un ID inexistant.

**Tests des routes**
~~~~~~~~~~~~~~~~~~~~

- :class:`LettingsURLsTest`

Vérifie que les noms de routes ``lettings:index`` et ``lettings:detail`` pointent bien vers les bonnes vues.
