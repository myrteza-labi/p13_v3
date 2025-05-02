Dockerfile – Image Docker de production
=======================================

Ce fichier ``Dockerfile`` définit comment construire une **image Docker** exécutable du projet Django.  
Elle est utilisée à la fois **en local** via ``docker-compose`` et **en production** via Render.

Objectif
--------

Créer une image autonome capable de :

- Installer les dépendances Python du projet ;
- Nettoyer les fichiers de fixtures JSON (BOM) ;
- Exécuter les **migrations**, charger les **fixtures** et collecter les **fichiers statiques** ;
- Lancer le serveur **Gunicorn**.

Étapes du Dockerfile
---------------------

1. **Base de l’image**

.. code-block:: dockerfile

   FROM python:3.11-slim

On utilise une image légère officielle de Python 3.11.

2. **Répertoire de travail**

.. code-block:: dockerfile

   WORKDIR /app

Tous les fichiers et instructions suivantes seront relatifs à ``/app``.

3. **Installation des dépendances**

.. code-block:: dockerfile

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

Cela permet d’installer toutes les librairies nécessaires, y compris Django, Sentry, etc.

4. **Ajout du code source**

.. code-block:: dockerfile

   COPY . .

Le reste du projet est copié dans le conteneur.

5. **Nettoyage des fichiers JSON (fixtures)**

Le Dockerfile intègre une étape pour retirer les éventuels BOM (Byte Order Mark) présents en début de fichiers JSON :

.. code-block:: python

   import glob
   for p in glob.glob("fixtures/*.json"):
       with open(p, "rb") as f:
           content = f.read()
       if content.startswith(b"\xef\xbb\xbf"):
           with open(p, "wb") as f_out:
               f_out.write(content.lstrip(b"\xef\xbb\xbf"))

Ce script est généré et exécuté automatiquement.

6. **Port exposé**

.. code-block:: dockerfile

   EXPOSE 8000

Cela indique que l’application écoute sur le port ``8000``.

7. **Commande par défaut à l’exécution**

.. code-block:: shell

   CMD ["sh", "-c", "..."]

Lors du démarrage du conteneur, les actions suivantes sont effectuées automatiquement :

- Affichage de debug (fixtures)
- ``python manage.py migrate --noinput``
- ``python manage.py loaddata fixtures/...``
- ``python manage.py collectstatic --noinput``
- Lancement du serveur via Gunicorn.

Utilisation
-----------

En local (avec Docker Desktop) :

.. code-block:: bash

   docker build -t oc-lettings-site .
   docker run -p 8000:8000 oc-lettings-site

En CI/CD, cette image est construite et publiée automatiquement grâce à GitHub Actions.

