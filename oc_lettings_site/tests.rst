Tests – oc_lettings_site.tests
==============================

Ce module contient les tests unitaires pour l’application principale ``oc_lettings_site``.  
Ils couvrent :

- La vue d’accueil (index)
- La page d’erreur personnalisée 404
- Le routage des URLs

.. automodule:: oc_lettings_site.tests
   :members:
   :undoc-members:
   :show-inheritance:

Structure des tests
-------------------

**Tests des vues**
~~~~~~~~~~~~~~~~~~

- :class:`SiteViewsTest`

  - ``test_index_view`` : vérifie que la page d’accueil (`/`) renvoie un code 200 et utilise le bon template.
  - ``test_custom_404_view`` : vérifie qu’une URL inexistante renvoie bien une erreur 404 avec le template personnalisé.

**Tests des routes**
~~~~~~~~~~~~~~~~~~~~

- :class:`SiteURLsTest`

  - ``test_index_url_resolves_to_index_view`` : assure que l’URL `/` est bien liée à la fonction `oc_lettings_site.views.index`.
  - ``test_404_handler_is_custom`` : confirme que le handler 404 du projet est bien redirigé vers `custom_404`.

Bonne pratique : ces tests garantissent que les pages centrales du site et la gestion des erreurs sont toujours fonctionnelles.
