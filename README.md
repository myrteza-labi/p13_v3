Orange County Lettings - Django Project

## Résumé

Site web d'Orange County Lettings.  
Projet Django avec gestion de profils, locations, administration et surveillance des erreurs via Sentry.

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- (Optionnel mais recommandé) : un éditeur comme VS Code avec les extensions Python et Django.

Remarque :
Dans toute la documentation, on considère que la commande `python` exécute l'interpréteur Python 3.6+ (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

cd /path/to/put/project/in
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

#### Créer et activer l'environnement virtuel

cd /path/to/Python-OC-Lettings-FR
python -m venv venv
Sur Ubuntu : apt-get install python3-venv si nécessaire
source venv/bin/activate

Vérifier que `python` pointe sur le bon interpréteur :
which python

Vérifier que la version est bien 3.6 ou supérieure :
python --version

Vérifier que `pip` utilise celui de l'environnement :
which pip

Pour désactiver l'environnement virtuel :
deactivate

#### Windows 

(PowerShell)

Pour activer l'environnement virtuel :

.\venv\Scripts\Activate.ps1

Pour vérifier les chemins :

(Get-Command python).Path
(Get-Command pip).Path

#### Exécuter le site localement

cd /path/to/Python-OC-Lettings-FR
source venv/bin/activate  ou .\venv\Scripts\Activate.ps1 sous Windows
pip install --requirement requirements.txt
python manage.py runserver

Accéder à http://localhost:8000

Vous devriez voir la page d'accueil et pouvoir naviguer entre profils et lettings.

#### Panel d'administration

Accéder à http://localhost:8000/admin

Utiliser les identifiants suivants :
- Utilisateur : admin
- Mot de passe : Abc1234!

#### Linting (code style)

flake8

#### Tests unitaires

pytest

Les tests couvrent les modèles, vues et routes principales.  
La couverture de code est supérieure à 90% (coverage run --source='.' manage.py test).

#### Base de données SQLite

Ouvrir la base existante :

sqlite3 oc-lettings-site.sqlite3
.tables                   Voir les tables
pragma table_info(oc_lettings_site_profile);   Voir la structure d'une table
select * from oc_lettings_site_profile;         Faire une requête
.quit                    Quitter SQLite

### Surveillance des erreurs - Intégration de Sentry

#### Installation

Sentry est intégré pour capter automatiquement :
- Les erreurs serveur (500, 404 personnalisées),
- Les erreurs inattendues (exceptions dans le code),
- Les logs critiques (warning, error).

Les dépendances nécessaires sont :

pip install sentry-sdk python-dotenv

(Déjà incluses dans requirements.txt.)

Variables d'environnement

Créer un fichier `.env` à la racine du projet contenant :

SENTRY_DSN=https://your_sentry_dsn_here

❗ Ne jamais committer votre DSN dans le code.

#### Configuration Sentry

Déjà configuré dans oc_lettings_site/settings.py :

import sentry_sdk
from dotenv import load_dotenv
import os

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    send_default_pii=True
)

send_default_pii=True permet d'avoir plus d'infos pour le debug (adresse IP, utilisateur connecté).

Logging des actions critiques

Un système de logging Django est actif :
- Tous les accès aux pages critiques (index, detail) sont logués en INFO.
- Toutes les erreurs et éléments manquants (letting not found, profile not found) sont logués en WARNING.
- Tous les logs critiques sont capturés et envoyés vers Sentry automatiquement.

#### Tester que Sentry fonctionne

Vous pouvez accéder à :
http://localhost:8000/sentry-debug/


Cela provoquera volontairement une division par zéro, pour tester l'envoi des erreurs à Sentry.

Résumé des bonnes pratiques

- Les données sensibles sont sécurisées via `.env`.
- Les logs sont présents uniquement aux endroits nécessaires.
- La couverture de tests dépasse 90%.
- Le projet est prêt pour un déploiement cloud avec monitoring d'erreurs intégré.

## Déploiement

### Fonctionnement général

Le projet est déployé automatiquement à chaque `push` sur la branche `main`.  
Voici le fonctionnement global du déploiement :

1. **GitHub Actions** teste le code (`flake8`, `coverage`) puis crée une image Docker.
2. Cette image est **poussée automatiquement sur Docker Hub** (`martinlabi/oc-lettings-site`).
3. **Render** télécharge cette image, lit les variables d’environnement définies dans son interface, exécute les commandes de déploiement (migrations, loaddata, collectstatic) et démarre le serveur avec Gunicorn.
4. **Sentry** est automatiquement activé pour remonter les erreurs de production si un `SENTRY_DSN` est fourni.

---

### Configuration requise

Avant tout déploiement, assurez-vous d’avoir :

- Un compte Docker Hub (et les identifiants en secrets GitHub `DOCKER_USERNAME`, `DOCKER_PASSWORD`).
- Un compte Render avec un service Docker configuré.
- Les fichiers suivants bien présents et configurés :
  - `Dockerfile`
  - `.env` (non committé) contenant `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `SENTRY_DSN`
  - `docker-compose.yml` (utile pour les tests en local)
  - `.github/workflows/ci.yml` et `ci-cd.yml` pour les tests et la CI/CD Docker.

---

### Étapes de déploiement

#### 1. Déploiement automatique via GitHub et Render (prod)

1. **Configurer GitHub Actions** :
   - Ajoutez vos identifiants Docker dans `Settings > Secrets and variables > Actions` :
     - `DOCKER_USERNAME`
     - `DOCKER_PASSWORD`

2. **Configurer Render** :
   - Créez un nouveau service Render de type **Docker**.
   - Renseignez :
     - **Image URL** : `martinlabi/oc-lettings-site:latest`
     - **Start command** : Laissez vide (géré par le `CMD` dans Dockerfile).
   - Ajoutez dans **Environment > Environment Variables** :
     - `SECRET_KEY`
     - `DEBUG=False`
     - `ALLOWED_HOSTS=yourdomain.onrender.com`
     - `SENTRY_DSN` (optionnel)

3. **Pousser sur GitHub** (`main`) :
   - Les tests tournent automatiquement.
   - L’image est publiée sur Docker Hub.
   - Render la récupère et déploie le projet.

---

#### 2. Déploiement/test local avec Docker Compose

1. Copier ou créer un fichier `.env` :
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=



2. Lancer le site local

  docker-compose up --build


3. Accéder au site :

  http://localhost:8000

  Admin : http://localhost:8000/admin (user/pass définis dans fixtures/users.json)