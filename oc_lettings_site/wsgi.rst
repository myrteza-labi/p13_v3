WSGI – oc_lettings_site.wsgi
============================

Ce module fournit le point d’entrée WSGI (Web Server Gateway Interface) du projet Django.  
Il est utilisé pour déployer l'application sur des serveurs compatibles avec WSGI (comme Gunicorn, uWSGI, etc.).

.. automodule:: oc_lettings_site.wsgi
   :members:
   :undoc-members:
   :show-inheritance:

Fonctionnement
--------------

**application**  
Cette variable expose l’interface WSGI via la fonction ``get_wsgi_application()`` fournie par Django.  
Elle est utilisée par le serveur web pour interagir avec le projet Django.

Le module commence par définir la variable d’environnement `DJANGO_SETTINGS_MODULE`, pointant vers le fichier de configuration du projet (`oc_lettings_site.settings`), afin que Django sache quel fichier utiliser au lancement.

Utilisation
-----------

Ce fichier est automatiquement utilisé lors d’un déploiement via Gunicorn, comme spécifié dans le `Dockerfile` :

```dockerfile
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]

Il n’est généralement pas modifié, sauf cas très spécifiques.
