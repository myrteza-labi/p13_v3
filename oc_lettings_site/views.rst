Vues – oc_lettings_site.views
=============================

Ce module contient les vues principales du site Orange County Lettings.  
Il gère notamment la page d’accueil et la page d’erreur 404 personnalisée.

.. automodule:: oc_lettings_site.views
   :members:
   :undoc-members:
   :show-inheritance:

Vues disponibles
----------------

**index(request)**  
Affiche la page d’accueil principale du site (`index.html`).  
Aucune logique complexe n’est appliquée, c’est une simple vue de rendu statique.  
Elle est appelée par la route ``/`` (racine du site).  

**custom_404(request, exception)**  
Vue appelée lorsqu'une URL ne correspond à aucune route définie dans le projet.  
Affiche une page 404 personnalisée (`404.html`) avec un statut HTTP 404.  
Cette vue utilise un logger pour journaliser les erreurs de type "Page non trouvée".  
Elle est liée au projet par l’attribut global `handler404` dans ``urls.py``.

Exemple d’erreur loguée :

WARNING 2025-05-02 12:00:00 views 404 error encountered: /bad-url/ - Resolver404(...)

Résumé
------

Ces vues servent d’entrée principale au site, et de filet de sécurité en cas d’URL invalide.