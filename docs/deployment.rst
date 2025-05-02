Déploiement et gestion
=======================

La CI/CD et le déploiement se font via GitHub Actions, Docker Hub et Render.

1. **Tests et build**  
   - À chaque push sur `main`, GitHub Actions exécute `flake8`, `pytest` (coverage) puis construit l’image Docker.  
   - Les workflows sont définis dans :
     - `.github/workflows/ci.yml`
     - `.github/workflows/ci-cd.yml`

2. **Publication de l’image Docker**  
   - L’image est poussée sur Docker Hub sous `martinlabi/oc-lettings-site:latest`.  
   - Les identifiants Docker sont configurés dans les secrets GitHub (`DOCKER_USERNAME`, `DOCKER_PASSWORD`).

3. **Déploiement sur Render**  
   - Render récupère l’image Docker et lance :
     ```bash
     docker run \
       -e SECRET_KEY=<SECRET_KEY> \
       -e DEBUG=False \
       -e ALLOWED_HOSTS=<HOST> \
       -e SENTRY_DSN=<SENTRY_DSN> \
       martinlabi/oc-lettings-site:latest
     ```
   - Render exécute ensuite les migrations, `collectstatic` et démarre Gunicorn.

4. **Surveillance des erreurs**  
   - Sentry (via `sentry-sdk`) remonte automatiquement les erreurs si `SENTRY_DSN` est défini.

Pour un **test local** avec Docker Compose :

```bash
docker-compose up --build
