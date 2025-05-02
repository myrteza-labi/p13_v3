OC Lettings Site – ASGI
========================

Ce module configure l'interface ASGI pour le projet Django ``oc_lettings_site``.

.. automodule:: oc_lettings_site.asgi
   :members:
   :undoc-members:
   :show-inheritance:

Description
-----------

Ce fichier expose une instance ASGI pour permettre le déploiement asynchrone de l’application Django.  
Il est utilisé notamment dans des environnements de production ou de développement compatibles avec ASGI (comme Daphne, Uvicorn).

Comportement
------------

- Définit la variable d’environnement ``DJANGO_SETTINGS_MODULE`` sur ``oc_lettings_site.settings`` si elle n’est pas déjà définie.
- Initialise et expose l’application ASGI via `get_asgi_application()`, qui sert de point d’entrée pour les serveurs ASGI.
