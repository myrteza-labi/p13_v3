Profiles – URL Routing
======================

Ce module définit les routes URL pour l’application ``profiles``.  
Il connecte les chemins d’URL aux vues correspondantes, permettant la navigation vers la liste des profils et les détails d’un utilisateur.

.. automodule:: profiles.urls
   :members:
   :undoc-members:
   :show-inheritance:

Structure des routes
--------------------

L'application utilise deux routes principales :

**1. Index des profils**
~~~~~~~~~~~~~~~~~~~~~~~~

- **URL** : ``profiles/``
- **Nom de route** : ``profiles:index``
- **Vue associée** : :func:`profiles.views.index`

Cette route affiche la liste de tous les profils enregistrés dans l’application.  
Elle est utilisée pour la navigation vers la vue d'ensemble.

**2. Détail d’un profil**
~~~~~~~~~~~~~~~~~~~~~~~~~

- **URL** : ``profiles/<str:username>/``
- **Nom de route** : ``profiles:detail``
- **Vue associée** : :func:`profiles.views.profile`

Cette route accepte un nom d’utilisateur comme paramètre.  
Elle affiche les détails du profil correspondant à ce nom, ou une page 404 personnalisée si le profil n’existe pas.

Utilisation du namespace
------------------------

Le champ ``app_name = 'profiles'`` permet de nommer les routes de manière unique (ex. ``profiles:index``), ce qui évite les conflits dans un projet multi-apps.
