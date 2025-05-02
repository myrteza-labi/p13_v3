Déploiement et gestion de l'application
=======================================

Cette section détaille les mécanismes de déploiement de l'application, qu'ils soient locaux ou cloud, ainsi que les bonnes pratiques de gestion.

Vue d’ensemble du déploiement
-----------------------------

Le projet utilise un pipeline CI/CD complet basé sur :

- **GitHub Actions** : exécute les tests, le linting et construit une image Docker
- **Docker Hub** : héberge l’image générée
- **Render** : plateforme d’hébergement qui déploie l’image Docker en production

Déploiement automatique via GitHub Actions et Docker
----------------------------------------------------

1. Le workflow `ci.yml` est déclenché à chaque `push` ou `pull_request`. Il exécute :
   - L’installation des dépendances
   - La vérification de style avec `flake8`
   - Les tests Django via `coverage`
   - Il échoue si la couverture descend sous 80 %

2. Le workflow `ci-cd.yml` est déclenché uniquement sur la branche `main`. Il effectue :
   - Une seconde exécution des tests (séparation explicite des jobs)
   - La construction d’une image Docker nommée `martinlabi/oc-lettings-site`
   - La publication de cette image sur Docker Hub (`latest` + `sha`)

Variables GitHub nécessaires dans **Settings > Secrets** :
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

Déploiement sur Render
-----------------------

Créer un nouveau service **Docker** sur Render :

- Image : `martinlabi/oc-lettings-site:latest`
- Start command : (laisser vide, déjà dans le `Dockerfile`)
- Ajouter les variables d’environnement :
  - `SECRET_KEY`
  - `DEBUG=False`
  - `ALLOWED_HOSTS=yourdomain.onrender.com`
  - `SENTRY_DSN` (facultatif)

Render exécutera automatiquement :

- `migrate`
- `loaddata`
- `collectstatic`
- puis démarrera Gunicorn

Déploiement local avec Docker Compose
-------------------------------------

Fichier : `docker-compose.yml`

Étapes :

1. Créer un fichier `.env` à la racine :

   .. code-block:: env

      SECRET_KEY=your_secret_key
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      SENTRY_DSN=

2. Lancer le site localement :

   .. code-block:: bash

      docker-compose up --build

3. Accéder à l'application :

   - http://localhost:8000
   - http://localhost:8000/admin

Bonnes pratiques
----------------

- Ne jamais activer `DEBUG=True` en production
- Ne pas versionner `.env` (exclu via `.dockerignore`)
- Utiliser Sentry pour le monitoring des erreurs
- Toujours vérifier la couverture des tests (`coverage report`)
- Garder le Dockerfile minimal et reproductible
