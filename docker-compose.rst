docker-compose.yml – Configuration des services Docker
======================================================

Ce fichier ``docker-compose.yml`` définit les services nécessaires pour exécuter le projet Django dans un environnement Docker local.  
Il permet de construire et d'exécuter le conteneur, avec une configuration dédiée à l'exécution de l'application.

Objectif
--------

Le fichier ``docker-compose.yml`` permet de :

- Définir et configurer le service ``web`` pour l'application Django.
- Lancer le projet localement, en exécutant le serveur Django via **Gunicorn**.
- Charger automatiquement les fixtures, appliquer les migrations et collecter les fichiers statiques.

Structure du fichier
--------------------

1. **Version de Docker Compose**

.. code-block:: yaml

   version: '3.8'

Cela spécifie que nous utilisons la version 3.8 de Docker Compose.

2. **Service Web**

.. code-block:: yaml

   services:
     web:
       build: .
       ports:
         - "8000:8000"
       env_file:
         - .env
       command: >
         sh -c "
         echo '🚀 MIGRATIONS' &&
         python manage.py migrate --noinput &&
         echo '📦 LOADDATA' &&
         python manage.py loaddata fixtures/users.json fixtures/lettings.json fixtures/profiles.json &&
         echo '🧹 COLLECTSTATIC' &&
         python manage.py collectstatic --noinput &&
         echo '🔥 Gunicorn Start' &&
         gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
         "

### 2.1 **Build du conteneur**

.. code-block:: yaml

   build: .

Le service ``web`` sera construit en utilisant le ``Dockerfile`` situé dans le même répertoire.

### 2.2 **Exposition du port**

.. code-block:: yaml

   ports:
     - "8000:8000"

Cela permet d'exposer le port 8000 du conteneur à l'hôte local, pour accéder à l'application à l'adresse ``http://localhost:8000``.

### 2.3 **Chargement des variables d'environnement**

.. code-block:: yaml

   env_file:
     - .env

Le fichier ``.env`` contient les variables d'environnement nécessaires pour la configuration de l'application (comme ``SECRET_KEY``, ``DEBUG``, ``ALLOWED_HOSTS``, etc.).

### 2.4 **Commande de démarrage**

La commande exécutée à chaque démarrage du service est définie dans ``command`` et comprend les étapes suivantes :

- Exécution des migrations : ``python manage.py migrate --noinput`` ;
- Chargement des fixtures (données initiales) : ``python manage.py loaddata fixtures/...`` ;
- Collecte des fichiers statiques avec ``collectstatic`` ;
- Démarrage de Gunicorn pour servir l'application : ``gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000``.

Utilisation
-----------

Pour démarrer l'application en local, exécutez la commande suivante :

.. code-block:: bash

   docker-compose up --build

Cette commande va construire le service, démarrer le serveur et effectuer les étapes nécessaires (migrations, chargement des fixtures, collecte des fichiers statiques) avant de lancer l'application avec Gunicorn.

