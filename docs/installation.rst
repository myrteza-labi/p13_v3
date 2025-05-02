Installation du projet
======================

Cette section détaille les étapes pour installer et exécuter localement l'application **Orange County Lettings**.

Prérequis
---------

- Python 3.6 ou supérieur
- Git
- pip (installé avec Python)
- SQLite3 (préinstallé avec Python)
- (Optionnel) : VS Code ou autre éditeur avec support Django

Clonage du dépôt
----------------

1. Ouvrez un terminal et placez-vous dans le dossier où vous voulez cloner le projet :

   .. code-block:: bash

      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

Création de l’environnement virtuel
-----------------------------------

2. Créez et activez un environnement virtuel :

   Sous macOS / Linux :

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

   Sous Windows (PowerShell) :

   .. code-block:: powershell

      python -m venv venv
      .\venv\Scripts\Activate.ps1

Installation des dépendances
----------------------------

3. Installez les dépendances du projet :

   .. code-block:: bash

      pip install -r requirements.txt

Fichier `.env`
--------------

4. Créez un fichier `.env` à la racine du projet avec les variables suivantes :

   .. code-block:: text

      SECRET_KEY=your_secret_key
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      SENTRY_DSN=

   .. warning::
      Ne versionnez jamais ce fichier `.env`. Il contient des données sensibles.

Initialisation de la base de données
------------------------------------

5. Appliquez les migrations et chargez les données de test :

   .. code-block:: bash

      python manage.py migrate
      python manage.py loaddata fixtures/users.json fixtures/lettings.json fixtures/profiles.json

Lancement du serveur local
--------------------------

6. Lancez le serveur :

   .. code-block:: bash

      python manage.py runserver

7. Accédez à l’application à l’adresse : http://localhost:8000

   L’administration est disponible sur : http://localhost:8000/admin

   Identifiants de test par défaut :
   - Utilisateur : `admin`
   - Mot de passe : `Abc1234!`
