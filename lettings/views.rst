Lettings – views.py
====================

Ce module contient les vues de l’application ``lettings``.

Il permet d’afficher :
- la liste de toutes les locations disponibles ;
- les détails d’une location spécifique ;
- une page 404 personnalisée si la location demandée n’existe pas.

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:


Vue : index
-----------

.. function:: index(request)

Affiche la liste complète des locations.  
Cette vue :

- Récupère tous les objets `Letting` via la base de données ;
- Génère un log en INFO pour le suivi ;
- Passe les résultats au template `lettings/index.html`.

**Template utilisé** : ``lettings/index.html``  
**URL associée** : ``/lettings/``  
**Nom de route Django** : ``lettings:index``


Vue : letting
-------------

.. function:: letting(request, letting_id)

Affiche les détails d’une location spécifique.  
Cette vue :

- Tente de récupérer un `Letting` à partir de son identifiant ;
- Si trouvé, rend le template `lettings/letting.html` avec les données ;
- Si non trouvé, loggue un warning et renvoie une page d’erreur 404 personnalisée.

**Templates utilisés** :  
- ``lettings/letting.html`` (si trouvé)  
- ``lettings/letting_404.html`` (si introuvable)

**URL associée** : ``/lettings/<id>/``  
**Nom de route Django** : ``lettings:detail``

**Logging** :  
- INFO : succès de l’affichage ;
- WARNING : id non trouvé, page 404 servie.
