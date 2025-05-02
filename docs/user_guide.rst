Guide d'utilisation
===================

Cette section décrit les cas d’usage principaux côté utilisateur.  
L’interface est simple et se compose principalement de trois sections : page d’accueil, profils, et locations.

---

1. Consulter la page d’accueil
------------------------------

**URL** : `/`  
**But** : Présenter une page d’accueil avec liens vers les profils et les locations.

**Étapes** :
- L’utilisateur accède à la racine du site
- Il voit un lien vers la liste des profils
- Il voit un lien vers la liste des logements

---

2. Afficher la liste des profils
--------------------------------

**URL** : `/profiles/`  
**But** : Visualiser tous les utilisateurs enregistrés.

**Étapes** :
- L’utilisateur clique sur “Profils”
- Il voit la liste des utilisateurs avec leur nom
- Il peut cliquer sur un nom pour voir les détails

---

3. Consulter un profil utilisateur
----------------------------------

**URL** : `/profiles/<username>/`  
**But** : Voir les détails d’un utilisateur spécifique.

**Étapes** :
- L’utilisateur accède à une page de profil
- Il voit la ville préférée de la personne

---

4. Afficher la liste des logements
----------------------------------

**URL** : `/lettings/`  
**But** : Voir tous les logements proposés à la location.

**Étapes** :
- L’utilisateur clique sur “Lettings”
- Il voit une liste de logements avec leurs titres

---

5. Consulter un logement spécifique
-----------------------------------

**URL** : `/lettings/<id>/`  
**But** : Voir les détails d’un logement.

**Étapes** :
- L’utilisateur clique sur un titre de logement
- Il voit l’adresse complète

---

6. Tester l’envoi d’erreurs à Sentry (dev uniquement)
------------------------------------------------------

**URL** : `/sentry-debug/`  
**But** : Provoquer une erreur pour tester l’intégration de Sentry.

**Étapes** :
- L’utilisateur accède à `/sentry-debug/`
- Une division par zéro est volontairement provoquée
- L’erreur est envoyée à Sentry si `SENTRY_DSN` est configuré
