Guide de démarrage rapide
=========================

Ce guide vous permet de lancer rapidement le projet en local, en quelques étapes simples.

.. code-block:: bash

   # 1. Cloner le dépôt
   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

   # 2. Créer et activer un environnement virtuel
   python -m venv venv
   # Sous Linux/macOS
   source venv/bin/activate
   # Sous Windows
   .\venv\Scripts\Activate.ps1

   # 3. Installer les dépendances
   pip install -r requirements.txt

   # 4. Créer un fichier .env
   echo SECRET_KEY=your_key > .env
   echo DEBUG=True >> .env
   echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
   echo SENTRY_DSN= >> .env

   # 5. Appliquer les migrations & charger les données
   python manage.py migrate
   python manage.py loaddata fixtures/users.json fixtures/lettings.json fixtures/profiles.json

   # 6. Lancer le serveur
   python manage.py runserver
