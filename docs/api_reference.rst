Référence des interfaces de programmation (API)
===============================================

Cette section décrit les routes accessibles dans l'application, les vues associées, les modèles utilisés, les templates HTML et les tests automatisés.

.. contents::
   :depth: 2
   :local:

oc_lettings_site
----------------

### Routes & Vues

.. list-table::
   :header-rows: 1

   * - Route
     - Vue
     - Description
   * - `/`
     - `index`
     - Affiche la page d’accueil
   * - `/admin/`
     - Django Admin
     - Interface d’administration Django
   * - `/sentry-debug/`
     - `trigger_error`
     - Déclenche une erreur volontaire (test Sentry)
   * - `404 handler`
     - `custom_404`
     - Gère les erreurs 404 avec un template personnalisé

### Templates

- `index.html` : page d’accueil  
- `404.html` : page d'erreur personnalisée

### Tests

- Vérifie le bon rendu de la page d’accueil (`200 OK`, template utilisé)
- Vérifie que `handler404` est bien configuré et retourne un `404` personnalisé

---

lettings
--------

Préfixe commun : `/lettings/`

### Routes & Vues

.. list-table::
   :header-rows: 1

   * - Route
     - Vue
     - Description
   * - `/lettings/`
     - `index`
     - Affiche la liste de tous les logements
   * - `/lettings/<int:letting_id>/`
     - `letting`
     - Affiche les détails d’un logement par ID

### Modèles

- **Address**  
  Champs : `number`, `street`, `city`, `state`, `zip_code`, `country_iso_code`  
  Représente une adresse postale complète.

- **Letting**  
  Champs : `title`, `address`  
  Représente un logement avec un titre et une adresse liée.

### Templates

- `lettings/index.html` : liste des logements  
- `lettings/letting.html` : détails d’un logement  
- `lettings/letting_404.html` : affiché si le logement n’existe pas

### Tests

- **Modèles** : `__str__` de `Address` et `Letting`
- **Vues** : rendu des pages, templates, contexte, 404 personnalisé
- **URLs** : bonne résolution des vues via `reverse` + `resolve`

---

profiles
--------

Préfixe commun : `/profiles/`

### Routes & Vues

.. list-table::
   :header-rows: 1

   * - Route
     - Vue
     - Description
   * - `/profiles/`
     - `index`
     - Affiche la liste de tous les profils utilisateurs
   * - `/profiles/<str:username>/`
     - `profile`
     - Affiche les détails d’un profil utilisateur par nom d’utilisateur

### Modèle

- **Profile**  
  Champs : `user`, `favorite_city`  
  Associe un utilisateur Django à sa ville préférée.

### Templates

- `profiles/index.html` : liste des profils  
- `profiles/profile.html` : détails d’un profil  
- `profiles/profile_404.html` : affiché si le profil n’existe pas

### Tests

- **Modèle** : `__str__` retourne le nom d'utilisateur
- **Vues** : rendu correct, gestion des erreurs
- **URLs** : résolution des vues `index` et `detail`
