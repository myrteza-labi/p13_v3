manage.py
=========

Description
-----------

Fichier d’entrée principal du projet Django.  
Il permet d’exécuter toutes les commandes de gestion : lancement du serveur, migrations, tests, chargement de fixtures, etc.

Fonctionnement
--------------

- Définit la variable d’environnement ``DJANGO_SETTINGS_MODULE`` pour indiquer à Django où trouver les réglages du projet.
- Utilise ``execute_from_command_line(sys.argv)`` pour lancer la commande passée en argument depuis le terminal.

Commandes courantes
-------------------

::

   python manage.py runserver
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py loaddata fixtures/users.json fixtures/lettings.json fixtures/profiles.json
   python manage.py test

Cas d’usage
-----------

- Lancement du serveur en local
- Exécution des migrations et chargement des données
- Utilisé dans le Dockerfile pour automatiser les étapes du déploiement
- Point d’entrée pour la gestion de l’application en développement ou en production
