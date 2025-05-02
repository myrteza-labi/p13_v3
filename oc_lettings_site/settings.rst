OC Lettings Site – Paramètres Django
=====================================

Ce module contient la configuration globale du projet Django ``oc_lettings_site``.

.. automodule:: oc_lettings_site.settings
   :members:
   :undoc-members:
   :show-inheritance:

Aperçu
------

Le fichier ``settings.py`` définit tous les paramètres nécessaires au bon fonctionnement du projet : configuration des applications, base de données, statiques, sécurité, logging, intégration Sentry, etc.

Points clés
-----------

**Chargement des variables d'environnement**  
Les paramètres sensibles (clé secrète, Sentry DSN...) sont chargés via un fichier `.env` grâce à la bibliothèque ``python-dotenv``.

**Applications enregistrées**

- ``lettings`` : Application dédiée aux locations.
- ``profiles`` : Application de gestion des profils utilisateurs.
- ``oc_lettings_site`` : Application principale, point d'entrée du projet.

**Base de données**  
Le projet utilise une base de données SQLite par défaut, stockée dans le fichier ``oc-lettings-site.sqlite3``.

**Fichiers statiques**

- ``STATICFILES_DIRS`` : inclut les fichiers dans ``/static``.
- ``STATIC_ROOT`` : destination pour la commande `collectstatic`.
- Le stockage statique varie selon l’environnement : `WhiteNoise` est utilisé en production pour optimiser les assets, et le stockage par défaut est utilisé lors des tests/CI.

**Sécurité**

- La `SECRET_KEY`, `DEBUG` et `ALLOWED_HOSTS` sont extraits de `.env` pour protéger les données sensibles.

**Sentry**  
L'intégration Sentry est conditionnelle à la présence d'un DSN via `SENTRY_DSN`.  
Elle permet de capturer les erreurs et de surveiller l'application en production.

**Logging**  
Un système de logging Django est configuré avec :
- Un format détaillé (niveau, date, module, message).
- Deux handlers : `console` et `sentry` pour centraliser les logs importants.
- Les erreurs `ERROR` sont envoyées à Sentry automatiquement.

Utilisation recommandée
------------------------

- Assurez-vous que le fichier `.env` contient au minimum les clés suivantes :  
  ``SECRET_KEY``, ``DEBUG``, ``ALLOWED_HOSTS``, et éventuellement ``SENTRY_DSN``.
- Ne jamais committer le fichier `.env` dans le dépôt.
- Adapter les paramètres en fonction de l'environnement (développement, CI, production).
