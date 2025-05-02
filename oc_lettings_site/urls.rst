URLs – oc_lettings_site.urls
============================

Ce module configure l’ensemble des routes (URLs) du projet ``oc_lettings_site``.

.. automodule:: oc_lettings_site.urls
   :members:
   :undoc-members:
   :show-inheritance:

Structure des routes
--------------------

- ``/``  
  Accueil du site. Route associée à la vue ``index`` dans ``oc_lettings_site.views``.

- ``/admin/``  
  Interface d’administration Django intégrée.

- ``/lettings/``  
  Inclus les routes de l’application ``lettings``. Les noms de vues sont accessibles avec le namespace ``lettings``.

- ``/profiles/``  
  Inclus les routes de l’application ``profiles``. Les noms de vues sont accessibles avec le namespace ``profiles``.

- ``/sentry-debug/``  
  Déclenche volontairement une erreur de division par zéro pour tester l’envoi des erreurs à Sentry.

Gestion des erreurs
-------------------

- ``handler404``  
  Définit un gestionnaire d’erreur 404 personnalisé : ``oc_lettings_site.views.custom_404``.  
  Cela permet d’afficher une page dédiée en cas d’URL non trouvée.

Fichiers statiques
------------------

La ligne :

```python
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
