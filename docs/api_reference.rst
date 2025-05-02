Référence des interfaces de programmation (API)
===============================================

Cette section décrit les routes accessibles dans l'application, ainsi que les vues associées.

---

oc_lettings_site
----------------

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

---

lettings
--------

Préfixe commun : `/lettings/`

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

---

profiles
--------

Préfixe commun : `/profiles/`

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
