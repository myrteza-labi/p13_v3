Templates
=========

Les fichiers de gabarits se trouvent dans le dossier `templates/`. On y distingue :

- **base.html**  
  Le gabarit de base, définissant la structure HTML et les blocs `{% block %}`.

- **index.html**  
  La page d’accueil du site (`oc_lettings_site.views.index`).

- **404.html**  
  Page d’erreur personnalisée en cas de ressource introuvable.

Sous-dossier **lettings/** :

- `templates/lettings/index.html`  
  Affiche la liste des biens (`lettings.views.lettings_index`).
- `templates/lettings/detail.html`  
  Détail d’une location (`lettings.views.letting`).

Sous-dossier **profiles/** :

- `templates/profiles/index.html`  
  Affiche la liste des profils (`profiles.views.profiles_index`).
- `templates/profiles/detail.html`  
  Détail d’un profil (`profiles.views.profile`).
