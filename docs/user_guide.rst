Guide d'utilisation
===================

Cette section décrit les cas d’usage principaux côté utilisateur.  
L’interface est simple et se compose principalement de trois sections : page d’accueil, profils, et locations.

---

1. Page d’accueil
-----------------

**URL** : `/`  
**But** : Présenter la page principale du site.

**Fonctionnement** :
- Affiche un message d’accueil simple.
- Propose deux liens : un vers la liste des profils, un vers la liste des logements.
- Utilise le gabarit `index.html`.

---

2. Liste des profils
--------------------

**URL** : `/profiles/`  
**But** : Visualiser tous les utilisateurs enregistrés.

**Fonctionnement** :
- Affiche une liste de noms d’utilisateurs.
- Chaque nom est cliquable pour accéder au profil complet.
- Utilise le gabarit `profiles/index.html`.

---

3. Détail d’un profil
---------------------

**URL** : `/profiles/<username>/`  
**But** : Afficher les informations d’un utilisateur spécifique.

**Fonctionnement** :
- Affiche le nom d’utilisateur et sa ville préférée.
- En cas de profil inexistant, redirige vers une page 404 personnalisée (`profiles/profile_404.html`).
- Utilise le gabarit `profiles/profile.html`.

---

4. Liste des logements
----------------------

**URL** : `/lettings/`  
**But** : Consulter tous les logements disponibles à la location.

**Fonctionnement** :
- Affiche une liste de titres de logements.
- Chaque titre est cliquable pour afficher les détails.
- Utilise le gabarit `lettings/index.html`.

---

5. Détail d’un logement
-----------------------

**URL** : `/lettings/<id>/`  
**But** : Visualiser les détails d’un logement.

**Fonctionnement** :
- Affiche le titre et l’adresse complète du logement.
- En cas d’ID invalide, redirige vers une page 404 personnalisée (`lettings/letting_404.html`).
- Utilise le gabarit `lettings/letting.html`.

---

6. Test Sentry (développeur uniquement)
---------------------------------------

**URL** : `/sentry-debug/`  
**But** : Provoquer une erreur pour vérifier l’intégration Sentry.

**Fonctionnement** :
- Accéder à cette URL déclenche une division par zéro.
- L’erreur est automatiquement envoyée à Sentry si la variable `SENTRY_DSN` est définie.
