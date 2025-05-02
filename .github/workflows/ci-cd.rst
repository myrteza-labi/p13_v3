CI/CD – GitHub Actions (ci-cd.yml)
==================================

Ce fichier configure le pipeline **CI/CD complet** du projet via **GitHub Actions**.

Il se déclenche automatiquement lors :

- d’un **push** sur la branche ``main`` ;
- ou d’une **pull request** vers ``main``.

Il contient deux étapes principales : les **tests** et la **publication Docker**.

Structure du fichier
--------------------

.. code-block:: yaml

   name: CI/CD Pipeline
   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]

Jobs définis
------------

1. **build-test**

   Ce job s'exécute sur un environnement ``ubuntu-latest`` et fait les étapes suivantes :

   - Cloner le dépôt ;
   - Installer Python 3.11 ;
   - Installer les dépendances du projet ;
   - Exécuter ``flake8`` pour vérifier le style du code ;
   - Lancer les tests unitaires via ``coverage``.

   .. code-block:: yaml

      - name: Run tests with coverage
        run: |
          coverage run --source='.' manage.py test
          coverage report --omit="*/venv/*" --fail-under=80

2. **docker**

   Ce job s'exécute **uniquement si le job `build-test` réussit**.  
   Il a pour rôle de **construire l’image Docker du projet et la publier sur Docker Hub**.

   Étapes clés :

   - Construction de l’image avec tag SHA et ``latest`` ;
   - Connexion à Docker Hub avec les secrets GitHub :
     - ``DOCKER_USERNAME``
     - ``DOCKER_PASSWORD``
   - Push des images Docker.

   .. code-block:: yaml

      - name: Build Docker image
        run: |
          docker build -t martinlabi/oc-lettings-site:${{ github.sha }} .
          docker tag martinlabi/oc-lettings-site:${{ github.sha }} martinlabi/oc-lettings-site:latest

      - name: Push Docker image to Docker Hub
        run: |
          docker push martinlabi/oc-lettings-site:${{ github.sha }}
          docker push martinlabi/oc-lettings-site:latest

Utilité
-------

- ✅ Automatiser les vérifications qualité du code (lint, tests).
- ✅ Générer une image Docker fonctionnelle.
- ✅ Publier cette image à chaque mise à jour de la branche ``main``, en toute sécurité.
