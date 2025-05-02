Profiles – Views
================

Ce module contient les vues principales de l’application ``profiles``.  
Il permet d’afficher la liste des profils ainsi que les détails d’un profil utilisateur.  
Les vues utilisent le système de templating de Django, les modèles de l’app ``profiles``, et un système de logs pour le suivi.

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:

Fonctionnalités fournies
------------------------

**1. Affichage de la liste des profils**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Vue** : :func:`index`
- **Route** : ``profiles:index``
- **Template** : ``profiles/index.html``

Cette vue récupère tous les objets ``Profile`` et les affiche via le template associé.  
Un log de niveau INFO est enregistré lors de l’appel.

**Exemple d’usage :**

- Un utilisateur accède à `/profiles/`.
- La vue charge tous les profils et rend la page HTML.

**2. Détail d’un profil utilisateur**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Vue** : :func:`profile`
- **Route** : ``profiles:detail``
- **Paramètre attendu** : ``username`` (string)
- **Template** : ``profiles/profile.html`` ou ``profiles/profile_404.html``

Cette vue récupère un profil spécifique à partir de son ``username``.  
Si le profil n’est pas trouvé, une page 404 personnalisée est affichée.  
Des logs de niveau INFO ou WARNING sont générés selon les cas.

**Comportement attendu :**

- Si un profil existe → page de détails avec ses données.
- Si aucun profil ne correspond → message d’erreur avec statut 404.

Logs intégrés
-------------

- Chaque affichage réussi d’un profil ou de la liste génère un `logger.info()`.
- Chaque tentative échouée d’accès à un profil génère un `logger.warning()`.

Ce système permet une traçabilité fine des interactions utilisateur avec les vues sensibles de l’app.

