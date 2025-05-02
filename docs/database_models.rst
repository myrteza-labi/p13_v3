Modèles de données
==================

Cette section décrit les modèles utilisés dans le projet et leur structure.  
Chaque application Django gère ses propres modèles de manière isolée.

---

oc_lettings_site
----------------

Cette app contient la configuration centrale du projet, mais **ne définit pas de modèle de données**.  
Elle sert à la configuration des routes, du monitoring, du logging, et des pages d’erreur.

---

lettings
--------

Modèle **Address**
^^^^^^^^^^^^^^^^^^

Représente une adresse postale.

Champs :
- `number` (int) : numéro de rue
- `street` (str) : nom de la rue
- `city` (str) : ville
- `state` (str) : état (abréviation, ex. CA)
- `zip_code` (int) : code postal
- `country_iso_code` (str) : code ISO du pays (ex. "US")

Modèle **Letting**
^^^^^^^^^^^^^^^^^^

Représente un logement proposé à la location.

Champs :
- `title` (str) : titre du logement
- `address` (FK → Address) : adresse associée

---

profiles
--------

Modèle **Profile**
^^^^^^^^^^^^^^^^^^

Représente les informations complémentaires d’un utilisateur.

Champs :
- `user` (OneToOne → User) : lien avec un utilisateur Django
- `favorite_city` (str) : ville préférée de l'utilisateur
