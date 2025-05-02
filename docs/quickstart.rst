Démarrage rapide
================

Une fois l'installation effectuée, suivez ces étapes pour lancer le projet :

.. code-block:: bash

    # Appliquer les migrations
    python manage.py migrate

    # Charger les données de test
    python manage.py loaddata fixtures/lettings.json fixtures/profiles.json fixtures/users.json

    # Lancer le serveur de développement
    python manage.py runserver

Accédez ensuite à :

- http://localhost:8000  
  pour voir le site en mode développeur  
- http://localhost:8000/admin  
  pour accéder au panneau d’administration  
