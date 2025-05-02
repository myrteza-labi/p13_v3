Commandes de gestion
====================

Ce projet utilise les commandes Django suivantes :

- **python manage.py migrate**  
  Applique les migrations de base de données.

- **python manage.py makemigrations**  
  Crée de nouvelles migrations à partir des modifications de modèles.

- **python manage.py loaddata**  
  Charge des fixtures JSON (ex. `fixtures/lettings.json`).

- **python manage.py runserver**  
  Démarre le serveur de développement.

- **python manage.py createsuperuser**  
  Crée un compte administrateur via la CLI.

- **python manage.py collectstatic**  
  Rassemble les fichiers statiques dans `STATIC_ROOT` pour la production.

- **python manage.py test**  
  Lance la suite de tests avec pytest (via `pytest-django`).
