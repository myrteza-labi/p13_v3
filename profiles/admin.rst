Profiles – admin.py
====================

Ce module configure l’intégration du modèle ``Profile`` dans l’interface d’administration Django.

.. automodule:: profiles.admin
   :members:
   :undoc-members:
   :show-inheritance:

Fonctionnalité
--------------

Le fichier utilise la fonction ``admin.site.register`` pour enregistrer le modèle ``Profile`` auprès de l’admin Django. Cela permet de :

- Visualiser les objets `Profile` depuis l’interface d’administration (http://localhost:8000/admin).
- Créer, éditer ou supprimer un profil à partir de l’interface web.
- Lier directement chaque `Profile` à un utilisateur `User`.

Aucune personnalisation avancée n’est effectuée ici (comme `ModelAdmin`), ce qui signifie que Django utilisera les options d’affichage par défaut.
