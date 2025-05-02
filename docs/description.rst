Description du projet
=====================

**Orange County Lettings** est une application web développée avec le framework Django.  
Elle permet la consultation de profils utilisateurs ainsi que la visualisation de logements disponibles à la location.

Ce projet est divisé en trois applications principales :

- **oc_lettings_site** : l'application principale du projet, contenant la configuration globale (paramètres, routes principales, gestion des erreurs, etc.)
- **lettings** : une application Django dédiée à la gestion des locations.
- **profiles** : une application Django dédiée à la gestion des profils utilisateurs.

L'application est conçue pour :
- être facilement maintenable grâce à une structure modulaire,
- offrir un déploiement automatisé via Docker, GitHub Actions et Render,
- inclure un système de monitoring des erreurs avec Sentry,
- atteindre un haut niveau de couverture de tests automatisés.

Cette documentation présente l'ensemble des aspects techniques du projet : installation, structure, API, déploiement et cas d’utilisation typiques.
