docker-compose.override.yml – Configuration de développement local
================================================================

Ce fichier ``docker-compose.override.yml`` est utilisé pour configurer les services Docker pendant le développement local.  
Il permet d'ajouter des volumes de partage et de définir des variables d'environnement spécifiques à l'environnement de développement.

Objectif
--------

Le fichier ``docker-compose.override.yml`` permet de :

- Partager les fichiers locaux avec le conteneur Docker pour le développement en temps réel.
- Assurer la persistance des données via le volume ``sqlite3``.
- Définir des variables d'environnement pour activer le mode ``DEBUG``.

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
       volumes:
         - .:/app
         - ./oc-lettings-site.sqlite3:/app/oc-lettings-site.sqlite3
       environment:
         DEBUG: "True"

### 2.1 **Volumes**

.. code-block:: yaml

   volumes:
     - .:/app
     - ./oc-lettings-site.sqlite3:/app/oc-lettings-site.sqlite3

Les volumes permettent de lier le répertoire du projet local avec le conteneur Docker, ce qui permet de modifier les fichiers du projet localement et de les voir reflétés immédiatement dans le conteneur.

- ``.:/app`` : Monte le répertoire actuel de l'application dans le conteneur, permettant ainsi de modifier les fichiers source en temps réel sans redémarrer le conteneur.
- ``./oc-lettings-site.sqlite3:/app/oc-lettings-site.sqlite3`` : Monte le fichier ``oc-lettings-site.sqlite3`` dans le conteneur, garantissant la persistance de la base de données locale à travers les redémarrages du conteneur.

### 2.2 **Variables d'environnement**

.. code-block:: yaml

   environment:
     DEBUG: "True"

La variable ``DEBUG`` est définie sur ``True`` pour activer le mode développement, ce qui permet de voir les erreurs détaillées pendant l'exécution du serveur local.

Utilisation
-----------

Le fichier ``docker-compose.override.yml`` est automatiquement pris en compte lorsqu'on exécute ``docker-compose`` en local. Il est donc inutile de spécifier ce fichier dans les commandes de Docker Compose.

Pour démarrer le conteneur en mode développement avec ce fichier de configuration, exécutez la commande suivante :

.. code-block:: bash

   docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build

Cette commande lancera les services en mode développement avec les volumes partagés et les variables d'environnement appropriées.

